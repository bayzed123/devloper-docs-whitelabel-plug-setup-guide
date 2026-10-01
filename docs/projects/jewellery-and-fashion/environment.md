# Jewellery and Fashion: Environment

## Configuration groups

CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID, WORKER_NAME, PUBLIC_URL, admin bootstrap values, DB/KV/ASSETS, optional MEDIA/AI, and payment, courier, SMS, WhatsApp, email, push, Meta/GA4, and Turnstile variables from docs/SETUP.md.

## Secret handling

Use the repository's example file as the starting point. Keep local values outside Git, configure production values in encrypted GitHub/Cloudflare settings, and rotate a secret immediately if it appears in a commit, log, screenshot, or chat. Client-visible variables are not secrets.

## Whitelabel variables

The main rebranding inputs are project brand configuration, storefront/admin assets, worker/wrangler.toml, public URL, catalog, and seed SQL. Add a project-specific `.env.example` or configuration table when a new integration is introduced.
