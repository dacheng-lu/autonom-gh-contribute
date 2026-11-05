# Local contribution record

Copy `examples/contribution-record.json` and replace every example with real information. Keep records outside the target repository if they may contain private information. The validator does not fetch URLs, inspect Git, run tests, decide whether actions are authorized, or guarantee project compliance.

All states require `type` (`report`, `docs`, `test`, `code`), `repository`, `base_branch`, 40-character `base_sha`, `problem`, `policy_source`, `policy_checked_at`, `duplicate_status` (`clear`, `related_resolved`, `unresolved`), `duplicate_decision` and `authorization_scope`. Record actual source links and dates in the text fields; the validator only checks that they are nonempty. Record a reason if a concept is not applicable; the base SHA anchors investigation even for a non-code report.

`preparing` records ongoing work. `blocked` records unresolved work. `ready` and `published` also require `evidence`, `verification`, `limitations`, and a duplicate status other than `unresolved`. `ready` means the record is prepared; it is not permission to publish. Record missing tests honestly in `limitations`.

For a published **PR**, add a `publication` object with `url`, `base_branch`, `head_sha`, `checked_sha`, `action_authorization`, and `ci_status` (`passed`, `failed`, `pending`, `approval_required`, `absent`, `unknown`). The checked SHA must match the head SHA, and the base must match the planned base. Match means only that recorded strings agree; verify actual remote state independently. For reports or comments without a PR head, retain `ready` and document their publication separately; the PR-specific published record is intentionally not applicable.
