"""Exercise the real Windows build script without downloading or linking CEF.

Requires Cargo, CMake, and `rustup target add x86_64-pc-windows-msvc`.
Run with: python3 sys/tests/prebuilt-wrapper.py
"""

import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest


class PrebuiltWrapperTest(unittest.TestCase):
    def test_windows_wrapper_handoff(self):
        sys_crate = Path(__file__).resolve().parents[1]
        metadata = json.loads(subprocess.check_output(
            ["cargo", "metadata", "--manifest-path", str(sys_crate / "Cargo.toml"),
             "--no-deps", "--format-version", "1"], text=True,
        ))
        package = next(p for p in metadata["packages"] if p["name"] == "cef-dll-sys")
        cef_version = package["version"].split("+", 1)[-1]
        with tempfile.TemporaryDirectory(prefix="cef-wrapper-test-") as scratch:
            root = Path(scratch)
            (root / "src").mkdir()
            (root / "src/lib.rs").write_text("")
            (root / "Cargo.toml").write_text(
                '[package]\nname = "prebuilt-wrapper-test"\n'
                'version = "0.0.0"\nedition = "2021"\n'
                '[dependencies]\ncef-dll-sys = { path = '
                + json.dumps(str(sys_crate))
                + " }\n[workspace]\n"
            )
            cef = root / "cef"
            (cef / "include").mkdir(parents=True)
            (cef / "locales").mkdir()
            (cef / "archive.json").write_text(json.dumps({
                "type": "minimal",
                "name": f"cef_binary_{cef_version}+fixture",
                "sha1": "fixture",
            }))
            (cef / "include/cef_api_versions.h").write_text(
                "#define CEF_API_VERSION_LAST CEF_API_VERSION_15101\n"
            )
            (cef / "CMakeLists.txt").write_text(
                'cmake_minimum_required(VERSION 3.10)\n'
                'project(PrebuiltWrapperTest NONE)\n'
                'message(FATAL_ERROR "PREBUILT_WRAPPER_TEST_NATIVE_BUILD")\n'
            )
            env = os.environ.copy()
            env.pop("FLATPAK", None)
            env.update(CEF_PATH=str(cef), RUSTC_WRAPPER="", CARGO_TARGET_DIR=str(root / "target"))

            def check():
                result = subprocess.run(
                    ["cargo", "check", "--manifest-path", str(root / "Cargo.toml"),
                     "--target", "x86_64-pc-windows-msvc", "-vv"],
                    env=env, capture_output=True, text=True,
                )
                return result.returncode, result.stdout + result.stderr

            wrapper = root / "prebuilt wrapper"
            wrapper.mkdir()
            library = wrapper / "libcef_dll_wrapper.lib"
            # cargo check runs build.rs and checks bindings, but does not link.
            library.write_bytes(b"fixture")
            env["CEF_RS_LIBCEF_DLL_WRAPPER_PATH"] = str(wrapper)
            status, output = check()
            self.assertEqual(status, 0, output)
            self.assertIn(f"cargo::rustc-link-search=native={wrapper}", output)
            self.assertIn("cargo::rustc-link-lib=static=libcef_dll_wrapper", output)
            self.assertIn("cargo::metadata=CEF_API_VERSION=15101", output)
            self.assertNotIn("PREBUILT_WRAPPER_TEST_NATIVE_BUILD", output)

            # A changed override must invalidate a successful Cargo build too.
            replacement = root / "replacement wrapper"
            replacement.mkdir()
            library = replacement / "libcef_dll_wrapper.lib"
            library.write_bytes(b"fixture")
            env["CEF_RS_LIBCEF_DLL_WRAPPER_PATH"] = str(replacement)
            status, output = check()
            self.assertEqual(status, 0, output)
            self.assertIn(f"cargo::rustc-link-search=native={replacement}", output)

            # A removed artifact must invalidate Cargo's previous successful run.
            library.unlink()
            status, output = check()
            self.assertNotEqual(status, 0, output)
            self.assertIn("prebuilt CEF wrapper does not exist", output)
            self.assertNotIn("PREBUILT_WRAPPER_TEST_NATIVE_BUILD", output)

            library.write_bytes(b"fixture")
            env["CEF_RS_LIBCEF_DLL_WRAPPER_PATH"] = str(root / "missing")
            status, output = check()
            self.assertNotEqual(status, 0, output)
            self.assertIn("prebuilt CEF wrapper does not exist", output)

            # Unset selects the existing native CMake path again.
            del env["CEF_RS_LIBCEF_DLL_WRAPPER_PATH"]
            status, output = check()
            self.assertNotEqual(status, 0, output)
            self.assertIn("PREBUILT_WRAPPER_TEST_NATIVE_BUILD", output)


if __name__ == "__main__":
    unittest.main()
