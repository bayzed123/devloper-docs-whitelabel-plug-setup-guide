# LKS Attire: Environment

## Configuration groups

CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID, WORKER_NAME, BRAND, PALETTE, PUBLIC_URL, BOOTSTRAP_TOKEN, admin values, DB/KV/ASSETS, optional MEDIA/AI, and bKash, SSLCommerz, courier, SMS, WhatsApp, Resend, and Turnstile variables.

## Secret handling

Use the repository's example file as the starting point. Keep local values outside Git, configure production values in encrypted GitHub/Cloudflare settings, and rotate a secret immediately if it appears in a commit, log, screenshot, or chat. Client-visible variables are not secrets.

## Whitelabel variables

The main rebranding inputs are brand build configuration, generated tokens/assets, worker/wrangler.toml, catalog seed, public URL, and theme palette. Add a project-specific `.env.example` or configuration table when a new integration is introduced.
