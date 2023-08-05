from typing import Union, Sequence
from solders.pubkey import Pubkey
from solders.signature import Signature
from solders.keypair import Keypair

class Presigner:
    def __init__(self, pubkey: Pubkey, signature: Signature) -> None: ...
    def pubkey(self) -> Pubkey: ...
    def sign_message(self, message: Union[bytes, Sequence[int]]) -> Signature: ...
    def __richcmp__(self, other: Union["Presigner", Keypair], op: int) -> bool: ...
    @staticmethod
    def default() -> "Presigner": ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
