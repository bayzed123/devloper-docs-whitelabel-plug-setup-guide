# Arif Gadget Store: Setup

Repository: https://github.com/bayzed123/arifgadget.store

## Prerequisites

Use **Node 20+**, Git, and the package manager selected by the committed lockfile. Never commit a real environment file or generated admin SQL.

## Clean local setup

```bash
npm install
printf 'JWT_SECRET=local-dev-secret\n' > worker/.dev.vars
npm run migrate:local --workspace worker
npm run dev:api
# second terminal
npm run dev:web
```

Local application URL: `127.0.0.1:5173 (web) and 127.0.0.1:8787 (API)`. Admin entry: `API admin routes/dashboard`. The exact local database command may require the project Wrangler configuration; use the repository's documented command if it differs.

## Verification

After startup, open the homepage, browse products, test search and filters, add/remove a cart item, verify delivery and checkout validation, and test the admin login only with local data. Then run the project's typecheck, unit test, E2E, and production build commands.
