# Arif Gadget Store: Troubleshooting

## Install or build failure

Confirm **Node 20+**, use only the package manager matching the lockfile, and do not delete the lockfile to force installation. Compare the local command with the CI command.

## Environment failure

Check exact variable names, restart the development server after changes, and confirm bindings/resources exist in the selected environment. Redact secrets from logs.

## Domain or API failure

Verify DNS, HTTPS, `PUBLIC_URL`/API base URL, CORS, auth callbacks, Worker routes, Pages base path, and provider health. A live storefront does not prove API or checkout health.

## Data or payment failure

Check migrations, seed state, inventory, delivery zones, provider sandbox mode, webhook signatures, and idempotency. Never test payment or courier callbacks against production customer data.

## Project-specific warning

The storefront was live at https://arifgadget.store/ during audit, but api.arifgadget.store did not resolve. Rotate any credentials shared in docs, set ALLOWED_ORIGINS, close first-run owner setup, and test API/checkout before accepting orders.
