# Skin-care-shop: Scripts and Workflow

The repository is not currently accessible, so exact script names are intentionally not asserted here. After access is restored, replace the placeholders with the values from `package.json`.

## Scripts to document

| Purpose | Command | Verified result |
|---|---|---|
| Install | `<lockfile-safe install command>` | Dependencies install without mutation |
| Development | `<package-manager> run dev` | Local server starts |
| Production build | `<package-manager> run build` | Deployable artifact is generated |
| Preview/start | `<package-manager> run preview` or `<package-manager> start` | Production output is served locally |
| Lint | `<package-manager> run lint` | No blocking lint errors |
| Tests | `<package-manager> test` | Test suite passes |

## Daily development loop

```bash
# 1. Update the branch
git pull --ff-only

# 2. Install using the committed lockfile
<install command>

# 3. Configure local environment
cp <environment-template> <local-environment-file>

# 4. Start the application
<development command>

# 5. Before opening a pull request
<lint command>
<test command>
<build command>
```

Replace every angle-bracket placeholder after inspecting the actual project. Keeping placeholders visible is safer than publishing commands that could silently install or deploy the wrong application.

## Branch and commit guidance

Use focused branches such as `docs/skin-care-setup` or `feature/product-search`. Keep dependency-lockfile changes with the dependency change that caused them, and describe any required environment or migration step in the pull request.
