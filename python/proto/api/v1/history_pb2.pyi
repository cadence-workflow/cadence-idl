from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from uber.cadence.api.v1 import common_pb2 as _common_pb2
from uber.cadence.api.v1 import tasklist_pb2 as _tasklist_pb2
from uber.cadence.api.v1 import workflow_pb2 as _workflow_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EventFilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_FILTER_TYPE_INVALID: _ClassVar[EventFilterType]
    EVENT_FILTER_TYPE_ALL_EVENT: _ClassVar[EventFilterType]
    EVENT_FILTER_TYPE_CLOSE_EVENT: _ClassVar[EventFilterType]
EVENT_FILTER_TYPE_INVALID: EventFilterType
EVENT_FILTER_TYPE_ALL_EVENT: EventFilterType
EVENT_FILTER_TYPE_CLOSE_EVENT: EventFilterType

class History(_message.Message):
    __slots__ = ("events",)
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    events: _containers.RepeatedCompositeFieldContainer[HistoryEvent]
    def __init__(self, events: _Optional[_Iterable[_Union[HistoryEvent, _Mapping]]] = ...) -> None: ...

class HistoryEvent(_message.Message):
    __slots__ = ("event_id", "event_time", "version", "task_id", "workflow_execution_started_event_attributes", "workflow_execution_completed_event_attributes", "workflow_execution_failed_event_attributes", "workflow_execution_timed_out_event_attributes", "decision_task_scheduled_event_attributes", "decision_task_started_event_attributes", "decision_task_completed_event_attributes", "decision_task_timed_out_event_attributes", "decision_task_failed_event_attributes", "activity_task_scheduled_event_attributes", "activity_task_started_event_attributes", "activity_task_completed_event_attributes", "activity_task_failed_event_attributes", "activity_task_timed_out_event_attributes", "timer_started_event_attributes", "timer_fired_event_attributes", "activity_task_cancel_requested_event_attributes", "request_cancel_activity_task_failed_event_attributes", "activity_task_canceled_event_attributes", "timer_canceled_event_attributes", "cancel_timer_failed_event_attributes", "marker_recorded_event_attributes", "workflow_execution_signaled_event_attributes", "workflow_execution_terminated_event_attributes", "workflow_execution_cancel_requested_event_attributes", "workflow_execution_canceled_event_attributes", "request_cancel_external_workflow_execution_initiated_event_attributes", "request_cancel_external_workflow_execution_failed_event_attributes", "external_workflow_execution_cancel_requested_event_attributes", "workflow_execution_continued_as_new_event_attributes", "start_child_workflow_execution_initiated_event_attributes", "start_child_workflow_execution_failed_event_attributes", "child_workflow_execution_started_event_attributes", "child_workflow_execution_completed_event_attributes", "child_workflow_execution_failed_event_attributes", "child_workflow_execution_canceled_event_attributes", "child_workflow_execution_timed_out_event_attributes", "child_workflow_execution_terminated_event_attributes", "signal_external_workflow_execution_initiated_event_attributes", "signal_external_workflow_execution_failed_event_attributes", "external_workflow_execution_signaled_event_attributes", "upsert_workflow_search_attributes_event_attributes")
    EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_STARTED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_COMPLETED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FAILED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_TIMED_OUT_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_SCHEDULED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_STARTED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_TIMED_OUT_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_FAILED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TASK_SCHEDULED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TASK_STARTED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TASK_COMPLETED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TASK_FAILED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TASK_TIMED_OUT_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TIMER_STARTED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TIMER_FIRED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TASK_CANCEL_REQUESTED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CANCEL_ACTIVITY_TASK_FAILED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TASK_CANCELED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TIMER_CANCELED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CANCEL_TIMER_FAILED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    MARKER_RECORDED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_SIGNALED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_TERMINATED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_CANCEL_REQUESTED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_CANCELED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_INITIATED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_WORKFLOW_EXECUTION_CANCEL_REQUESTED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_CONTINUED_AS_NEW_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    START_CHILD_WORKFLOW_EXECUTION_INITIATED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    START_CHILD_WORKFLOW_EXECUTION_FAILED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CHILD_WORKFLOW_EXECUTION_STARTED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CHILD_WORKFLOW_EXECUTION_COMPLETED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CHILD_WORKFLOW_EXECUTION_FAILED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CHILD_WORKFLOW_EXECUTION_CANCELED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CHILD_WORKFLOW_EXECUTION_TIMED_OUT_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CHILD_WORKFLOW_EXECUTION_TERMINATED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_INITIATED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_WORKFLOW_EXECUTION_SIGNALED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    UPSERT_WORKFLOW_SEARCH_ATTRIBUTES_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    event_id: int
    event_time: _timestamp_pb2.Timestamp
    version: int
    task_id: int
    workflow_execution_started_event_attributes: WorkflowExecutionStartedEventAttributes
    workflow_execution_completed_event_attributes: WorkflowExecutionCompletedEventAttributes
    workflow_execution_failed_event_attributes: WorkflowExecutionFailedEventAttributes
    workflow_execution_timed_out_event_attributes: WorkflowExecutionTimedOutEventAttributes
    decision_task_scheduled_event_attributes: DecisionTaskScheduledEventAttributes
    decision_task_started_event_attributes: DecisionTaskStartedEventAttributes
    decision_task_completed_event_attributes: DecisionTaskCompletedEventAttributes
    decision_task_timed_out_event_attributes: DecisionTaskTimedOutEventAttributes
    decision_task_failed_event_attributes: DecisionTaskFailedEventAttributes
    activity_task_scheduled_event_attributes: ActivityTaskScheduledEventAttributes
    activity_task_started_event_attributes: ActivityTaskStartedEventAttributes
    activity_task_completed_event_attributes: ActivityTaskCompletedEventAttributes
    activity_task_failed_event_attributes: ActivityTaskFailedEventAttributes
    activity_task_timed_out_event_attributes: ActivityTaskTimedOutEventAttributes
    timer_started_event_attributes: TimerStartedEventAttributes
    timer_fired_event_attributes: TimerFiredEventAttributes
    activity_task_cancel_requested_event_attributes: ActivityTaskCancelRequestedEventAttributes
    request_cancel_activity_task_failed_event_attributes: RequestCancelActivityTaskFailedEventAttributes
    activity_task_canceled_event_attributes: ActivityTaskCanceledEventAttributes
    timer_canceled_event_attributes: TimerCanceledEventAttributes
    cancel_timer_failed_event_attributes: CancelTimerFailedEventAttributes
    marker_recorded_event_attributes: MarkerRecordedEventAttributes
    workflow_execution_signaled_event_attributes: WorkflowExecutionSignaledEventAttributes
    workflow_execution_terminated_event_attributes: WorkflowExecutionTerminatedEventAttributes
    workflow_execution_cancel_requested_event_attributes: WorkflowExecutionCancelRequestedEventAttributes
    workflow_execution_canceled_event_attributes: WorkflowExecutionCanceledEventAttributes
    request_cancel_external_workflow_execution_initiated_event_attributes: RequestCancelExternalWorkflowExecutionInitiatedEventAttributes
    request_cancel_external_workflow_execution_failed_event_attributes: RequestCancelExternalWorkflowExecutionFailedEventAttributes
    external_workflow_execution_cancel_requested_event_attributes: ExternalWorkflowExecutionCancelRequestedEventAttributes
    workflow_execution_continued_as_new_event_attributes: WorkflowExecutionContinuedAsNewEventAttributes
    start_child_workflow_execution_initiated_event_attributes: StartChildWorkflowExecutionInitiatedEventAttributes
    start_child_workflow_execution_failed_event_attributes: StartChildWorkflowExecutionFailedEventAttributes
    child_workflow_execution_started_event_attributes: ChildWorkflowExecutionStartedEventAttributes
    child_workflow_execution_completed_event_attributes: ChildWorkflowExecutionCompletedEventAttributes
    child_workflow_execution_failed_event_attributes: ChildWorkflowExecutionFailedEventAttributes
    child_workflow_execution_canceled_event_attributes: ChildWorkflowExecutionCanceledEventAttributes
    child_workflow_execution_timed_out_event_attributes: ChildWorkflowExecutionTimedOutEventAttributes
    child_workflow_execution_terminated_event_attributes: ChildWorkflowExecutionTerminatedEventAttributes
    signal_external_workflow_execution_initiated_event_attributes: SignalExternalWorkflowExecutionInitiatedEventAttributes
    signal_external_workflow_execution_failed_event_attributes: SignalExternalWorkflowExecutionFailedEventAttributes
    external_workflow_execution_signaled_event_attributes: ExternalWorkflowExecutionSignaledEventAttributes
    upsert_workflow_search_attributes_event_attributes: UpsertWorkflowSearchAttributesEventAttributes
    def __init__(self, event_id: _Optional[int] = ..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., version: _Optional[int] = ..., task_id: _Optional[int] = ..., workflow_execution_started_event_attributes: _Optional[_Union[WorkflowExecutionStartedEventAttributes, _Mapping]] = ..., workflow_execution_completed_event_attributes: _Optional[_Union[WorkflowExecutionCompletedEventAttributes, _Mapping]] = ..., workflow_execution_failed_event_attributes: _Optional[_Union[WorkflowExecutionFailedEventAttributes, _Mapping]] = ..., workflow_execution_timed_out_event_attributes: _Optional[_Union[WorkflowExecutionTimedOutEventAttributes, _Mapping]] = ..., decision_task_scheduled_event_attributes: _Optional[_Union[DecisionTaskScheduledEventAttributes, _Mapping]] = ..., decision_task_started_event_attributes: _Optional[_Union[DecisionTaskStartedEventAttributes, _Mapping]] = ..., decision_task_completed_event_attributes: _Optional[_Union[DecisionTaskCompletedEventAttributes, _Mapping]] = ..., decision_task_timed_out_event_attributes: _Optional[_Union[DecisionTaskTimedOutEventAttributes, _Mapping]] = ..., decision_task_failed_event_attributes: _Optional[_Union[DecisionTaskFailedEventAttributes, _Mapping]] = ..., activity_task_scheduled_event_attributes: _Optional[_Union[ActivityTaskScheduledEventAttributes, _Mapping]] = ..., activity_task_started_event_attributes: _Optional[_Union[ActivityTaskStartedEventAttributes, _Mapping]] = ..., activity_task_completed_event_attributes: _Optional[_Union[ActivityTaskCompletedEventAttributes, _Mapping]] = ..., activity_task_failed_event_attributes: _Optional[_Union[ActivityTaskFailedEventAttributes, _Mapping]] = ..., activity_task_timed_out_event_attributes: _Optional[_Union[ActivityTaskTimedOutEventAttributes, _Mapping]] = ..., timer_started_event_attributes: _Optional[_Union[TimerStartedEventAttributes, _Mapping]] = ..., timer_fired_event_attributes: _Optional[_Union[TimerFiredEventAttributes, _Mapping]] = ..., activity_task_cancel_requested_event_attributes: _Optional[_Union[ActivityTaskCancelRequestedEventAttributes, _Mapping]] = ..., request_cancel_activity_task_failed_event_attributes: _Optional[_Union[RequestCancelActivityTaskFailedEventAttributes, _Mapping]] = ..., activity_task_canceled_event_attributes: _Optional[_Union[ActivityTaskCanceledEventAttributes, _Mapping]] = ..., timer_canceled_event_attributes: _Optional[_Union[TimerCanceledEventAttributes, _Mapping]] = ..., cancel_timer_failed_event_attributes: _Optional[_Union[CancelTimerFailedEventAttributes, _Mapping]] = ..., marker_recorded_event_attributes: _Optional[_Union[MarkerRecordedEventAttributes, _Mapping]] = ..., workflow_execution_signaled_event_attributes: _Optional[_Union[WorkflowExecutionSignaledEventAttributes, _Mapping]] = ..., workflow_execution_terminated_event_attributes: _Optional[_Union[WorkflowExecutionTerminatedEventAttributes, _Mapping]] = ..., workflow_execution_cancel_requested_event_attributes: _Optional[_Union[WorkflowExecutionCancelRequestedEventAttributes, _Mapping]] = ..., workflow_execution_canceled_event_attributes: _Optional[_Union[WorkflowExecutionCanceledEventAttributes, _Mapping]] = ..., request_cancel_external_workflow_execution_initiated_event_attributes: _Optional[_Union[RequestCancelExternalWorkflowExecutionInitiatedEventAttributes, _Mapping]] = ..., request_cancel_external_workflow_execution_failed_event_attributes: _Optional[_Union[RequestCancelExternalWorkflowExecutionFailedEventAttributes, _Mapping]] = ..., external_workflow_execution_cancel_requested_event_attributes: _Optional[_Union[ExternalWorkflowExecutionCancelRequestedEventAttributes, _Mapping]] = ..., workflow_execution_continued_as_new_event_attributes: _Optional[_Union[WorkflowExecutionContinuedAsNewEventAttributes, _Mapping]] = ..., start_child_workflow_execution_initiated_event_attributes: _Optional[_Union[StartChildWorkflowExecutionInitiatedEventAttributes, _Mapping]] = ..., start_child_workflow_execution_failed_event_attributes: _Optional[_Union[StartChildWorkflowExecutionFailedEventAttributes, _Mapping]] = ..., child_workflow_execution_started_event_attributes: _Optional[_Union[ChildWorkflowExecutionStartedEventAttributes, _Mapping]] = ..., child_workflow_execution_completed_event_attributes: _Optional[_Union[ChildWorkflowExecutionCompletedEventAttributes, _Mapping]] = ..., child_workflow_execution_failed_event_attributes: _Optional[_Union[ChildWorkflowExecutionFailedEventAttributes, _Mapping]] = ..., child_workflow_execution_canceled_event_attributes: _Optional[_Union[ChildWorkflowExecutionCanceledEventAttributes, _Mapping]] = ..., child_workflow_execution_timed_out_event_attributes: _Optional[_Union[ChildWorkflowExecutionTimedOutEventAttributes, _Mapping]] = ..., child_workflow_execution_terminated_event_attributes: _Optional[_Union[ChildWorkflowExecutionTerminatedEventAttributes, _Mapping]] = ..., signal_external_workflow_execution_initiated_event_attributes: _Optional[_Union[SignalExternalWorkflowExecutionInitiatedEventAttributes, _Mapping]] = ..., signal_external_workflow_execution_failed_event_attributes: _Optional[_Union[SignalExternalWorkflowExecutionFailedEventAttributes, _Mapping]] = ..., external_workflow_execution_signaled_event_attributes: _Optional[_Union[ExternalWorkflowExecutionSignaledEventAttributes, _Mapping]] = ..., upsert_workflow_search_attributes_event_attributes: _Optional[_Union[UpsertWorkflowSearchAttributesEventAttributes, _Mapping]] = ...) -> None: ...

