# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [0-based versioning](https://0ver.org/).

## [Unreleased]

## v0.1.4 - 2022-10-14

### Added

- Add `-b` option to crawl site by actual browser
- Add `-bs` option to set the number of session/page to open by browser
- Add `-bd` option to set the delay to wait for a page to load in browser

### Changed

- Use simpler asyncio syntax that support Python 3.7
- Sync asyncio debugging with `-d` option
- Switch to pre-commit as default linter tool from tox
- Resolve mypy and pylint warnings

## v0.1.3 - 2022-08-09

### Added

- Add `-w` option to wrap text at specify length
- Add `-ic` option to set indent characters for a paragraph only if `-w` option
  is more than zero

### Fixed

- Fix not showing exact regex debug log
- Show individual config item in debug log

### Changed

- Upgrade the TOML config file if there are changes in the config template file
  for both xsget and xstxt app

## v0.1.2 - 2022-07-29

### Fixed

- Fix invalid base_url in config
- Enable debug by default in config

### Changed

- Switch to pre-commit to manage code linting
- Update FAQ for xstxt usage
- Add more html replacement regex rules to xstxt.toml

## v0.1.1 - 2022-07-09

### Changed

- Fix missing description in PyPi page
- Test version using dynamic value

## v0.1.0 - 2022-07-08

### Added

- Initial public release
