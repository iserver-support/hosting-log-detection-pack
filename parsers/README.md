# Parser notes

## SSH authentication logs

Common sources:
- Debian/Ubuntu: `/var/log/auth.log`
- RHEL-family: `/var/log/secure`

Example message:
`Failed password for invalid user admin from 203.0.113.10 port 51422 ssh2`

Useful normalized fields: `event.action=authentication_failure`, `user.name`, `source.ip`, `source.port`, `network.transport=ssh`.

## Apache/Nginx access logs

Common combined-log format resembles:
`198.51.100.24 - - [07/Oct/2026:10:11:12 +0000] "GET /.env HTTP/1.1" 404 153 "-" "ExampleScanner/1.0"`

Extract at least `source.ip`, `http.request.method`, `url.path`, `http.response.status_code`, and `user_agent.original`.

## WordPress login attempts

In access logs, repeated `POST /wp-login.php` requests are only a proxy for login attempts. A 200 status can represent a login page or failed login response, and status alone does not reliably prove whether authentication failed. For high-confidence results, combine web access logs with WordPress/application authentication events when available.
