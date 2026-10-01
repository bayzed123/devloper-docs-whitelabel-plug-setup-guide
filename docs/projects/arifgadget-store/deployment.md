# Arif Gadget Store: Deployment

## Target platform

React 18/Vite GitHub Pages SPA + Hono Cloudflare Worker API + D1/KV/optional R2/AI

## Deployment sequence

1. Replace placeholder brand and business data.
2. Provision the required database, KV, storage, Worker/API, and Pages resources.
3. Configure secrets and public runtime variables.
4. Apply migrations and seed only intended initial data.
5. Create the first admin and close bootstrap access.
6. Deploy the tested commit through CI/CD.
7. Verify domain, HTTPS, API health, nested routes, assets, checkout, notifications, and admin access.
8. Confirm backups and restore before launch.

## Project warning

The storefront was live at https://arifgadget.store/ during audit, but api.arifgadget.store did not resolve. Rotate any credentials shared in docs, set ALLOWED_ORIGINS, close first-run owner setup, and test API/checkout before accepting orders.
