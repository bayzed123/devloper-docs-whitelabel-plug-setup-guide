# Developer Docs

Reusable multi-page setup, feature, pipeline, deployment, and whitelabel rebranding guides for Bayzed123 projects. Built with [SmartGen Docs](https://pypi.org/project/smartgen-docs/) in the reading-first style of [docs.smartgentools.com](https://docs.smartgentools.com).

## Folder-based project guides

Every repository has a separate folder under `docs/projects/`. Each folder contains multiple Markdown pages; there is no single all-in-one project guide:

```text
docs/projects/<project>/
├── index.md
├── setup.md
├── features.md
├── environment.md
├── pipeline.md
├── deployment.md
├── whitelabel.md
└── troubleshooting.md
```

Projects covered:

- `harbal-pakriti`
- `jewellery-and-fashion`
- `babyshop`
- `arifgadget-store`
- `lks-attire`

## Rebuild order

For any client, read the folder's `index.md`, then follow Setup, Environment, Features, Pipeline, Deployment, Whitelabel Rebranding, and Troubleshooting. Install from the lockfile, use a fresh local database, configure isolated client secrets, replace all placeholders, run tests and health checks, and record the deployed commit.

## Local docs development

```bash
python -m pip install smartgen-docs
smartgen-docs serve
```

Build and preview the generated static site:

```bash
smartgen-docs build
python -m http.server 8000 --directory site
```

## Publish

Push `main` to run `.github/workflows/deploy-docs.yml`. GitHub Pages should use **GitHub Actions** as its source:

https://bayzed123.github.io/devloper-docs-whitelabel-plug-setup-guide/

## Evidence and safety

Source-verified features are not the same as runtime-verified behavior. Never copy credentials, payment settings, customer data, domains, or analytics identifiers between clients. Replace sample contact information, products, prices, stock, legal text, and certification claims before a client launch.
