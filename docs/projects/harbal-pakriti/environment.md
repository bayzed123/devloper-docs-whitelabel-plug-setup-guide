# Harbal Pakriti: Environment

## Configuration groups

CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID, ADMIN_USERNAME or ADMIN_EMAIL, ADMIN_PASSWORD, ADMIN_NAME, ENVIRONMENT, PUBLIC_URL, DB, KV, ASSETS, optional MEDIA, plus provider variables in docs/SETUP.md.

## Secret handling

Use the repository's example file as the starting point. Keep local values outside Git, configure production values in encrypted GitHub/Cloudflare settings, and rotate a secret immediately if it appears in a commit, log, screenshot, or chat. Client-visible variables are not secrets.

## Whitelabel variables

The main rebranding inputs are worker/wrangler.toml, project brand configuration, generated catalog/seed data, and the public URL. Add a project-specific `.env.example` or configuration table when a new integration is introduced.
