# Local Setup

This page becomes project-specific after repository access is restored. Use the lockfile to choose the package manager; do not mix package managers during installation.

## Clone the repository

```bash
git clone https://github.com/bayzed123/Skin-care-shop.git
cd Skin-care-shop
```

If the repository is private, authenticate first:

```bash
gh auth login
gh repo clone bayzed123/Skin-care-shop
cd Skin-care-shop
```

## Select the package manager

| Lockfile | Package manager | Install command |
|---|---|---|
| `pnpm-lock.yaml` | pnpm | `pnpm install --frozen-lockfile` |
| `yarn.lock` | Yarn | `yarn install --frozen-lockfile` |
| `package-lock.json` | npm | `npm ci` |
| no lockfile | Confirm with the maintainer | Do not guess |

## Install and run

Run the command matching the repository's lockfile, then inspect `package.json` for the exact development script:

```bash
# Example only; confirm the actual package manager first
npm ci
npm run dev
```

Open the URL printed by the development server. Verify at least the home page, product browsing, cart behavior, checkout or contact flow, and any admin/authenticated flow included by the application.

## Build locally

```bash
npm run build
```

The exact output directory depends on the framework. Confirm it in the build output and hosting configuration before deploying.

[Configure environment variables](environment.md) before starting the app if the project requires them.
