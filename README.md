# Hosting Log Detection Pack

Example parsers and detection scenarios for common hosting logs. The pack includes Sigma-style rules, sample log lines, lightweight Python tests, and setup notes.

## Detection coverage

- SSH: repeated failed authentication attempts from the same source IP
- Apache/Nginx: suspicious automated requests to common sensitive paths and exploit probes
- WordPress: repeated failed login attempts against `wp-login.php`

## Repository layout

- `rules/` — Sigma-style YAML detection rules
- `parsers/` — field extraction patterns and normalized field notes
- `tests/` — synthetic sample logs and test runner
- `docs/` — tuning, limitations, and integration notes

## Quick start

Requires Python 3.9+ for the lightweight sample tests.

```bash
python3 tests/run_tests.py
```

The test runner uses synthetic lines and simple matching logic to demonstrate expected detections. It is not a production SIEM engine and does not replace testing rules in your own log pipeline.

## Detection scenarios

| Scenario | Input source | Expected signal |
|---|---|---|
| SSH brute-force-like activity | `/var/log/auth.log` or `/var/log/secure` | Multiple failed password/public-key authentication messages from one IP |
| Sensitive-path probing | Apache/Nginx access logs | Requests to paths such as `/.env`, `/.git/config`, or `/wp-config.php` |
| WordPress login failures | Apache/Nginx access logs | Repeated POST requests to `/wp-login.php` returning a failure-like status |

## Tuning and safe use

These are starting-point detections, not proof of compromise. Legitimate scanners, monitoring tools, NAT gateways, misconfigured clients, and authorized security testing can create similar events. Tune thresholds to your traffic and aggregate by reliable source fields. Consider trusted proxy configuration before treating an access-log client IP as the actual origin.

The sample test harness proves only that the bundled synthetic test cases match the demonstration logic. Validate the YAML and adapt field names for your SIEM or log shipper before production use.

## Related resource

For broader hosting security and server protection information, see [iServerSupport Server Security Service](https://iserversupport.com/server-security-service/).

## Contributions

Please include sanitized or synthetic test cases, identify the target log format and SIEM version, and document false-positive considerations. Never commit real customer logs, credentials, session cookies, or tokens.
