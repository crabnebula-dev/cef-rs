# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [152.0.0+151.1.0-HEAD.3585](https://github.com/crabnebula-dev/cef-rs/compare/cef-v151.1.0+151.1.0-HEAD.3585...cef-v152.0.0+151.1.0-HEAD.3585) - 2026-09-04

### Added

- breaking changes and clippy warnings on windows
- *(test)* port tests/shared library from CEF
- support symlink for helper binaries
- decouple the crate version from CEF version
- Debug trait and constructor methods for string collections ([#86](https://github.com/crabnebula-dev/cef-rs/pull/86))
- rename sys crate and always build/link cef_wrapper_lib
- generate macOS bindings
- generate Windows bindings
- integrate upgrade.rs with update-bindings
- impl wrapper constructors with WrapType::wrap_rc callback

### Fixed

- breaking changes and clippy warnings on linux
- breaking changes on macos
- init_methods needs to cast to sub-class pointers
- move `SimpleApplication` to the cefsimple example per review
- add commas to fn new parameters ([#239](https://github.com/crabnebula-dev/cef-rs/pull/239))
- do not impl Default for structs with methods ([#225](https://github.com/crabnebula-dev/cef-rs/pull/225))
- windows build with wgpu@27
- macos build with wgpu@27
- macos osr texture handling now builds correctly
- macos metal texture fetching wrongly used macro and variables
- *(macos)* revert io_surface handle creation to original example, fix improper hal vs non-hal device usage
- (last attempt) macos accelerated rendering implementation
- (attempt) macos accelerated rendering implementation
- convert iostream implementation to previous one, since the original impl is broken
- attempt macos impl fix
- patch removed essential dependency in linux
- Windows accelerated paint now running
- modify osr_texture_import and example code for its new location
- cleanup logic for copying back out-params
- handle out-params ([#173](https://github.com/crabnebula-dev/cef-rs/pull/173))
- warnings about usize < 0 comparisons
- disable sandbox in cefsimple on Windows
- #121
- #89 rename get_ methods where possible
- wrap call to unsafe cef_dll_sys function
- port macos cef_dll_sys test code to cef::string module
- replace CefStringData::Clear with CefStringCollection::Free
- cleanup pointer casts and fix #98
- cleanup clippy warnings in cef crate
- cleanup Drop trait impls ([#88](https://github.com/crabnebula-dev/cef-rs/pull/88))
- turn runtime ptr comparison into an assert
- add try_set method to string types ([#85](https://github.com/crabnebula-dev/cef-rs/pull/85))
- write back to out-param pointer in WrapParamRef for *mut types ([#84](https://github.com/crabnebula-dev/cef-rs/pull/84))
- put conversion traits back on non-userfree strings
- preserve CefString alias in arguments
- update args string handling on Windows
- preserve CefStringUserfree types in cef crate
- implement separate CefStringUserfree structs
- CefString conversion bugs/gaps
- convert bundle script to example and update helper for api_hash #75
- move bundle_script to separate bundle_cefsimple example
- *(doc)* move crate doc comments into README files
- framework path passed to cef_load_library should be null-terminated
- reformat doc comment
- replace crate doc header to unblock publish
- build breaks on non-windows targets
- windows tests and examples with cef-dll-sys
- linux build of cefsimple helper
- unit tests and bundle_script work with cef-dll-sys on macos
- add missing window delegate methods to cefsimple
- reintegrate window.has_one_ref check
- clean up demo
- get Windows targets building/running
- cleanup unreferenced const buffer arguments
- remove default fn on scoped struct traits
- expose methods on base scoped types
- ref-counted in-out elements should call add_ref
- ref-counted output array elements should call add_ref
- rustfmt cleanup and doc comment improvements
- nullable return types should be wrapped in Option<>
- nullable pointers args should be wrapped in Option<>
- generate get_raw function in derived traits
- initialize size members in Default impl
- generate proper Default impl for enums
- must add_ref structs before passing to CEF
- CEF increments refs on arguments and relies on callee to release
- demo works but ref counts are not right yet
- get demo to compile (but not working yet)
- typos in doc comments
- bindings build without errors
- more error cleanup
- add lifetime annotations to methods/params
- add missing sys bindnigs
- update demo example
- wrap non-value type pointers in zero-copy WrapParamRef
- move demo into new cef crate directory

### Other

- merge upstream dev ([#5](https://github.com/crabnebula-dev/cef-rs/pull/5))
- update bindings ([#3](https://github.com/crabnebula-dev/cef-rs/pull/3))
- get latest ([#444](https://github.com/crabnebula-dev/cef-rs/pull/444))
- release v150.2.1+150.0.14 ([#441](https://github.com/crabnebula-dev/cef-rs/pull/441))
- *(deps)* update wgpu to v30
- release v150.0.0+150.0.10
- *(release)* update CEF version to 150.0.10 ([#438](https://github.com/crabnebula-dev/cef-rs/pull/438))
- Fix #364: remove spurious eprintln! for null pointer in UTF-16 string conversion ([#425](https://github.com/crabnebula-dev/cef-rs/pull/425))
- get latest ([#418](https://github.com/crabnebula-dev/cef-rs/pull/418))
- get latest ([#415](https://github.com/crabnebula-dev/cef-rs/pull/415))
- *(cef-dll-sys)* release v148.1.0+147.0.14 ([#411](https://github.com/crabnebula-dev/cef-rs/pull/411))
- *(release)* update CEF version to 148.0.8
- release ([#405](https://github.com/crabnebula-dev/cef-rs/pull/405))
- *(deps)* switch to objc2-metal crate
- release v147.0.0+147.0.9
- update bindings
- update bindings
- update bindings
- update bindings
- release
- update bindings
- release v145.1.1+145.0.23
- Merge branch 'dev' into fix/cefquery-persistent-field
- Merge pull request #348 from tasuren/message-router-patch
- update bindings
- release v144.0.1+144.0.6
- Merge pull request #332 from csmoe/patch-1
- release v144.0.0+144.0.6
- update bindings
- release v143.7.1+143.0.14
- release v143.6.0+143.0.13
- release
- update bindings
- update bindings
- release v143.4.0+143.0.13
- update bindings
- update bindings
- update bindings
- release v143.2.0+143.0.10
- update bindings
- *(release)* update CEF version to 143.0.10
- update bindings
- *(release)* update CEF version to 143.0.9
- release v142.5.1+142.0.17
- update bindings
- *(release)* update CEF version to 142.0.17
- *(release)* update CEF version to 142.0.15
- release v142.3.1+142.0.14
- Merge pull request #282 from csmoe/fix-color
- *(release)* update CEF version to 142.0.14
- release v142.2.1+142.0.10
- update bindings
- *(release)* update CEF version to 142.0.10
- release v142.1.0+142.0.8
- Merge pull request #272 from timon-schelling/osr_texture_import_iosurface_use_srgb
- *(release)* update CEF version to 142.0.8
- release v141.6.1+141.0.11
- update bindings
- *(release)* update CEF version to 141.0.11
- *(release)* update CEF version to 141.0.10
- release v141.4.1+141.0.9
- Merge branch 'dev' of https://github.com/tauri-apps/cef-rs into dev
- Merge branch 'dev' of https://github.com/tauri-apps/cef-rs into dev
- *(release)* update CEF version to 141.0.7
- *(release)* update CEF version to 141.0.6
- update bindings
- *(release)* update CEF version to 141.0.5
- release v140.3.6+140.1.14
- update bindings
- release v140.3.5+140.1.14
- update bindings
- release v140.3.4+140.1.14
- update bindings
- update bindings
- update bindings
- release v140.3.3+140.1.14
- update bindings
- release v140.3.2+140.1.14
- Merge pull request #219 from rgon/fix/osr-on-linux
- cleanup dependencies
- cargo fmt
- upgrade wgpu to ^26
- throw compile error if accelerated_osr requested on unsupported platform
- fix cargo fmt
- clean up import_via_metal code into closures
- remove unused objc2-metal dependency
- fix format
- attempt macos build error fix
- fix macos missing dependencies
- (attempt) fix windows build errors
- fix create proper docstring for mod.rs
- describe the accelerated_osr feature flag in Cargo.toml
- move osr_texture_import onto main cef crate
- *(release)* update CEF version to 140.1.14
- update bindings
- *(release)* update CEF version to 140.1.13
- *(release)* update CEF version to 139.0.40
- release v139.7.2+139.0.38
- update bindings
- release v139.7.1+139.0.38
- *(release)* update CEF version to 139.0.38
- *(release)* update CEF version to 139.0.37
- *(release)* update CEF version to 139.0.30
- *(release)* update CEF version to 139.0.28
- *(release)* update CEF version to 139.0.26
- release
- *(release)* update CEF version to 139.0.23
- *(release)* update CEF version to 139.0.20
- release v139.0.1+139.0.17
- Merge pull request #174 from csmoe/fix-from-raw-parts
- *(release)* update CEF version to 139.0.17
- *(release)* update CEF version to 138.0.36
- *(release)* update CEF version to 138.0.34
- release v138.7.1+138.0.33
- move examples into separate crates
- Merge pull request #136 from csmoe/osr
- Merge pull request #144 from csmoe/138-mac-sandbox
- *(release)* update CEF version to 138.0.33
- release
- *(doc)* regenerate CHANGELOG.md
- release
- seed CHANGELOG.md files
- webauthn bluetooth NSBluetoothAlwaysUsageDescription
- update bindings
- update bindings
- update bindings
- Do not export sealed traits in api
- update bindings
- Merge pull request #14 from wravery/update-bindings
- update bindings
- update bindings
- update bindings
- Merge pull request #9 from wravery/update-bindings
- update bindings
- update bindings
- update bindings
- update bindings
- Merge branch 'dev' of https://github.com/tauri-apps/cef-rs into xb284524239/dev
- Add compatibility settings in the manifest file to fix the issue of GPU process crashes.
- *(doc)* add top-level doc comments to published crates
- *(doc)* update README explaining how to use `export-cef-dir`
- update macos bindings
- update windows bindings
- update linux bindings
- remove linux32 since CEF dropped support in 2022
- reintroduce sandbox
- open browser window
- add bundle script
- add support for macos
- merge pointer + size arguments into slices
- use quote/syn to propagate type information
- convert most return types back to wrappers
- start fixing type conversions
- generate bindings that almost work
- rearrange crate/workspace structure

## [151.5.0+151.3.17](https://github.com/tauri-apps/cef-rs/compare/cef-v151.4.0+151.3.17...cef-v151.5.0+151.3.17) - 2026-08-15

### Added

- generate resource ID constants ([#452](https://github.com/tauri-apps/cef-rs/pull/452))

## [150.2.1+150.0.14](https://github.com/tauri-apps/cef-rs/compare/cef-v150.2.0+150.0.14...cef-v150.2.1+150.0.14) - 2026-07-21

### Other

- *(deps)* update wgpu to v30

## [150.0.0+150.0.10](https://github.com/tauri-apps/cef-rs/compare/cef-v149.3.0+149.0.6...cef-v150.0.0+150.0.10) - 2026-07-10

### Other

- *(release)* update CEF version to 150.0.10 ([#438](https://github.com/tauri-apps/cef-rs/pull/438))
- Fix #364: remove spurious eprintln! for null pointer in UTF-16 string conversion ([#425](https://github.com/tauri-apps/cef-rs/pull/425))

## [148.2.0+148.0.8](https://github.com/tauri-apps/cef-rs/compare/cef-v148.1.0+147.0.14...cef-v148.2.0+148.0.8) - 2026-05-25

### Other

- *(release)* update CEF version to 148.0.8

## [148.0.0+147.0.10](https://github.com/tauri-apps/cef-rs/compare/cef-v147.1.0+147.0.10...cef-v148.0.0+147.0.10) - 2026-05-07

### Other

- *(deps)* switch to objc2-metal crate

## [147.0.0+147.0.9](https://github.com/tauri-apps/cef-rs/compare/cef-v146.7.0+146.0.12...cef-v147.0.0+147.0.9) - 2026-04-25

### Other

- update bindings

## [145.6.1+145.0.28](https://github.com/tauri-apps/cef-rs/compare/cef-v145.6.0+145.0.28...cef-v145.6.1+145.0.28) - 2026-03-08

### Other

- update bindings

## [145.1.1+145.0.23](https://github.com/tauri-apps/cef-rs/compare/cef-v145.1.0+145.0.23...cef-v145.1.1+145.0.23) - 2026-02-16

### Other

- Merge branch 'dev' into fix/cefquery-persistent-field
- Merge pull request #348 from tasuren/message-router-patch

### Fixed

- Filter undefined values for optional cefQuery persistent field
- port missing early returns in BrowserSideRouter and BrowserInfoMap to prevent panics during startup
- return string responses as V8 strings instead of ArrayBuffer from RendererSideRouter

## [144.0.1+144.0.6](https://github.com/tauri-apps/cef-rs/compare/cef-v144.0.0+144.0.6...cef-v144.0.1+144.0.6) - 2026-01-22

### Other

- Merge pull request #332 from csmoe/patch-1
- release v144.0.0+144.0.6
- update bindings

## [144.0.0+144.0.6](https://github.com/tauri-apps/cef-rs/releases/tag/cef-v144.0.0+144.0.6) - 2026-01-22

### Other

- update bindings

## [143.7.1+143.0.14](https://github.com/tauri-apps/cef-rs/compare/cef-v143.7.0+143.0.14...cef-v143.7.1+143.0.14) - 2026-01-13

### Other

- update Cargo.toml dependencies

## [143.6.0+143.0.13](https://github.com/tauri-apps/cef-rs/compare/cef-v143.5.0+143.0.13...cef-v143.6.0+143.0.13) - 2026-01-03

### Added

- breaking changes and clippy warnings on windows

### Fixed

- breaking changes and clippy warnings on linux
- breaking changes on macos

## [143.5.0+143.0.13](https://github.com/tauri-apps/cef-rs/compare/cef-v143.4.0+143.0.13...cef-v143.5.0+143.0.13) - 2026-01-01

### Added

- *(test)* port tests/shared library from CEF

### Other

- update bindings
- update bindings

## [143.4.0+143.0.13](https://github.com/tauri-apps/cef-rs/compare/cef-v143.3.0+143.0.13...cef-v143.4.0+143.0.13) - 2025-12-30

### Other

- update bindings
- update bindings
- update bindings

## [143.2.0+143.0.10](https://github.com/tauri-apps/cef-rs/compare/cef-v143.1.0+143.0.10...cef-v143.2.0+143.0.10) - 2025-12-23

### Other

- update bindings

## [143.1.0+143.0.10](https://github.com/tauri-apps/cef-rs/compare/cef-v143.0.0+143.0.9...cef-v143.1.0+143.0.10) - 2025-12-13

### Other

- *(release)* update CEF version to 143.0.10

## [143.0.0+143.0.9](https://github.com/tauri-apps/cef-rs/compare/cef-v142.5.1+142.0.17...cef-v143.0.0+143.0.9) - 2025-12-11

### Other

- update bindings
- *(release)* update CEF version to 143.0.9

## [142.5.1+142.0.17](https://github.com/tauri-apps/cef-rs/compare/cef-v142.5.0+142.0.17...cef-v142.5.1+142.0.17) - 2025-12-09

### Other

- release v142.5.1+142.0.17
- update bindings

## [142.5.0+142.0.17](https://github.com/tauri-apps/cef-rs/compare/cef-v142.4.1+142.0.15...cef-v142.5.0+142.0.17) - 2025-11-27

### Other

- *(release)* update CEF version to 142.0.17
- *(deps)* update rust crate convert_case to 0.10

## [142.4.1+142.0.15](https://github.com/tauri-apps/cef-rs/compare/cef-v142.4.0+142.0.15...cef-v142.4.1+142.0.15) - 2025-11-22

### Other

- release v142.4.1+142.0.15

## [142.4.0+142.0.15](https://github.com/tauri-apps/cef-rs/compare/cef-v142.3.1+142.0.14...cef-v142.4.0+142.0.15) - 2025-11-21

### Other

- *(release)* update CEF version to 142.0.15

## [142.3.1+142.0.14](https://github.com/tauri-apps/cef-rs/compare/cef-v142.3.0+142.0.14...cef-v142.3.1+142.0.14) - 2025-11-20

### Other

- release v142.3.1+142.0.14

## [142.3.0+142.0.14](https://github.com/tauri-apps/cef-rs/compare/cef-v142.2.1+142.0.10...cef-v142.3.0+142.0.14) - 2025-11-20

### Other

- *(release)* update CEF version to 142.0.14

## [142.2.1+142.0.10](https://github.com/tauri-apps/cef-rs/compare/cef-v142.2.0+142.0.10...cef-v142.2.1+142.0.10) - 2025-11-16

### Other

- release v142.2.1+142.0.10
- update bindings

## [142.2.0+142.0.10](https://github.com/tauri-apps/cef-rs/compare/cef-v142.1.0+142.0.8...cef-v142.2.0+142.0.10) - 2025-11-13

### Other

- *(release)* update CEF version to 142.0.10

## [142.1.0+142.0.8](https://github.com/tauri-apps/cef-rs/compare/cef-v142.0.0+142.0.8...cef-v142.1.0+142.0.8) - 2025-11-12

### Added

- support symlink for helper binaries

### Fixed

- osr texture is srgb

### Other

- release v142.1.0+142.0.8

## [142.0.0+142.0.8](https://github.com/tauri-apps/cef-rs/compare/cef-v141.6.1+141.0.11...cef-v142.0.0+142.0.8) - 2025-11-11

### Other

- *(release)* update CEF version to 142.0.8

## [141.6.1+141.0.11](https://github.com/tauri-apps/cef-rs/compare/cef-v141.6.0+141.0.11...cef-v141.6.1+141.0.11) - 2025-11-09

### Fixed

- init_methods needs to cast to sub-class pointers

### Other

- release v141.6.1+141.0.11
- *(deps)* update rust crate convert_case to 0.9
- *(deps)* update rust crate libloading to 0.9
- update bindings

## [141.6.0+141.0.11](https://github.com/tauri-apps/cef-rs/compare/cef-v141.5.0+141.0.10...cef-v141.6.0+141.0.11) - 2025-10-26

### Other

- *(release)* update CEF version to 141.0.11

## [141.5.0+141.0.10](https://github.com/tauri-apps/cef-rs/compare/cef-v141.4.1+141.0.9...cef-v141.5.0+141.0.10) - 2025-10-24

### Other

- *(release)* update CEF version to 141.0.10

## [141.4.1+141.0.9](https://github.com/tauri-apps/cef-rs/compare/cef-v141.4.0+141.0.9...cef-v141.4.1+141.0.9) - 2025-10-23

### Other

- release v141.4.1+141.0.9

## [141.4.0+141.0.9](https://github.com/tauri-apps/cef-rs/compare/cef-v141.3.1+141.0.8...cef-v141.4.0+141.0.9) - 2025-10-23

### Other

- *(release)* update CEF version to 141.0.9

## [141.3.1+141.0.8](https://github.com/tauri-apps/cef-rs/compare/cef-v141.3.0+141.0.8...cef-v141.3.1+141.0.8) - 2025-10-22

### Other

- release v141.3.0+141.0.7
- update bindings

## [141.3.0+141.0.8](https://github.com/tauri-apps/cef-rs/compare/cef-v141.2.0+141.0.7...cef-v141.3.0+141.0.8) - 2025-10-22

### Added

- debug scalar types

### Fixed

- move `SimpleApplication` to the cefsimple example per review

### Other

- *(release)* update CEF version to 141.0.8

## [141.2.0+141.0.7](https://github.com/tauri-apps/cef-rs/compare/cef-v141.1.0+141.0.6...cef-v141.2.0+141.0.7) - 2025-10-19

### Other

- *(release)* update CEF version to 141.0.7

## [141.1.0+141.0.6](https://github.com/tauri-apps/cef-rs/compare/cef-v141.0.0+141.0.5...cef-v141.1.0+141.0.6) - 2025-10-17

### Other

- *(release)* update CEF version to 141.0.6

## [141.0.0+141.0.5](https://github.com/tauri-apps/cef-rs/compare/cef-v140.3.6+140.1.14...cef-v141.0.0+141.0.5) - 2025-10-16

### Other

- update bindings
- *(release)* update CEF version to 141.0.5

## [140.3.6+140.1.14](https://github.com/tauri-apps/cef-rs/compare/cef-v140.3.5+140.1.14...cef-v140.3.6+140.1.14) - 2025-10-14

### Other

- release v140.3.6+140.1.14
- update bindings

## [140.3.5+140.1.14](https://github.com/tauri-apps/cef-rs/compare/cef-v140.3.4+140.1.14...cef-v140.3.5+140.1.14) - 2025-10-13

### Fixed

- add commas to fn new parameters ([#239](https://github.com/tauri-apps/cef-rs/issues/239))

### Other

- release v140.3.5+140.1.14
- update bindings

## [140.3.4+140.1.14](https://github.com/tauri-apps/cef-rs/compare/cef-v140.3.3+140.1.14...cef-v140.3.4+140.1.14) - 2025-10-13

### Added

- port SimpleApplication from original cefsimple
- add CefAppProtocol bindings

### Fixed

- resolve cargo build warning about default-features on macOS

### Other

- release v140.3.4+140.1.14
- update bindings
- update bindings
- update bindings

## [140.3.3+140.1.14](https://github.com/tauri-apps/cef-rs/compare/cef-v140.3.2+140.1.14...cef-v140.3.3+140.1.14) - 2025-10-11

### Fixed

- do not impl Default for structs with methods ([#225](https://github.com/tauri-apps/cef-rs/issues/225))

### Other

- release v140.3.3+140.1.14
- update bindings

## [140.3.2+140.1.14](https://github.com/tauri-apps/cef-rs/compare/cef-v140.3.1+140.1.14...cef-v140.3.2+140.1.14) - 2025-10-11

### Fixed

- windows build with wgpu@27
- macos build with wgpu@27
- macos osr texture handling now builds correctly
- macos metal texture fetching wrongly used macro and variables
- *(macos)* revert io_surface handle creation to original example, fix improper hal vs non-hal device usage
- (last attempt) macos accelerated rendering implementation
- (attempt) macos accelerated rendering implementation
- convert iostream implementation to previous one, since the original impl is broken
- attempt macos impl fix
- patch removed essential dependency in linux
- Windows accelerated paint now running
- modify osr_texture_import and example code for its new location

### Other

- release v140.3.2+140.1.14
- cleanup dependencies
- cargo fmt
- upgrade wgpu to ^26
- throw compile error if accelerated_osr requested on unsupported platform
- fix cargo fmt
- clean up import_via_metal code into closures
- remove unused objc2-metal dependency
- fix format
- attempt macos build error fix
- fix macos missing dependencies
- (attempt) fix windows build errors
- fix create proper docstring for mod.rs
- describe the accelerated_osr feature flag in Cargo.toml
- move osr_texture_import onto main cef crate

## [140.3.1+140.1.14](https://github.com/tauri-apps/cef-rs/compare/cef-v140.3.0+140.1.14...cef-v140.3.1+140.1.14) - 2025-10-03

### Fixed

- copy wrapped out-params back to pointers ([#224](https://github.com/tauri-apps/cef-rs/issues/224))

### Other

- release v140.3.1+140.1.14
- update bindings
- *(test)* test out-params

## [140.3.0+140.1.14](https://github.com/tauri-apps/cef-rs/compare/cef-v140.2.0+140.1.14...cef-v140.3.0+140.1.14) - 2025-09-23

### Other

- release

## [140.2.0+140.1.14](https://github.com/tauri-apps/cef-rs/compare/cef-v140.1.0+140.1.13...cef-v140.2.0+140.1.14) - 2025-09-21

### Other

- *(release)* update CEF version to 140.1.14

## [140.1.0+140.1.13](https://github.com/tauri-apps/cef-rs/compare/cef-v140.0.0+140.1.13...cef-v140.1.0+140.1.13) - 2025-09-19

### Other

- release

## [140.0.0+140.1.13](https://github.com/tauri-apps/cef-rs/compare/cef-v139.8.0+139.0.40...cef-v140.0.0+140.1.13) - 2025-09-19

### Other

- update bindings
- *(release)* update CEF version to 140.1.13

## [139.8.0+139.0.40](https://github.com/tauri-apps/cef-rs/compare/cef-v139.7.2+139.0.38...cef-v139.8.0+139.0.40) - 2025-09-12

### Other

- *(release)* update CEF version to 139.0.40

## [139.7.2+139.0.38](https://github.com/tauri-apps/cef-rs/compare/cef-v139.7.1+139.0.38...cef-v139.7.2+139.0.38) - 2025-09-08

### Fixed

- cleanup logic for copying back out-params
- handle out-params ([#173](https://github.com/tauri-apps/cef-rs/issues/173))

### Other

- release v139.7.2+139.0.38
- update bindings

## [139.7.1+139.0.38](https://github.com/tauri-apps/cef-rs/compare/cef-v139.7.0+139.0.38...cef-v139.7.1+139.0.38) - 2025-09-07

### Other

- release v139.7.1+139.0.38
- *(deps)* update rust crate windows-sys to 0.61

## [139.7.0+139.0.38](https://github.com/tauri-apps/cef-rs/compare/cef-v139.6.0+139.0.37...cef-v139.7.0+139.0.38) - 2025-08-31

### Other

- *(release)* update CEF version to 139.0.38

## [139.6.0+139.0.37](https://github.com/tauri-apps/cef-rs/compare/cef-v139.5.0+139.0.30...cef-v139.6.0+139.0.37) - 2025-08-29

### Other

- *(release)* update CEF version to 139.0.37

## [139.5.0+139.0.30](https://github.com/tauri-apps/cef-rs/compare/cef-v139.4.0+139.0.28...cef-v139.5.0+139.0.30) - 2025-08-28

### Other

- *(release)* update CEF version to 139.0.30

## [139.4.0+139.0.28](https://github.com/tauri-apps/cef-rs/compare/cef-v139.3.0+139.0.26...cef-v139.4.0+139.0.28) - 2025-08-23

### Other

- *(release)* update CEF version to 139.0.28

## [139.3.0+139.0.26](https://github.com/tauri-apps/cef-rs/compare/cef-v139.2.1+139.0.23...cef-v139.3.0+139.0.26) - 2025-08-22

### Other

- *(release)* update CEF version to 139.0.26

## [139.2.1+139.0.23](https://github.com/tauri-apps/cef-rs/compare/cef-v139.2.0+139.0.23...cef-v139.2.1+139.0.23) - 2025-08-16

### Fixed

- warnings about usize < 0 comparisons

### Other

- release

## [139.2.0+139.0.23](https://github.com/tauri-apps/cef-rs/compare/cef-v139.1.0+139.0.20...cef-v139.2.0+139.0.23) - 2025-08-16

### Other

- *(release)* update CEF version to 139.0.23

## [139.1.0+139.0.20](https://github.com/tauri-apps/cef-rs/compare/cef-v139.0.1+139.0.17...cef-v139.1.0+139.0.20) - 2025-08-15

### Other

- *(release)* update CEF version to 139.0.20

## [139.0.1+139.0.17](https://github.com/tauri-apps/cef-rs/compare/cef-v139.0.0+139.0.17...cef-v139.0.1+139.0.17) - 2025-08-08

### Other

- release v139.0.1+139.0.17

## [139.0.0+139.0.17](https://github.com/tauri-apps/cef-rs/compare/cef-v138.9.0+138.0.36...cef-v139.0.0+139.0.17) - 2025-08-08

### Other

- *(release)* update CEF version to 139.0.17

## [138.9.0+138.0.36](https://github.com/tauri-apps/cef-rs/compare/cef-v138.8.0+138.0.34...cef-v138.9.0+138.0.36) - 2025-08-07

### Other

- *(release)* update CEF version to 138.0.36

## [138.8.0+138.0.34](https://github.com/tauri-apps/cef-rs/compare/cef-v138.7.1+138.0.33...cef-v138.8.0+138.0.34) - 2025-08-02

### Fixed

- remove cef version from example dependencies

### Other

- *(release)* update CEF version to 138.0.34

## [138.7.1+138.0.33](https://github.com/tauri-apps/cef-rs/compare/cef-v138.7.0+138.0.33...cef-v138.7.1+138.0.33) - 2025-07-29

### Other

- release v138.7.1+138.0.33
- move examples into separate crates

## [138.7.0+138.0.33](https://github.com/tauri-apps/cef-rs/compare/cef-v138.6.1+138.0.27...cef-v138.7.0+138.0.33) - 2025-07-29

### Other

- *(release)* update CEF version to 138.0.33

## [138.6.1+138.0.27](https://github.com/tauri-apps/cef-rs/compare/cef-v138.6.0+138.0.27...cef-v138.6.1+138.0.27) - 2025-07-28

### Fixed

- embed git-cliff as a library in get-latest

### Other

- *(release)* bump version for get-latest updates

## [138.6.0+138.0.27](https://github.com/tauri-apps/cef-rs/compare/cef-v138.5.1+138.0.26...cef-v138.6.0+138.0.27) - 2025-07-28

### Added

- update CEF version to 138.0.27

### Fixed

- bump version for release

## [138.5.1+138.0.26](https://github.com/tauri-apps/cef-rs/compare/cef-v138.5.0+138.0.26...cef-v138.5.1+138.0.26) - 2025-07-22

### Other

- release
- *(doc)* regenerate CHANGELOG.md

## [138.5.0+138.0.26](https://github.com/tauri-apps/cef-rs/compare/cef-v138.4.0+138.0.25...cef-v138.5.0+138.0.26) - 2025-07-19

### Other

- update CEF version

## [138.4.0+138.0.25](https://github.com/tauri-apps/cef-rs/compare/cef-v138.3.0+138.0.23...cef-v138.4.0+138.0.25) - 2025-07-18

### Other

- update CEF version

## [138.3.0+138.0.23](https://github.com/tauri-apps/cef-rs/compare/cef-v138.2.2+138.0.21...cef-v138.3.0+138.0.23) - 2025-07-17

### Other

- update CEF version

## [138.2.2+138.0.21](https://github.com/tauri-apps/cef-rs/compare/cef-v138.2.1+138.0.21...cef-v138.2.2+138.0.21) - 2025-07-14

### Other

- release
- seed CHANGELOG.md files

## [138.2.1+138.0.21](https://github.com/tauri-apps/cef-rs/compare/cef-v138.2.0+138.0.21...cef-v138.2.1+138.0.21) - 2025-07-14

### Fixed

- bump major version of download-cef [#145](https://github.com/tauri-apps/cef-rs/issues/145)

