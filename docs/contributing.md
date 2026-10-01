# Contributing to the Docs

## Folder rule

Each repository gets its own folder under `docs/projects/<project-name>/`. Keep the guide split into these pages:

- `index.md`: identity, repository, audited commit, stack, and evidence status
- `setup.md`: prerequisites, installation, local database, admin, and first run
- `features.md`: customer, admin, and integration capabilities
- `environment.md`: variables, bindings, secrets, and brand configuration
- `pipeline.md`: CI, tests, migrations, release gates, and handoff record
- `deployment.md`: provisioning, production sequence, verification, and launch risks
- `whitelabel.md`: client rebranding, content replacement, domain, and acceptance checklist
- `troubleshooting.md`: diagnostics and recovery

Do not add a replacement single Markdown file for the whole project.

## Update workflow

Clone the target repository at the intended branch, record the audited commit, inspect the README, package manifest, lockfile, environment declarations, migrations, scripts, CI workflows, and deployment configuration, then update only the relevant page(s). Capture a Playwright screenshot only for a reachable public URL and state exactly what it proves.

Run `smartgen-docs build`, check all generated pages and image assets, commit the source and generated site, and verify the GitHub Actions deployment.

## Whitelabel standards

Never reuse another client's credentials, database, media bucket, admin account, webhook secret, payment account, or analytics property. Treat sample contacts, domains, catalog, prices, stock, and certification claims as placeholders. A client handoff is complete only when the rebranded metadata, content, domain, integrations, backups, admin roles, privacy, and rollback have been verified.
