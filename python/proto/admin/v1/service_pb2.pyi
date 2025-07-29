from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from uber.cadence.api.v1 import common_pb2 as _common_pb2
from uber.cadence.api.v1 import tasklist_pb2 as _tasklist_pb2
from uber.cadence.api.v1 import visibility_pb2 as _visibility_pb2
from uber.cadence.admin.v1 import cluster_pb2 as _cluster_pb2
from uber.cadence.admin.v1 import history_pb2 as _history_pb2
from uber.cadence.admin.v1 import queue_pb2 as _queue_pb2
from uber.cadence.admin.v1 import replication_pb2 as _replication_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UpdateTaskListPartitionConfigRequest(_message.Message):
    __slots__ = ("domain", "task_list", "task_list_type", "partition_config")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARTITION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    domain: str
    task_list: _tasklist_pb2.TaskList
    task_list_type: _tasklist_pb2.TaskListType
    partition_config: _tasklist_pb2.TaskListPartitionConfig
    def __init__(self, domain: _Optional[str] = ..., task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., task_list_type: _Optional[_Union[_tasklist_pb2.TaskListType, str]] = ..., partition_config: _Optional[_Union[_tasklist_pb2.TaskListPartitionConfig, _Mapping]] = ...) -> None: ...

class UpdateTaskListPartitionConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeWorkflowExecutionRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ...) -> None: ...

class DescribeWorkflowExecutionResponse(_message.Message):
    __slots__ = ("shard_id", "history_addr", "mutable_state_in_cache", "mutable_state_in_database")
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    HISTORY_ADDR_FIELD_NUMBER: _ClassVar[int]
    MUTABLE_STATE_IN_CACHE_FIELD_NUMBER: _ClassVar[int]
    MUTABLE_STATE_IN_DATABASE_FIELD_NUMBER: _ClassVar[int]
    shard_id: int
    history_addr: str
    mutable_state_in_cache: str
    mutable_state_in_database: str
    def __init__(self, shard_id: _Optional[int] = ..., history_addr: _Optional[str] = ..., mutable_state_in_cache: _Optional[str] = ..., mutable_state_in_database: _Optional[str] = ...) -> None: ...

class DescribeHistoryHostRequest(_message.Message):
    __slots__ = ("host_address", "shard_id", "workflow_execution")
    HOST_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    host_address: str
    shard_id: int
    workflow_execution: _common_pb2.WorkflowExecution
    def __init__(self, host_address: _Optional[str] = ..., shard_id: _Optional[int] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ...) -> None: ...

class DescribeShardDistributionRequest(_message.Message):
    __slots__ = ("page_size", "page_id")
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_ID_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_id: int
    def __init__(self, page_size: _Optional[int] = ..., page_id: _Optional[int] = ...) -> None: ...

