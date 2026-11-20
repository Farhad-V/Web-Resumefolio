# 8. Security Implementation

[Low-Level Design index](03-Low-Level-Design.md)

## 8.1 Input Validation
Validate shape, length, scope and state. Keep access checks on the server for browser, API, Git and direct file entry points.

## 8.2 Password and Token Handling
Use framework password hashing and explicit credential expiry and revocation. Keep signing keys and machine credentials server-side and outside version control.

## 8.3 Access Control
Check actor, resource, action and current grant. Keep employer content scope and repository roles independent. Deny access when required authority cannot be established.
