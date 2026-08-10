# update-bindings

Download the prebuilt [Chromium Embedded Framework](https://github.com/chromiumembedded/cef)
archive on any supported platform and run `bindgen` on the C API for the `cef-dll-sys` crate,
then regenerate the safe bindings in the `cef` crate.

You can find the latest version of the prebuilt CEF archives on the [CrabNebula CEF
Builds](https://cef-builds.crabnebula.work/index.html).
