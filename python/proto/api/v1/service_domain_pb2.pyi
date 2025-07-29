from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from uber.cadence.api.v1 import domain_pb2 as _domain_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RegisterDomainRequest(_message.Message):
    __slots__ = ("security_token", "name", "description", "owner_email", "workflow_execution_retention_period", "clusters", "active_cluster_name", "data", "is_global_domain", "history_archival_status", "history_archival_uri", "visibility_archival_status", "visibility_archival_uri", "active_clusters_by_region")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    class ActiveClustersByRegionEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SECURITY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    IS_GLOBAL_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    HISTORY_ARCHIVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    HISTORY_ARCHIVAL_URI_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_ARCHIVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_ARCHIVAL_URI_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTERS_BY_REGION_FIELD_NUMBER: _ClassVar[int]
    security_token: str
    name: str
    description: str
    owner_email: str
    workflow_execution_retention_period: _duration_pb2.Duration
    clusters: _containers.RepeatedCompositeFieldContainer[_domain_pb2.ClusterReplicationConfiguration]
    active_cluster_name: str
    data: _containers.ScalarMap[str, str]
    is_global_domain: bool
    history_archival_status: _domain_pb2.ArchivalStatus
    history_archival_uri: str
    visibility_archival_status: _domain_pb2.ArchivalStatus
    visibility_archival_uri: str
    active_clusters_by_region: _containers.ScalarMap[str, str]
    def __init__(self, security_token: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., owner_email: _Optional[str] = ..., workflow_execution_retention_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., clusters: _Optional[_Iterable[_Union[_domain_pb2.ClusterReplicationConfiguration, _Mapping]]] = ..., active_cluster_name: _Optional[str] = ..., data: _Optional[_Mapping[str, str]] = ..., is_global_domain: bool = ..., history_archival_status: _Optional[_Union[_domain_pb2.ArchivalStatus, str]] = ..., history_archival_uri: _Optional[str] = ..., visibility_archival_status: _Optional[_Union[_domain_pb2.ArchivalStatus, str]] = ..., visibility_archival_uri: _Optional[str] = ..., active_clusters_by_region: _Optional[_Mapping[str, str]] = ...) -> None: ...

class RegisterDomainResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class UpdateDomainRequest(_message.Message):
    __slots__ = ("security_token", "name", "update_mask", "description", "owner_email", "data", "workflow_execution_retention_period", "bad_binaries", "history_archival_status", "history_archival_uri", "visibility_archival_status", "visibility_archival_uri", "active_cluster_name", "clusters", "delete_bad_binary", "failover_timeout", "active_clusters")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    SECURITY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    OWNER_EMAIL_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_RETENTION_PERIOD_FIELD_NUMBER: _ClassVar[int]
    BAD_BINARIES_FIELD_NUMBER: _ClassVar[int]
    HISTORY_ARCHIVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    HISTORY_ARCHIVAL_URI_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_ARCHIVAL_STATUS_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_ARCHIVAL_URI_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    DELETE_BAD_BINARY_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    security_token: str
    name: str
    update_mask: _field_mask_pb2.FieldMask
    description: str
    owner_email: str
    data: _containers.ScalarMap[str, str]
    workflow_execution_retention_period: _duration_pb2.Duration
    bad_binaries: _domain_pb2.BadBinaries
    history_archival_status: _domain_pb2.ArchivalStatus
    history_archival_uri: str
    visibility_archival_status: _domain_pb2.ArchivalStatus
    visibility_archival_uri: str
    active_cluster_name: str
    clusters: _containers.RepeatedCompositeFieldContainer[_domain_pb2.ClusterReplicationConfiguration]
    delete_bad_binary: str
    failover_timeout: _duration_pb2.Duration
    active_clusters: _domain_pb2.ActiveClusters
    def __init__(self, security_token: _Optional[str] = ..., name: _Optional[str] = ..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]] = ..., description: _Optional[str] = ..., owner_email: _Optional[str] = ..., data: _Optional[_Mapping[str, str]] = ..., workflow_execution_retention_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., bad_binaries: _Optional[_Union[_domain_pb2.BadBinaries, _Mapping]] = ..., history_archival_status: _Optional[_Union[_domain_pb2.ArchivalStatus, str]] = ..., history_archival_uri: _Optional[str] = ..., visibility_archival_status: _Optional[_Union[_domain_pb2.ArchivalStatus, str]] = ..., visibility_archival_uri: _Optional[str] = ..., active_cluster_name: _Optional[str] = ..., clusters: _Optional[_Iterable[_Union[_domain_pb2.ClusterReplicationConfiguration, _Mapping]]] = ..., delete_bad_binary: _Optional[str] = ..., failover_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., active_clusters: _Optional[_Union[_domain_pb2.ActiveClusters, _Mapping]] = ...) -> None: ...

class UpdateDomainResponse(_message.Message):
    __slots__ = ("domain",)
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    domain: _domain_pb2.Domain
    def __init__(self, domain: _Optional[_Union[_domain_pb2.Domain, _Mapping]] = ...) -> None: ...

class DeprecateDomainRequest(_message.Message):
    __slots__ = ("security_token", "name")
    SECURITY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    security_token: str
    name: str
    def __init__(self, security_token: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class DeprecateDomainResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteDomainRequest(_message.Message):
    __slots__ = ("security_token", "name")
    SECURITY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    security_token: str
    name: str
    def __init__(self, security_token: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class DeleteDomainResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeDomainRequest(_message.Message):
    __slots__ = ("id", "name")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class DescribeDomainResponse(_message.Message):
    __slots__ = ("domain",)
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    domain: _domain_pb2.Domain
    def __init__(self, domain: _Optional[_Union[_domain_pb2.Domain, _Mapping]] = ...) -> None: ...

class ListDomainsRequest(_message.Message):
    __slots__ = ("page_size", "next_page_token")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    next_page_token: bytes
    def __init__(self, page_size: _Optional[int] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class ListDomainsResponse(_message.Message):
    __slots__ = ("domains", "next_page_token")
    DOMAINS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    domains: _containers.RepeatedCompositeFieldContainer[_domain_pb2.Domain]
    next_page_token: bytes
    def __init__(self, domains: _Optional[_Iterable[_Union[_domain_pb2.Domain, _Mapping]]] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...
