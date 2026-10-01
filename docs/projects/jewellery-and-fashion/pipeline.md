# Jewellery and Fashion: Pipeline

CI installs Node 22, builds, typechecks, parses scripts, runs Vitest and Playwright. Main deployment provisions D1/KV/R2, migrates, seeds, creates the first admin, deploys, syncs secrets, smoke-tests /api/health, and runs Doctor. Restrict manual dispatch to approved refs.

## Release gate

A release is ready only when install, build, typecheck, unit tests, E2E tests, migrations, health checks, and the primary customer journey succeed on the same commit. A workflow file alone is not proof of a successful deployment.

## Client handoff record

Record the repository commit, runtime version, deployment URL, environment variables configured, migrations applied, admin owner, enabled integrations, test results, and rollback commit.