class DescribeShardDistributionResponse(_message.Message):
    __slots__ = ("number_of_shards", "shards")
    class ShardsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: str
        def __init__(self, key: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...
    NUMBER_OF_SHARDS_FIELD_NUMBER: _ClassVar[int]
    SHARDS_FIELD_NUMBER: _ClassVar[int]
    number_of_shards: int
    shards: _containers.ScalarMap[int, str]
    def __init__(self, number_of_shards: _Optional[int] = ..., shards: _Optional[_Mapping[int, str]] = ...) -> None: ...

class DescribeHistoryHostResponse(_message.Message):
    __slots__ = ("number_of_shards", "shard_ids", "domain_cache", "shard_controller_status", "address")
    NUMBER_OF_SHARDS_FIELD_NUMBER: _ClassVar[int]
    SHARD_IDS_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_CACHE_FIELD_NUMBER: _ClassVar[int]
    SHARD_CONTROLLER_STATUS_FIELD_NUMBER: _ClassVar[int]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    number_of_shards: int
    shard_ids: _containers.RepeatedScalarFieldContainer[int]
    domain_cache: _cluster_pb2.DomainCacheInfo
    shard_controller_status: str
    address: str
    def __init__(self, number_of_shards: _Optional[int] = ..., shard_ids: _Optional[_Iterable[int]] = ..., domain_cache: _Optional[_Union[_cluster_pb2.DomainCacheInfo, _Mapping]] = ..., shard_controller_status: _Optional[str] = ..., address: _Optional[str] = ...) -> None: ...

class CloseShardRequest(_message.Message):
    __slots__ = ("shard_id",)
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    shard_id: int
    def __init__(self, shard_id: _Optional[int] = ...) -> None: ...

class CloseShardResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RemoveTaskRequest(_message.Message):
    __slots__ = ("shard_id", "task_type", "task_id", "visibility_time", "cluster_name")
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_TIME_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    shard_id: int
    task_type: _queue_pb2.TaskType
    task_id: int
    visibility_time: _timestamp_pb2.Timestamp
    cluster_name: str
    def __init__(self, shard_id: _Optional[int] = ..., task_type: _Optional[_Union[_queue_pb2.TaskType, str]] = ..., task_id: _Optional[int] = ..., visibility_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cluster_name: _Optional[str] = ...) -> None: ...

class RemoveTaskResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetQueueRequest(_message.Message):
    __slots__ = ("shard_id", "cluster_name", "task_type")
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    shard_id: int
    cluster_name: str
    task_type: _queue_pb2.TaskType
    def __init__(self, shard_id: _Optional[int] = ..., cluster_name: _Optional[str] = ..., task_type: _Optional[_Union[_queue_pb2.TaskType, str]] = ...) -> None: ...

class ResetQueueResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeQueueRequest(_message.Message):
    __slots__ = ("shard_id", "cluster_name", "task_type")
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    shard_id: int
    cluster_name: str
    task_type: _queue_pb2.TaskType
    def __init__(self, shard_id: _Optional[int] = ..., cluster_name: _Optional[str] = ..., task_type: _Optional[_Union[_queue_pb2.TaskType, str]] = ...) -> None: ...

class DescribeQueueResponse(_message.Message):
    __slots__ = ("processing_queue_states",)
    PROCESSING_QUEUE_STATES_FIELD_NUMBER: _ClassVar[int]
    processing_queue_states: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, processing_queue_states: _Optional[_Iterable[str]] = ...) -> None: ...

class GetWorkflowExecutionRawHistoryV2Request(_message.Message):
    __slots__ = ("domain", "workflow_execution", "start_event", "end_event", "page_size", "next_page_token")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    START_EVENT_FIELD_NUMBER: _ClassVar[int]
    END_EVENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    start_event: _history_pb2.VersionHistoryItem
    end_event: _history_pb2.VersionHistoryItem
    page_size: int
    next_page_token: bytes
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., start_event: _Optional[_Union[_history_pb2.VersionHistoryItem, _Mapping]] = ..., end_event: _Optional[_Union[_history_pb2.VersionHistoryItem, _Mapping]] = ..., page_size: _Optional[int] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class GetWorkflowExecutionRawHistoryV2Response(_message.Message):
    __slots__ = ("next_page_token", "history_batches", "version_history")
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    HISTORY_BATCHES_FIELD_NUMBER: _ClassVar[int]
    VERSION_HISTORY_FIELD_NUMBER: _ClassVar[int]
    next_page_token: bytes
    history_batches: _containers.RepeatedCompositeFieldContainer[_common_pb2.DataBlob]
    version_history: _history_pb2.VersionHistory
    def __init__(self, next_page_token: _Optional[bytes] = ..., history_batches: _Optional[_Iterable[_Union[_common_pb2.DataBlob, _Mapping]]] = ..., version_history: _Optional[_Union[_history_pb2.VersionHistory, _Mapping]] = ...) -> None: ...

