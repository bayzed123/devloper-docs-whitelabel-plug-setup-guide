# Developer Docs

This is the reusable setup and deployment guide for Bayzed123 web projects. Each project page is based on a static audit of the repository's source, package manifests, environment documentation, and CI/CD workflows.

> **Evidence rule:** a feature listed in source or README documentation is labeled as documented/source-verified. A live URL, deployment, test run, payment integration, or browser behavior is only labeled verified when it was actually checked.

## Project guides

| Project | Architecture | Evidence status |
|---|---|---|
| [Harbal Pakriti](projects/harbal-pakriti.md) | Cloudflare Worker + Hono + D1/KV/R2 | Repository audited; live deployment not confirmed |
| [Jewellery and Fashion](projects/jewellery-and-fashion.md) | Cloudflare Worker + Hono + D1/KV/R2 | Repository audited; live deployment not confirmed |
| [Babyshop](projects/babyshop.md) | Cloudflare Worker + Hono + D1/KV/R2 | Repository audited; live deployment not confirmed |
| [Arif Gadget Store](projects/arifgadget-store.md) | React/Vite Pages + Cloudflare Worker API | **Live storefront reachable and screenshot captured** |
| [LKS Attire](projects/lks-attire.md) | Cloudflare Worker + static storefront/admin | Repository audited; backup failures need attention |

## Rebuild any project from this guide

1. Open the project guide and confirm the repository URL and audited commit.
2. Install the runtime version and dependencies using the repository lockfile.
3. Copy the documented environment template and configure local-only values.
4. Run the build, migrations, seed, admin bootstrap, and local server commands in order.
5. Run type checks, unit tests, and end-to-end tests before deployment.
6. Configure provider secrets and bindings in the hosting platform.
7. Deploy through the tested CI/CD pipeline, then run health and smoke checks.
8. Replace placeholders, verify customer-facing content, and record the deployed commit.

## Common architecture pattern

Four projects are Cloudflare Worker storefronts with Hono APIs, D1 databases, KV, optional R2 media, and scheduled jobs. They share similar Bangladesh e-commerce integrations such as COD, manual mobile-wallet payments, courier tracking, SMS, email, WhatsApp, analytics, and Turnstile. Arif Gadget Store is the exception: its frontend is a React/Vite GitHub Pages SPA and its API runs separately on Cloudflare Workers.

## Live evidence

The only live domain confirmed during this audit was `https://arifgadget.store/`. Its home page was captured with Playwright and included in the Arif Gadget guide. The repository metadata for the remaining projects did not provide a confirmed homepage, so no live screenshots are claimed for them.
