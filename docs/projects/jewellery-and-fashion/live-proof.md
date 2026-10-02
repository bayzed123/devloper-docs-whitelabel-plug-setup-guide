# Jewellery and Fashion: Live Proof

## Evidence status

The storefront route returned **HTTP 200** during the longer Playwright verification pass. The admin route returned **HTTP 304** and rendered the page title **স্টাফ সাইন ইন — Sidra Jewellery & Fashion**.

> HTTP status and screenshots prove that the routes responded at capture time. They do not prove authenticated admin access, database correctness, payment success, checkout completion, backups, or security. The admin screenshots show the public entry/login surface only; no credentials were entered.

## Live links

- Storefront: [https://sidra-jewellery.sayadmdbayezidhosan.workers.dev/](https://sidra-jewellery.sayadmdbayezidhosan.workers.dev/)
- Admin dashboard entry: [https://sidra-jewellery.sayadmdbayezidhosan.workers.dev/admin/](https://sidra-jewellery.sayadmdbayezidhosan.workers.dev/admin/)
- Source repository: [https://github.com/bayzed123/jewellery-and-Fashion-](https://github.com/bayzed123/jewellery-and-Fashion-)

## Storefront screenshot

![Jewellery and Fashion storefront captured with Playwright](live-proof/storefront.png)

## Admin dashboard screenshot

![Jewellery and Fashion admin dashboard entry captured with Playwright](live-proof/admin.png)

## What to verify next

Use the project setup and deployment pages to run the authenticated acceptance pass: sign in with an authorized client account, verify products and inventory, test cart and checkout in the intended sandbox, inspect order and customer views, verify role permissions, test webhooks and notifications, and confirm backups and restore. Never place real payment credentials or customer data in this documentation.

## Cross-reference

This live Worker is the supplied deployment proof for the Jewellery and Fashion repository guide. The live brand name is Sidra Jewellery & Fashion; verify the client mapping before reuse.

- [Setup](setup.md)
- [Features](features.md)
- [Whitelabel Rebranding](whitelabel.md)
- [Harbal Pakriti](../harbal-pakriti/index.md)
- [Babyshop](../babyshop/index.md)

- [Demu Highlighted Showcase](../../showcase/index.md)
