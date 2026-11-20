# 10. Accessibility

[UI/UX Design index](02-UI-UX-Design.md)

## Accessibility Target
Use WCAG 2.2 AA as the planned target. Confirm applicable criteria and record verification evidence with each implemented screen.

## Keyboard, Screen Reader, Contrast and Text
Provide meaningful labels, keyboard access, visible focus and announced status changes. Check contrast, text resizing and reflow in the supported environments.

## Existing Design Records

## 5. Accessibility and responsive behavior

### Target and semantics

[WCAG 2.2](https://www.w3.org/TR/WCAG22/) is the standard referenced by the proposed AA target. Review applicable A/AA criteria across complete journeys; selected checks below are not a full conformance checklist. Page language, semantic structure, text alternatives, contrast, focus, input assistance and accessible authentication require actual implementation assessment. PDF accessibility is a separate evaluation from the web interface.

Prefer native semantic controls. The [W3C ARIA Authoring Practices guidance](https://www.w3.org/WAI/ARIA/apg/practices/read-me-first/) explains that adding a role does not supply expected keyboard behavior; custom patterns require actual browser/assistive-technology testing. Do not add ARIA that obscures correct native semantics. Sources reviewed November 2, 2026; actual client/widget compatibility remains unverified.

### Keyboard, focus and pointer interaction

The [W3C Keyboard explanation](https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html) informs equivalent keyboard operation for pointer actions. Provide logical focus order, visible focus and no keyboard traps. Dialogs need meaningful initial focus, contained interaction while modal and appropriate focus restoration. Provide buttons/menu actions for selection/reordering/work movement rather than drag-only operation. Avoid hover-only information and maintain accessible names for icon controls.

### Layout, enlargement and content

Use content-driven responsive layouts that preserve actions, relationships and feedback at narrow widths/enlargement. Where tables/boards genuinely need two-dimensional space, supply understandable navigation and useful alternative detail/list views; do not hide required cells or primary controls solely to fit a viewport. Avoid sticky overlays obscuring focused controls or errors.

The [W3C Reflow explanation](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html) includes a 320-CSS-pixel equivalent width for vertical content, with specific two-dimensional-content exceptions. Q-D25's proposed 390-pixel/200%-zoom checks alone do not cover every reflow obligation. Evaluate text enlargement, wrapping and input/error feedback separately from a screenshot at one mobile width.

Support readable long multilingual content, explicit dates/time zones and language identification for professional variants. Evidence media needs meaningful alternatives and applicable captions/descriptions under the reviewed criteria; a generic filename does not describe its professional meaning. Avoid unnecessary motion and honor relevant reduced-motion behavior. Exact styles/target dimensions and criterion-specific exceptions must be documented in the implementation assessment rather than guessed from this guide.
