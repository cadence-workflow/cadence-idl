from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from uber.cadence.api.v1 import common_pb2 as _common_pb2
from uber.cadence.api.v1 import history_pb2 as _history_pb2
from uber.cadence.api.v1 import query_pb2 as _query_pb2
from uber.cadence.api.v1 import tasklist_pb2 as _tasklist_pb2
from uber.cadence.api.v1 import workflow_pb2 as _workflow_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RestartWorkflowExecutionRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution", "identity", "reason")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    identity: str
    reason: str
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., identity: _Optional[str] = ..., reason: _Optional[str] = ...) -> None: ...

class DiagnoseWorkflowExecutionRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution", "identity")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    identity: str
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., identity: _Optional[str] = ...) -> None: ...

class DiagnoseWorkflowExecutionResponse(_message.Message):
    __slots__ = ("domain", "diagnostic_workflow_execution")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    DIAGNOSTIC_WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    domain: str
    diagnostic_workflow_execution: _common_pb2.WorkflowExecution
    def __init__(self, domain: _Optional[str] = ..., diagnostic_workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ...) -> None: ...

class StartWorkflowExecutionRequest(_message.Message):
    __slots__ = ("domain", "workflow_id", "workflow_type", "task_list", "input", "execution_start_to_close_timeout", "task_start_to_close_timeout", "identity", "request_id", "workflow_id_reuse_policy", "retry_policy", "cron_schedule", "memo", "search_attributes", "header", "delay_start", "jitter_start", "first_run_at", "cron_overlap_policy", "active_cluster_selection_policy")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TASK_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_REUSE_POLICY_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    CRON_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    DELAY_START_FIELD_NUMBER: _ClassVar[int]
    JITTER_START_FIELD_NUMBER: _ClassVar[int]
    FIRST_RUN_AT_FIELD_NUMBER: _ClassVar[int]
    CRON_OVERLAP_POLICY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTER_SELECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_id: str
    workflow_type: _common_pb2.WorkflowType
    task_list: _tasklist_pb2.TaskList
    input: _common_pb2.Payload
    execution_start_to_close_timeout: _duration_pb2.Duration
    task_start_to_close_timeout: _duration_pb2.Duration
    identity: str
    request_id: str
    workflow_id_reuse_policy: _workflow_pb2.WorkflowIdReusePolicy
    retry_policy: _common_pb2.RetryPolicy
    cron_schedule: str
    memo: _common_pb2.Memo
    search_attributes: _common_pb2.SearchAttributes
    header: _common_pb2.Header
    delay_start: _duration_pb2.Duration
    jitter_start: _duration_pb2.Duration
    first_run_at: _timestamp_pb2.Timestamp
    cron_overlap_policy: _workflow_pb2.CronOverlapPolicy
    active_cluster_selection_policy: _common_pb2.ActiveClusterSelectionPolicy
    def __init__(self, domain: _Optional[str] = ..., workflow_id: _Optional[str] = ..., workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., execution_start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., task_start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., identity: _Optional[str] = ..., request_id: _Optional[str] = ..., workflow_id_reuse_policy: _Optional[_Union[_workflow_pb2.WorkflowIdReusePolicy, str]] = ..., retry_policy: _Optional[_Union[_common_pb2.RetryPolicy, _Mapping]] = ..., cron_schedule: _Optional[str] = ..., memo: _Optional[_Union[_common_pb2.Memo, _Mapping]] = ..., search_attributes: _Optional[_Union[_common_pb2.SearchAttributes, _Mapping]] = ..., header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., delay_start: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., jitter_start: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., first_run_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cron_overlap_policy: _Optional[_Union[_workflow_pb2.CronOverlapPolicy, str]] = ..., active_cluster_selection_policy: _Optional[_Union[_common_pb2.ActiveClusterSelectionPolicy, _Mapping]] = ...) -> None: ...

