# Arif Gadget Store: Pipeline

CI runs Node 20, install, typecheck, web build, local D1 migrations, Worker startup, and API smoke tests. API deployment provisions resources, migrates, deploys, sets secrets, provisions the owner, and retries health. Pages deployment builds the SPA, writes 404.html/.nojekyll/CNAME, generates a sitemap, and publishes Pages.

## Release gate

A release is ready only when install, build, typecheck, unit tests, E2E tests, migrations, health checks, and the primary customer journey succeed on the same commit. A workflow file alone is not proof of a successful deployment.

## Client handoff record

Record the repository commit, runtime version, deployment URL, environment variables configured, migrations applied, admin owner, enabled integrations, test results, and rollback commit.