class GetReplicationMessagesRequest(_message.Message):
    __slots__ = ("tokens", "cluster_name")
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    tokens: _containers.RepeatedCompositeFieldContainer[_replication_pb2.ReplicationToken]
    cluster_name: str
    def __init__(self, tokens: _Optional[_Iterable[_Union[_replication_pb2.ReplicationToken, _Mapping]]] = ..., cluster_name: _Optional[str] = ...) -> None: ...

class GetReplicationMessagesResponse(_message.Message):
    __slots__ = ("shard_messages",)
    class ShardMessagesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _replication_pb2.ReplicationMessages
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_replication_pb2.ReplicationMessages, _Mapping]] = ...) -> None: ...
    SHARD_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    shard_messages: _containers.MessageMap[int, _replication_pb2.ReplicationMessages]
    def __init__(self, shard_messages: _Optional[_Mapping[int, _replication_pb2.ReplicationMessages]] = ...) -> None: ...

class GetDLQReplicationMessagesRequest(_message.Message):
    __slots__ = ("task_infos",)
    TASK_INFOS_FIELD_NUMBER: _ClassVar[int]
    task_infos: _containers.RepeatedCompositeFieldContainer[_replication_pb2.ReplicationTaskInfo]
    def __init__(self, task_infos: _Optional[_Iterable[_Union[_replication_pb2.ReplicationTaskInfo, _Mapping]]] = ...) -> None: ...

class GetDLQReplicationMessagesResponse(_message.Message):
    __slots__ = ("replication_tasks",)
    REPLICATION_TASKS_FIELD_NUMBER: _ClassVar[int]
    replication_tasks: _containers.RepeatedCompositeFieldContainer[_replication_pb2.ReplicationTask]
    def __init__(self, replication_tasks: _Optional[_Iterable[_Union[_replication_pb2.ReplicationTask, _Mapping]]] = ...) -> None: ...

class GetDomainReplicationMessagesRequest(_message.Message):
    __slots__ = ("last_retrieved_message_id", "last_processed_message_id", "cluster_name")
    LAST_RETRIEVED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    LAST_PROCESSED_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    CLUSTER_NAME_FIELD_NUMBER: _ClassVar[int]
    last_retrieved_message_id: _wrappers_pb2.Int64Value
    last_processed_message_id: _wrappers_pb2.Int64Value
    cluster_name: str
    def __init__(self, last_retrieved_message_id: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., last_processed_message_id: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., cluster_name: _Optional[str] = ...) -> None: ...

class GetDomainReplicationMessagesResponse(_message.Message):
    __slots__ = ("messages",)
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    messages: _replication_pb2.ReplicationMessages
    def __init__(self, messages: _Optional[_Union[_replication_pb2.ReplicationMessages, _Mapping]] = ...) -> None: ...

class ReapplyEventsRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution", "events")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    events: _common_pb2.DataBlob
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., events: _Optional[_Union[_common_pb2.DataBlob, _Mapping]] = ...) -> None: ...

class ReapplyEventsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AddSearchAttributeRequest(_message.Message):
    __slots__ = ("search_attribute", "security_token")
    class SearchAttributeEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _visibility_pb2.IndexedValueType
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_visibility_pb2.IndexedValueType, str]] = ...) -> None: ...
    SEARCH_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_TOKEN_FIELD_NUMBER: _ClassVar[int]
    search_attribute: _containers.ScalarMap[str, _visibility_pb2.IndexedValueType]
    security_token: str
    def __init__(self, search_attribute: _Optional[_Mapping[str, _visibility_pb2.IndexedValueType]] = ..., security_token: _Optional[str] = ...) -> None: ...

class AddSearchAttributeResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeClusterRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeClusterResponse(_message.Message):
    __slots__ = ("supported_client_versions", "membership_info", "persistence_info")
    class PersistenceInfoEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _cluster_pb2.PersistenceInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_cluster_pb2.PersistenceInfo, _Mapping]] = ...) -> None: ...
    SUPPORTED_CLIENT_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    MEMBERSHIP_INFO_FIELD_NUMBER: _ClassVar[int]
    PERSISTENCE_INFO_FIELD_NUMBER: _ClassVar[int]
    supported_client_versions: _common_pb2.SupportedClientVersions
    membership_info: _cluster_pb2.MembershipInfo
    persistence_info: _containers.MessageMap[str, _cluster_pb2.PersistenceInfo]
    def __init__(self, supported_client_versions: _Optional[_Union[_common_pb2.SupportedClientVersions, _Mapping]] = ..., membership_info: _Optional[_Union[_cluster_pb2.MembershipInfo, _Mapping]] = ..., persistence_info: _Optional[_Mapping[str, _cluster_pb2.PersistenceInfo]] = ...) -> None: ...

class CountDLQMessagesRequest(_message.Message):
    __slots__ = ("force_fetch",)
    FORCE_FETCH_FIELD_NUMBER: _ClassVar[int]
    force_fetch: bool
    def __init__(self, force_fetch: bool = ...) -> None: ...

class CountDLQMessagesResponse(_message.Message):
    __slots__ = ("history", "domain")
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    history: _containers.RepeatedCompositeFieldContainer[_replication_pb2.HistoryDLQCountEntry]
    domain: int
    def __init__(self, history: _Optional[_Iterable[_Union[_replication_pb2.HistoryDLQCountEntry, _Mapping]]] = ..., domain: _Optional[int] = ...) -> None: ...

