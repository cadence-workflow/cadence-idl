from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WorkflowExecutionAlreadyStartedError(_message.Message):
    __slots__ = ("start_request_id", "run_id")
    START_REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    start_request_id: str
    run_id: str
    def __init__(self, start_request_id: _Optional[str] = ..., run_id: _Optional[str] = ...) -> None: ...

class EntityNotExistsError(_message.Message):
    __slots__ = ("current_cluster", "active_cluster", "active_clusters")
    CURRENT_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    current_cluster: str
    active_cluster: str
    active_clusters: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, current_cluster: _Optional[str] = ..., active_cluster: _Optional[str] = ..., active_clusters: _Optional[_Iterable[str]] = ...) -> None: ...

class WorkflowExecutionAlreadyCompletedError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DomainNotActiveError(_message.Message):
    __slots__ = ("domain", "current_cluster", "active_cluster", "active_clusters")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    CURRENT_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    current_cluster: str
    active_cluster: str
    active_clusters: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, domain: _Optional[str] = ..., current_cluster: _Optional[str] = ..., active_cluster: _Optional[str] = ..., active_clusters: _Optional[_Iterable[str]] = ...) -> None: ...

class ClientVersionNotSupportedError(_message.Message):
    __slots__ = ("feature_version", "client_impl", "supported_versions")
    FEATURE_VERSION_FIELD_NUMBER: _ClassVar[int]
    CLIENT_IMPL_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    feature_version: str
    client_impl: str
    supported_versions: str
    def __init__(self, feature_version: _Optional[str] = ..., client_impl: _Optional[str] = ..., supported_versions: _Optional[str] = ...) -> None: ...

class FeatureNotEnabledError(_message.Message):
    __slots__ = ("feature_flag",)
    FEATURE_FLAG_FIELD_NUMBER: _ClassVar[int]
    feature_flag: str
    def __init__(self, feature_flag: _Optional[str] = ...) -> None: ...

class CancellationAlreadyRequestedError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DomainAlreadyExistsError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LimitExceededError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class QueryFailedError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ServiceBusyError(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class StickyWorkerUnavailableError(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
