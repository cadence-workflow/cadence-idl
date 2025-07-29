from google.protobuf import timestamp_pb2 as _timestamp_pb2
from uber.cadence.api.v1 import common_pb2 as _common_pb2
from uber.cadence.api.v1 import domain_pb2 as _domain_pb2
from uber.cadence.admin.v1 import history_pb2 as _history_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReplicationTaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    REPLICATION_TASK_TYPE_INVALID: _ClassVar[ReplicationTaskType]
    REPLICATION_TASK_TYPE_DOMAIN: _ClassVar[ReplicationTaskType]
    REPLICATION_TASK_TYPE_HISTORY: _ClassVar[ReplicationTaskType]
    REPLICATION_TASK_TYPE_SYNC_SHARD_STATUS: _ClassVar[ReplicationTaskType]
    REPLICATION_TASK_TYPE_SYNC_ACTIVITY: _ClassVar[ReplicationTaskType]
    REPLICATION_TASK_TYPE_HISTORY_METADATA: _ClassVar[ReplicationTaskType]
    REPLICATION_TASK_TYPE_HISTORY_V2: _ClassVar[ReplicationTaskType]
    REPLICATION_TASK_TYPE_FAILOVER_MARKER: _ClassVar[ReplicationTaskType]

class DomainOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DOMAIN_OPERATION_INVALID: _ClassVar[DomainOperation]
    DOMAIN_OPERATION_CREATE: _ClassVar[DomainOperation]
    DOMAIN_OPERATION_UPDATE: _ClassVar[DomainOperation]
    DOMAIN_OPERATION_DELETE: _ClassVar[DomainOperation]

class DLQType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DLQ_TYPE_INVALID: _ClassVar[DLQType]
    DLQ_TYPE_REPLICATION: _ClassVar[DLQType]
    DLQ_TYPE_DOMAIN: _ClassVar[DLQType]
REPLICATION_TASK_TYPE_INVALID: ReplicationTaskType
REPLICATION_TASK_TYPE_DOMAIN: ReplicationTaskType
REPLICATION_TASK_TYPE_HISTORY: ReplicationTaskType
REPLICATION_TASK_TYPE_SYNC_SHARD_STATUS: ReplicationTaskType
REPLICATION_TASK_TYPE_SYNC_ACTIVITY: ReplicationTaskType
REPLICATION_TASK_TYPE_HISTORY_METADATA: ReplicationTaskType
REPLICATION_TASK_TYPE_HISTORY_V2: ReplicationTaskType
REPLICATION_TASK_TYPE_FAILOVER_MARKER: ReplicationTaskType
DOMAIN_OPERATION_INVALID: DomainOperation
DOMAIN_OPERATION_CREATE: DomainOperation
DOMAIN_OPERATION_UPDATE: DomainOperation
DOMAIN_OPERATION_DELETE: DomainOperation
DLQ_TYPE_INVALID: DLQType
DLQ_TYPE_REPLICATION: DLQType
DLQ_TYPE_DOMAIN: DLQType

class ReplicationMessages(_message.Message):
    __slots__ = ("replication_tasks", "last_retrieved_message_id", "has_more", "sync_shard_status")
    REPLICATION_TASKS_FIELD_NUMBER: _ClassVar[int]
    LAST_RETRIEVED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    HAS_MORE_FIELD_NUMBER: _ClassVar[int]
    SYNC_SHARD_STATUS_FIELD_NUMBER: _ClassVar[int]
    replication_tasks: _containers.RepeatedCompositeFieldContainer[ReplicationTask]
    last_retrieved_message_id: int
    has_more: bool
    sync_shard_status: SyncShardStatus
    def __init__(self, replication_tasks: _Optional[_Iterable[_Union[ReplicationTask, _Mapping]]] = ..., last_retrieved_message_id: _Optional[int] = ..., has_more: bool = ..., sync_shard_status: _Optional[_Union[SyncShardStatus, _Mapping]] = ...) -> None: ...

