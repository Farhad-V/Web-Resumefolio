# 1. Introduction

[UI/UX Design index](02-UI-UX-Design.md)

## Purpose
Describe how invited users, employer viewers and repository collaborators interact with the MVP.

## Scope
Cover the private workspace, resume editing and publication, sharing, application history and authorized ProjectForge journeys.

## References
Use the [SRS](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md), [HLD](../01-High-Level-Design/01-High-Level-Design.md) and [user stories and scenarios](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#scenarios-and-models-user-stories-and-scenarios).

## Existing Design Records

## 1. Sources and experience boundaries

Use [EIF-D02 and interface requirements](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#requirements-specification-external-interface-requirements), [QSR-D03/Q-D25](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#requirements-specification-quality-security-and-recovery-requirements--id-resolution-q-d25), [source scenarios](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#scenarios-and-models-user-stories-and-scenarios) and [analysis interactions](../../03-System-Analysis/01-System-Analysis.md#analysis-behavioral-and-scenario-analysis--06-scenario-based-view). Required business meaning stays with the relevant component and source decision, not a button label or visual prototype.

The current design uses English interface copy with explicit manually maintained English/German professional content. Content language is separate from interface language, provider time zone and uploaded-document language. Automatic translation is outside accepted scope; fallback/completeness details retain their source status. Preserve the [accepted update/publication policy](../../02-Requirements-Engineering/01-Software-Requirements-Specification.md#change-and-baseline-open-questions-and-decisions--id-owner-accepted-profile-update-policy).

This file owns shared interaction behavior. [Component designs](../03-Low-Level-Design/02-Module-Breakdown.md#design-record-03-component-and-module-design-component-and-module-design-md) own operations and invariants; [API contracts](../03-Low-Level-Design/05-API-Specification.md#design-record-05-interface-and-api-design-01-api-protocols-contracts-and-compatibility-md) own result semantics; [Security](../01-High-Level-Design/14-Appendices.md#design-record-06-design-quality-and-security-analysis-02-security-threat-modeling-and-trust-boundaries-md) owns current authority/control design. Disabled or hidden UI alone never enforces permission.