class ReadDLQMessagesRequest(_message.Message):
    __slots__ = ("type", "shard_id", "source_cluster", "inclusive_end_message_id", "page_size", "next_page_token")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    INCLUSIVE_END_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    type: _replication_pb2.DLQType
    shard_id: int
    source_cluster: str
    inclusive_end_message_id: _wrappers_pb2.Int64Value
    page_size: int
    next_page_token: bytes
    def __init__(self, type: _Optional[_Union[_replication_pb2.DLQType, str]] = ..., shard_id: _Optional[int] = ..., source_cluster: _Optional[str] = ..., inclusive_end_message_id: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., page_size: _Optional[int] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class ReadDLQMessagesResponse(_message.Message):
    __slots__ = ("type", "replication_tasks", "replication_tasks_info", "next_page_token")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_TASKS_FIELD_NUMBER: _ClassVar[int]
    REPLICATION_TASKS_INFO_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    type: _replication_pb2.DLQType
    replication_tasks: _containers.RepeatedCompositeFieldContainer[_replication_pb2.ReplicationTask]
    replication_tasks_info: _containers.RepeatedCompositeFieldContainer[_replication_pb2.ReplicationTaskInfo]
    next_page_token: bytes
    def __init__(self, type: _Optional[_Union[_replication_pb2.DLQType, str]] = ..., replication_tasks: _Optional[_Iterable[_Union[_replication_pb2.ReplicationTask, _Mapping]]] = ..., replication_tasks_info: _Optional[_Iterable[_Union[_replication_pb2.ReplicationTaskInfo, _Mapping]]] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class PurgeDLQMessagesRequest(_message.Message):
    __slots__ = ("type", "shard_id", "source_cluster", "inclusive_end_message_id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    INCLUSIVE_END_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    type: _replication_pb2.DLQType
    shard_id: int
    source_cluster: str
    inclusive_end_message_id: _wrappers_pb2.Int64Value
    def __init__(self, type: _Optional[_Union[_replication_pb2.DLQType, str]] = ..., shard_id: _Optional[int] = ..., source_cluster: _Optional[str] = ..., inclusive_end_message_id: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class PurgeDLQMessagesResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class MergeDLQMessagesRequest(_message.Message):
    __slots__ = ("type", "shard_id", "source_cluster", "inclusive_end_message_id", "page_size", "next_page_token")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    INCLUSIVE_END_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    type: _replication_pb2.DLQType
    shard_id: int
    source_cluster: str
    inclusive_end_message_id: _wrappers_pb2.Int64Value
    page_size: int
    next_page_token: bytes
    def __init__(self, type: _Optional[_Union[_replication_pb2.DLQType, str]] = ..., shard_id: _Optional[int] = ..., source_cluster: _Optional[str] = ..., inclusive_end_message_id: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., page_size: _Optional[int] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class MergeDLQMessagesResponse(_message.Message):
    __slots__ = ("next_page_token",)
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    next_page_token: bytes
    def __init__(self, next_page_token: _Optional[bytes] = ...) -> None: ...

class RefreshWorkflowTasksRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ...) -> None: ...

class RefreshWorkflowTasksResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResendReplicationTasksRequest(_message.Message):
    __slots__ = ("domain_id", "workflow_execution", "remote_cluster", "start_event", "end_event")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    REMOTE_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    START_EVENT_FIELD_NUMBER: _ClassVar[int]
    END_EVENT_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    workflow_execution: _common_pb2.WorkflowExecution
    remote_cluster: str
    start_event: _history_pb2.VersionHistoryItem
    end_event: _history_pb2.VersionHistoryItem
    def __init__(self, domain_id: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., remote_cluster: _Optional[str] = ..., start_event: _Optional[_Union[_history_pb2.VersionHistoryItem, _Mapping]] = ..., end_event: _Optional[_Union[_history_pb2.VersionHistoryItem, _Mapping]] = ...) -> None: ...

class ResendReplicationTasksResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetCrossClusterTasksRequest(_message.Message):
    __slots__ = ("shard_ids", "target_cluster")
    SHARD_IDS_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    shard_ids: _containers.RepeatedScalarFieldContainer[int]
    target_cluster: str
    def __init__(self, shard_ids: _Optional[_Iterable[int]] = ..., target_cluster: _Optional[str] = ...) -> None: ...

class GetCrossClusterTasksResponse(_message.Message):
    __slots__ = ("tasks_by_shard", "failed_cause_by_shard")
    class TasksByShardEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _queue_pb2.CrossClusterTaskRequests
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_queue_pb2.CrossClusterTaskRequests, _Mapping]] = ...) -> None: ...
    class FailedCauseByShardEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: _queue_pb2.GetTaskFailedCause
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[_queue_pb2.GetTaskFailedCause, str]] = ...) -> None: ...
    TASKS_BY_SHARD_FIELD_NUMBER: _ClassVar[int]
    FAILED_CAUSE_BY_SHARD_FIELD_NUMBER: _ClassVar[int]
    tasks_by_shard: _containers.MessageMap[int, _queue_pb2.CrossClusterTaskRequests]
    failed_cause_by_shard: _containers.ScalarMap[int, _queue_pb2.GetTaskFailedCause]
    def __init__(self, tasks_by_shard: _Optional[_Mapping[int, _queue_pb2.CrossClusterTaskRequests]] = ..., failed_cause_by_shard: _Optional[_Mapping[int, _queue_pb2.GetTaskFailedCause]] = ...) -> None: ...

class RespondCrossClusterTasksCompletedRequest(_message.Message):
    __slots__ = ("shard_id", "target_cluster", "task_responses", "fetch_new_tasks")
    SHARD_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_CLUSTER_FIELD_NUMBER: _ClassVar[int]
    TASK_RESPONSES_FIELD_NUMBER: _ClassVar[int]
    FETCH_NEW_TASKS_FIELD_NUMBER: _ClassVar[int]
    shard_id: int
    target_cluster: str
    task_responses: _containers.RepeatedCompositeFieldContainer[_queue_pb2.CrossClusterTaskResponse]
    fetch_new_tasks: bool
    def __init__(self, shard_id: _Optional[int] = ..., target_cluster: _Optional[str] = ..., task_responses: _Optional[_Iterable[_Union[_queue_pb2.CrossClusterTaskResponse, _Mapping]]] = ..., fetch_new_tasks: bool = ...) -> None: ...

