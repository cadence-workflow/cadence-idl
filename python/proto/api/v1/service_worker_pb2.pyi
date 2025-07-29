from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from uber.cadence.api.v1 import common_pb2 as _common_pb2
from uber.cadence.api.v1 import decision_pb2 as _decision_pb2
from uber.cadence.api.v1 import history_pb2 as _history_pb2
from uber.cadence.api.v1 import query_pb2 as _query_pb2
from uber.cadence.api.v1 import tasklist_pb2 as _tasklist_pb2
from uber.cadence.api.v1 import workflow_pb2 as _workflow_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PollForDecisionTaskRequest(_message.Message):
    __slots__ = ("domain", "task_list", "identity", "binary_checksum")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    BINARY_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    domain: str
    task_list: _tasklist_pb2.TaskList
    identity: str
    binary_checksum: str
    def __init__(self, domain: _Optional[str] = ..., task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., identity: _Optional[str] = ..., binary_checksum: _Optional[str] = ...) -> None: ...

class PollForDecisionTaskResponse(_message.Message):
    __slots__ = ("task_token", "workflow_execution", "workflow_type", "previous_started_event_id", "started_event_id", "attempt", "backlog_count_hint", "history", "next_page_token", "query", "workflow_execution_task_list", "scheduled_time", "started_time", "queries", "next_event_id", "total_history_bytes", "auto_config_hint")
    class QueriesEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _query_pb2.WorkflowQuery
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_query_pb2.WorkflowQuery, _Mapping]] = ...) -> None: ...
    TASK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    BACKLOG_COUNT_HINT_FIELD_NUMBER: _ClassVar[int]
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_TIME_FIELD_NUMBER: _ClassVar[int]
    STARTED_TIME_FIELD_NUMBER: _ClassVar[int]
    QUERIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    TOTAL_HISTORY_BYTES_FIELD_NUMBER: _ClassVar[int]
    AUTO_CONFIG_HINT_FIELD_NUMBER: _ClassVar[int]
    task_token: bytes
    workflow_execution: _common_pb2.WorkflowExecution
    workflow_type: _common_pb2.WorkflowType
    previous_started_event_id: _wrappers_pb2.Int64Value
    started_event_id: int
    attempt: int
    backlog_count_hint: int
    history: _history_pb2.History
    next_page_token: bytes
    query: _query_pb2.WorkflowQuery
    workflow_execution_task_list: _tasklist_pb2.TaskList
    scheduled_time: _timestamp_pb2.Timestamp
    started_time: _timestamp_pb2.Timestamp
    queries: _containers.MessageMap[str, _query_pb2.WorkflowQuery]
    next_event_id: int
    total_history_bytes: int
    auto_config_hint: AutoConfigHint
    def __init__(self, task_token: _Optional[bytes] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., previous_started_event_id: _Optional[_Union[_wrappers_pb2.Int64Value, _Mapping]] = ..., started_event_id: _Optional[int] = ..., attempt: _Optional[int] = ..., backlog_count_hint: _Optional[int] = ..., history: _Optional[_Union[_history_pb2.History, _Mapping]] = ..., next_page_token: _Optional[bytes] = ..., query: _Optional[_Union[_query_pb2.WorkflowQuery, _Mapping]] = ..., workflow_execution_task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., scheduled_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., queries: _Optional[_Mapping[str, _query_pb2.WorkflowQuery]] = ..., next_event_id: _Optional[int] = ..., total_history_bytes: _Optional[int] = ..., auto_config_hint: _Optional[_Union[AutoConfigHint, _Mapping]] = ...) -> None: ...

class RespondDecisionTaskCompletedRequest(_message.Message):
    __slots__ = ("task_token", "decisions", "execution_context", "identity", "sticky_attributes", "return_new_decision_task", "force_create_new_decision_task", "binary_checksum", "query_results")
    class QueryResultsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _query_pb2.WorkflowQueryResult
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_query_pb2.WorkflowQueryResult, _Mapping]] = ...) -> None: ...
    TASK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DECISIONS_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    STICKY_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    RETURN_NEW_DECISION_TASK_FIELD_NUMBER: _ClassVar[int]
    FORCE_CREATE_NEW_DECISION_TASK_FIELD_NUMBER: _ClassVar[int]
    BINARY_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    QUERY_RESULTS_FIELD_NUMBER: _ClassVar[int]
    task_token: bytes
    decisions: _containers.RepeatedCompositeFieldContainer[_decision_pb2.Decision]
    execution_context: bytes
    identity: str
    sticky_attributes: _tasklist_pb2.StickyExecutionAttributes
    return_new_decision_task: bool
    force_create_new_decision_task: bool
    binary_checksum: str
    query_results: _containers.MessageMap[str, _query_pb2.WorkflowQueryResult]
    def __init__(self, task_token: _Optional[bytes] = ..., decisions: _Optional[_Iterable[_Union[_decision_pb2.Decision, _Mapping]]] = ..., execution_context: _Optional[bytes] = ..., identity: _Optional[str] = ..., sticky_attributes: _Optional[_Union[_tasklist_pb2.StickyExecutionAttributes, _Mapping]] = ..., return_new_decision_task: bool = ..., force_create_new_decision_task: bool = ..., binary_checksum: _Optional[str] = ..., query_results: _Optional[_Mapping[str, _query_pb2.WorkflowQueryResult]] = ...) -> None: ...

