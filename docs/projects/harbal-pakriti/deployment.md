# Harbal Pakriti: Deployment

## Target platform

Cloudflare Worker + Hono + D1/KV/optional R2

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

Replace sample products, prices, delivery fees, contacts, certification claims, and placeholder Cloudflare IDs. Rotate BOOTSTRAP_TOKEN after bootstrap.
