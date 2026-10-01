# LKS Attire: Pipeline

CI builds brand assets, typechecks, runs Vitest and Playwright Chromium, then deploys after provisioning D1/KV/R2, migrating, seeding, and optionally creating an admin. Health is retried up to five times. Scheduled D1 backups run separately.

## Release gate

A release is ready only when install, build, typecheck, unit tests, E2E tests, migrations, health checks, and the primary customer journey succeed on the same commit. A workflow file alone is not proof of a successful deployment.

## Client handoff record

Record the repository commit, runtime version, deployment URL, environment variables configured, migrations applied, admin owner, enabled integrations, test results, and rollback commit.
