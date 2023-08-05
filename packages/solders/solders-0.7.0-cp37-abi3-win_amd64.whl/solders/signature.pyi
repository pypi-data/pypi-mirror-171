from typing import ClassVar, Sequence, Union, List
from solders.pubkey import Pubkey

class Signature:
    LENGTH: ClassVar[int]
    def __init__(self, signature_slice: bytes) -> None: ...
    @staticmethod
    def new_unique() -> "Signature": ...
    @staticmethod
    def default() -> "Signature": ...
    @staticmethod
    def from_string(s: str) -> "Signature": ...
    def verify(self, pubkey: Pubkey, message_bytes: bytes) -> bool: ...
    def to_bytes_array(self) -> List[int]: ...
    def __bytes__(self) -> bytes: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self, other: "Signature", op: int) -> bool: ...
    def __hash__(self) -> int: ...
    @staticmethod
    def from_bytes(raw_bytes: bytes) -> "Signature": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "Signature": ...
