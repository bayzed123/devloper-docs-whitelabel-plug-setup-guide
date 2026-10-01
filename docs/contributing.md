# Contributing to the Docs

## Edit content

Documentation pages live under `docs/`. Navigation and site metadata live in `smartgen.yml`.

1. Create a focused branch.
2. Update the relevant Markdown page.
3. Keep commands copyable and tested.
4. Link related pages with relative Markdown links.
5. Run a local build before committing.
6. Open a pull request with the source repository commit or issue used to verify the change.

## Content standards

- Prefer verified commands over generic examples.
- Label examples and placeholders clearly.
- Never include credentials or private customer data.
- Document prerequisites before commands.
- Explain expected results and recovery steps.
- Keep the navigation order aligned with the reader's setup journey.

## Replacing the access blocker

When `Skin-care-shop` becomes accessible, update these pages in one pass:

- `getting-started/before-you-begin.md`
- `getting-started/local-setup.md`
- `getting-started/environment.md`
- `projects/skin-care-shop/setup.md`
- `projects/skin-care-shop/workflow.md`
- `projects/skin-care-shop/deployment.md`
- `projects/skin-care-shop/troubleshooting.md`

Then verify every command against a clean clone and record the tested commit SHA.
