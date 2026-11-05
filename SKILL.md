---
name: autonom-gh-contribute
description: Prepare and verify responsible contributions to third-party GitHub repositories, including reproductions, documentation, tests and pull requests. Use when investigating or contributing upstream, checking repository policies, or following up on an existing contribution.
---

# Autonom GitHub Contribution

Work on one useful contribution at a time. The goal is a verifiable outcome for the upstream project, not a merged-PR quota. Adapt this procedure to the user's instructions, available tools, the target project and its current rules.

## 1. Discover and decide

- Identify the upstream repository, contribution type (report, documentation, test or code), problem and intended beneficiaries. Check the actual source or behavior where relevant.
- Read the current README, contribution guidelines, license, issue/PR templates and relevant policies, including rules for AI assistance, attribution, CLA/DCO and disclosure. Record source links and access date; distinguish absent policy from an inaccessible or unknown one. Follow the stricter applicable rules.
- Search issues and PRs, including closed results, for duplicates, linked work, active assignees and maintainer decisions. A related item is not automatically a duplicate: document the decision. If already being addressed, prohibited, or acceptance is unclear, stop publication and consider adding evidence to an existing discussion or asking maintainers through an authorized action.
- Identify upstream's actual default branch and contribution base; these may differ. Record the base branch and its fetched commit SHA. Never infer freshness from the fork's `origin` alone.
- Choose a focused approach appropriate to the task. Discuss substantial or uncertain work with maintainers when the project asks for it. Do not invent a problem or send low-value changes to obtain credit.

## 2. Authorization and preparation

Distinguish read-only investigation, local changes, fork/branch creation, push and public actions (issue, comment, PR). Check the user's existing instructions and permissions for each action; do not request approval again when already granted. Prepare a concrete reviewable result before asking for any missing permission. Never imply a user authorized outreach merely by asking for analysis. Respect platform and project policies, use minimum necessary credentials, do not expose secrets, and stop/back off on rate limiting. Do not mass-submit or automatically ping maintainers.

For code, fetch the actual upstream base and work in an isolated branch/worktree when possible. Preserve the user's existing work and repository formatting, including `.gitattributes`; avoid stashing untracked work just to run baseline tests. Follow the target's contribution process and use its own test tooling. For non-code reports, no fork is required.

## 3. Evidence and verification

Reproduce a real problem where feasible; record environment, commands, observed and expected results, and base SHA. For a bug fix, prefer the same meaningful regression case failing before the change and passing afterward; state explicitly when a baseline cannot be reproduced. Verify the relevant real entry point: CLI, API/adapter, browser, documentation steps or other applicable surface. Run appropriate tests, including target-required checks where possible. Test count alone is not proof. Record limitations, skipped checks and actual output; never assert results that were not observed.

Before publishing, review the diff, attribution, licenses, secrets, and the project-specific template. Use a concise problem/change/verification description unless the repository requires another format. Explain compatibility or limitations when relevant. Adhere to the upstream AI-assistance policy; human review does not override a prohibition.

## 4. Publish only within authorization, then verify

Use the upstream's required base branch and correct fork/head. After creating a PR, independently read back its URL, state, base, head SHA and changed files; compare with intended changes. Check CI/check-runs against that exact head SHA. Report success, failure, pending, approval-required, absent and unknown distinctly. A `mergeable` value can be pending and does not prove approval or successful CI. If the head changes, prior checks no longer prove the new head; rerun applicable checks and reread status.

After publication, monitor and respond to review only within user authorization and project norms. Revalidate after changes, record decisions and closure/merge accurately, and do not claim a merge or contributor listing without evidence.

## Optional local record

Use `examples/contribution-record.json` as a starting point and `python3 scripts/validate_record.py PATH` to check record completeness and consistency. The validator is offline: it does not verify whether evidence, policy, authorization, commits or CI claims are true, and does not publish anything. `CHECKLIST.md` provides a human review. Report outcome, evidence, remaining limits and any action needed.
