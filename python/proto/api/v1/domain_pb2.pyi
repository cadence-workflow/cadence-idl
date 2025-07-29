from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from uber.cadence.api.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DomainStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DOMAIN_STATUS_INVALID: _ClassVar[DomainStatus]
    DOMAIN_STATUS_REGISTERED: _ClassVar[DomainStatus]
    DOMAIN_STATUS_DEPRECATED: _ClassVar[DomainStatus]
    DOMAIN_STATUS_DELETED: _ClassVar[DomainStatus]

class ArchivalStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ARCHIVAL_STATUS_INVALID: _ClassVar[ArchivalStatus]
    ARCHIVAL_STATUS_DISABLED: _ClassVar[ArchivalStatus]
    ARCHIVAL_STATUS_ENABLED: _ClassVar[ArchivalStatus]
DOMAIN_STATUS_INVALID: DomainStatus
DOMAIN_STATUS_REGISTERED: DomainStatus
DOMAIN_STATUS_DEPRECATED: DomainStatus
DOMAIN_STATUS_DELETED: DomainStatus
ARCHIVAL_STATUS_INVALID: ArchivalStatus
ARCHIVAL_STATUS_DISABLED: ArchivalStatus
ARCHIVAL_STATUS_ENABLED: ArchivalStatus

class Domain(_message.Message):
    __slots__ = ("id", "name", "status", "description", "owner_email", "data", "workflow_execution_retention_period", "bad_binaries", "history_archival_status", "history_archival_uri", "visibility_archival_status", "visibility_archival_uri", "active_cluster_name", "clusters", "failover_version", "is_global_domain", "failover_info", "isolation_groups", "async_workflow_config", "active_clusters")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
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
    FAILOVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    IS_GLOBAL_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_INFO_FIELD_NUMBER: _ClassVar[int]
    ISOLATION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    ASYNC_WORKFLOW_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTERS_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    status: DomainStatus
    description: str
    owner_email: str
    data: _containers.ScalarMap[str, str]
    workflow_execution_retention_period: _duration_pb2.Duration
    bad_binaries: BadBinaries
    history_archival_status: ArchivalStatus
    history_archival_uri: str
    visibility_archival_status: ArchivalStatus
    visibility_archival_uri: str
    active_cluster_name: str
    clusters: _containers.RepeatedCompositeFieldContainer[ClusterReplicationConfiguration]
    failover_version: int
    is_global_domain: bool
    failover_info: FailoverInfo
    isolation_groups: _common_pb2.IsolationGroupConfiguration
    async_workflow_config: _common_pb2.AsyncWorkflowConfiguration
    active_clusters: ActiveClusters
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., status: _Optional[_Union[DomainStatus, str]] = ..., description: _Optional[str] = ..., owner_email: _Optional[str] = ..., data: _Optional[_Mapping[str, str]] = ..., workflow_execution_retention_period: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., bad_binaries: _Optional[_Union[BadBinaries, _Mapping]] = ..., history_archival_status: _Optional[_Union[ArchivalStatus, str]] = ..., history_archival_uri: _Optional[str] = ..., visibility_archival_status: _Optional[_Union[ArchivalStatus, str]] = ..., visibility_archival_uri: _Optional[str] = ..., active_cluster_name: _Optional[str] = ..., clusters: _Optional[_Iterable[_Union[ClusterReplicationConfiguration, _Mapping]]] = ..., failover_version: _Optional[int] = ..., is_global_domain: bool = ..., failover_info: _Optional[_Union[FailoverInfo, _Mapping]] = ..., isolation_groups: _Optional[_Union[_common_pb2.IsolationGroupConfiguration, _Mapping]] = ..., async_workflow_config: _Optional[_Union[_common_pb2.AsyncWorkflowConfiguration, _Mapping]] = ..., active_clusters: _Optional[_Union[ActiveClusters, _Mapping]] = ...) -> None: ...

class ClusterReplicationConfiguration(_message.Message):
    __slots__ = ("cluster_name",)
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    cluster_name: str
    def __init__(self, cluster_name: _Optional[str] = ...) -> None: ...

class BadBinaries(_message.Message):
    __slots__ = ("binaries",)
    class BinariesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: BadBinaryInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[BadBinaryInfo, _Mapping]] = ...) -> None: ...
    BINARIES_FIELD_NUMBER: _ClassVar[int]
    binaries: _containers.MessageMap[str, BadBinaryInfo]
    def __init__(self, binaries: _Optional[_Mapping[str, BadBinaryInfo]] = ...) -> None: ...

class BadBinaryInfo(_message.Message):
    __slots__ = ("reason", "operator", "created_time")
    REASON_FIELD_NUMBER: _ClassVar[int]
    OPERATOR_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_FIELD_NUMBER: _ClassVar[int]
    reason: str
    operator: str
    created_time: _timestamp_pb2.Timestamp
    def __init__(self, reason: _Optional[str] = ..., operator: _Optional[str] = ..., created_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class FailoverInfo(_message.Message):
    __slots__ = ("failover_version", "failover_start_timestamp", "failover_expire_timestamp", "completed_shard_count", "pending_shards")
    FAILOVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_START_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_EXPIRE_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    COMPLETED_SHARD_COUNT_FIELD_NUMBER: _ClassVar[int]
    PENDING_SHARDS_FIELD_NUMBER: _ClassVar[int]
    failover_version: int
    failover_start_timestamp: _timestamp_pb2.Timestamp
    failover_expire_timestamp: _timestamp_pb2.Timestamp
    completed_shard_count: int
    pending_shards: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, failover_version: _Optional[int] = ..., failover_start_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., failover_expire_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., completed_shard_count: _Optional[int] = ..., pending_shards: _Optional[_Iterable[int]] = ...) -> None: ...

class ActiveClusters(_message.Message):
    __slots__ = ("region_to_cluster",)
    class RegionToClusterEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ActiveClusterInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[ActiveClusterInfo, _Mapping]] = ...) -> None: ...
    REGION_TO_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    region_to_cluster: _containers.MessageMap[str, ActiveClusterInfo]
    def __init__(self, region_to_cluster: _Optional[_Mapping[str, ActiveClusterInfo]] = ...) -> None: ...

class ActiveClusterInfo(_message.Message):
    __slots__ = ("active_cluster_name", "failover_version")
    ACTIVE_CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    active_cluster_name: str
    failover_version: int
    def __init__(self, active_cluster_name: _Optional[str] = ..., failover_version: _Optional[int] = ...) -> None: ...
