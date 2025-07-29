from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from uber.cadence.api.v1 import common_pb2 as _common_pb2
from uber.cadence.api.v1 import tasklist_pb2 as _tasklist_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PendingActivityState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PENDING_ACTIVITY_STATE_INVALID: _ClassVar[PendingActivityState]
    PENDING_ACTIVITY_STATE_SCHEDULED: _ClassVar[PendingActivityState]
    PENDING_ACTIVITY_STATE_STARTED: _ClassVar[PendingActivityState]
    PENDING_ACTIVITY_STATE_CANCEL_REQUESTED: _ClassVar[PendingActivityState]

class PendingDecisionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PENDING_DECISION_STATE_INVALID: _ClassVar[PendingDecisionState]
    PENDING_DECISION_STATE_SCHEDULED: _ClassVar[PendingDecisionState]
    PENDING_DECISION_STATE_STARTED: _ClassVar[PendingDecisionState]

class WorkflowIdReusePolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WORKFLOW_ID_REUSE_POLICY_INVALID: _ClassVar[WorkflowIdReusePolicy]
    WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE_FAILED_ONLY: _ClassVar[WorkflowIdReusePolicy]
    WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE: _ClassVar[WorkflowIdReusePolicy]
    WORKFLOW_ID_REUSE_POLICY_REJECT_DUPLICATE: _ClassVar[WorkflowIdReusePolicy]
    WORKFLOW_ID_REUSE_POLICY_TERMINATE_IF_RUNNING: _ClassVar[WorkflowIdReusePolicy]

class CronOverlapPolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CRON_OVERLAP_POLICY_INVALID: _ClassVar[CronOverlapPolicy]
    CRON_OVERLAP_POLICY_SKIPPED: _ClassVar[CronOverlapPolicy]
    CRON_OVERLAP_POLICY_BUFFER_ONE: _ClassVar[CronOverlapPolicy]

class ParentClosePolicy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PARENT_CLOSE_POLICY_INVALID: _ClassVar[ParentClosePolicy]
    PARENT_CLOSE_POLICY_ABANDON: _ClassVar[ParentClosePolicy]
    PARENT_CLOSE_POLICY_REQUEST_CANCEL: _ClassVar[ParentClosePolicy]
    PARENT_CLOSE_POLICY_TERMINATE: _ClassVar[ParentClosePolicy]

class WorkflowExecutionCloseStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    WORKFLOW_EXECUTION_CLOSE_STATUS_INVALID: _ClassVar[WorkflowExecutionCloseStatus]
    WORKFLOW_EXECUTION_CLOSE_STATUS_COMPLETED: _ClassVar[WorkflowExecutionCloseStatus]
    WORKFLOW_EXECUTION_CLOSE_STATUS_FAILED: _ClassVar[WorkflowExecutionCloseStatus]
    WORKFLOW_EXECUTION_CLOSE_STATUS_CANCELED: _ClassVar[WorkflowExecutionCloseStatus]
    WORKFLOW_EXECUTION_CLOSE_STATUS_TERMINATED: _ClassVar[WorkflowExecutionCloseStatus]
    WORKFLOW_EXECUTION_CLOSE_STATUS_CONTINUED_AS_NEW: _ClassVar[WorkflowExecutionCloseStatus]
    WORKFLOW_EXECUTION_CLOSE_STATUS_TIMED_OUT: _ClassVar[WorkflowExecutionCloseStatus]

class ContinueAsNewInitiator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTINUE_AS_NEW_INITIATOR_INVALID: _ClassVar[ContinueAsNewInitiator]
    CONTINUE_AS_NEW_INITIATOR_DECIDER: _ClassVar[ContinueAsNewInitiator]
    CONTINUE_AS_NEW_INITIATOR_RETRY_POLICY: _ClassVar[ContinueAsNewInitiator]
    CONTINUE_AS_NEW_INITIATOR_CRON_SCHEDULE: _ClassVar[ContinueAsNewInitiator]

