# Harbal Pakriti

Repository: [bayzed123/harbal-pakriti](https://github.com/bayzed123/harbal-pakriti)  
Audited commit: `dee93f14f76f0928b5dab27691498db7ce5a7134` on `main`

## What this project is

A Bangla-first bilingual Bangladesh herbal-products storefront and admin system. It runs as one Cloudflare Worker with a Hono API, static HTML/CSS/JavaScript UI, Cloudflare D1/SQLite, KV, and optional R2 media storage.

## Documented features

The source and project documentation cover catalogue search/filtering, variants and kits, kit builder, collections, journal and campaigns, accounts, wishlist, reviews, referrals, guest checkout, delivery-area fees, COD, manual bKash/Nagad/Rocket flows, optional bKash and SSLCommerz, order tracking, invoices, admin inventory and batches, expiry tracking, returns, reports, delivery zones, roles, audit logs, scheduled jobs, certification badges, and medical-claims checks.

Payment, courier, SMS, email, push, analytics, fraud, WhatsApp, and Turnstile features are configuration-dependent and were not runtime-tested.

## Local rebuild

Use Node 22 (the manifest requires Node 20+, while CI uses Node 22):

```bash
npm ci
cp worker/.dev.vars.example worker/.dev.vars
npm run build
npm run db:migrate:local
npm run db:seed:local
node scripts/create-admin.mjs
npm run dev
```

The documented local URL is `http://localhost:8787`; the admin area is `/admin/`. Create the first Super Admin from the generated SQL, apply it to local D1, then delete the temporary SQL file. First sign-in requires TOTP setup.

## Scripts and pipeline

Key scripts are `build`, `typecheck`, `dev`, `db:migrate:local`, `db:migrate:remote`, `db:seed:local`, `db:seed:remote`, `admin:create`, `test`, `test:e2e`, and `deploy`. CI runs install, build, TypeScript checks, script parsing, Vitest, and Playwright mobile/desktop tests. Main-branch deployment provisions D1/KV/R2, migrates, seeds only an empty database, creates an admin only when none exists, deploys the Worker, syncs optional secrets, smoke-tests, and runs Doctor. Scheduled Doctor checks are read-only.

## Production variables

Required deployment secrets are `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`. Initial admin values are `ADMIN_USERNAME` or `ADMIN_EMAIL`, `ADMIN_PASSWORD`, and optional `ADMIN_NAME`. Runtime values include `ENVIRONMENT` and `PUBLIC_URL`; bindings include `DB`, `KV`, `ASSETS`, and optional `MEDIA`. Provider variables are documented in the repository's `docs/SETUP.md`, including bKash, SSLCommerz, courier, SMS, WhatsApp, Resend, VAPID, Meta, GA4, and Turnstile credentials.

## Deployment checklist

Replace placeholder contact details, delivery fees, catalog, prices, stock, batches, and certification claims. Provision valid Cloudflare resources, configure DNS and `PUBLIC_URL`, rotate or remove `BOOTSTRAP_TOKEN` after bootstrap, test payment and courier callbacks in sandbox, verify backups and restore, then release the audited commit.

## Known limits

No live homepage was present in GitHub metadata. Build, tests, deployment, integrations, DNS, and security headers were inspected but not executed in this audit. D1/KV IDs are placeholders until provisioning runs.

## Live proof

The supplied deployment URLs and Playwright storefront/admin screenshots are recorded in the [Live Proof](live-proof.md) page.