class RespondDecisionTaskCompletedResponse(_message.Message):
    __slots__ = ("decision_task", "activities_to_dispatch_locally")
    class ActivitiesToDispatchLocallyEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _workflow_pb2.ActivityLocalDispatchInfo
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_workflow_pb2.ActivityLocalDispatchInfo, _Mapping]] = ...) -> None: ...
    DECISION_TASK_FIELD_NUMBER: _ClassVar[int]
    ACTIVITIES_TO_DISPATCH_LOCALLY_FIELD_NUMBER: _ClassVar[int]
    decision_task: PollForDecisionTaskResponse
    activities_to_dispatch_locally: _containers.MessageMap[str, _workflow_pb2.ActivityLocalDispatchInfo]
    def __init__(self, decision_task: _Optional[_Union[PollForDecisionTaskResponse, _Mapping]] = ..., activities_to_dispatch_locally: _Optional[_Mapping[str, _workflow_pb2.ActivityLocalDispatchInfo]] = ...) -> None: ...

class RespondDecisionTaskFailedRequest(_message.Message):
    __slots__ = ("task_token", "cause", "details", "identity", "binary_checksum")
    TASK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    BINARY_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    task_token: bytes
    cause: _workflow_pb2.DecisionTaskFailedCause
    details: _common_pb2.Payload
    identity: str
    binary_checksum: str
    def __init__(self, task_token: _Optional[bytes] = ..., cause: _Optional[_Union[_workflow_pb2.DecisionTaskFailedCause, str]] = ..., details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., identity: _Optional[str] = ..., binary_checksum: _Optional[str] = ...) -> None: ...

class RespondDecisionTaskFailedResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class PollForActivityTaskRequest(_message.Message):
    __slots__ = ("domain", "task_list", "identity", "task_list_metadata")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_METADATA_FIELD_NUMBER: _ClassVar[int]
    domain: str
    task_list: _tasklist_pb2.TaskList
    identity: str
    task_list_metadata: _tasklist_pb2.TaskListMetadata
    def __init__(self, domain: _Optional[str] = ..., task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., identity: _Optional[str] = ..., task_list_metadata: _Optional[_Union[_tasklist_pb2.TaskListMetadata, _Mapping]] = ...) -> None: ...

class PollForActivityTaskResponse(_message.Message):
    __slots__ = ("task_token", "workflow_execution", "activity_id", "activity_type", "input", "scheduled_time", "started_time", "schedule_to_close_timeout", "start_to_close_timeout", "heartbeat_timeout", "attempt", "scheduled_time_of_this_attempt", "heartbeat_details", "workflow_type", "workflow_domain", "header", "auto_config_hint")
    TASK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_TIME_FIELD_NUMBER: _ClassVar[int]
    STARTED_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_TIME_OF_THIS_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_DOMAIN_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    AUTO_CONFIG_HINT_FIELD_NUMBER: _ClassVar[int]
    task_token: bytes
    workflow_execution: _common_pb2.WorkflowExecution
    activity_id: str
    activity_type: _common_pb2.ActivityType
    input: _common_pb2.Payload
    scheduled_time: _timestamp_pb2.Timestamp
    started_time: _timestamp_pb2.Timestamp
    schedule_to_close_timeout: _duration_pb2.Duration
    start_to_close_timeout: _duration_pb2.Duration
    heartbeat_timeout: _duration_pb2.Duration
    attempt: int
    scheduled_time_of_this_attempt: _timestamp_pb2.Timestamp
    heartbeat_details: _common_pb2.Payload
    workflow_type: _common_pb2.WorkflowType
    workflow_domain: str
    header: _common_pb2.Header
    auto_config_hint: AutoConfigHint
    def __init__(self, task_token: _Optional[bytes] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., activity_id: _Optional[str] = ..., activity_type: _Optional[_Union[_common_pb2.ActivityType, _Mapping]] = ..., input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., scheduled_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., schedule_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., heartbeat_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., attempt: _Optional[int] = ..., scheduled_time_of_this_attempt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., heartbeat_details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., workflow_domain: _Optional[str] = ..., header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., auto_config_hint: _Optional[_Union[AutoConfigHint, _Mapping]] = ...) -> None: ...

