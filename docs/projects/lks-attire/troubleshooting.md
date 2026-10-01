# LKS Attire: Troubleshooting

## Install or build failure

Confirm **Node 22 recommended**, use only the package manager matching the lockfile, and do not delete the lockfile to force installation. Compare the local command with the CI command.

## Environment failure

Check exact variable names, restart the development server after changes, and confirm bindings/resources exist in the selected environment. Redact secrets from logs.

## Domain or API failure

Verify DNS, HTTPS, `PUBLIC_URL`/API base URL, CORS, auth callbacks, Worker routes, Pages base path, and provider health. A live storefront does not prove API or checkout health.

## Data or payment failure

Check migrations, seed state, inventory, delivery zones, provider sandbox mode, webhook signatures, and idempotency. Never test payment or courier callbacks against production customer data.

## Project-specific warning

The latest five scheduled D1 backups were observed failed, latest during Export D1. Fix and verify backup/restore before relying on recovery. Replace placeholder contact, phone, email, domain, WhatsApp, and demo catalog.
