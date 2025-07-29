from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HostInfo(_message.Message):
    __slots__ = ("identity",)
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    identity: str
    def __init__(self, identity: _Optional[str] = ...) -> None: ...

class RingInfo(_message.Message):
    __slots__ = ("role", "member_count", "members")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    role: str
    member_count: int
    members: _containers.RepeatedCompositeFieldContainer[HostInfo]
    def __init__(self, role: _Optional[str] = ..., member_count: _Optional[int] = ..., members: _Optional[_Iterable[_Union[HostInfo, _Mapping]]] = ...) -> None: ...

class MembershipInfo(_message.Message):
    __slots__ = ("current_host", "reachable_members", "rings")
    CURRENT_HOST_FIELD_NUMBER: _ClassVar[int]
    REACHABLE_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    RINGS_FIELD_NUMBER: _ClassVar[int]
    current_host: HostInfo
    reachable_members: _containers.RepeatedScalarFieldContainer[str]
    rings: _containers.RepeatedCompositeFieldContainer[RingInfo]
    def __init__(self, current_host: _Optional[_Union[HostInfo, _Mapping]] = ..., reachable_members: _Optional[_Iterable[str]] = ..., rings: _Optional[_Iterable[_Union[RingInfo, _Mapping]]] = ...) -> None: ...

class DomainCacheInfo(_message.Message):
    __slots__ = ("num_of_items_in_cache_by_id", "num_of_items_in_cache_by_name")
    NUM_OF_ITEMS_IN_CACHE_BY_ID_FIELD_NUMBER: _ClassVar[int]
    NUM_OF_ITEMS_IN_CACHE_BY_NAME_FIELD_NUMBER: _ClassVar[int]
    num_of_items_in_cache_by_id: int
    num_of_items_in_cache_by_name: int
    def __init__(self, num_of_items_in_cache_by_id: _Optional[int] = ..., num_of_items_in_cache_by_name: _Optional[int] = ...) -> None: ...

class PersistenceSetting(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class PersistenceFeature(_message.Message):
    __slots__ = ("key", "enabled")
    KEY_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    key: str
    enabled: bool
    def __init__(self, key: _Optional[str] = ..., enabled: bool = ...) -> None: ...

class PersistenceInfo(_message.Message):
    __slots__ = ("backend", "settings", "features")
    BACKEND_FIELD_NUMBER: _ClassVar[int]
    SETTINGS_FIELD_NUMBER: _ClassVar[int]
    FEATURES_FIELD_NUMBER: _ClassVar[int]
    backend: str
    settings: _containers.RepeatedCompositeFieldContainer[PersistenceSetting]
    features: _containers.RepeatedCompositeFieldContainer[PersistenceFeature]
    def __init__(self, backend: _Optional[str] = ..., settings: _Optional[_Iterable[_Union[PersistenceSetting, _Mapping]]] = ..., features: _Optional[_Iterable[_Union[PersistenceFeature, _Mapping]]] = ...) -> None: ...
