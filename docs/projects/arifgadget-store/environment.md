# Arif Gadget Store: Environment

## Configuration groups

CLOUD_FLARE_API, CLOUD_FLARE_ACCOUNT_ID, ADMIN_USERNAME, ADMIN_PASSWORD, ADMIN_NAME, ADMIN_EMAIL, API_DOMAIN or WORKERS_SUBDOMAIN or API_BASE_URL, CUSTOM_DOMAIN, JWT_SECRET, ALLOWED_ORIGINS, and optional Steadfast, Google, Groq, Resend, Meta, and report-trigger variables.

## Secret handling

Use the repository's example file as the starting point. Keep local values outside Git, configure production values in encrypted GitHub/Cloudflare settings, and rotate a secret immediately if it appears in a commit, log, screenshot, or chat. Client-visible variables are not secrets.

## Whitelabel variables

The main rebranding inputs are web/CNAME, Vite base/API variables, worker configuration, storefront assets, catalog data, and API domain. Add a project-specific `.env.example` or configuration table when a new integration is introduced.
