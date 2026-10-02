# Developer Docs

This is the reusable setup, feature, pipeline, deployment, and whitelabel rebranding documentation for Bayzed123 web projects.

> **Folder rule:** every project has its own directory. Do not create a single all-in-one project Markdown file. Use the separate Overview, Setup, Features, Environment, Pipeline, Deployment, Whitelabel Rebranding, and Troubleshooting pages for each client rebuild.

## Highlighted live showcase

Review the related [Demu client demo showcase](showcase/index.md) for verified storefront/admin screenshots, raw demo links, feature highlights, and the mapping between the public demos and these source repositories. The showcase uses fictional demo data and is separate from production deployment proof.

## Project guides

| Project | Guide folder | Architecture | Evidence |
|---|---|---|---|
| [Harbal Pakriti](projects/harbal-pakriti/index.md) | `projects/harbal-pakriti/` | Cloudflare Worker + Hono + D1/KV/R2 | Live proof: Prakriti Herbal storefront and admin both HTTP 200 |
| [Jewellery and Fashion](projects/jewellery-and-fashion/index.md) | `projects/jewellery-and-fashion/` | Cloudflare Worker + Hono + D1/KV/R2 | Live proof: Sidra Jewellery storefront and admin both HTTP 200 |
| [Babyshop](projects/babyshop/index.md) | `projects/babyshop/` | Cloudflare Worker + Hono + D1/KV/R2 | Live proof: Zamil Shop storefront and admin both HTTP 200 |
| [Arif Gadget Store](projects/arifgadget-store/index.md) | `projects/arifgadget-store/` | React/Vite Pages + Cloudflare Worker API | Live storefront reachable and screenshot captured |
| [LKS Attire](projects/lks-attire/index.md) | `projects/lks-attire/` | Cloudflare Worker + static storefront/admin | Live proof: storefront and admin both HTTP 200; backup warning remains |
| [Sidra Glow Studio](projects/sidra-glow-studio/index.md) | `projects/sidra-glow-studio/` | Supplied live Worker; source repository not supplied | Live proof only; source setup unknown |

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
├── troubleshooting.md    # project-specific recovery and diagnostic steps
└── live-proof.md         # live storefront/admin URLs, screenshots, and evidence limits
```

## Rebuild any client project

Read `index.md` first, then follow **Setup → Environment → Features → Pipeline → Deployment → Whitelabel Rebranding → Troubleshooting → Live Proof**. Confirm the audited commit, use the repository lockfile, test on a fresh database, keep client secrets isolated, replace placeholder content, and record the deployed commit. For a new client, keep the live URL and source repository mapped explicitly; do not infer the mapping from a brand name.

## Supplied live deployments

| Project guide | Storefront | Admin entry | Live proof |
|---|---|---|---|
| Harbal Pakriti | [Prakriti Herbal](https://prakriti-herbal.sayadmdbayezidhosan.workers.dev/) | [Admin](https://prakriti-herbal.sayadmdbayezidhosan.workers.dev/admin/) | [Screenshots and limits](projects/harbal-pakriti/live-proof.md) |
| Jewellery and Fashion | [Sidra Jewellery](https://sidra-jewellery.sayadmdbayezidhosan.workers.dev/) | [Admin](https://sidra-jewellery.sayadmdbayezidhosan.workers.dev/admin/) | [Screenshots and limits](projects/jewellery-and-fashion/live-proof.md) |
| Babyshop | [Zamil Shop BD](https://zamil-shop-bd-api.sayadmdbayezidhosan.workers.dev/) | [Admin](https://zamil-shop-bd-api.sayadmdbayezidhosan.workers.dev/admin/) | [Screenshots and limits](projects/babyshop/live-proof.md) |
| LKS Attire | [Lk's Attire](https://lks-attire.sayadmdbayezidhosan.workers.dev/) | [Admin](https://lks-attire.sayadmdbayezidhosan.workers.dev/admin/) | [Screenshots and limits](projects/lks-attire/live-proof.md) |
| Sidra Glow Studio | [Storefront](https://sidra-glow-studio.sayadmdbayezidhosan.workers.dev/) | [Admin](https://sidra-glow-studio.sayadmdbayezidhosan.workers.dev/admin/) | [Live-only proof](projects/sidra-glow-studio/live-proof.md) |

## Evidence policy

Source features and commands are based on repository audits. The five supplied storefront URLs returned HTTP 200 during Playwright verification; their `/admin/` routes returned HTTP 200 or HTTP 304 and rendered the admin entry surface. Each has storefront/admin screenshots in its project folder. HTTP status and screenshots prove route response at capture time; they do not prove authenticated admin access, database correctness, checkout, payments, backups, or security. The existing Arif Gadget live proof remains in its project folder as a separate confirmed domain.