class TimeoutType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TIMEOUT_TYPE_INVALID: _ClassVar[TimeoutType]
    TIMEOUT_TYPE_START_TO_CLOSE: _ClassVar[TimeoutType]
    TIMEOUT_TYPE_SCHEDULE_TO_START: _ClassVar[TimeoutType]
    TIMEOUT_TYPE_SCHEDULE_TO_CLOSE: _ClassVar[TimeoutType]
    TIMEOUT_TYPE_HEARTBEAT: _ClassVar[TimeoutType]

class DecisionTaskTimedOutCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DECISION_TASK_TIMED_OUT_CAUSE_INVALID: _ClassVar[DecisionTaskTimedOutCause]
    DECISION_TASK_TIMED_OUT_CAUSE_TIMEOUT: _ClassVar[DecisionTaskTimedOutCause]
    DECISION_TASK_TIMED_OUT_CAUSE_RESET: _ClassVar[DecisionTaskTimedOutCause]

class DecisionTaskFailedCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DECISION_TASK_FAILED_CAUSE_INVALID: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_UNHANDLED_DECISION: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_SCHEDULE_ACTIVITY_ATTRIBUTES: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_REQUEST_CANCEL_ACTIVITY_ATTRIBUTES: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_START_TIMER_ATTRIBUTES: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_CANCEL_TIMER_ATTRIBUTES: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_RECORD_MARKER_ATTRIBUTES: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_COMPLETE_WORKFLOW_EXECUTION_ATTRIBUTES: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_FAIL_WORKFLOW_EXECUTION_ATTRIBUTES: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_CANCEL_WORKFLOW_EXECUTION_ATTRIBUTES: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_ATTRIBUTES: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_CONTINUE_AS_NEW_ATTRIBUTES: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_START_TIMER_DUPLICATE_ID: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_RESET_STICKY_TASK_LIST: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_WORKFLOW_WORKER_UNHANDLED_FAILURE: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_SIGNAL_WORKFLOW_EXECUTION_ATTRIBUTES: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_START_CHILD_EXECUTION_ATTRIBUTES: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_FORCE_CLOSE_DECISION: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_FAILOVER_CLOSE_DECISION: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_SIGNAL_INPUT_SIZE: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_RESET_WORKFLOW: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_BINARY: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_SCHEDULE_ACTIVITY_DUPLICATE_ID: _ClassVar[DecisionTaskFailedCause]
    DECISION_TASK_FAILED_CAUSE_BAD_SEARCH_ATTRIBUTES: _ClassVar[DecisionTaskFailedCause]

class ChildWorkflowExecutionFailedCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHILD_WORKFLOW_EXECUTION_FAILED_CAUSE_INVALID: _ClassVar[ChildWorkflowExecutionFailedCause]
    CHILD_WORKFLOW_EXECUTION_FAILED_CAUSE_WORKFLOW_ALREADY_RUNNING: _ClassVar[ChildWorkflowExecutionFailedCause]

class CancelExternalWorkflowExecutionFailedCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CANCEL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_INVALID: _ClassVar[CancelExternalWorkflowExecutionFailedCause]
    CANCEL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION: _ClassVar[CancelExternalWorkflowExecutionFailedCause]
    CANCEL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_WORKFLOW_ALREADY_COMPLETED: _ClassVar[CancelExternalWorkflowExecutionFailedCause]

class SignalExternalWorkflowExecutionFailedCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_INVALID: _ClassVar[SignalExternalWorkflowExecutionFailedCause]
    SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION: _ClassVar[SignalExternalWorkflowExecutionFailedCause]
    SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_WORKFLOW_ALREADY_COMPLETED: _ClassVar[SignalExternalWorkflowExecutionFailedCause]