class StartWorkflowExecutionResponse(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class StartWorkflowExecutionAsyncRequest(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: StartWorkflowExecutionRequest
    def __init__(self, request: _Optional[_Union[StartWorkflowExecutionRequest, _Mapping]] = ...) -> None: ...

class StartWorkflowExecutionAsyncResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RestartWorkflowExecutionResponse(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class SignalWorkflowExecutionRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution", "identity", "request_id", "signal_name", "signal_input", "control")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_NAME_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_INPUT_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    identity: str
    request_id: str
    signal_name: str
    signal_input: _common_pb2.Payload
    control: bytes
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., identity: _Optional[str] = ..., request_id: _Optional[str] = ..., signal_name: _Optional[str] = ..., signal_input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., control: _Optional[bytes] = ...) -> None: ...

class SignalWorkflowExecutionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SignalWithStartWorkflowExecutionRequest(_message.Message):
    __slots__ = ("start_request", "signal_name", "signal_input", "control")
    START_REQUEST_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_NAME_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_INPUT_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    start_request: StartWorkflowExecutionRequest
    signal_name: str
    signal_input: _common_pb2.Payload
    control: bytes
    def __init__(self, start_request: _Optional[_Union[StartWorkflowExecutionRequest, _Mapping]] = ..., signal_name: _Optional[str] = ..., signal_input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., control: _Optional[bytes] = ...) -> None: ...

class SignalWithStartWorkflowExecutionResponse(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class SignalWithStartWorkflowExecutionAsyncRequest(_message.Message):
    __slots__ = ("request",)
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    request: SignalWithStartWorkflowExecutionRequest
    def __init__(self, request: _Optional[_Union[SignalWithStartWorkflowExecutionRequest, _Mapping]] = ...) -> None: ...

class SignalWithStartWorkflowExecutionAsyncResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetWorkflowExecutionRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution", "reason", "decision_finish_event_id", "request_id", "skip_signal_reapply")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DECISION_FINISH_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    SKIP_SIGNAL_REAPPLY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    reason: str
    decision_finish_event_id: int
    request_id: str
    skip_signal_reapply: bool
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., reason: _Optional[str] = ..., decision_finish_event_id: _Optional[int] = ..., request_id: _Optional[str] = ..., skip_signal_reapply: bool = ...) -> None: ...

class ResetWorkflowExecutionResponse(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class RequestCancelWorkflowExecutionRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution", "identity", "request_id", "cause", "first_execution_run_id")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    FIRST_EXECUTION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    identity: str
    request_id: str
    cause: str
    first_execution_run_id: str
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., identity: _Optional[str] = ..., request_id: _Optional[str] = ..., cause: _Optional[str] = ..., first_execution_run_id: _Optional[str] = ...) -> None: ...

class RequestCancelWorkflowExecutionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class TerminateWorkflowExecutionRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution", "reason", "details", "identity", "first_execution_run_id")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    FIRST_EXECUTION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    reason: str
    details: _common_pb2.Payload
    identity: str
    first_execution_run_id: str
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., reason: _Optional[str] = ..., details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., identity: _Optional[str] = ..., first_execution_run_id: _Optional[str] = ...) -> None: ...

class TerminateWorkflowExecutionResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class DescribeWorkflowExecutionRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution", "query_consistency_level")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    QUERY_CONSISTENCY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    query_consistency_level: _query_pb2.QueryConsistencyLevel
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., query_consistency_level: _Optional[_Union[_query_pb2.QueryConsistencyLevel, str]] = ...) -> None: ...

class DescribeWorkflowExecutionResponse(_message.Message):
    __slots__ = ("execution_configuration", "workflow_execution_info", "pending_activities", "pending_children", "pending_decision")
    EXECUTION_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_INFO_FIELD_NUMBER: _ClassVar[int]
    PENDING_ACTIVITIES_FIELD_NUMBER: _ClassVar[int]
    PENDING_CHILDREN_FIELD_NUMBER: _ClassVar[int]
    PENDING_DECISION_FIELD_NUMBER: _ClassVar[int]
    execution_configuration: _workflow_pb2.WorkflowExecutionConfiguration
    workflow_execution_info: _workflow_pb2.WorkflowExecutionInfo
    pending_activities: _containers.RepeatedCompositeFieldContainer[_workflow_pb2.PendingActivityInfo]
    pending_children: _containers.RepeatedCompositeFieldContainer[_workflow_pb2.PendingChildExecutionInfo]
    pending_decision: _workflow_pb2.PendingDecisionInfo
    def __init__(self, execution_configuration: _Optional[_Union[_workflow_pb2.WorkflowExecutionConfiguration, _Mapping]] = ..., workflow_execution_info: _Optional[_Union[_workflow_pb2.WorkflowExecutionInfo, _Mapping]] = ..., pending_activities: _Optional[_Iterable[_Union[_workflow_pb2.PendingActivityInfo, _Mapping]]] = ..., pending_children: _Optional[_Iterable[_Union[_workflow_pb2.PendingChildExecutionInfo, _Mapping]]] = ..., pending_decision: _Optional[_Union[_workflow_pb2.PendingDecisionInfo, _Mapping]] = ...) -> None: ...

class QueryWorkflowRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution", "query", "query_reject_condition", "query_consistency_level")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    QUERY_REJECT_CONDITION_FIELD_NUMBER: _ClassVar[int]
    QUERY_CONSISTENCY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    query: _query_pb2.WorkflowQuery
    query_reject_condition: _query_pb2.QueryRejectCondition
    query_consistency_level: _query_pb2.QueryConsistencyLevel
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., query: _Optional[_Union[_query_pb2.WorkflowQuery, _Mapping]] = ..., query_reject_condition: _Optional[_Union[_query_pb2.QueryRejectCondition, str]] = ..., query_consistency_level: _Optional[_Union[_query_pb2.QueryConsistencyLevel, str]] = ...) -> None: ...

class QueryWorkflowResponse(_message.Message):
    __slots__ = ("query_result", "query_rejected")
    QUERY_RESULT_FIELD_NUMBER: _ClassVar[int]
    QUERY_REJECTED_FIELD_NUMBER: _ClassVar[int]
    query_result: _common_pb2.Payload
    query_rejected: _query_pb2.QueryRejected
    def __init__(self, query_result: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., query_rejected: _Optional[_Union[_query_pb2.QueryRejected, _Mapping]] = ...) -> None: ...

class DescribeTaskListRequest(_message.Message):
    __slots__ = ("domain", "task_list", "task_list_type", "include_task_list_status")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_TYPE_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_TASK_LIST_STATUS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    task_list: _tasklist_pb2.TaskList
    task_list_type: _tasklist_pb2.TaskListType
    include_task_list_status: bool
    def __init__(self, domain: _Optional[str] = ..., task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., task_list_type: _Optional[_Union[_tasklist_pb2.TaskListType, str]] = ..., include_task_list_status: bool = ...) -> None: ...

class DescribeTaskListResponse(_message.Message):
    __slots__ = ("pollers", "task_list_status", "partition_config", "task_list")
    POLLERS_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_STATUS_FIELD_NUMBER: _ClassVar[int]
    PARTITION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    pollers: _containers.RepeatedCompositeFieldContainer[_tasklist_pb2.PollerInfo]
    task_list_status: _tasklist_pb2.TaskListStatus
    partition_config: _tasklist_pb2.TaskListPartitionConfig
    task_list: _tasklist_pb2.TaskList
    def __init__(self, pollers: _Optional[_Iterable[_Union[_tasklist_pb2.PollerInfo, _Mapping]]] = ..., task_list_status: _Optional[_Union[_tasklist_pb2.TaskListStatus, _Mapping]] = ..., partition_config: _Optional[_Union[_tasklist_pb2.TaskListPartitionConfig, _Mapping]] = ..., task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ...) -> None: ...

class GetTaskListsByDomainRequest(_message.Message):
    __slots__ = ("domain",)
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    domain: str
    def __init__(self, domain: _Optional[str] = ...) -> None: ...

class GetTaskListsByDomainResponse(_message.Message):
    __slots__ = ("decision_task_list_map", "activity_task_list_map")
    class DecisionTaskListMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DescribeTaskListResponse
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[DescribeTaskListResponse, _Mapping]] = ...) -> None: ...
    class ActivityTaskListMapEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: DescribeTaskListResponse
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[DescribeTaskListResponse, _Mapping]] = ...) -> None: ...
    DECISION_TASK_LIST_MAP_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TASK_LIST_MAP_FIELD_NUMBER: _ClassVar[int]
    decision_task_list_map: _containers.MessageMap[str, DescribeTaskListResponse]
    activity_task_list_map: _containers.MessageMap[str, DescribeTaskListResponse]
    def __init__(self, decision_task_list_map: _Optional[_Mapping[str, DescribeTaskListResponse]] = ..., activity_task_list_map: _Optional[_Mapping[str, DescribeTaskListResponse]] = ...) -> None: ...

