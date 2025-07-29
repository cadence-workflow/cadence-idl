from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VersionHistoryItem(_message.Message):
    __slots__ = ("event_id", "version")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    version: int
    def __init__(self, event_id: _Optional[int] = ..., version: _Optional[int] = ...) -> None: ...

class VersionHistory(_message.Message):
    __slots__ = ("branch_token", "items")
    BRANCH_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    branch_token: bytes
    items: _containers.RepeatedCompositeFieldContainer[VersionHistoryItem]
    def __init__(self, branch_token: _Optional[bytes] = ..., items: _Optional[_Iterable[_Union[VersionHistoryItem, _Mapping]]] = ...) -> None: ...
