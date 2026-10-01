# Babyshop: Environment

## Configuration groups

CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID, WORKER_NAME, PUBLIC_URL, BOOTSTRAP_TOKEN, admin values, ENVIRONMENT, DB/KV/ASSETS, optional MEDIA, and payment, courier, fraud, SMS, WhatsApp, email, push, Meta/GA4, and Turnstile variables.

## Secret handling

Use the repository's example file as the starting point. Keep local values outside Git, configure production values in encrypted GitHub/Cloudflare settings, and rotate a secret immediately if it appears in a commit, log, screenshot, or chat. Client-visible variables are not secrets.

## Whitelabel variables

The main rebranding inputs are brand configuration, PWA assets, catalog seed, worker bindings, public URL, and delivery/payment settings. Add a project-specific `.env.example` or configuration table when a new integration is introduced.
