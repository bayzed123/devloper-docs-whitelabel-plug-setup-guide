# Developer Docs

Setup and deployment documentation for Bayzed123 web projects, built with [SmartGen Docs](https://pypi.org/project/smartgen-docs/).

## Local development

```bash
python -m pip install smartgen-docs
smartgen-docs serve
```

Open `http://localhost:8000` while editing Markdown under `docs/`.

## Build

```bash
smartgen-docs build
```

The generated static site is written to `site/`. It can be served locally with:

```bash
python -m http.server 8000 --directory site
```

## Publish

The repository is configured for a GitHub Pages deployment workflow. Push to `main`, then check the **Actions** tab and the repository's **Pages** settings. The Pages source should use the workflow artifact.

## Current project note

The requested `bayzed123/Skin-care-shop` repository is not currently visible to the authenticated GitHub account, so the project guide clearly marks unverified commands instead of inventing them. Once the correct URL or access is available, replace the placeholders with commands tested against a clean clone.
