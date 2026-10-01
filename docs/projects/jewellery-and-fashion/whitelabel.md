# Jewellery and Fashion: Whitelabel Rebranding

This page is the repeatable client handoff recipe for creating a new brand from this project without copying secrets or production data.

## Brand replacement order

1. Create a client brand record: name, logo, favicon, colors, typography, language, domain, contact channels, address, social links, and support hours.
2. Replace storefront title, metadata, Open Graph image, footer, policy links, delivery text, payment instructions, transactional email/SMS templates, and WhatsApp links.
3. Replace demo products, images, categories, variants, prices, discounts, stock, delivery zones, and seed data.
4. Configure the client domain, API origin, CORS allowlist, auth callbacks, sitemap, robots rules, PWA manifest, and canonical URLs.
5. Configure only the client's integrations and store credentials in the provider secret manager.
6. Rebuild, migrate a fresh database, seed reviewed content, create the client owner, and test the complete shopping journey.

## Project-specific touchpoints

For this project, update **project brand configuration, storefront/admin assets, worker/wrangler.toml, public URL, catalog, and seed SQL.**. Keep a separate client checklist and never reuse another client's database, admin account, payment credentials, media bucket, webhook secret, or analytics property.

## Acceptance checklist

- [ ] No previous brand name remains in source, metadata, assets, emails, or generated HTML.
- [ ] No sample phone, email, address, price, product, or certification claim remains.
- [ ] Client domain and API origin work over HTTPS.
- [ ] Client payment, courier, notification, analytics, and bot-protection integrations are tested or explicitly disabled.
- [ ] Admin owner, staff roles, backups, privacy, retention, and rollback are documented.
