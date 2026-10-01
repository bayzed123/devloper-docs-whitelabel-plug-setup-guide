# Skin-care-shop: Production Deployment

The correct deployment target cannot be selected until the framework and runtime are confirmed. A static frontend, server-rendered app, and full-stack app have different hosting requirements.

## Deployment decision

| Application shape | Suitable target | Required confirmation |
|---|---|---|
| Static frontend | GitHub Pages, Cloudflare Pages, Netlify, or similar | Build output directory and client-side routing fallback |
| Server-rendered app | Vercel, Netlify, a Node host, or equivalent | Runtime version, start command, and server environment |
| Full-stack app | Provider with frontend, API, database, and secret support | Migrations, backups, CORS, auth callbacks, and service credentials |

## Pre-deployment checklist

- [ ] Repository access and framework are confirmed.
- [ ] Production build succeeds in CI.
- [ ] All required production variables are configured securely.
- [ ] API URLs, auth callback URLs, CORS, and allowed origins use the production domain.
- [ ] No development credentials or localhost URLs remain.
- [ ] Client-side routes have a fallback configuration where needed.
- [ ] Images and static assets use production-safe paths.
- [ ] Error monitoring and analytics are configured if required.
- [ ] A rollback commit or previous deployment is available.

## Verify after deployment

1. Open the production URL in a private browser window.
2. Test the primary shopping journey from landing page to checkout/contact completion.
3. Refresh a nested route directly.
4. Test the mobile viewport.
5. Inspect browser console and network failures.
6. Confirm secrets are not present in generated client bundles.
7. Record the deployed commit SHA and date in the release notes.

Do not publish provider-specific commands until the app repository's build output and deployment configuration have been inspected.