PENDING_ACTIVITY_STATE_INVALID: PendingActivityState
PENDING_ACTIVITY_STATE_SCHEDULED: PendingActivityState
PENDING_ACTIVITY_STATE_STARTED: PendingActivityState
PENDING_ACTIVITY_STATE_CANCEL_REQUESTED: PendingActivityState
PENDING_DECISION_STATE_INVALID: PendingDecisionState
PENDING_DECISION_STATE_SCHEDULED: PendingDecisionState
PENDING_DECISION_STATE_STARTED: PendingDecisionState
WORKFLOW_ID_REUSE_POLICY_INVALID: WorkflowIdReusePolicy
WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE_FAILED_ONLY: WorkflowIdReusePolicy
WORKFLOW_ID_REUSE_POLICY_ALLOW_DUPLICATE: WorkflowIdReusePolicy
WORKFLOW_ID_REUSE_POLICY_REJECT_DUPLICATE: WorkflowIdReusePolicy
WORKFLOW_ID_REUSE_POLICY_TERMINATE_IF_RUNNING: WorkflowIdReusePolicy
CRON_OVERLAP_POLICY_INVALID: CronOverlapPolicy
CRON_OVERLAP_POLICY_SKIPPED: CronOverlapPolicy
CRON_OVERLAP_POLICY_BUFFER_ONE: CronOverlapPolicy
PARENT_CLOSE_POLICY_INVALID: ParentClosePolicy
PARENT_CLOSE_POLICY_ABANDON: ParentClosePolicy
PARENT_CLOSE_POLICY_REQUEST_CANCEL: ParentClosePolicy
PARENT_CLOSE_POLICY_TERMINATE: ParentClosePolicy
WORKFLOW_EXECUTION_CLOSE_STATUS_INVALID: WorkflowExecutionCloseStatus
WORKFLOW_EXECUTION_CLOSE_STATUS_COMPLETED: WorkflowExecutionCloseStatus
WORKFLOW_EXECUTION_CLOSE_STATUS_FAILED: WorkflowExecutionCloseStatus
WORKFLOW_EXECUTION_CLOSE_STATUS_CANCELED: WorkflowExecutionCloseStatus
WORKFLOW_EXECUTION_CLOSE_STATUS_TERMINATED: WorkflowExecutionCloseStatus
WORKFLOW_EXECUTION_CLOSE_STATUS_CONTINUED_AS_NEW: WorkflowExecutionCloseStatus
WORKFLOW_EXECUTION_CLOSE_STATUS_TIMED_OUT: WorkflowExecutionCloseStatus
CONTINUE_AS_NEW_INITIATOR_INVALID: ContinueAsNewInitiator
CONTINUE_AS_NEW_INITIATOR_DECIDER: ContinueAsNewInitiator
CONTINUE_AS_NEW_INITIATOR_RETRY_POLICY: ContinueAsNewInitiator
CONTINUE_AS_NEW_INITIATOR_CRON_SCHEDULE: ContinueAsNewInitiator
TIMEOUT_TYPE_INVALID: TimeoutType
TIMEOUT_TYPE_START_TO_CLOSE: TimeoutType
TIMEOUT_TYPE_SCHEDULE_TO_START: TimeoutType
TIMEOUT_TYPE_SCHEDULE_TO_CLOSE: TimeoutType
TIMEOUT_TYPE_HEARTBEAT: TimeoutType
DECISION_TASK_TIMED_OUT_CAUSE_INVALID: DecisionTaskTimedOutCause
DECISION_TASK_TIMED_OUT_CAUSE_TIMEOUT: DecisionTaskTimedOutCause
DECISION_TASK_TIMED_OUT_CAUSE_RESET: DecisionTaskTimedOutCause
DECISION_TASK_FAILED_CAUSE_INVALID: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_UNHANDLED_DECISION: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_SCHEDULE_ACTIVITY_ATTRIBUTES: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_REQUEST_CANCEL_ACTIVITY_ATTRIBUTES: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_START_TIMER_ATTRIBUTES: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_CANCEL_TIMER_ATTRIBUTES: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_RECORD_MARKER_ATTRIBUTES: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_COMPLETE_WORKFLOW_EXECUTION_ATTRIBUTES: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_FAIL_WORKFLOW_EXECUTION_ATTRIBUTES: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_CANCEL_WORKFLOW_EXECUTION_ATTRIBUTES: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_REQUEST_CANCEL_EXTERNAL_WORKFLOW_EXECUTION_ATTRIBUTES: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_CONTINUE_AS_NEW_ATTRIBUTES: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_START_TIMER_DUPLICATE_ID: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_RESET_STICKY_TASK_LIST: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_WORKFLOW_WORKER_UNHANDLED_FAILURE: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_SIGNAL_WORKFLOW_EXECUTION_ATTRIBUTES: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_START_CHILD_EXECUTION_ATTRIBUTES: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_FORCE_CLOSE_DECISION: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_FAILOVER_CLOSE_DECISION: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_SIGNAL_INPUT_SIZE: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_RESET_WORKFLOW: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_BINARY: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_SCHEDULE_ACTIVITY_DUPLICATE_ID: DecisionTaskFailedCause
DECISION_TASK_FAILED_CAUSE_BAD_SEARCH_ATTRIBUTES: DecisionTaskFailedCause
CHILD_WORKFLOW_EXECUTION_FAILED_CAUSE_INVALID: ChildWorkflowExecutionFailedCause
CHILD_WORKFLOW_EXECUTION_FAILED_CAUSE_WORKFLOW_ALREADY_RUNNING: ChildWorkflowExecutionFailedCause
CANCEL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_INVALID: CancelExternalWorkflowExecutionFailedCause
CANCEL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION: CancelExternalWorkflowExecutionFailedCause
CANCEL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_WORKFLOW_ALREADY_COMPLETED: CancelExternalWorkflowExecutionFailedCause
SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_INVALID: SignalExternalWorkflowExecutionFailedCause
SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_UNKNOWN_EXTERNAL_WORKFLOW_EXECUTION: SignalExternalWorkflowExecutionFailedCause
SIGNAL_EXTERNAL_WORKFLOW_EXECUTION_FAILED_CAUSE_WORKFLOW_ALREADY_COMPLETED: SignalExternalWorkflowExecutionFailedCause

