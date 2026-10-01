# Skin-care-shop: Troubleshooting

## GitHub says the repository does not exist

Confirm spelling and capitalization, check the owner, and verify the signed-in account:

```bash
gh auth status
gh repo view bayzed123/Skin-care-shop
```

If the repository is private, ask an owner to grant access to the account used for this setup. Do not work around access controls or use a similarly named repository.

## Dependency installation fails

- Confirm the Node.js version required by the repository.
- Use only the package manager matching the lockfile.
- Remove `node_modules` only when a clean reinstall is appropriate.
- Do not delete the lockfile to make installation pass.

## Environment errors

Check that the local file was copied from the repository's template, variable names match exactly, and the development server was restarted after changes. Never paste secret values into issues or documentation.

## Build succeeds locally but fails in deployment

Compare runtime versions, build command, working directory, environment variables, and output directory. Read the hosting provider's build log and reproduce the same command locally.

## Browser route returns 404 after refresh

The host may need a single-page-app fallback or server-side route configuration. Confirm the framework before applying a provider-specific fix.

## Reporting a new issue

Include the commit SHA, operating system, runtime and package-manager versions, exact command, relevant non-secret log lines, and a minimal reproduction. Redact tokens, cookies, and customer data.
