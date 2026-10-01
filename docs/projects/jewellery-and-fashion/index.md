# Jewellery and Fashion

Repository: [bayzed123/jewellery-and-Fashion-](https://github.com/bayzed123/jewellery-and-Fashion-)  
Audited commit: `99207c9b02862faf6f7f2437c0d1483a39e2d89d` on `main`

## What this project is

A bilingual jewellery e-commerce storefront, admin dashboard, and Hono API on Cloudflare Workers. The frontend is static HTML/CSS/browser JavaScript; the backend uses TypeScript, D1, KV, optional R2, and optional Workers AI.

## Documented features

The repository documents a mobile storefront and PWA, shop/search/filtering, collections and sets, gift finder, cart, Bangladesh delivery fees, coupons, referrals, gift wrap, guest checkout, checkout OTP and Turnstile hooks, abandoned-checkout recovery, accounts, addresses, wishlists, registries, returns, invoices, order tracking, and admin modules for orders, products, inventory, reports, staff, settings, delivery zones, and audit logs.

COD, manual bKash/Nagad/Rocket, optional bKash API, SSLCommerz, Steadfast, SMS, WhatsApp, email, web push, Meta CAPI, and analytics require provider setup. Nagad API and RedX are documented as reserved.

## Local rebuild

Use Node 22 because the locked Wrangler version requires it:

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

Open `http://localhost:8787`; the admin path is `/admin/`.

## Scripts and pipeline

Use `build`, `typecheck`, `dev`, migration and seed scripts, `admin:create`, `test`, `test:e2e`, and `deploy`. CI runs Node 22, install, build, TypeScript, script syntax checks, Vitest, Chromium, and Playwright. Main deployment provisions D1/KV/R2, migrates, seeds, conditionally creates the first admin, deploys, syncs secrets, smoke-tests `/api/health`, and runs Doctor. Manual deployment can bypass the successful-CI gate, so protect production with branch/ref restrictions and approvals.

## Production variables

Configure `CLOUDFLARE_API_TOKEN`, `CLOUDFLARE_ACCOUNT_ID`, optional `WORKER_NAME` and `PUBLIC_URL`, admin bootstrap values, Worker bindings, and the integration groups documented in `docs/SETUP.md`: payment, courier/fraud, SMS/WhatsApp/email, push, Meta/GA4, and Turnstile.

## Deployment checklist

Replace placeholder domain, contact, location, catalog, prices, and stock. Use Node 22, replace placeholder Cloudflare IDs through provisioning, configure DNS and custom routes, verify CORS and auth callbacks, test payment modes and webhooks, and confirm the first-admin bootstrap is closed after setup.

## Known limits

No live homepage was present in GitHub metadata. Tests and deployment were not run during the audit. Customer data and abandoned-checkout records require explicit access, retention, consent, provider, and backup controls. The repository has no visible dependency vulnerability audit or static security scan.

## Live proof

The supplied deployment URLs and Playwright storefront/admin screenshots are recorded in the [Live Proof](live-proof.md) page.
