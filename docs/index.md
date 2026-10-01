# Developer Docs

Welcome to the setup and deployment guide for Bayzed123 web projects.

This site is written in Markdown and built with [SmartGen Docs](https://pypi.org/project/smartgen-docs/). It follows the reading-first documentation style used by [docs.smartgentools.com](https://docs.smartgentools.com), with grouped navigation, copyable commands, and project-specific troubleshooting.

## Current project

### Skin-care-shop

The **Skin-care-shop** guide is ready for the repository-specific setup details. The repository URL supplied for this project is currently not visible to the authenticated GitHub account:

`https://github.com/bayzed123/Skin-care-shop`

Until that repository is made accessible or its URL is corrected, this guide deliberately does not invent framework, package-manager, environment-variable, or deployment commands. Start with the access checklist, then complete the project setup page using the app's actual files.

[Start with Before You Begin](getting-started/before-you-begin.md)

## Documentation workflow

1. Confirm repository access and identify the package manager.
2. Install the required runtime and dependencies.
3. Configure local environment variables without committing secrets.
4. Run the development server and verify the main user journey.
5. Build the production artifact and deploy it to the selected host.
6. Record project-specific decisions and known issues here.

> **Source of truth:** setup commands must come from the target repository's `README`, package manifest, lockfile, environment template, and deployment configuration. If those files disagree, prefer the lockfile and the CI configuration, then document the decision.