class ReplicationTask(_message.Message):
    __slots__ = ("task_type", "source_task_id", "creation_time", "domain_task_attributes", "sync_shard_status_task_attributes", "sync_activity_task_attributes", "history_task_v2_attributes", "failover_marker_attributes")
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_TASK_ID_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_TASK_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SYNC_SHARD_STATUS_TASK_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SYNC_ACTIVITY_TASK_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    HISTORY_TASK_V2_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_MARKER_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    task_type: ReplicationTaskType
    source_task_id: int
    creation_time: _timestamp_pb2.Timestamp
    domain_task_attributes: DomainTaskAttributes
    sync_shard_status_task_attributes: SyncShardStatusTaskAttributes
    sync_activity_task_attributes: SyncActivityTaskAttributes
    history_task_v2_attributes: HistoryTaskV2Attributes
    failover_marker_attributes: FailoverMarkerAttributes
    def __init__(self, task_type: _Optional[_Union[ReplicationTaskType, str]] = ..., source_task_id: _Optional[int] = ..., creation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., domain_task_attributes: _Optional[_Union[DomainTaskAttributes, _Mapping]] = ..., sync_shard_status_task_attributes: _Optional[_Union[SyncShardStatusTaskAttributes, _Mapping]] = ..., sync_activity_task_attributes: _Optional[_Union[SyncActivityTaskAttributes, _Mapping]] = ..., history_task_v2_attributes: _Optional[_Union[HistoryTaskV2Attributes, _Mapping]] = ..., failover_marker_attributes: _Optional[_Union[FailoverMarkerAttributes, _Mapping]] = ...) -> None: ...

class DomainTaskAttributes(_message.Message):
    __slots__ = ("domain_operation", "id", "domain", "config_version", "failover_version", "previous_failover_version")
    DOMAIN_OPERATION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VERSION_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_FAILOVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    domain_operation: DomainOperation
    id: str
    domain: _domain_pb2.Domain
    config_version: int
    failover_version: int
    previous_failover_version: int
    def __init__(self, domain_operation: _Optional[_Union[DomainOperation, str]] = ..., id: _Optional[str] = ..., domain: _Optional[_Union[_domain_pb2.Domain, _Mapping]] = ..., config_version: _Optional[int] = ..., failover_version: _Optional[int] = ..., previous_failover_version: _Optional[int] = ...) -> None: ...

class SyncShardStatusTaskAttributes(_message.Message):
    __slots__ = ("source_cluster", "shard_id", "timestamp")
    SOURCE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    source_cluster: str
    shard_id: int
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, source_cluster: _Optional[str] = ..., shard_id: _Optional[int] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SyncActivityTaskAttributes(_message.Message):
    __slots__ = ("domain_id", "workflow_execution", "version", "scheduled_id", "scheduled_time", "started_id", "started_time", "last_heartbeat_time", "details", "attempt", "last_failure", "last_worker_identity", "version_history")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_TIME_FIELD_NUMBER: _ClassVar[int]
    STARTED_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_HEARTBEAT_TIME_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    LAST_FAILURE_FIELD_NUMBER: _ClassVar[int]
    LAST_WORKER_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    VERSION_HISTORY_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    workflow_execution: _common_pb2.WorkflowExecution
    version: int
    scheduled_id: int
    scheduled_time: _timestamp_pb2.Timestamp
    started_id: int
    started_time: _timestamp_pb2.Timestamp
    last_heartbeat_time: _timestamp_pb2.Timestamp
    details: _common_pb2.Payload
    attempt: int
    last_failure: _common_pb2.Failure
    last_worker_identity: str
    version_history: _history_pb2.VersionHistory
    def __init__(self, domain_id: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., version: _Optional[int] = ..., scheduled_id: _Optional[int] = ..., scheduled_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_id: _Optional[int] = ..., started_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_heartbeat_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., attempt: _Optional[int] = ..., last_failure: _Optional[_Union[_common_pb2.Failure, _Mapping]] = ..., last_worker_identity: _Optional[str] = ..., version_history: _Optional[_Union[_history_pb2.VersionHistory, _Mapping]] = ...) -> None: ...

