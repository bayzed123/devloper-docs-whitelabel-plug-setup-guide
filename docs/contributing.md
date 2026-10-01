# Contributing to the Docs

Each project guide should be updated from the project's source repository, not from memory. Record the repository URL and audited commit, then verify the package manifest, lockfile, environment template, migrations, scripts, CI workflows, deployment configuration, and any live URL.

## Update workflow

1. Clone the target repository at the intended branch.
2. Read the README and deployment documentation.
3. Inspect the source tree, package scripts, environment declarations, migrations, and workflows.
4. Run only safe local checks unless production authorization is explicit.
5. Capture a Playwright screenshot only for a reachable, public live URL; record the capture date and what it proves.
6. Update the matching page under `docs/projects/` and the project table on `docs/index.md`.
7. Run `smartgen-docs build` and check generated links and assets.
8. Commit the docs update with the audited commit references.

## Evidence labels

Use **source-verified** for behavior found in source or repository documentation. Use **runtime-verified** only after running the application. Use **live-verified** only after checking a public URL. Use **unknown** when access, credentials, DNS, provider state, or tests were unavailable.

## Safety rules

Never commit real environment files, tokens, customer data, or payment credentials. Treat sample products, prices, addresses, phone numbers, domains, and certification claims as placeholders until the owner verifies them. Do not claim a successful deployment based only on a workflow file.
