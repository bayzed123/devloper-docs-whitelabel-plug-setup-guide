# Babyshop: Pipeline

CI builds, typechecks, parses scripts, runs Vitest, installs Chromium, and runs Playwright mobile/desktop tests. Main deployment provisions resources, migrates, seeds only an empty catalog, creates an admin, deploys, syncs secrets, smoke-tests, and runs Doctor. Daily Doctor is read-only.

## Release gate

A release is ready only when install, build, typecheck, unit tests, E2E tests, migrations, health checks, and the primary customer journey succeed on the same commit. A workflow file alone is not proof of a successful deployment.

## Client handoff record

Record the repository commit, runtime version, deployment URL, environment variables configured, migrations applied, admin owner, enabled integrations, test results, and rollback commit.