class WorkflowExecutionStartedEventAttributes(_message.Message):
    __slots__ = ("workflow_type", "parent_execution_info", "task_list", "input", "execution_start_to_close_timeout", "task_start_to_close_timeout", "continued_execution_run_id", "initiator", "continued_failure", "last_completion_result", "original_execution_run_id", "identity", "first_execution_run_id", "retry_policy", "attempt", "expiration_time", "cron_schedule", "first_decision_task_backoff", "memo", "search_attributes", "prev_auto_reset_points", "header", "first_scheduled_time", "partition_config", "request_id", "cron_overlap_policy", "active_cluster_selection_policy")
    class PartitionConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_EXECUTION_INFO_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TASK_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    CONTINUED_EXECUTION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_FIELD_NUMBER: _ClassVar[int]
    CONTINUED_FAILURE_FIELD_NUMBER: _ClassVar[int]
    LAST_COMPLETION_RESULT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_EXECUTION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    FIRST_EXECUTION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    CRON_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    FIRST_DECISION_TASK_BACKOFF_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PREV_AUTO_RESET_POINTS_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    FIRST_SCHEDULED_TIME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    CRON_OVERLAP_POLICY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTER_SELECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    workflow_type: _common_pb2.WorkflowType
    parent_execution_info: _workflow_pb2.ParentExecutionInfo
    task_list: _tasklist_pb2.TaskList
    input: _common_pb2.Payload
    execution_start_to_close_timeout: _duration_pb2.Duration
    task_start_to_close_timeout: _duration_pb2.Duration
    continued_execution_run_id: str
    initiator: _workflow_pb2.ContinueAsNewInitiator
    continued_failure: _common_pb2.Failure
    last_completion_result: _common_pb2.Payload
    original_execution_run_id: str
    identity: str
    first_execution_run_id: str
    retry_policy: _common_pb2.RetryPolicy
    attempt: int
    expiration_time: _timestamp_pb2.Timestamp
    cron_schedule: str
    first_decision_task_backoff: _duration_pb2.Duration
    memo: _common_pb2.Memo
    search_attributes: _common_pb2.SearchAttributes
    prev_auto_reset_points: _workflow_pb2.ResetPoints
    header: _common_pb2.Header
    first_scheduled_time: _timestamp_pb2.Timestamp
    partition_config: _containers.ScalarMap[str, str]
    request_id: str
    cron_overlap_policy: _workflow_pb2.CronOverlapPolicy
    active_cluster_selection_policy: _common_pb2.ActiveClusterSelectionPolicy
    def __init__(self, workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., parent_execution_info: _Optional[_Union[_workflow_pb2.ParentExecutionInfo, _Mapping]] = ..., task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., execution_start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., task_start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., continued_execution_run_id: _Optional[str] = ..., initiator: _Optional[_Union[_workflow_pb2.ContinueAsNewInitiator, str]] = ..., continued_failure: _Optional[_Union[_common_pb2.Failure, _Mapping]] = ..., last_completion_result: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., original_execution_run_id: _Optional[str] = ..., identity: _Optional[str] = ..., first_execution_run_id: _Optional[str] = ..., retry_policy: _Optional[_Union[_common_pb2.RetryPolicy, _Mapping]] = ..., attempt: _Optional[int] = ..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cron_schedule: _Optional[str] = ..., first_decision_task_backoff: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., memo: _Optional[_Union[_common_pb2.Memo, _Mapping]] = ..., search_attributes: _Optional[_Union[_common_pb2.SearchAttributes, _Mapping]] = ..., prev_auto_reset_points: _Optional[_Union[_workflow_pb2.ResetPoints, _Mapping]] = ..., header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., first_scheduled_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., partition_config: _Optional[_Mapping[str, str]] = ..., request_id: _Optional[str] = ..., cron_overlap_policy: _Optional[_Union[_workflow_pb2.CronOverlapPolicy, str]] = ..., active_cluster_selection_policy: _Optional[_Union[_common_pb2.ActiveClusterSelectionPolicy, _Mapping]] = ...) -> None: ...