class RespondActivityTaskCompletedRequest(_message.Message):
    __slots__ = ("task_token", "result", "identity")
    TASK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    task_token: bytes
    result: _common_pb2.Payload
    identity: str
    def __init__(self, task_token: _Optional[bytes] = ..., result: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., identity: _Optional[str] = ...) -> None: ...

class RespondActivityTaskCompletedResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RespondActivityTaskCompletedByIDRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution", "activity_id", "result", "identity")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    activity_id: str
    result: _common_pb2.Payload
    identity: str
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., activity_id: _Optional[str] = ..., result: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., identity: _Optional[str] = ...) -> None: ...

class RespondActivityTaskCompletedByIDResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RespondActivityTaskFailedRequest(_message.Message):
    __slots__ = ("task_token", "failure", "identity")
    TASK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    task_token: bytes
    failure: _common_pb2.Failure
    identity: str
    def __init__(self, task_token: _Optional[bytes] = ..., failure: _Optional[_Union[_common_pb2.Failure, _Mapping]] = ..., identity: _Optional[str] = ...) -> None: ...

class RespondActivityTaskFailedResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RespondActivityTaskFailedByIDRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution", "activity_id", "failure", "identity")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    activity_id: str
    failure: _common_pb2.Failure
    identity: str
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., activity_id: _Optional[str] = ..., failure: _Optional[_Union[_common_pb2.Failure, _Mapping]] = ..., identity: _Optional[str] = ...) -> None: ...

class RespondActivityTaskFailedByIDResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RespondActivityTaskCanceledRequest(_message.Message):
    __slots__ = ("task_token", "details", "identity")
    TASK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    task_token: bytes
    details: _common_pb2.Payload
    identity: str
    def __init__(self, task_token: _Optional[bytes] = ..., details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., identity: _Optional[str] = ...) -> None: ...

class RespondActivityTaskCanceledResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RespondActivityTaskCanceledByIDRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution", "activity_id", "details", "identity")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    activity_id: str
    details: _common_pb2.Payload
    identity: str
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., activity_id: _Optional[str] = ..., details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., identity: _Optional[str] = ...) -> None: ...

class RespondActivityTaskCanceledByIDResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class RecordActivityTaskHeartbeatRequest(_message.Message):
    __slots__ = ("task_token", "details", "identity")
    TASK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    task_token: bytes
    details: _common_pb2.Payload
    identity: str
    def __init__(self, task_token: _Optional[bytes] = ..., details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., identity: _Optional[str] = ...) -> None: ...

class RecordActivityTaskHeartbeatResponse(_message.Message):
    __slots__ = ("cancel_requested",)
    CANCEL_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    cancel_requested: bool
    def __init__(self, cancel_requested: bool = ...) -> None: ...

class RecordActivityTaskHeartbeatByIDRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution", "activity_id", "details", "identity")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    activity_id: str
    details: _common_pb2.Payload
    identity: str
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., activity_id: _Optional[str] = ..., details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., identity: _Optional[str] = ...) -> None: ...

class RecordActivityTaskHeartbeatByIDResponse(_message.Message):
    __slots__ = ("cancel_requested",)
    CANCEL_REQUESTED_FIELD_NUMBER: _ClassVar[int]
    cancel_requested: bool
    def __init__(self, cancel_requested: bool = ...) -> None: ...

class RespondQueryTaskCompletedRequest(_message.Message):
    __slots__ = ("task_token", "result", "worker_version_info")
    TASK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    WORKER_VERSION_INFO_FIELD_NUMBER: _ClassVar[int]
    task_token: bytes
    result: _query_pb2.WorkflowQueryResult
    worker_version_info: _common_pb2.WorkerVersionInfo
    def __init__(self, task_token: _Optional[bytes] = ..., result: _Optional[_Union[_query_pb2.WorkflowQueryResult, _Mapping]] = ..., worker_version_info: _Optional[_Union[_common_pb2.WorkerVersionInfo, _Mapping]] = ...) -> None: ...

class RespondQueryTaskCompletedResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ResetStickyTaskListRequest(_message.Message):
    __slots__ = ("domain", "workflow_execution")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ...) -> None: ...

class ResetStickyTaskListResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class AutoConfigHint(_message.Message):
    __slots__ = ("enable_auto_config", "poller_wait_time_in_ms")
    ENABLE_AUTO_CONFIG_FIELD_NUMBER: _ClassVar[int]
    POLLER_WAIT_TIME_IN_MS_FIELD_NUMBER: _ClassVar[int]
    enable_auto_config: bool
    poller_wait_time_in_ms: int
    def __init__(self, enable_auto_config: bool = ..., poller_wait_time_in_ms: _Optional[int] = ...) -> None: ...
