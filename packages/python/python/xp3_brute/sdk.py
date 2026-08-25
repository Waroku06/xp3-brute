"""Pythonic conveniences layered over the native extension."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional, Union
import json

from . import xp3_brute as _native

PathLike = Union[str, Path]


@dataclass(frozen=True)
class ArchiveSummary:
    """A stable summary of an XP3 container returned by :meth:`Xp3.inspect`."""

    path: Optional[str]
    xp3_offset: int
    physical_size: int
    file_backed: bool
    hxv4: bool
    entries: int
    index_blocks: int
    root_chunks: int

    @classmethod
    def from_json(cls, value: str) -> "ArchiveSummary":
        return cls(**json.loads(value))


class Xp3:
    """Top-level SDK facade for the native XP3 operations."""

    @staticmethod
    def open_archive(path: PathLike, *, tolerant: bool = True) -> _native.Archive:
        """Open an XP3 archive without loading its full payload into memory."""

        return _native.Archive(str(path), tolerant=tolerant)

    @staticmethod
    def inspect(path: PathLike, *, tolerant: bool = True) -> ArchiveSummary:
        """Open an archive and return its compact structural summary."""

        return ArchiveSummary.from_json(Xp3.open_archive(path, tolerant=tolerant).summary_json())

    @staticmethod
    def detect_filter(path: Optional[PathLike] = None) -> dict[str, Any]:
        """Detect the archive's executable content-filter backend, if any."""

        return json.loads(_native.detect_filter_json(None if path is None else str(path)))

    @staticmethod
    def recover_xor(
        data: bytes,
        filename: str,
        *,
        min_period: int = 1,
        max_period: int = 1024,
        top_periods: int = 8,
        exhaustive_dynamic: bool = False,
    ) -> dict[str, Any]:
        """Run the native repeating-XOR recovery planner and return candidates."""

        return json.loads(
            _native.recover_xor_json(
                data,
                filename,
                min_period=min_period,
                max_period=max_period,
                top_periods=top_periods,
                exhaustive_dynamic=exhaustive_dynamic,
            )
        )
