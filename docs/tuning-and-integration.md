# Tuning and integration notes

## SSH

Use a SIEM aggregation rule for a configurable number of failures per source IP within a time window (for example, 5 or more failures in 5 minutes as an initial lab threshold). This is a sample starting point, not a universal recommendation. Exclude known monitoring sources only after validating them.

## Web probes

Match normalized URL paths rather than raw request strings where possible. Consider URL encoding, query strings, case sensitivity, and reverse-proxy behavior. A 404 response can still be useful evidence of probing; it does not mean the requested file existed.

## WordPress

A POST to `/wp-login.php` is not proof of a failed login. Prefer WordPress security/audit plugin events or application-level authentication logs to confirm outcomes. Otherwise label this scenario as repeated login endpoint activity, not confirmed brute force.

## Privacy

Minimize collected fields, restrict access to logs, define retention, and redact credentials, tokens, cookies, and personal data. Do not publish raw production logs.
