# Harbal Pakriti: Pipeline

CI runs npm ci, build, TypeScript, script parsing, Vitest, and Playwright mobile/desktop tests. Main deployment provisions resources, migrates, seeds only an empty DB, creates an admin only when none exists, deploys, syncs secrets, smoke-tests, and runs Doctor. Doctor is scheduled and read-only.

## Release gate

A release is ready only when install, build, typecheck, unit tests, E2E tests, migrations, health checks, and the primary customer journey succeed on the same commit. A workflow file alone is not proof of a successful deployment.

## Client handoff record

Record the repository commit, runtime version, deployment URL, environment variables configured, migrations applied, admin owner, enabled integrations, test results, and rollback commit.