class HistoryTaskV2Attributes(_message.Message):
    __slots__ = ("task_id", "domain_id", "workflow_execution", "version_history_items", "events", "new_run_events")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    VERSION_HISTORY_ITEMS_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    NEW_RUN_EVENTS_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    domain_id: str
    workflow_execution: _common_pb2.WorkflowExecution
    version_history_items: _containers.RepeatedCompositeFieldContainer[_history_pb2.VersionHistoryItem]
    events: _common_pb2.DataBlob
    new_run_events: _common_pb2.DataBlob
    def __init__(self, task_id: _Optional[int] = ..., domain_id: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., version_history_items: _Optional[_Iterable[_Union[_history_pb2.VersionHistoryItem, _Mapping]]] = ..., events: _Optional[_Union[_common_pb2.DataBlob, _Mapping]] = ..., new_run_events: _Optional[_Union[_common_pb2.DataBlob, _Mapping]] = ...) -> None: ...

class FailoverMarkerAttributes(_message.Message):
    __slots__ = ("domain_id", "failover_version", "creation_time")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATION_TIME_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    failover_version: int
    creation_time: _timestamp_pb2.Timestamp
    def __init__(self, domain_id: _Optional[str] = ..., failover_version: _Optional[int] = ..., creation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class FailoverMarkerToken(_message.Message):
    __slots__ = ("shard_ids", "failover_marker")
    SHARD_IDS_FIELD_NUMBER: _ClassVar[int]
    FAILOVER_MARKER_FIELD_NUMBER: _ClassVar[int]
    shard_ids: _containers.RepeatedScalarFieldContainer[int]
    failover_marker: FailoverMarkerAttributes
    def __init__(self, shard_ids: _Optional[_Iterable[int]] = ..., failover_marker: _Optional[_Union[FailoverMarkerAttributes, _Mapping]] = ...) -> None: ...

class ReplicationTaskInfo(_message.Message):
    __slots__ = ("domain_id", "workflow_execution", "task_type", "task_id", "version", "first_event_id", "next_event_id", "scheduled_id")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    FIRST_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    NEXT_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_ID_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    workflow_execution: _common_pb2.WorkflowExecution
    task_type: int
    task_id: int
    version: int
    first_event_id: int
    next_event_id: int
    scheduled_id: int
    def __init__(self, domain_id: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., task_type: _Optional[int] = ..., task_id: _Optional[int] = ..., version: _Optional[int] = ..., first_event_id: _Optional[int] = ..., next_event_id: _Optional[int] = ..., scheduled_id: _Optional[int] = ...) -> None: ...

class ReplicationToken(_message.Message):
    __slots__ = ("shard_id", "last_retrieved_message_id", "last_processed_message_id")
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_RETRIEVED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_PROCESSED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    shard_id: int
    last_retrieved_message_id: int
    last_processed_message_id: int
    def __init__(self, shard_id: _Optional[int] = ..., last_retrieved_message_id: _Optional[int] = ..., last_processed_message_id: _Optional[int] = ...) -> None: ...

class SyncShardStatus(_message.Message):
    __slots__ = ("timestamp",)
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    timestamp: _timestamp_pb2.Timestamp
    def __init__(self, timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class HistoryDLQCountEntry(_message.Message):
    __slots__ = ("count", "shard_id", "source_cluster")
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    count: int
    shard_id: int
    source_cluster: str
    def __init__(self, count: _Optional[int] = ..., shard_id: _Optional[int] = ..., source_cluster: _Optional[str] = ...) -> None: ...
