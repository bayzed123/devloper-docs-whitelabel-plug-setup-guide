# Environment Variables

No environment-variable names are documented yet because the source repository is not accessible. Once access is restored, copy the repository's example file rather than creating names manually.

```bash
cp .env.example .env.local
```

If the project uses a different template, follow its documented convention, for example `.env.local.example`.

## Rules

- Never commit `.env`, `.env.local`, production credentials, API tokens, or private keys.
- Keep a safe `.env.example` containing names only and non-sensitive example values.
- Use the framework's required public-prefix convention for browser-exposed values (for example, a framework may require `VITE_` or `NEXT_PUBLIC_`).
- Treat client-visible values as public; they cannot hold secrets.
- Configure production variables in the hosting provider's encrypted environment settings.
- If a secret is accidentally committed, rotate it immediately and remove it from repository history.

## Document each variable

After inspecting the app, add a table like this to this page:

| Variable | Required | Used by | Example/safe value |
|---|---:|---|---|
| `APP_VARIABLE_NAME` | Yes/No | Local and production | `replace-me` |

Also record which values are safe in the browser and which must remain server-side.
