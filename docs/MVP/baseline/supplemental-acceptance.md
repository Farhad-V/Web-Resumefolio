# Supplemental MVP acceptance obligations

These add explicit owner-scope and selected-policy checks to the original 470 preserved locators; they do not renumber or silently rewrite historical criteria. All results: Not executed. They are Must for the applicable MVP component.

| ID | Acceptance obligation | Gate |
| --- | --- | --- |
| MVP-AC01 | User saves application status, next action and timezone-defined follow-up date without a mail/calendar connection; other users and employer viewers cannot retrieve it | G3 |
| MVP-AC02 | User uploads each supported media category privately, selects it for one resume and publishes explicitly; another resume/link cannot retrieve it through preview/direct/range URLs | G3 |
| MVP-AC03 | ProjectForge SSO binds pinned issuer + immutable Core UUID, rejects bad state/PKCE/redirect, and requires explicit active entitlement; disable stops the next new browser/API/Git request | G2 |
| MVP-AC04 | Real clients clone/fetch/pull/push through authorized Smart HTTP; expired/revoked/wrong-repo PAT, anonymous/dumb HTTP, traversal/header/environment/hook bypasses and quota races fail safely | G2 |
| MVP-AC05 | A 10-page English/German PDF preserves accents/fonts/page flow within T06/T09 bounds; uploaded/generated modes and missing language remain explicit | G3/G5 |
| MVP-AC06 | Publication or submitted-set crash/retry never loses a referenced artifact, silently changes actual submitted bytes or reports success before durable capture | G3 |
| MVP-AC07 | Concurrent upload/Git writes honor effective per-file/user/global reservations and free-space thresholds including temporary bytes; denial retains consistent existing data | G2/G5 |
| MVP-AC08 | Independent encrypted coherent backup restores Core + ProjectForge and byte checksums within the selected target; revoked access/deletion records stay enforced and no external effect replays | G4 |
| MVP-AC09 | Admin provisions accounts/policies without acquiring user-private content; invited user completes login/recovery and Admin TOTP; public signup and cross-user ID changes fail | G3/G4 |
| MVP-AC10 | Fixed ProjectForge Kanban moves preserve issue identity, authorized assignee, Low/Normal/High priority and optional due date; board access never confers repository write | G3 |
