from google.protobuf import duration_pb2 as _duration_pb2
from uber.cadence.api.v1 import common_pb2 as _common_pb2
from uber.cadence.api.v1 import tasklist_pb2 as _tasklist_pb2
from uber.cadence.api.v1 import workflow_pb2 as _workflow_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Decision(_message.Message):
    __slots__ = ("schedule_activity_task_decision_attributes", "start_timer_decision_attributes", "complete_workflow_execution_decision_attributes", "fail_workflow_execution_decision_attributes", "request_cancel_activity_task_decision_attributes", "cancel_timer_decision_attributes", "cancel_workflow_execution_decision_attributes", "request_cancel_external_workflow_execution_decision_attributes", "record_marker_decision_attributes", "continue_as_new_workflow_execution_decision_attributes", "start_child_workflow_execution_decision_attributes", "signal_external_workflow_execution_decision_attributes", "upsert_workflow_search_attributes_decision_attributes")
    SCHEDULE_ACTIVITY_TASK_DECISION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    START_TIMER_DECISION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    COMPLETE_WORKFLOW_EXECUTION_DECISION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    FAIL_WORKFLOW_EXECUTION_DECISION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CANCEL_ACTIVITY_TASK_DECISION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIMER_DECISION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CANCEL_WORKFLOW_EXECUTION_DECISION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_DECISION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    RECORD_MARKER_DECISION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CONTINUE_AS_NEW_WORKFLOW_EXECUTION_DECISION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    START_CHILD_WORKFLOW_EXECUTION_DECISION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_DECISION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    UPSERT_WORKFLOW_SEARCH_ATTRIBUTES_DECISION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    schedule_activity_task_decision_attributes: ScheduleActivityTaskDecisionAttributes
    start_timer_decision_attributes: StartTimerDecisionAttributes
    complete_workflow_execution_decision_attributes: CompleteWorkflowExecutionDecisionAttributes
    fail_workflow_execution_decision_attributes: FailWorkflowExecutionDecisionAttributes
    request_cancel_activity_task_decision_attributes: RequestCancelActivityTaskDecisionAttributes
    cancel_timer_decision_attributes: CancelTimerDecisionAttributes
    cancel_workflow_execution_decision_attributes: CancelWorkflowExecutionDecisionAttributes
    request_cancel_external_workflow_execution_decision_attributes: RequestCancelExternalWorkflowExecutionDecisionAttributes
    record_marker_decision_attributes: RecordMarkerDecisionAttributes
    continue_as_new_workflow_execution_decision_attributes: ContinueAsNewWorkflowExecutionDecisionAttributes
    start_child_workflow_execution_decision_attributes: StartChildWorkflowExecutionDecisionAttributes
    signal_external_workflow_execution_decision_attributes: SignalExternalWorkflowExecutionDecisionAttributes
    upsert_workflow_search_attributes_decision_attributes: UpsertWorkflowSearchAttributesDecisionAttributes
    def __init__(self, schedule_activity_task_decision_attributes: _Optional[_Union[ScheduleActivityTaskDecisionAttributes, _Mapping]] = ..., start_timer_decision_attributes: _Optional[_Union[StartTimerDecisionAttributes, _Mapping]] = ..., complete_workflow_execution_decision_attributes: _Optional[_Union[CompleteWorkflowExecutionDecisionAttributes, _Mapping]] = ..., fail_workflow_execution_decision_attributes: _Optional[_Union[FailWorkflowExecutionDecisionAttributes, _Mapping]] = ..., request_cancel_activity_task_decision_attributes: _Optional[_Union[RequestCancelActivityTaskDecisionAttributes, _Mapping]] = ..., cancel_timer_decision_attributes: _Optional[_Union[CancelTimerDecisionAttributes, _Mapping]] = ..., cancel_workflow_execution_decision_attributes: _Optional[_Union[CancelWorkflowExecutionDecisionAttributes, _Mapping]] = ..., request_cancel_external_workflow_execution_decision_attributes: _Optional[_Union[RequestCancelExternalWorkflowExecutionDecisionAttributes, _Mapping]] = ..., record_marker_decision_attributes: _Optional[_Union[RecordMarkerDecisionAttributes, _Mapping]] = ..., continue_as_new_workflow_execution_decision_attributes: _Optional[_Union[ContinueAsNewWorkflowExecutionDecisionAttributes, _Mapping]] = ..., start_child_workflow_execution_decision_attributes: _Optional[_Union[StartChildWorkflowExecutionDecisionAttributes, _Mapping]] = ..., signal_external_workflow_execution_decision_attributes: _Optional[_Union[SignalExternalWorkflowExecutionDecisionAttributes, _Mapping]] = ..., upsert_workflow_search_attributes_decision_attributes: _Optional[_Union[UpsertWorkflowSearchAttributesDecisionAttributes, _Mapping]] = ...) -> None: ...

