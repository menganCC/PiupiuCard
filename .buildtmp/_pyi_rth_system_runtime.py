import ctypes
import os
import sys


_system_runtime_handles = []

if sys.platform == "win32":
    system_root = os.environ.get("SystemRoot") or os.environ.get("WINDIR")
    bundle_root = getattr(sys, "_MEIPASS", "")
    if system_root and bundle_root:
        system32 = os.path.join(system_root, "System32")
        runtime_names = set()
        for root, _dirs, files in os.walk(bundle_root):
            for filename in files:
                lowered = filename.lower()
                if lowered.endswith(".dll") and lowered.startswith(
                    ("msvcp", "vcruntime", "concrt")
                ):
                    runtime_names.add(filename)

        for filename in sorted(runtime_names, key=str.lower):
            system_dll = os.path.join(system32, filename)
            if not os.path.isfile(system_dll):
                continue
            try:
                _system_runtime_handles.append(ctypes.WinDLL(system_dll))
            except OSError:
                pass
