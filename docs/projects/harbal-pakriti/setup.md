# Harbal Pakriti: Setup

Repository: https://github.com/bayzed123/harbal-pakriti

## Prerequisites

Use **Node 22**, Git, and the package manager selected by the committed lockfile. Never commit a real environment file or generated admin SQL.

## Clean local setup

```bash
npm ci
cp worker/.dev.vars.example worker/.dev.vars
npm run build
npm run db:migrate:local
npm run db:seed:local
npm run dev
```

Local application URL: `http://localhost:8787`. Admin entry: `/admin/`. The exact local database command may require the project Wrangler configuration; use the repository's documented command if it differs.

## Verification

After startup, open the homepage, browse products, test search and filters, add/remove a cart item, verify delivery and checkout validation, and test the admin login only with local data. Then run the project's typecheck, unit test, E2E, and production build commands.