class ScheduleActivityTaskDecisionAttributes(_message.Message):
    __slots__ = ("activity_id", "activity_type", "domain", "task_list", "input", "schedule_to_close_timeout", "schedule_to_start_timeout", "start_to_close_timeout", "heartbeat_timeout", "retry_policy", "header", "request_local_dispatch")
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TO_START_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_LOCAL_DISPATCH_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    activity_type: _common_pb2.ActivityType
    domain: str
    task_list: _tasklist_pb2.TaskList
    input: _common_pb2.Payload
    schedule_to_close_timeout: _duration_pb2.Duration
    schedule_to_start_timeout: _duration_pb2.Duration
    start_to_close_timeout: _duration_pb2.Duration
    heartbeat_timeout: _duration_pb2.Duration
    retry_policy: _common_pb2.RetryPolicy
    header: _common_pb2.Header
    request_local_dispatch: bool
    def __init__(self, activity_id: _Optional[str] = ..., activity_type: _Optional[_Union[_common_pb2.ActivityType, _Mapping]] = ..., domain: _Optional[str] = ..., task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., schedule_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., schedule_to_start_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., heartbeat_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., retry_policy: _Optional[_Union[_common_pb2.RetryPolicy, _Mapping]] = ..., header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., request_local_dispatch: bool = ...) -> None: ...

class StartTimerDecisionAttributes(_message.Message):
    __slots__ = ("timer_id", "start_to_fire_timeout")
    TIMER_ID_FIELD_NUMBER: _ClassVar[int]
    START_TO_FIRE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    timer_id: str
    start_to_fire_timeout: _duration_pb2.Duration
    def __init__(self, timer_id: _Optional[str] = ..., start_to_fire_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class CompleteWorkflowExecutionDecisionAttributes(_message.Message):
    __slots__ = ("result",)
    RESULT_FIELD_NUMBER: _ClassVar[int]
    result: _common_pb2.Payload
    def __init__(self, result: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ...) -> None: ...

class FailWorkflowExecutionDecisionAttributes(_message.Message):
    __slots__ = ("failure",)
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    failure: _common_pb2.Failure
    def __init__(self, failure: _Optional[_Union[_common_pb2.Failure, _Mapping]] = ...) -> None: ...

class RequestCancelActivityTaskDecisionAttributes(_message.Message):
    __slots__ = ("activity_id",)
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    def __init__(self, activity_id: _Optional[str] = ...) -> None: ...

class CancelTimerDecisionAttributes(_message.Message):
    __slots__ = ("timer_id",)
    TIMER_ID_FIELD_NUMBER: _ClassVar[int]
    timer_id: str
    def __init__(self, timer_id: _Optional[str] = ...) -> None: ...

class CancelWorkflowExecutionDecisionAttributes(_message.Message):
    __slots__ = ("details",)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _common_pb2.Payload
    def __init__(self, details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ...) -> None: ...

class RequestCancelExternalWorkflowExecutionDecisionAttributes(_message.Message):
    __slots__ = ("domain", "workflow_execution", "control", "child_workflow_only")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    CHILD_WORKFLOW_ONLY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    control: bytes
    child_workflow_only: bool
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., control: _Optional[bytes] = ..., child_workflow_only: bool = ...) -> None: ...

class RecordMarkerDecisionAttributes(_message.Message):
    __slots__ = ("marker_name", "details", "header")
    MARKER_NAME_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    marker_name: str
    details: _common_pb2.Payload
    header: _common_pb2.Header
    def __init__(self, marker_name: _Optional[str] = ..., details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ...) -> None: ...