class RespondCrossClusterTasksCompletedResponse(_message.Message):
    __slots__ = ("tasks",)
    TASKS_FIELD_NUMBER: _ClassVar[int]
    tasks: _queue_pb2.CrossClusterTaskRequests
    def __init__(self, tasks: _Optional[_Union[_queue_pb2.CrossClusterTaskRequests, _Mapping]] = ...) -> None: ...

class GetDynamicConfigRequest(_message.Message):
    __slots__ = ("config_name", "filters")
    CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    config_name: str
    filters: _containers.RepeatedCompositeFieldContainer[DynamicConfigFilter]
    def __init__(self, config_name: _Optional[str] = ..., filters: _Optional[_Iterable[_Union[DynamicConfigFilter, _Mapping]]] = ...) -> None: ...

class GetDynamicConfigResponse(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: _common_pb2.DataBlob
    def __init__(self, value: _Optional[_Union[_common_pb2.DataBlob, _Mapping]] = ...) -> None: ...

class UpdateDynamicConfigRequest(_message.Message):
    __slots__ = ("config_name", "config_values")
    CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    CONFIG_VALUES_FIELD_NUMBER: _ClassVar[int]
    config_name: str
    config_values: _containers.RepeatedCompositeFieldContainer[DynamicConfigValue]
    def __init__(self, config_name: _Optional[str] = ..., config_values: _Optional[_Iterable[_Union[DynamicConfigValue, _Mapping]]] = ...) -> None: ...

class UpdateDynamicConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RestoreDynamicConfigRequest(_message.Message):
    __slots__ = ("config_name", "filters")
    CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    config_name: str
    filters: _containers.RepeatedCompositeFieldContainer[DynamicConfigFilter]
    def __init__(self, config_name: _Optional[str] = ..., filters: _Optional[_Iterable[_Union[DynamicConfigFilter, _Mapping]]] = ...) -> None: ...

class RestoreDynamicConfigResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DeleteWorkflowRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ...) -> None: ...

class DeleteWorkflowResponse(_message.Message):
    __slots__ = ("history_deleted", "executions_deleted", "visibility_deleted")
    HISTORY_DELETED_FIELD_NUMBER: _ClassVar[int]
    EXECUTIONS_DELETED_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_DELETED_FIELD_NUMBER: _ClassVar[int]
    history_deleted: bool
    executions_deleted: bool
    visibility_deleted: bool
    def __init__(self, history_deleted: bool = ..., executions_deleted: bool = ..., visibility_deleted: bool = ...) -> None: ...

class MaintainCorruptWorkflowRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ...) -> None: ...

class MaintainCorruptWorkflowResponse(_message.Message):
    __slots__ = ("history_deleted", "executions_deleted", "visibility_deleted")
    HISTORY_DELETED_FIELD_NUMBER: _ClassVar[int]
    EXECUTIONS_DELETED_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_DELETED_FIELD_NUMBER: _ClassVar[int]
    history_deleted: bool
    executions_deleted: bool
    visibility_deleted: bool
    def __init__(self, history_deleted: bool = ..., executions_deleted: bool = ..., visibility_deleted: bool = ...) -> None: ...

class ListDynamicConfigRequest(_message.Message):
    __slots__ = ("config_name",)
    CONFIG_NAME_FIELD_NUMBER: _ClassVar[int]
    config_name: str
    def __init__(self, config_name: _Optional[str] = ...) -> None: ...

class ListDynamicConfigResponse(_message.Message):
    __slots__ = ("entries",)
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[DynamicConfigEntry]
    def __init__(self, entries: _Optional[_Iterable[_Union[DynamicConfigEntry, _Mapping]]] = ...) -> None: ...