class WorkflowExecutionCompletedEventAttributes(_message.Message):
    __slots__ = ("result", "decision_task_completed_event_id")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    result: _common_pb2.Payload
    decision_task_completed_event_id: int
    def __init__(self, result: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., decision_task_completed_event_id: _Optional[int] = ...) -> None: ...

class WorkflowExecutionFailedEventAttributes(_message.Message):
    __slots__ = ("failure", "decision_task_completed_event_id")
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    failure: _common_pb2.Failure
    decision_task_completed_event_id: int
    def __init__(self, failure: _Optional[_Union[_common_pb2.Failure, _Mapping]] = ..., decision_task_completed_event_id: _Optional[int] = ...) -> None: ...

class WorkflowExecutionTimedOutEventAttributes(_message.Message):
    __slots__ = ("timeout_type",)
    TIMEOUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    timeout_type: _workflow_pb2.TimeoutType
    def __init__(self, timeout_type: _Optional[_Union[_workflow_pb2.TimeoutType, str]] = ...) -> None: ...

class DecisionTaskScheduledEventAttributes(_message.Message):
    __slots__ = ("task_list", "start_to_close_timeout", "attempt")
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    task_list: _tasklist_pb2.TaskList
    start_to_close_timeout: _duration_pb2.Duration
    attempt: int
    def __init__(self, task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., attempt: _Optional[int] = ...) -> None: ...

