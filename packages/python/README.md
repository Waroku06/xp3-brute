# xp3-brute Python SDK

`xp3-brute` provides CPython bindings for inspecting, reconstructing,
converting, packing, and validating KiriKiri XP3 archives.

The distribution contains a small Python API layer and a platform-native Rust
extension. Wheels are published for Linux x86_64 (manylinux2014), macOS arm64,
and Windows x86_64. The native extension uses CPython's stable ABI and supports
Python 3.9 and newer.

```python
from xp3_brute import Xp3

archive = Xp3.open_archive("data.xp3")
print(Xp3.inspect("data.xp3"))

for entry in archive.entries():
    print(entry.index, entry.name, entry.original_size)

# This returns the reconstructed XP3 storage stream for entry 0.
payload = archive.reconstruct_entry(0)
```

## Install

```bash
pip install xp3-brute
```

## Build from source

```bash
cd packages/python
python -m pip install 'maturin>=1.12,<2'
maturin develop --release
```

For source builds on macOS, ensure that Xcode Command Line Tools are installed.
On Linux the packaged wheel avoids a local Rust toolchain; source builds require
Rust 1.92 or newer.
