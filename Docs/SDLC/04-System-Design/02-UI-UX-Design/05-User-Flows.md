# 5. User Flows

[UI/UX Design index](02-UI-UX-Design.md)

## Main Flows
Cover invited access, editing, explicit publication, protected employer viewing, application submission history and authorized repository work.

## Alternative and Error Flows
Show expiry, invalid input, stale drafts, revoked access, missing artifacts and denied actions with appropriate recovery cues.

## Existing Design Records

## 3. Consequential journey design

[Explicit source apply, saved draft and separate publication](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/ui-source-apply-publication.svg)

[Editable PlantUML](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/SDLC/04-system-design/06-design-quality-and-security-analysis/diagrams/ui-source-apply-publication.puml) · ![ui source apply publication](../Diagrams/Archived-Png/Ui-Source-Apply-Publication.png)

### Presentation and history

Label **Saved Draft**, **Published Revision** and **Actual Submitted Materials** distinctly. A source comparison identifies exact source/draft versions, proposed differences, selections and affected overrides. Applying selected changes saves only the draft; show the unchanged published revision. Publication is a separate explicit action confirming the intended candidate/language and its relevant consequences.

Stale comparison/save conflicts preserve the user's permitted intended edits and offer review against current state; do not silently overwrite or publish a newer unseen draft. Actual-material views identify real capture/completeness rather than rebuilding submitted content from today's resume. See [Presentation](../03-Low-Level-Design/03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-professional-presentation-md) and [Applications](../03-Low-Level-Design/03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-applications-md).

### Sharing and files

Separate download mode, variant availability, link state and password controls. A configured option may still be processing/unavailable. Explain failed replacement without pretending the prior usable association changed. Link disabling/password rotation communicates the defined subsequent-access consequence and the limit that downloaded/emitted bytes cannot be recalled. See [Sharing](../03-Low-Level-Design/03-Detailed-Module-Design.md#design-record-03-component-and-module-design-components-representation-and-sharing-md).

### Communication, Work and execution

**After MVP.** Shared operating and recovery controls still apply where relevant.

Send review exposes intended recipients, content, attachments and current provider context before deliberate dispatch. Pending/unknown outcomes offer operation lookup/reconciliation rather than an unconditional Send again action. Acceptance is not reading/delivery. Calendar feedback distinguishes local save from provider synchronization.

Board movement offers non-drag controls. Task completion, item acceptance and Sprint-end/goal outcomes have distinct labels/actions. Ending a period must not imply all work succeeded. Native Git/review interfaces show exact revision/ref context; execution and target deployment have separate authority/approval/status. Cancellation requested is not stopped; terminal run is not cleaned up. See the [interaction realizations](../03-Low-Level-Design/05-API-Specification.md#design-record-05-interface-and-api-design-03-use-case-realizations-and-interactions-md).