class DecisionTaskStartedEventAttributes(_message.Message):
    __slots__ = ("scheduled_event_id", "identity", "request_id")
    SCHEDULED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    scheduled_event_id: int
    identity: str
    request_id: str
    def __init__(self, scheduled_event_id: _Optional[int] = ..., identity: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class DecisionTaskCompletedEventAttributes(_message.Message):
    __slots__ = ("scheduled_event_id", "started_event_id", "identity", "binary_checksum", "execution_context")
    SCHEDULED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    BINARY_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    scheduled_event_id: int
    started_event_id: int
    identity: str
    binary_checksum: str
    execution_context: bytes
    def __init__(self, scheduled_event_id: _Optional[int] = ..., started_event_id: _Optional[int] = ..., identity: _Optional[str] = ..., binary_checksum: _Optional[str] = ..., execution_context: _Optional[bytes] = ...) -> None: ...

class DecisionTaskTimedOutEventAttributes(_message.Message):
    __slots__ = ("scheduled_event_id", "started_event_id", "timeout_type", "base_run_id", "new_run_id", "fork_event_version", "reason", "cause", "request_id")
    SCHEDULED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    BASE_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    FORK_EVENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    scheduled_event_id: int
    started_event_id: int
    timeout_type: _workflow_pb2.TimeoutType
    base_run_id: str
    new_run_id: str
    fork_event_version: int
    reason: str
    cause: _workflow_pb2.DecisionTaskTimedOutCause
    request_id: str
    def __init__(self, scheduled_event_id: _Optional[int] = ..., started_event_id: _Optional[int] = ..., timeout_type: _Optional[_Union[_workflow_pb2.TimeoutType, str]] = ..., base_run_id: _Optional[str] = ..., new_run_id: _Optional[str] = ..., fork_event_version: _Optional[int] = ..., reason: _Optional[str] = ..., cause: _Optional[_Union[_workflow_pb2.DecisionTaskTimedOutCause, str]] = ..., request_id: _Optional[str] = ...) -> None: ...

class DecisionTaskFailedEventAttributes(_message.Message):
    __slots__ = ("scheduled_event_id", "started_event_id", "cause", "failure", "identity", "base_run_id", "new_run_id", "fork_event_version", "binary_checksum", "request_id")
    SCHEDULED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    BASE_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    FORK_EVENT_VERSION_FIELD_NUMBER: _ClassVar[int]
    BINARY_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    scheduled_event_id: int
    started_event_id: int
    cause: _workflow_pb2.DecisionTaskFailedCause
    failure: _common_pb2.Failure
    identity: str
    base_run_id: str
    new_run_id: str
    fork_event_version: int
    binary_checksum: str
    request_id: str
    def __init__(self, scheduled_event_id: _Optional[int] = ..., started_event_id: _Optional[int] = ..., cause: _Optional[_Union[_workflow_pb2.DecisionTaskFailedCause, str]] = ..., failure: _Optional[_Union[_common_pb2.Failure, _Mapping]] = ..., identity: _Optional[str] = ..., base_run_id: _Optional[str] = ..., new_run_id: _Optional[str] = ..., fork_event_version: _Optional[int] = ..., binary_checksum: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class ActivityTaskScheduledEventAttributes(_message.Message):
    __slots__ = ("activity_id", "activity_type", "domain", "task_list", "input", "schedule_to_close_timeout", "schedule_to_start_timeout", "start_to_close_timeout", "heartbeat_timeout", "decision_task_completed_event_id", "retry_policy", "header")
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TO_START_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    activity_type: _common_pb2.ActivityType
    domain: str
    task_list: _tasklist_pb2.TaskList
    input: _common_pb2.Payload
    schedule_to_close_timeout: _duration_pb2.Duration
    schedule_to_start_timeout: _duration_pb2.Duration
    start_to_close_timeout: _duration_pb2.Duration
    heartbeat_timeout: _duration_pb2.Duration
    decision_task_completed_event_id: int
    retry_policy: _common_pb2.RetryPolicy
    header: _common_pb2.Header
    def __init__(self, activity_id: _Optional[str] = ..., activity_type: _Optional[_Union[_common_pb2.ActivityType, _Mapping]] = ..., domain: _Optional[str] = ..., task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., schedule_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., schedule_to_start_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., heartbeat_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., decision_task_completed_event_id: _Optional[int] = ..., retry_policy: _Optional[_Union[_common_pb2.RetryPolicy, _Mapping]] = ..., header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ...) -> None: ...

class ActivityTaskStartedEventAttributes(_message.Message):
    __slots__ = ("scheduled_event_id", "identity", "request_id", "attempt", "last_failure")
    SCHEDULED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    LAST_FAILURE_FIELD_NUMBER: _ClassVar[int]
    scheduled_event_id: int
    identity: str
    request_id: str
    attempt: int
    last_failure: _common_pb2.Failure
    def __init__(self, scheduled_event_id: _Optional[int] = ..., identity: _Optional[str] = ..., request_id: _Optional[str] = ..., attempt: _Optional[int] = ..., last_failure: _Optional[_Union[_common_pb2.Failure, _Mapping]] = ...) -> None: ...

class ActivityTaskCompletedEventAttributes(_message.Message):
    __slots__ = ("result", "scheduled_event_id", "started_event_id", "identity")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    result: _common_pb2.Payload
    scheduled_event_id: int
    started_event_id: int
    identity: str
    def __init__(self, result: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., scheduled_event_id: _Optional[int] = ..., started_event_id: _Optional[int] = ..., identity: _Optional[str] = ...) -> None: ...

class ActivityTaskFailedEventAttributes(_message.Message):
    __slots__ = ("failure", "scheduled_event_id", "started_event_id", "identity")
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    failure: _common_pb2.Failure
    scheduled_event_id: int
    started_event_id: int
    identity: str
    def __init__(self, failure: _Optional[_Union[_common_pb2.Failure, _Mapping]] = ..., scheduled_event_id: _Optional[int] = ..., started_event_id: _Optional[int] = ..., identity: _Optional[str] = ...) -> None: ...

class ActivityTaskTimedOutEventAttributes(_message.Message):
    __slots__ = ("details", "scheduled_event_id", "started_event_id", "timeout_type", "last_failure")
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    LAST_FAILURE_FIELD_NUMBER: _ClassVar[int]
    details: _common_pb2.Payload
    scheduled_event_id: int
    started_event_id: int
    timeout_type: _workflow_pb2.TimeoutType
    last_failure: _common_pb2.Failure
    def __init__(self, details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., scheduled_event_id: _Optional[int] = ..., started_event_id: _Optional[int] = ..., timeout_type: _Optional[_Union[_workflow_pb2.TimeoutType, str]] = ..., last_failure: _Optional[_Union[_common_pb2.Failure, _Mapping]] = ...) -> None: ...

class ActivityTaskCancelRequestedEventAttributes(_message.Message):
    __slots__ = ("activity_id", "decision_task_completed_event_id")
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    decision_task_completed_event_id: int
    def __init__(self, activity_id: _Optional[str] = ..., decision_task_completed_event_id: _Optional[int] = ...) -> None: ...

class RequestCancelActivityTaskFailedEventAttributes(_message.Message):
    __slots__ = ("activity_id", "cause", "decision_task_completed_event_id")
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    cause: str
    decision_task_completed_event_id: int
    def __init__(self, activity_id: _Optional[str] = ..., cause: _Optional[str] = ..., decision_task_completed_event_id: _Optional[int] = ...) -> None: ...

class ActivityTaskCanceledEventAttributes(_message.Message):
    __slots__ = ("details", "latest_cancel_requested_event_id", "scheduled_event_id", "started_event_id", "identity")
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    LATEST_CANCEL_REQUESTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    details: _common_pb2.Payload
    latest_cancel_requested_event_id: int
    scheduled_event_id: int
    started_event_id: int
    identity: str
    def __init__(self, details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., latest_cancel_requested_event_id: _Optional[int] = ..., scheduled_event_id: _Optional[int] = ..., started_event_id: _Optional[int] = ..., identity: _Optional[str] = ...) -> None: ...

class TimerStartedEventAttributes(_message.Message):
    __slots__ = ("timer_id", "start_to_fire_timeout", "decision_task_completed_event_id")
    TIMER_ID_FIELD_NUMBER: _ClassVar[int]
    START_TO_FIRE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    timer_id: str
    start_to_fire_timeout: _duration_pb2.Duration
    decision_task_completed_event_id: int
    def __init__(self, timer_id: _Optional[str] = ..., start_to_fire_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., decision_task_completed_event_id: _Optional[int] = ...) -> None: ...

class TimerFiredEventAttributes(_message.Message):
    __slots__ = ("timer_id", "started_event_id")
    TIMER_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    timer_id: str
    started_event_id: int
    def __init__(self, timer_id: _Optional[str] = ..., started_event_id: _Optional[int] = ...) -> None: ...

class TimerCanceledEventAttributes(_message.Message):
    __slots__ = ("timer_id", "started_event_id", "decision_task_completed_event_id", "identity")
    TIMER_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    timer_id: str
    started_event_id: int
    decision_task_completed_event_id: int
    identity: str
    def __init__(self, timer_id: _Optional[str] = ..., started_event_id: _Optional[int] = ..., decision_task_completed_event_id: _Optional[int] = ..., identity: _Optional[str] = ...) -> None: ...

class CancelTimerFailedEventAttributes(_message.Message):
    __slots__ = ("timer_id", "cause", "decision_task_completed_event_id", "identity")
    TIMER_ID_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    timer_id: str
    cause: str
    decision_task_completed_event_id: int
    identity: str
    def __init__(self, timer_id: _Optional[str] = ..., cause: _Optional[str] = ..., decision_task_completed_event_id: _Optional[int] = ..., identity: _Optional[str] = ...) -> None: ...

class WorkflowExecutionContinuedAsNewEventAttributes(_message.Message):
    __slots__ = ("new_execution_run_id", "workflow_type", "task_list", "input", "execution_start_to_close_timeout", "task_start_to_close_timeout", "decision_task_completed_event_id", "backoff_start_interval", "initiator", "failure", "last_completion_result", "header", "memo", "search_attributes")
    NEW_EXECUTION_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TASK_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_START_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    INITIATOR_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    LAST_COMPLETION_RESULT_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    new_execution_run_id: str
    workflow_type: _common_pb2.WorkflowType
    task_list: _tasklist_pb2.TaskList
    input: _common_pb2.Payload
    execution_start_to_close_timeout: _duration_pb2.Duration
    task_start_to_close_timeout: _duration_pb2.Duration
    decision_task_completed_event_id: int
    backoff_start_interval: _duration_pb2.Duration
    initiator: _workflow_pb2.ContinueAsNewInitiator
    failure: _common_pb2.Failure
    last_completion_result: _common_pb2.Payload
    header: _common_pb2.Header
    memo: _common_pb2.Memo
    search_attributes: _common_pb2.SearchAttributes
    def __init__(self, new_execution_run_id: _Optional[str] = ..., workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., execution_start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., task_start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., decision_task_completed_event_id: _Optional[int] = ..., backoff_start_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., initiator: _Optional[_Union[_workflow_pb2.ContinueAsNewInitiator, str]] = ..., failure: _Optional[_Union[_common_pb2.Failure, _Mapping]] = ..., last_completion_result: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., memo: _Optional[_Union[_common_pb2.Memo, _Mapping]] = ..., search_attributes: _Optional[_Union[_common_pb2.SearchAttributes, _Mapping]] = ...) -> None: ...

class WorkflowExecutionCancelRequestedEventAttributes(_message.Message):
    __slots__ = ("cause", "identity", "external_execution_info", "request_id")
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_EXECUTION_INFO_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    cause: str
    identity: str
    external_execution_info: _workflow_pb2.ExternalExecutionInfo
    request_id: str
    def __init__(self, cause: _Optional[str] = ..., identity: _Optional[str] = ..., external_execution_info: _Optional[_Union[_workflow_pb2.ExternalExecutionInfo, _Mapping]] = ..., request_id: _Optional[str] = ...) -> None: ...

class WorkflowExecutionCanceledEventAttributes(_message.Message):
    __slots__ = ("decision_task_completed_event_id", "details")
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    decision_task_completed_event_id: int
    details: _common_pb2.Payload
    def __init__(self, decision_task_completed_event_id: _Optional[int] = ..., details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ...) -> None: ...

class MarkerRecordedEventAttributes(_message.Message):
    __slots__ = ("marker_name", "details", "decision_task_completed_event_id", "header")
    MARKER_NAME_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    marker_name: str
    details: _common_pb2.Payload
    decision_task_completed_event_id: int
    header: _common_pb2.Header
    def __init__(self, marker_name: _Optional[str] = ..., details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., decision_task_completed_event_id: _Optional[int] = ..., header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ...) -> None: ...

class WorkflowExecutionSignaledEventAttributes(_message.Message):
    __slots__ = ("signal_name", "input", "identity", "request_id")
    SIGNAL_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    signal_name: str
    input: _common_pb2.Payload
    identity: str
    request_id: str
    def __init__(self, signal_name: _Optional[str] = ..., input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., identity: _Optional[str] = ..., request_id: _Optional[str] = ...) -> None: ...

class WorkflowExecutionTerminatedEventAttributes(_message.Message):
    __slots__ = ("reason", "details", "identity")
    REASON_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    reason: str
    details: _common_pb2.Payload
    identity: str
    def __init__(self, reason: _Optional[str] = ..., details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., identity: _Optional[str] = ...) -> None: ...

class RequestCancelExternalWorkflowExecutionInitiatedEventAttributes(_message.Message):
    __slots__ = ("decision_task_completed_event_id", "domain", "workflow_execution", "control", "child_workflow_only")
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    CHILD_WORKFLOW_ONLY_FIELD_NUMBER: _ClassVar[int]
    decision_task_completed_event_id: int
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    control: bytes
    child_workflow_only: bool
    def __init__(self, decision_task_completed_event_id: _Optional[int] = ..., domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., control: _Optional[bytes] = ..., child_workflow_only: bool = ...) -> None: ...

class RequestCancelExternalWorkflowExecutionFailedEventAttributes(_message.Message):
    __slots__ = ("cause", "decision_task_completed_event_id", "domain", "workflow_execution", "initiated_event_id", "control")
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    cause: _workflow_pb2.CancelExternalWorkflowExecutionFailedCause
    decision_task_completed_event_id: int
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    initiated_event_id: int
    control: bytes
    def __init__(self, cause: _Optional[_Union[_workflow_pb2.CancelExternalWorkflowExecutionFailedCause, str]] = ..., decision_task_completed_event_id: _Optional[int] = ..., domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., initiated_event_id: _Optional[int] = ..., control: _Optional[bytes] = ...) -> None: ...

class ExternalWorkflowExecutionCancelRequestedEventAttributes(_message.Message):
    __slots__ = ("initiated_event_id", "domain", "workflow_execution")
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    initiated_event_id: int
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    def __init__(self, initiated_event_id: _Optional[int] = ..., domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ...) -> None: ...

class SignalExternalWorkflowExecutionInitiatedEventAttributes(_message.Message):
    __slots__ = ("decision_task_completed_event_id", "domain", "workflow_execution", "signal_name", "input", "control", "child_workflow_only")
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    CHILD_WORKFLOW_ONLY_FIELD_NUMBER: _ClassVar[int]
    decision_task_completed_event_id: int
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    signal_name: str
    input: _common_pb2.Payload
    control: bytes
    child_workflow_only: bool
    def __init__(self, decision_task_completed_event_id: _Optional[int] = ..., domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., signal_name: _Optional[str] = ..., input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., control: _Optional[bytes] = ..., child_workflow_only: bool = ...) -> None: ...

class SignalExternalWorkflowExecutionFailedEventAttributes(_message.Message):
    __slots__ = ("cause", "decision_task_completed_event_id", "domain", "workflow_execution", "initiated_event_id", "control")
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    cause: _workflow_pb2.SignalExternalWorkflowExecutionFailedCause
    decision_task_completed_event_id: int
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    initiated_event_id: int
    control: bytes
    def __init__(self, cause: _Optional[_Union[_workflow_pb2.SignalExternalWorkflowExecutionFailedCause, str]] = ..., decision_task_completed_event_id: _Optional[int] = ..., domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., initiated_event_id: _Optional[int] = ..., control: _Optional[bytes] = ...) -> None: ...

class ExternalWorkflowExecutionSignaledEventAttributes(_message.Message):
    __slots__ = ("initiated_event_id", "domain", "workflow_execution", "control")
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    initiated_event_id: int
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    control: bytes
    def __init__(self, initiated_event_id: _Optional[int] = ..., domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., control: _Optional[bytes] = ...) -> None: ...

class UpsertWorkflowSearchAttributesEventAttributes(_message.Message):
    __slots__ = ("decision_task_completed_event_id", "search_attributes")
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    decision_task_completed_event_id: int
    search_attributes: _common_pb2.SearchAttributes
    def __init__(self, decision_task_completed_event_id: _Optional[int] = ..., search_attributes: _Optional[_Union[_common_pb2.SearchAttributes, _Mapping]] = ...) -> None: ...

class StartChildWorkflowExecutionInitiatedEventAttributes(_message.Message):
    __slots__ = ("domain", "workflow_id", "workflow_type", "task_list", "input", "execution_start_to_close_timeout", "task_start_to_close_timeout", "parent_close_policy", "control", "decision_task_completed_event_id", "workflow_id_reuse_policy", "retry_policy", "cron_schedule", "header", "memo", "search_attributes", "delay_start", "jitter_start", "first_run_at", "cron_overlap_policy", "active_cluster_selection_policy")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TASK_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    PARENT_CLOSE_POLICY_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_REUSE_POLICY_FIELD_NUMBER: _ClassVar[int]
    RETRY_POLICY_FIELD_NUMBER: _ClassVar[int]
    CRON_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
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
    parent_close_policy: _workflow_pb2.ParentClosePolicy
    control: bytes
    decision_task_completed_event_id: int
    workflow_id_reuse_policy: _workflow_pb2.WorkflowIdReusePolicy
    retry_policy: _common_pb2.RetryPolicy
    cron_schedule: str
    header: _common_pb2.Header
    memo: _common_pb2.Memo
    search_attributes: _common_pb2.SearchAttributes
    delay_start: _duration_pb2.Duration
    jitter_start: _duration_pb2.Duration
    first_run_at: _timestamp_pb2.Timestamp
    cron_overlap_policy: _workflow_pb2.CronOverlapPolicy
    active_cluster_selection_policy: _common_pb2.ActiveClusterSelectionPolicy
    def __init__(self, domain: _Optional[str] = ..., workflow_id: _Optional[str] = ..., workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., execution_start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., task_start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., parent_close_policy: _Optional[_Union[_workflow_pb2.ParentClosePolicy, str]] = ..., control: _Optional[bytes] = ..., decision_task_completed_event_id: _Optional[int] = ..., workflow_id_reuse_policy: _Optional[_Union[_workflow_pb2.WorkflowIdReusePolicy, str]] = ..., retry_policy: _Optional[_Union[_common_pb2.RetryPolicy, _Mapping]] = ..., cron_schedule: _Optional[str] = ..., header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ..., memo: _Optional[_Union[_common_pb2.Memo, _Mapping]] = ..., search_attributes: _Optional[_Union[_common_pb2.SearchAttributes, _Mapping]] = ..., delay_start: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., jitter_start: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., first_run_at: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., cron_overlap_policy: _Optional[_Union[_workflow_pb2.CronOverlapPolicy, str]] = ..., active_cluster_selection_policy: _Optional[_Union[_common_pb2.ActiveClusterSelectionPolicy, _Mapping]] = ...) -> None: ...

class StartChildWorkflowExecutionFailedEventAttributes(_message.Message):
    __slots__ = ("domain", "workflow_id", "workflow_type", "cause", "control", "initiated_event_id", "decision_task_completed_event_id")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    CAUSE_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DECISION_TASK_COMPLETED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_id: str
    workflow_type: _common_pb2.WorkflowType
    cause: _workflow_pb2.ChildWorkflowExecutionFailedCause
    control: bytes
    initiated_event_id: int
    decision_task_completed_event_id: int
    def __init__(self, domain: _Optional[str] = ..., workflow_id: _Optional[str] = ..., workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., cause: _Optional[_Union[_workflow_pb2.ChildWorkflowExecutionFailedCause, str]] = ..., control: _Optional[bytes] = ..., initiated_event_id: _Optional[int] = ..., decision_task_completed_event_id: _Optional[int] = ...) -> None: ...

class ChildWorkflowExecutionStartedEventAttributes(_message.Message):
    __slots__ = ("domain", "workflow_execution", "workflow_type", "initiated_event_id", "header")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    HEADER_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    workflow_type: _common_pb2.WorkflowType
    initiated_event_id: int
    header: _common_pb2.Header
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., initiated_event_id: _Optional[int] = ..., header: _Optional[_Union[_common_pb2.Header, _Mapping]] = ...) -> None: ...

class ChildWorkflowExecutionCompletedEventAttributes(_message.Message):
    __slots__ = ("domain", "workflow_execution", "workflow_type", "initiated_event_id", "started_event_id", "result")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    workflow_type: _common_pb2.WorkflowType
    initiated_event_id: int
    started_event_id: int
    result: _common_pb2.Payload
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., initiated_event_id: _Optional[int] = ..., started_event_id: _Optional[int] = ..., result: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ...) -> None: ...

