# Developer Docs

This is the reusable setup, feature, pipeline, deployment, and whitelabel rebranding documentation for Bayzed123 web projects.

> **Folder rule:** every project has its own directory. Do not create a single all-in-one project Markdown file. Use the separate Overview, Setup, Features, Environment, Pipeline, Deployment, Whitelabel Rebranding, and Troubleshooting pages for each client rebuild.

## Project guides

| Project | Guide folder | Architecture | Evidence |
|---|---|---|---|
| [Harbal Pakriti](projects/harbal-pakriti/index.md) | `projects/harbal-pakriti/` | Cloudflare Worker + Hono + D1/KV/R2 | Repository audited; live deployment not confirmed |
| [Jewellery and Fashion](projects/jewellery-and-fashion/index.md) | `projects/jewellery-and-fashion/` | Cloudflare Worker + Hono + D1/KV/R2 | Repository audited; live deployment not confirmed |
| [Babyshop](projects/babyshop/index.md) | `projects/babyshop/` | Cloudflare Worker + Hono + D1/KV/R2 | Repository audited; live deployment not confirmed |
| [Arif Gadget Store](projects/arifgadget-store/index.md) | `projects/arifgadget-store/` | React/Vite Pages + Cloudflare Worker API | Live storefront reachable and screenshot captured |
| [LKS Attire](projects/lks-attire/index.md) | `projects/lks-attire/` | Cloudflare Worker + static storefront/admin | Repository audited; backup failures need attention |

## Standard project folder

Every project folder follows this structure:

```text
projects/<project-name>/
├── index.md              # project identity, stack, audited commit, evidence
├── setup.md              # clean local setup and first run
├── features.md           # source-verified product and admin features
├── environment.md        # secrets, bindings, integrations, and brand settings
├── pipeline.md           # CI, tests, migrations, release gates
├── deployment.md         # production provisioning and launch sequence
├── whitelabel.md         # reusable client rebranding and content replacement
└── troubleshooting.md    # project-specific recovery and diagnostic steps
```

## Rebuild any client project

Read `index.md` first, then follow **Setup → Environment → Features → Pipeline → Deployment → Whitelabel Rebranding → Troubleshooting**. Confirm the audited commit, use the repository lockfile, test on a fresh database, keep client secrets isolated, replace placeholder content, and record the deployed commit.

## Evidence policy

Source features and commands are based on repository audits. Live behavior is only claimed when tested. `https://arifgadget.store/` was reachable during the audit and has a Playwright screenshot in its folder. The other projects had no confirmed homepage in GitHub metadata, so no unverified live screenshots are claimed.
