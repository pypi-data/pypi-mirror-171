from typing import Sequence, List
from solders.pubkey import Pubkey

class AddressLookupTableAccount:
    def __init__(
        self,
        key: Pubkey,
        addresses: Sequence[Pubkey],
    ) -> None: ...
    def __bytes__(self) -> bytes: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __richcmp__(self, other: "AddressLookupTableAccount", op: int) -> bool: ...
    @staticmethod
    def from_bytes(raw_bytes: bytes) -> "AddressLookupTableAccount": ...
    def to_json(self) -> str: ...
    @staticmethod
    def from_json(raw: str) -> "AddressLookupTableAccount": ...
    @property
    def key(self) -> Pubkey: ...
    @property
    def addresses(self) -> List[Pubkey]: ...