class ChildWorkflowExecutionFailedEventAttributes(_message.Message):
    __slots__ = ("domain", "workflow_execution", "workflow_type", "initiated_event_id", "started_event_id", "failure")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    FAILURE_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    workflow_type: _common_pb2.WorkflowType
    initiated_event_id: int
    started_event_id: int
    failure: _common_pb2.Failure
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., initiated_event_id: _Optional[int] = ..., started_event_id: _Optional[int] = ..., failure: _Optional[_Union[_common_pb2.Failure, _Mapping]] = ...) -> None: ...

class ChildWorkflowExecutionCanceledEventAttributes(_message.Message):
    __slots__ = ("domain", "workflow_execution", "workflow_type", "initiated_event_id", "started_event_id", "details")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    workflow_type: _common_pb2.WorkflowType
    initiated_event_id: int
    started_event_id: int
    details: _common_pb2.Payload
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., initiated_event_id: _Optional[int] = ..., started_event_id: _Optional[int] = ..., details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ...) -> None: ...

class ChildWorkflowExecutionTimedOutEventAttributes(_message.Message):
    __slots__ = ("domain", "workflow_execution", "workflow_type", "initiated_event_id", "started_event_id", "timeout_type")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_TYPE_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    workflow_type: _common_pb2.WorkflowType
    initiated_event_id: int
    started_event_id: int
    timeout_type: _workflow_pb2.TimeoutType
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., initiated_event_id: _Optional[int] = ..., started_event_id: _Optional[int] = ..., timeout_type: _Optional[_Union[_workflow_pb2.TimeoutType, str]] = ...) -> None: ...

class ChildWorkflowExecutionTerminatedEventAttributes(_message.Message):
    __slots__ = ("domain", "workflow_execution", "workflow_type", "initiated_event_id", "started_event_id")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_FIELD_NUMBER: _ClassVar[int]
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    STARTED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    domain: str
    workflow_execution: _common_pb2.WorkflowExecution
    workflow_type: _common_pb2.WorkflowType
    initiated_event_id: int
    started_event_id: int
    def __init__(self, domain: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., workflow_type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., initiated_event_id: _Optional[int] = ..., started_event_id: _Optional[int] = ...) -> None: ...
