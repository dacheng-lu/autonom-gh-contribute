#!/usr/bin/env python3
"""Validate a local contribution record; no network or claim verification."""
import argparse
import json
import re
import sys
from pathlib import Path

SHA = re.compile(r'^[0-9a-fA-F]{40}$')
STATES = {'preparing', 'ready', 'published', 'blocked'}
TYPES = {'report', 'docs', 'test', 'code'}
CI = {'passed', 'failed', 'pending', 'approval_required', 'absent', 'unknown'}


def validate(record):
    errors = []
    if not isinstance(record, dict):
        return ['record must be a JSON object']

    def string(obj, key, prefix=''):
        value = obj.get(key)
        if not isinstance(value, str) or not value.strip():
            errors.append(f'{prefix}{key} must be a non-empty string')
            return ''
        return value

    state = record.get('state')
    if state not in STATES:
        errors.append('state must be preparing, ready, published or blocked')
    if record.get('type') not in TYPES:
        errors.append('type must be report, docs, test or code')
    for key in ('repository', 'base_branch', 'problem', 'policy_source', 'policy_checked_at', 'duplicate_decision', 'authorization_scope'):
        string(record, key)
    base = string(record, 'base_sha')
    if base and not SHA.fullmatch(base):
        errors.append('base_sha must be a 40-character hex SHA')
    if record.get('duplicate_status') not in {'clear', 'related_resolved', 'unresolved'}:
        errors.append('duplicate_status must be clear, related_resolved or unresolved')
    if state in {'ready', 'published'}:
        if record.get('duplicate_status') == 'unresolved':
            errors.append('unresolved duplicate blocks ready/published state')
        string(record, 'evidence')
        string(record, 'verification')
        string(record, 'limitations')
    if state == 'published':
        pub = record.get('publication')
        if not isinstance(pub, dict):
            errors.append('publication must be an object for published state')
        else:
            for key in ('url', 'base_branch', 'action_authorization'):
                string(pub, key, 'publication.')
            if pub.get('base_branch') != record.get('base_branch'):
                errors.append('publication.base_branch differs from intended base_branch')
            head = string(pub, 'head_sha', 'publication.')
            checked = string(pub, 'checked_sha', 'publication.')
            for key, value in (('head_sha', head), ('checked_sha', checked)):
                if value and not SHA.fullmatch(value):
                    errors.append(f'publication.{key} must be a 40-character hex SHA')
            if head and checked and head.lower() != checked.lower():
                errors.append('publication.checked_sha differs from head_sha; checks are stale')
            if pub.get('ci_status') not in CI:
                errors.append('publication.ci_status is invalid')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('record', type=Path)
    args = parser.parse_args()
    try:
        record = json.loads(args.record.read_text(encoding='utf-8'))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f'Cannot read record: {exc}', file=sys.stderr)
        return 2
    errors = validate(record)
    if errors:
        for error in errors:
            print(f'ERROR: {error}', file=sys.stderr)
        return 1
    print('Record structure and selected state checks passed; claims were not verified.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
