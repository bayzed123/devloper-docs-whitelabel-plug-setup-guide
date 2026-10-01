# Developer Docs

Reusable setup, feature, pipeline, and deployment guides for rebuilding Bayzed123 projects or handing them to another client/developer. Built with [SmartGen Docs](https://pypi.org/project/smartgen-docs/) in the reading-first style of [docs.smartgentools.com](https://docs.smartgentools.com).

## Projects covered

- [Harbal Pakriti](docs/projects/harbal-pakriti.md)
- [Jewellery and Fashion](docs/projects/jewellery-and-fashion.md)
- [Babyshop](docs/projects/babyshop.md)
- [Arif Gadget Store](docs/projects/arifgadget-store.md)
- [LKS Attire](docs/projects/lks-attire.md)

## Rebuild order

For any project, use this order: confirm the audited repository commit, install the documented runtime, install from the lockfile, copy the environment template, build assets, migrate and seed local data, create a local admin, start the app, run type checks and tests, configure production secrets and bindings, deploy through CI, run health checks, replace placeholders, and record the release commit.

## Local docs development

```bash
python -m pip install smartgen-docs
smartgen-docs serve
```

Open `http://localhost:8000` while editing `docs/`. Build the static site with:

```bash
smartgen-docs build
```

The generated site is written to `site/` and can be previewed with `python -m http.server 8000 --directory site`.

## Evidence policy

Source features and commands are based on repository audits. Live behavior is only claimed when tested. During this update, `https://arifgadget.store/` returned HTTP 200 and a Playwright screenshot was captured. The other repositories had no confirmed homepage in GitHub metadata. Never copy a payment, secret, domain, or deployment value from one project into another.

## Publish

Push `main` to run `.github/workflows/deploy-docs.yml`. In GitHub repository settings, enable Pages with **GitHub Actions** as the source. The expected site URL is:

https://bayzed123.github.io/devloper-docs-whitelabel-plug-setup-guide/