class WorkflowExecutionInfo(_message.Message):
    __slots__ = ("workflow_execution", "type", "start_time", "close_time", "close_status", "history_length", "parent_execution_info", "execution_time", "memo", "search_attributes", "auto_reset_points", "task_list", "task_list_info", "is_cron", "update_time", "partition_config", "cron_overlap_policy", "active_cluster_selection_policy")
    class PartitionConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    CLOSE_TIME_FIELD_NUMBER: _ClassVar[int]
    CLOSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    HISTORY_LENGTH_FIELD_NUMBER: _ClassVar[int]
    PARENT_EXECUTION_INFO_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    SEARCH_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    AUTO_RESET_POINTS_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    TASK_LIST_INFO_FIELD_NUMBER: _ClassVar[int]
    IS_CRON_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    PARTITION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CRON_OVERLAP_POLICY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTER_SELECTION_POLICY_FIELD_NUMBER: _ClassVar[int]
    workflow_execution: _common_pb2.WorkflowExecution
    type: _common_pb2.WorkflowType
    start_time: _timestamp_pb2.Timestamp
    close_time: _timestamp_pb2.Timestamp
    close_status: WorkflowExecutionCloseStatus
    history_length: int
    parent_execution_info: ParentExecutionInfo
    execution_time: _timestamp_pb2.Timestamp
    memo: _common_pb2.Memo
    search_attributes: _common_pb2.SearchAttributes
    auto_reset_points: ResetPoints
    task_list: str
    task_list_info: _tasklist_pb2.TaskList
    is_cron: bool
    update_time: _timestamp_pb2.Timestamp
    partition_config: _containers.ScalarMap[str, str]
    cron_overlap_policy: CronOverlapPolicy
    active_cluster_selection_policy: _common_pb2.ActiveClusterSelectionPolicy
    def __init__(self, workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., type: _Optional[_Union[_common_pb2.WorkflowType, _Mapping]] = ..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., close_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., close_status: _Optional[_Union[WorkflowExecutionCloseStatus, str]] = ..., history_length: _Optional[int] = ..., parent_execution_info: _Optional[_Union[ParentExecutionInfo, _Mapping]] = ..., execution_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., memo: _Optional[_Union[_common_pb2.Memo, _Mapping]] = ..., search_attributes: _Optional[_Union[_common_pb2.SearchAttributes, _Mapping]] = ..., auto_reset_points: _Optional[_Union[ResetPoints, _Mapping]] = ..., task_list: _Optional[str] = ..., task_list_info: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., is_cron: bool = ..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., partition_config: _Optional[_Mapping[str, str]] = ..., cron_overlap_policy: _Optional[_Union[CronOverlapPolicy, str]] = ..., active_cluster_selection_policy: _Optional[_Union[_common_pb2.ActiveClusterSelectionPolicy, _Mapping]] = ...) -> None: ...

