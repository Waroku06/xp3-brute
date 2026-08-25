"""Cross-platform Python SDK for KiriKiri XP3 archives."""

from .xp3_brute import (
    Archive,
    Entry,
    __version__,
    decode_pbd_json,
    decode_tlg_to_file,
    detect_filter_json,
    encode_pbd_json_bytes,
    encode_tlg_file,
    export_amv,
    pack_xp3,
    rebuild_assets,
    recover_xor_json,
    verify_roundtrip_json,
)
from .sdk import ArchiveSummary, Xp3

__all__ = [
    "Archive",
    "ArchiveSummary",
    "Entry",
    "Xp3",
    "__version__",
    "decode_pbd_json",
    "decode_tlg_to_file",
    "detect_filter_json",
    "encode_pbd_json_bytes",
    "encode_tlg_file",
    "export_amv",
    "pack_xp3",
    "rebuild_assets",
    "recover_xor_json",
    "verify_roundtrip_json",
]
