# Contributing

When contributing to this repository, please first discuss the change you wish to make via issue,
email, or any other method with the owners of this repository before making a change.

Please note we have a code of conduct, please follow it in all your interactions with the project. See [Code of Conduct](CODE_OF_CONDUCT.md).

## Repository Owners

See [CODEOWNERS](CODEOWNERS) for the list of filters on protected branches and items within a repository.

In this guide you will get an overview of the contribution workflow from opening an issue, creating a PR, reviewing, and merging the PR.

## New contributor guide

### Initial Setup

For initial setup, please refer to [LIFECYCLE](LIFECYCLE.md) to configure your Git User and also for initializing a freshly pulled down repository.

To get an overview of the project, read the [README](README.md). Here are some resources to help you get started with open source contributions:

- [Finding ways to contribute to open source on GitHub](https://docs.github.com/en/get-started/exploring-projects-on-github/finding-ways-to-contribute-to-open-source-on-github)
- [Set up Git](https://docs.github.com/en/get-started/quickstart/set-up-git)
- [GitHub Flow](https://docs.github.com/en/get-started/quickstart/github-flow)
- [Collaborating with pull requests](https://docs.github.com/en/github/collaborating-with-pull-requests)

## Getting started

To navigate our codebase with confidence, see [the introduction to working in the current repository](README.md) and ensure all initial requirements are installed and/or configured. Consult help by referring to the [SUPPORT.md] for direction as to where to find help. For more information on how we write our markdown files, [see](https://commonmark.org/help/).

## Making a change

To begin making changes, one MUST first pull down the repository.

### Branching Strategy

#### Branching Strategy Overrides

- `main` follows [GCSDO ADR 0008](https://confluence.hyland.com/display/GCSDEVOPS/GCSDO+ADR+0008%3A+Git+Repository+Lifecycle).
- All other branches use prefixes aligned to [SemVer](https://semver.org/). This is necessary for the releaser CI to run properly.
    - `release/foo-details` bumps the major version number on merge.
    - `feat/bar-details` bumps the minor version number on merge.
    - `fix/baz-details` bumps the patch version on merge.

## Pull Request Process

1. Ensure all files that are not related to the Repository are removed or excluded via a given `.gitignore` filter.
2. Update the README.md with details of changes to the interface, this includes new environment variables, exposed ports, useful file locations and container parameters.
3. Increase the version numbers in any examples files and the README.md to the new version that this Pull Request would represent. The versioning scheme we use is [Semantic Versioning](http://semver.org/).
4. You may merge the Pull Request in once you have the sign-off of two other developers, or if you do not have permission to do that, you may request the second reviewer to merge it for you.
5. Pull Requests will be merged with a squash merge.
6. If a branch is intended to be archived, then create a git tag with the following format: `archive/feature/branch-name-here`.

## Git Tags

### Release Tags

This repository will follow the [Semantic Versioning](http://semver.org/) format for Git Tags and GitHub Releases. It is automated via the terraform-releaser workflow.

### Archive Tags

An archive tag is a way for preserving a decomissioned branch for future reference. A branch may be archived at a repository owner's discretion.

Git Tags that are created with the intention to archive a branch for future reference must follow the following format: `archive/feature-branch-class/branch-name`.
Git Tags that are created with the intention to archive must be initiated by the repository owner.
If a contributor wishes for a branch to be preserved, they must create an Issue on the Git repository through GitHub with the following format for its title: `GIT_ARCHIVE_TAG_REQURED: branch-name`.

## Conventions
<!-- Taken from https://github.com/atom/atom/blob/master/CONTRIBUTING.md#styleguides -->

### Git Commit Messages

This repository follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line
- When only changing documentation, include `[ci skip]` in the commit title
- Consider starting the commit message with an applicable emoji:
  - :art: `:art:` when improving the format/structure of the code
  - :racehorse: `:racehorse:` when improving performance
  - :non-potable_water: `:non-potable_water:` when plugging memory leaks
  - :memo: `:memo:` when writing docs
  - :penguin: `:penguin:` when fixing something on Linux
  - :apple: `:apple:` when fixing something on macOS
  - :checkered_flag: `:checkered_flag:` when fixing something on Windows
  - :bug: `:bug:` when fixing a bug
  - :fire: `:fire:` when removing code or files
  - :green_heart: `:green_heart:` when fixing the CI build
  - :white_check_mark: `:white_check_mark:` when adding tests
  - :lock: `:lock:` when dealing with security
  - :arrow_up: `:arrow_up:` when upgrading dependencies
  - :arrow_down: `:arrow_down:` when downgrading dependencies
  - :shirt: `:shirt:` when removing linter warnings