class WorkflowExecutionConfiguration(_message.Message):
    __slots__ = ("task_list", "execution_start_to_close_timeout", "task_start_to_close_timeout")
    TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    TASK_START_TO_CLOSE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    task_list: _tasklist_pb2.TaskList
    execution_start_to_close_timeout: _duration_pb2.Duration
    task_start_to_close_timeout: _duration_pb2.Duration
    def __init__(self, task_list: _Optional[_Union[_tasklist_pb2.TaskList, _Mapping]] = ..., execution_start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., task_start_to_close_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class ParentExecutionInfo(_message.Message):
    __slots__ = ("domain_id", "domain_name", "workflow_execution", "initiated_id")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_NAME_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    INITIATED_ID_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    domain_name: str
    workflow_execution: _common_pb2.WorkflowExecution
    initiated_id: int
    def __init__(self, domain_id: _Optional[str] = ..., domain_name: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., initiated_id: _Optional[int] = ...) -> None: ...

class ExternalExecutionInfo(_message.Message):
    __slots__ = ("workflow_execution", "initiated_id")
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    INITIATED_ID_FIELD_NUMBER: _ClassVar[int]
    workflow_execution: _common_pb2.WorkflowExecution
    initiated_id: int
    def __init__(self, workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., initiated_id: _Optional[int] = ...) -> None: ...

class PendingActivityInfo(_message.Message):
    __slots__ = ("activity_id", "activity_type", "state", "heartbeat_details", "last_heartbeat_time", "last_started_time", "attempt", "maximum_attempts", "scheduled_time", "expiration_time", "last_failure", "last_worker_identity", "started_worker_identity", "schedule_id")
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIVITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    HEARTBEAT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    LAST_HEARTBEAT_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_STARTED_TIME_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_FAILURE_FIELD_NUMBER: _ClassVar[int]
    LAST_WORKER_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    STARTED_WORKER_IDENTITY_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    activity_type: _common_pb2.ActivityType
    state: PendingActivityState
    heartbeat_details: _common_pb2.Payload
    last_heartbeat_time: _timestamp_pb2.Timestamp
    last_started_time: _timestamp_pb2.Timestamp
    attempt: int
    maximum_attempts: int
    scheduled_time: _timestamp_pb2.Timestamp
    expiration_time: _timestamp_pb2.Timestamp
    last_failure: _common_pb2.Failure
    last_worker_identity: str
    started_worker_identity: str
    schedule_id: int
    def __init__(self, activity_id: _Optional[str] = ..., activity_type: _Optional[_Union[_common_pb2.ActivityType, _Mapping]] = ..., state: _Optional[_Union[PendingActivityState, str]] = ..., heartbeat_details: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., last_heartbeat_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_started_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., attempt: _Optional[int] = ..., maximum_attempts: _Optional[int] = ..., scheduled_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expiration_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., last_failure: _Optional[_Union[_common_pb2.Failure, _Mapping]] = ..., last_worker_identity: _Optional[str] = ..., started_worker_identity: _Optional[str] = ..., schedule_id: _Optional[int] = ...) -> None: ...

class PendingChildExecutionInfo(_message.Message):
    __slots__ = ("workflow_execution", "workflow_type_name", "initiated_id", "parent_close_policy", "domain")
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_TYPE_NAME_FIELD_NUMBER: _ClassVar[int]
    INITIATED_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_CLOSE_POLICY_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    workflow_execution: _common_pb2.WorkflowExecution
    workflow_type_name: str
    initiated_id: int
    parent_close_policy: ParentClosePolicy
    domain: str
    def __init__(self, workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., workflow_type_name: _Optional[str] = ..., initiated_id: _Optional[int] = ..., parent_close_policy: _Optional[_Union[ParentClosePolicy, str]] = ..., domain: _Optional[str] = ...) -> None: ...

class PendingDecisionInfo(_message.Message):
    __slots__ = ("state", "scheduled_time", "started_time", "attempt", "original_scheduled_time", "schedule_id")
    STATE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_TIME_FIELD_NUMBER: _ClassVar[int]
    STARTED_TIME_FIELD_NUMBER: _ClassVar[int]
    ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_SCHEDULED_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_ID_FIELD_NUMBER: _ClassVar[int]
    state: PendingDecisionState
    scheduled_time: _timestamp_pb2.Timestamp
    started_time: _timestamp_pb2.Timestamp
    attempt: int
    original_scheduled_time: _timestamp_pb2.Timestamp
    schedule_id: int
    def __init__(self, state: _Optional[_Union[PendingDecisionState, str]] = ..., scheduled_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., attempt: _Optional[int] = ..., original_scheduled_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., schedule_id: _Optional[int] = ...) -> None: ...

class ActivityLocalDispatchInfo(_message.Message):
    __slots__ = ("activity_id", "scheduled_time", "started_time", "scheduled_time_of_this_attempt", "task_token")
    ACTIVITY_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_TIME_FIELD_NUMBER: _ClassVar[int]
    STARTED_TIME_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_TIME_OF_THIS_ATTEMPT_FIELD_NUMBER: _ClassVar[int]
    TASK_TOKEN_FIELD_NUMBER: _ClassVar[int]
    activity_id: str
    scheduled_time: _timestamp_pb2.Timestamp
    started_time: _timestamp_pb2.Timestamp
    scheduled_time_of_this_attempt: _timestamp_pb2.Timestamp
    task_token: bytes
    def __init__(self, activity_id: _Optional[str] = ..., scheduled_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., started_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., scheduled_time_of_this_attempt: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., task_token: _Optional[bytes] = ...) -> None: ...

class ResetPoints(_message.Message):
    __slots__ = ("points",)
    POINTS_FIELD_NUMBER: _ClassVar[int]
    points: _containers.RepeatedCompositeFieldContainer[ResetPointInfo]
    def __init__(self, points: _Optional[_Iterable[_Union[ResetPointInfo, _Mapping]]] = ...) -> None: ...

class ResetPointInfo(_message.Message):
    __slots__ = ("binary_checksum", "run_id", "first_decision_completed_id", "created_time", "expiring_time", "resettable")
    BINARY_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    FIRST_DECISION_COMPLETED_ID_FIELD_NUMBER: _ClassVar[int]
    CREATED_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRING_TIME_FIELD_NUMBER: _ClassVar[int]
    RESETTABLE_FIELD_NUMBER: _ClassVar[int]
    binary_checksum: str
    run_id: str
    first_decision_completed_id: int
    created_time: _timestamp_pb2.Timestamp
    expiring_time: _timestamp_pb2.Timestamp
    resettable: bool
    def __init__(self, binary_checksum: _Optional[str] = ..., run_id: _Optional[str] = ..., first_decision_completed_id: _Optional[int] = ..., created_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., expiring_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., resettable: bool = ...) -> None: ...
