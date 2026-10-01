# LKS Attire

Repository: [bayzed123/lks-attire](https://github.com/bayzed123/lks-attire)  
Audited commit: `f8b3c7ab2c1a1a628e4a8c45bf842571576da90c` on `main`

## What this project is

A bilingual Bangla/English mobile-first fashion storefront and admin system on Cloudflare Workers. It uses Hono, TypeScript, D1, KV, Worker Static Assets, optional R2, optional Workers AI, Vitest, and Playwright.

## Documented features

The source covers browse/search/category/product/cart/checkout, guest checkout, accounts, tracking, wishlist, reviews, size guide, variants and stock, discounts and coupons, Bangladesh address and delivery zones, invoices, admin orders/products/inventory/customers/coupons/banners/reviews/zones/staff/reports/settings/help/audit, SEO/sitemap/structured data, PWA, and brand-configurable themes.

COD and manual bKash/Nagad/Rocket are supported. bKash Tokenized and SSLCommerz are conditional; Nagad API is explicitly a stub, and Pathao/RedX booking is not implemented.

## Local rebuild

```bash
npm ci
cp .dev.vars.example .dev.vars
npm run build
npm run db:migrate:local
npm run db:seed:local
node scripts/create-admin.mjs "Owner" owner@example.com 'Choose-A-Long-Password' > /tmp/admin.sql
npx wrangler d1 execute DB --local --file=/tmp/admin.sql
rm /tmp/admin.sql
npm run dev
```

The documented local storefront is `http://localhost:8787`; admin is `/admin/`. Run `npm run typecheck`, `npm test`, and `npm run test:e2e` before deployment.

## Scripts and pipeline

Use `brand:build`/`build`, typecheck, dev, migration and seed scripts, admin creation, test, E2E, and deploy. CI installs Node 22, builds brand assets, typechecks, runs Vitest and Playwright Chromium, then deploys after provisioning D1/KV/R2, migrating, seeding, and optionally creating an admin. Deployment health is retried up to five times and links are published in the workflow summary.

## Production variables

Required secrets are `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`; configure admin values, `WORKER_NAME`, `BRAND`, `PALETTE`, `PUBLIC_URL`, `BOOTSTRAP_TOKEN`, bindings, and the documented bKash, SSLCommerz, courier, SMS, WhatsApp, Resend, Turnstile, and optional AI variables. Secret presence could not be verified because the GitHub secrets API returned 403.

## Deployment checklist

Replace placeholder contact, phone, email, domain, WhatsApp number, and demo catalog. Configure custom routes and `PUBLIC_URL`, verify media storage and R2 backup behavior, test all configured payment and notification integrations, and close the admin bootstrap path.

## Critical pipeline warning

The latest five scheduled D1 backup workflow runs were observed as failed; the latest failed during **Export D1**, and artifact upload was skipped. The exact cause is unknown. Fix and verify a successful backup plus restore before treating this project as production-ready.

## Known limits

No live homepage was present in GitHub metadata. Tests, deployment, and security controls were inspected but not independently executed. Cloudflare IDs are placeholders until provisioning runs.

## Live proof

The supplied deployment URLs and Playwright storefront/admin screenshots are recorded in the [Live Proof](live-proof.md) page.
