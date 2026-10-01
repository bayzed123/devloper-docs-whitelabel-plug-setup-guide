# Babyshop

Repository: [bayzed123/babyshop](https://github.com/bayzed123/babyshop)  
Audited commit: `c83e6a4` on `main`

## What this project is

A bilingual Bangladesh baby-and-kids e-commerce storefront branded Zamil Shop BD. Static storefront and admin routes plus a TypeScript/Hono API run on one Cloudflare Worker with D1, KV, and optional R2.

## Documented features

The source covers catalogue, categories, search and filters, product details, cart, guest checkout, delivery zones, coupons, referrals, gift wrap, OTP, order tracking, PDF invoices, accounts, addresses, wishlists, registries, returns, reminders, gift finder, inventory and variants, reviews, back-in-stock, admin operations, courier hooks, marketing analytics, WhatsApp/email/SMS, web push, Turnstile, scheduled jobs, backups, and a PWA shell.

COD and manual bKash/Nagad/Rocket flows are available. bKash Tokenized Checkout and SSLCommerz are conditional integrations; Nagad is explicitly a stub and RedX uses staff-entered tracking.

## Local rebuild

```bash
npm ci
cp worker/.dev.vars.example worker/.dev.vars
npm run build
npm run db:migrate:local
npm run db:seed:local
node scripts/create-admin.mjs "Owner" owner super_admin 'A-Long-Password-123' > .admin.sql
npx wrangler d1 execute DB --local -c worker/wrangler.toml --file=.admin.sql
rm .admin.sql
npm run dev
```

The documented local shop is `http://localhost:8787`; admin is `/admin/`. Run `npm run typecheck`, `npm test`, and `npm run test:e2e` before deployment.

## Scripts and pipeline

Key scripts include build, typecheck, dev, local/remote migration and seed, admin creation, geo generation, test, E2E, and deploy. CI installs, builds, typechecks, parses scripts, runs Vitest, installs Chromium, and runs Playwright mobile/desktop tests. Main deployment provisions D1/KV/R2, applies migrations, seeds only an empty catalog, creates an admin when credentials are present, deploys, syncs secrets, smoke-tests health, and runs Doctor. Daily Doctor is read-only.

## Production variables

Required deployment secrets are `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`. Configure admin bootstrap values, `WORKER_NAME`, `PUBLIC_URL`, `BOOTSTRAP_TOKEN`, runtime vars and bindings, then add optional bKash, SSLCommerz, courier, fraud, SMS, WhatsApp, Resend, VAPID, Meta, GA4, and Turnstile settings.

## Deployment checklist

Replace sample domain, contact, location, catalog, images, prices, and stock. Verify payment modes in the intended sandbox or production mode, configure Cloudflare routes and DNS, set consent and PII retention rules, confirm backups and restore, and protect manual workflow dispatch with production approvals.

## Known limits

No live homepage was present in GitHub metadata. This audit did not run tests or deployment. bKash defaults to sandbox unless configured otherwise; provider onboarding is required. Customer PII is present in application data and backups.

## Live proof

The supplied deployment URLs and Playwright storefront/admin screenshots are recorded in the [Live Proof](live-proof.md) page.