class ListTaskListPartitionsRequest(_message.Message):
    __slots__ = ("domain", "task_list")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    domain: str
    task_list: _tasklist_pb2.TaskList
    def __init__(self, domain: _Optional[str] = ..., task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ...) -> None: ...

class ListTaskListPartitionsResponse(_message.Message):
    __slots__ = ("activity_task_list_partitions", "decision_task_list_partitions")
    ACTIVITY_TASK_LIST_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_LIST_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    activity_task_list_partitions: _containers.RepeatedCompositeFieldContainer[_tasklist_pb2.TaskListPartitionMetadata]
    decision_task_list_partitions: _containers.RepeatedCompositeFieldContainer[_tasklist_pb2.TaskListPartitionMetadata]
    def __init__(self, activity_task_list_partitions: _Optional[_Iterable[_Union[_tasklist_pb2.TaskListPartitionMetadata, _Mapping]]] = ..., decision_task_list_partitions: _Optional[_Iterable[_Union[_tasklist_pb2.TaskListPartitionMetadata, _Mapping]]] = ...) -> None: ...

class GetClusterInfoRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetClusterInfoResponse(_message.Message):
    __slots__ = ("supported_client_versions",)
    SUPPORTED_CLIENT_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    supported_client_versions: _common_pb2.SupportedClientVersions
    def __init__(self, supported_client_versions: _Optional[_Union[_common_pb2.SupportedClientVersions, _Mapping]] = ...) -> None: ...

class GetWorkflowExecutionHistoryRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution", "page_size", "next_page_token", "wait_for_new_event", "history_event_filter_type", "skip_archival", "query_consistency_level")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    WAIT_FOR_NEW_EVENT_FIELD_NUMBER: _ClassVar[int]
    HISTORY_EVENT_FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SKIP_ARCHIVAL_FIELD_NUMBER: _ClassVar[int]
    QUERY_CONSISTENCY_LEVEL_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    page_size: int
    next_page_token: bytes
    wait_for_new_event: bool
    history_event_filter_type: _history_pb2.EventFilterType
    skip_archival: bool
    query_consistency_level: _query_pb2.QueryConsistencyLevel
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., page_size: _Optional[int] = ..., next_page_token: _Optional[bytes] = ..., wait_for_new_event: bool = ..., history_event_filter_type: _Optional[_Union[_history_pb2.EventFilterType, str]] = ..., skip_archival: bool = ..., query_consistency_level: _Optional[_Union[_query_pb2.QueryConsistencyLevel, str]] = ...) -> None: ...

class GetWorkflowExecutionHistoryResponse(_message.Message):
    __slots__ = ("history", "raw_history", "next_page_token", "archived")
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    RAW_HISTORY_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ARCHIVED_FIELD_NUMBER: _ClassVar[int]
    history: _history_pb2.History
    raw_history: _containers.RepeatedCompositeFieldContainer[_common_pb2.DataBlob]
    next_page_token: bytes
    archived: bool
    def __init__(self, history: _Optional[_Union[_history_pb2.History, _Mapping]] = ..., raw_history: _Optional[_Iterable[_Union[_common_pb2.DataBlob, _Mapping]]] = ..., next_page_token: _Optional[bytes] = ..., archived: bool = ...) -> None: ...

class FeatureFlags(_message.Message):
    __slots__ = ("workflow_execution_already_completed_error_enabled",)
    WORKFLOW_EXECUTION_ALREADY_COMPLETED_ERROR_ENABLED_FIELD_NUMBER: _ClassVar[int]
    workflow_execution_already_completed_error_enabled: bool
    def __init__(self, workflow_execution_already_completed_error_enabled: bool = ...) -> None: ...

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
