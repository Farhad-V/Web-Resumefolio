# ADR 007 React Inertia Frontend

<a id="design-record-07-design-decisions-adr-007-react-inertia-frontend-md"></a>

<details>
<summary>ADR-007 — React and Inertia frontend</summary>

<a id="design-record-07-design-decisions-adr-007-react-inertia-frontend-md--heading-adr-007--react-and-inertia-frontend"></a>

### ADR-007 — React and Inertia frontend

Status: Selected by Farhad, November 4, 2026. Supersedes only the interactive Blade/Alpine choice in T01. Documentation revision 1.4; no Software Release or implementation is asserted.

<a id="design-record-07-design-decisions-adr-007-react-inertia-frontend-md--heading-decision-and-reason"></a>

#### Decision and reason

Use React 19 with Inertia 3 inside each Laravel 13 application, with Tailwind 4 and Vite. Farhad confirmed familiarity with both React and Blade and explicitly selected React/Inertia for dashboard interactions, resume forms and reusable components. Retain Blade for trusted Dompdf templates. No Alpine dependency is required for interactive application pages.

Laravel retains routing, controllers, server-side validation, sessions, Fortify authentication and policies. Do not add an independently deployed frontend or a separate browser REST authentication layer. Core and ProjectForge remain independent Laravel applications; Inertia does not connect them or replace their scoped API/SSO boundary.

<a id="design-record-07-design-decisions-adr-007-react-inertia-frontend-md--heading-consequences-and-verification"></a>

#### Consequences and verification

Resolve compatible maintained adapter/package patches at Setup and commit lockfiles. Include React page/form behavior, validation errors, navigation, accessibility and protected direct requests in the existing requirement-linked verification. Preserve draft/conflict handling and authorization on every server entry point. React components do not replace server-side permission checks. PDF rendering continues to use trusted Blade templates and does not require browser rendering or frontend SSR.

No code or dependency is installed by this amendment. MVP scope, requirement IDs, acceptance criteria, storage, identity and release gates are unchanged. The [technical decisions](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/technical-decisions.md#t01--runtime-frontend-and-persistence), [Setup](../../05-Agile-Iterative-Development/01-Project-Setup.md) and dark architecture diagram reflect this selection. The [Baseline manifest](https://github.com/Farhad-V/Web-Resumefolio/blob/1f2acaa351ac306cb57cbe4fe9742e8bd90720d9/docs/MVP/baseline/manifest.json) identifies the revised documentary inputs and links the previous immutable revision.

</details>