class ContinueAsNewWorkflowExecutionDecisionAttributes(_message.Message):
    __slots__ = ("workflow_type", "task_list", "input", "execution_start_to_close_timeout", "task_start_to_close_timeout", "backoff_start_interval", "retry_policy", "initiator", "failure", "last_completion_result", "cron_schedule", "header", "memo", "search_attributes", "jitter_start", "cron_overlap_policy", "active_cluster_selection_policy")
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TASK_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_START_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    LAST_COMPLETION_RESULT_FIELD_NUMBER: _ClassVar[int]
    CRON_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    JITTER_START_FIELD_NUMBER: _ClassVar[int]
    CRON_OVERLAP_POLICY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTER_SELECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    workflow_type: _common_pb2.WorkflowType
    task_list: _tasklist_pb2.TaskList
    input: _common_pb2.Payload
    execution_start_to_close_timeout: _duration_pb2.Duration
    task_start_to_close_timeout: _duration_pb2.Duration
    backoff_start_interval: _duration_pb2.Duration
    retry_policy: _common_pb2.RetryPolicy
    initiator: _workflow_pb2.ContinueAsNewInitiator
    failure: _common_pb2.Failure
    last_completion_result: _common_pb2.Payload
    cron_schedule: str
    header: _common_pb2.Header
    memo: _common_pb2.Memo
    search_attributes: _common_pb2.SearchAttributes
    jitter_start: _duration_pb2.Duration
    cron_overlap_policy: _workflow_pb2.CronOverlapPolicy
    active_cluster_selection_policy: _common_pb2.ActiveClusterSelectionPolicy
    def __init__(self, workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., execution_start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., task_start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., backoff_start_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., retry_policy: _Optional[_Union[_common_pb2.RetryPolicy, _Mapping]] = ..., initiator: _Optional[_Union[_workflow_pb2.ContinueAsNewInitiator, str]] = ..., failure: _Optional[_Union[_common_pb2.Failure, _Mapping]] = ..., last_completion_result: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., cron_schedule: _Optional[str] = ..., header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., memo: _Optional[_Union[_common_pb2.Memo, _Mapping]] = ..., search_attributes: _Optional[_Union[_common_pb2.SearchAttributes, _Mapping]] = ..., jitter_start: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., cron_overlap_policy: _Optional[_Union[_workflow_pb2.CronOverlapPolicy, str]] = ..., active_cluster_selection_policy: _Optional[_Union[_common_pb2.ActiveClusterSelectionPolicy, _Mapping]] = ...) -> None: ...

class StartChildWorkflowExecutionDecisionAttributes(_message.Message):
    __slots__ = ("domain", "workflow_id", "workflow_type", "task_list", "input", "execution_start_to_close_timeout", "task_start_to_close_timeout", "parent_close_policy", "control", "workflow_id_reuse_policy", "retry_policy", "cron_schedule", "header", "memo", "search_attributes", "cron_overlap_policy", "active_cluster_selection_policy")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TASK_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    PARENT_CLOSE_POLICY_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_REUSE_POLICY_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    CRON_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CRON_OVERLAP_POLICY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTER_SELECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_id: str
    workflow_type: _common_pb2.WorkflowType
    task_list: _tasklist_pb2.TaskList
    input: _common_pb2.Payload
    execution_start_to_close_timeout: _duration_pb2.Duration
    task_start_to_close_timeout: _duration_pb2.Duration
    parent_close_policy: _workflow_pb2.ParentClosePolicy
    control: bytes
    workflow_id_reuse_policy: _workflow_pb2.WorkflowIdReusePolicy
    retry_policy: _common_pb2.RetryPolicy
    cron_schedule: str
    header: _common_pb2.Header
    memo: _common_pb2.Memo
    search_attributes: _common_pb2.SearchAttributes
    cron_overlap_policy: _workflow_pb2.CronOverlapPolicy
    active_cluster_selection_policy: _common_pb2.ActiveClusterSelectionPolicy
    def __init__(self, domain: _Optional[str] = ..., workflow_id: _Optional[str] = ..., workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., execution_start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., task_start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., parent_close_policy: _Optional[_Union[_workflow_pb2.ParentClosePolicy, str]] = ..., control: _Optional[bytes] = ..., workflow_id_reuse_policy: _Optional[_Union[_workflow_pb2.WorkflowIdReusePolicy, str]] = ..., retry_policy: _Optional[_Union[_common_pb2.RetryPolicy, _Mapping]] = ..., cron_schedule: _Optional[str] = ..., header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., memo: _Optional[_Union[_common_pb2.Memo, _Mapping]] = ..., search_attributes: _Optional[_Union[_common_pb2.SearchAttributes, _Mapping]] = ..., cron_overlap_policy: _Optional[_Union[_workflow_pb2.CronOverlapPolicy, str]] = ..., active_cluster_selection_policy: _Optional[_Union[_common_pb2.ActiveClusterSelectionPolicy, _Mapping]] = ...) -> None: ...

class SignalExternalWorkflowExecutionDecisionAttributes(_message.Message):
    __slots__ = ("domain", "workflow_execution", "signal_name", "input", "control", "child_workflow_only")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    CHILD_WORKFLOW_ONLY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    signal_name: str
    input: _common_pb2.Payload
    control: bytes
    child_workflow_only: bool
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., signal_name: _Optional[str] = ..., input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., control: _Optional[bytes] = ..., child_workflow_only: bool = ...) -> None: ...

class UpsertWorkflowSearchAttributesDecisionAttributes(_message.Message):
    __slots__ = ("search_attributes",)
    SEARCH_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    search_attributes: _common_pb2.SearchAttributes
    def __init__(self, search_attributes: _Optional[_Union[_common_pb2.SearchAttributes, _Mapping]] = ...) -> None: ...
