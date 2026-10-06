#!/usr/bin/env python3
"""Small demonstration tests for bundled synthetic log examples. Not a SIEM engine."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent

def main():
    ssh = (ROOT / "sample-ssh.log").read_text(encoding="utf-8").splitlines()
    web = (ROOT / "sample-web-access.log").read_text(encoding="utf-8").splitlines()

    ssh_hits = [line for line in ssh if "Failed password" in line or "authentication failure" in line]
    probe_hits = [line for line in web if any(path in line for path in ("/.env", "/.git/config", "/wp-config.php", "/.htpasswd"))]
    wp_hits = [line for line in web if re.search(r'"POST /wp-login\.php(?:\?| )', line)]

    assert len(ssh_hits) == 2, f"Expected 2 SSH failure matches, got {len(ssh_hits)}"
    assert len(probe_hits) == 2, f"Expected 2 sensitive-path probe matches, got {len(probe_hits)}"
    assert len(wp_hits) == 2, f"Expected 2 WordPress login endpoint matches, got {len(wp_hits)}"

    print(f"PASS: SSH authentication failure demo matched {len(ssh_hits)} lines")
    print(f"PASS: Sensitive-path probe demo matched {len(probe_hits)} lines")
    print(f"PASS: WordPress login endpoint demo matched {len(wp_hits)} lines")
    print("NOTE: These tests validate only the included demonstration logic, not a production SIEM parser.")

if __name__ == "__main__":
    main()
