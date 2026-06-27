# API and Data Notes — Web Application Example

## Candidate data objects

```text
Issue
IssueCategory
IssueComment
IssueStatusHistory
User
Role
AttachmentMetadata
AuditLogEntry
```

## Candidate API areas

```text
POST /issues
GET /issues
GET /issues/{id}
PATCH /issues/{id}/status
POST /issues/{id}/comments
GET /categories
POST /admin/categories
GET /reports/summary
```

## Review-gated areas

```text
- authentication;
- authorization;
- personal data;
- location data;
- audit logs;
- file attachments;
- public visibility rules.
```