class DynamicConfigEntry(_message.Message):
    __slots__ = ("name", "values")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUES_FIELD_NUMBER: _ClassVar[int]
    name: str
    values: _containers.RepeatedCompositeFieldContainer[DynamicConfigValue]
    def __init__(self, name: _Optional[str] = ..., values: _Optional[_Iterable[_Union[DynamicConfigValue, _Mapping]]] = ...) -> None: ...

class DynamicConfigValue(_message.Message):
    __slots__ = ("value", "filters")
    VALUE_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    value: _common_pb2.DataBlob
    filters: _containers.RepeatedCompositeFieldContainer[DynamicConfigFilter]
    def __init__(self, value: _Optional[_Union[_common_pb2.DataBlob, _Mapping]] = ..., filters: _Optional[_Iterable[_Union[DynamicConfigFilter, _Mapping]]] = ...) -> None: ...

class DynamicConfigFilter(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _common_pb2.DataBlob
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[_common_pb2.DataBlob, _Mapping]] = ...) -> None: ...

class GetGlobalIsolationGroupsRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetGlobalIsolationGroupsResponse(_message.Message):
    __slots__ = ("isolation_groups",)
    ISOLATION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    isolation_groups: _common_pb2.IsolationGroupConfiguration
    def __init__(self, isolation_groups: _Optional[_Union[_common_pb2.IsolationGroupConfiguration, _Mapping]] = ...) -> None: ...

class UpdateGlobalIsolationGroupsRequest(_message.Message):
    __slots__ = ("isolation_groups",)
    ISOLATION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    isolation_groups: _common_pb2.IsolationGroupConfiguration
    def __init__(self, isolation_groups: _Optional[_Union[_common_pb2.IsolationGroupConfiguration, _Mapping]] = ...) -> None: ...

class UpdateGlobalIsolationGroupsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDomainIsolationGroupsRequest(_message.Message):
    __slots__ = ("domain",)
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    domain: str
    def __init__(self, domain: _Optional[str] = ...) -> None: ...

class GetDomainIsolationGroupsResponse(_message.Message):
    __slots__ = ("isolation_groups",)
    ISOLATION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    isolation_groups: _common_pb2.IsolationGroupConfiguration
    def __init__(self, isolation_groups: _Optional[_Union[_common_pb2.IsolationGroupConfiguration, _Mapping]] = ...) -> None: ...

class UpdateDomainIsolationGroupsRequest(_message.Message):
    __slots__ = ("domain", "isolation_groups")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    ISOLATION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    isolation_groups: _common_pb2.IsolationGroupConfiguration
    def __init__(self, domain: _Optional[str] = ..., isolation_groups: _Optional[_Union[_common_pb2.IsolationGroupConfiguration, _Mapping]] = ...) -> None: ...

class UpdateDomainIsolationGroupsResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetDomainAsyncWorkflowConfiguratonRequest(_message.Message):
    __slots__ = ("domain",)
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    domain: str
    def __init__(self, domain: _Optional[str] = ...) -> None: ...

class GetDomainAsyncWorkflowConfiguratonResponse(_message.Message):
    __slots__ = ("configuration",)
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    configuration: _common_pb2.AsyncWorkflowConfiguration
    def __init__(self, configuration: _Optional[_Union[_common_pb2.AsyncWorkflowConfiguration, _Mapping]] = ...) -> None: ...

class UpdateDomainAsyncWorkflowConfiguratonRequest(_message.Message):
    __slots__ = ("domain", "configuration")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    domain: str
    configuration: _common_pb2.AsyncWorkflowConfiguration
    def __init__(self, domain: _Optional[str] = ..., configuration: _Optional[_Union[_common_pb2.AsyncWorkflowConfiguration, _Mapping]] = ...) -> None: ...

class UpdateDomainAsyncWorkflowConfiguratonResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
