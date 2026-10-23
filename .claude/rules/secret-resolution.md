# secret-resolution

## binding

Use GitHub CLI's native macOS Keychain login for local GitHub operations across projects. Do not require 1Password enrollment, export the token, or request repeated sign-ins when a session cannot access Keychain. Verify through an authenticated endpoint in a permitted execution context; report access failures explicitly. Read the full rule before troubleshooting.

Other managed secrets use secrets-v1 (`secret://<namespace>/<key>`) and configured providers. Never hardcode credentials or print them. `${VAR}` references in files require a documented injector. Literals are covered by `no-secret-exposure`.

Full rule: `$HOME/projects/active/0-llm-root/rules/secret-resolution.md`.
