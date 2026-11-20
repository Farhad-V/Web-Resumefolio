# 7. Error Handling And Logging

[Low-Level Design index](03-Low-Level-Design.md)

## 7.1 Error Categories
Represent input, authority, conflict, dependency and unexpected failures separately. Convert them at the application boundary into the documented response.

## 7.2 Error Codes
Use the [API error contract](05-API-Specification.md#mvp-api-contracts) for status codes and safe public errors. Preserve the correlation ID for investigation.

## 7.3 Logging
Use structured severity, timestamp, correlation ID, operation, outcome and safe resource metadata. Log recoverable conditions as warnings and unexpected failures as errors. Exclude raw tokens, passwords and private material.
