# Before You Begin

## 1. Confirm repository access

The supplied project URL is:

```text
https://github.com/bayzed123/Skin-care-shop
```

GitHub currently responds with **Not Found** for the authenticated account. This usually means one of the following:

- the repository name or capitalization is different;
- the repository is owned by another account or organization;
- the repository is private and the current GitHub account is not a collaborator; or
- the repository has not been created yet.

Check the URL in a browser or with GitHub CLI:

```bash
gh repo view bayzed123/Skin-care-shop
gh repo list bayzed123 --limit 100
```

Do not create a local setup guide from a similarly named repository: it may use a different framework, scripts, or data model.

## 2. Minimum information needed

Before completing the project-specific commands, confirm these files exist in the app repository:

- `README.md`
- `package.json` or the equivalent package manifest
- exactly one lockfile (`package-lock.json`, `pnpm-lock.yaml`, or `yarn.lock`)
- `.env.example`, `.env.local.example`, or documented environment variables
- the build/deployment configuration (`vite.config.*`, `next.config.*`, `vercel.json`, GitHub Actions, or equivalent)

## 3. Recommended tools

Install the versions required by the repository. If no version is documented, use a current LTS release of Node.js and the package manager selected by the lockfile. Also install:

- Git
- GitHub CLI (`gh`) if you manage private repositories or Actions
- a code editor
- a browser with developer tools

[Continue to Local Setup](local-setup.md)
