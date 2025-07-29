from google.protobuf import timestamp_pb2 as _timestamp_pb2
from uber.cadence.api.v1 import common_pb2 as _common_pb2
from uber.cadence.api.v1 import history_pb2 as _history_pb2
from uber.cadence.api.v1 import workflow_pb2 as _workflow_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_TYPE_INVALID: _ClassVar[TaskType]
    TASK_TYPE_TRANSFER: _ClassVar[TaskType]
    TASK_TYPE_TIMER: _ClassVar[TaskType]
    TASK_TYPE_REPLICATION: _ClassVar[TaskType]
    TASK_TYPE_CROSS_CLUSTER: _ClassVar[TaskType]

class CrossClusterTaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CROSS_CLUSTER_TASK_TYPE_INVALID: _ClassVar[CrossClusterTaskType]
    CROSS_CLUSTER_TASK_TYPE_START_CHILD_EXECUTION: _ClassVar[CrossClusterTaskType]
    CROSS_CLUSTER_TASK_TYPE_CANCEL_EXECUTION: _ClassVar[CrossClusterTaskType]
    CROSS_CLUSTER_TASK_TYPE_SIGNAL_EXECUTION: _ClassVar[CrossClusterTaskType]
    CROSS_CLUSTER_TASK_TYPE_RECORD_CHILD_WORKKLOW_EXECUTION_COMPLETE: _ClassVar[CrossClusterTaskType]
    CROSS_CLUSTER_TASK_TYPE_APPLY_PARENT_CLOSE_POLICY: _ClassVar[CrossClusterTaskType]

class CrossClusterTaskFailedCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CROSS_CLUSTER_TASK_FAILED_CAUSE_INVALID: _ClassVar[CrossClusterTaskFailedCause]
    CROSS_CLUSTER_TASK_FAILED_CAUSE_DOMAIN_NOT_ACTIVE: _ClassVar[CrossClusterTaskFailedCause]
    CROSS_CLUSTER_TASK_FAILED_CAUSE_DOMAIN_NOT_EXISTS: _ClassVar[CrossClusterTaskFailedCause]
    CROSS_CLUSTER_TASK_FAILED_CAUSE_WORKFLOW_ALREADY_RUNNING: _ClassVar[CrossClusterTaskFailedCause]
    CROSS_CLUSTER_TASK_FAILED_CAUSE_WORKFLOW_NOT_EXISTS: _ClassVar[CrossClusterTaskFailedCause]
    CROSS_CLUSTER_TASK_FAILED_CAUSE_WORKFLOW_ALREADY_COMPLETED: _ClassVar[CrossClusterTaskFailedCause]
    CROSS_CLUSTER_TASK_FAILED_CAUSE_UNCATEGORIZED: _ClassVar[CrossClusterTaskFailedCause]

class GetTaskFailedCause(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GET_TASK_FAILED_CAUSE_INVALID: _ClassVar[GetTaskFailedCause]
    GET_TASK_FAILED_CAUSE_SERVICE_BUSY: _ClassVar[GetTaskFailedCause]
    GET_TASK_FAILED_CAUSE_TIMEOUT: _ClassVar[GetTaskFailedCause]
    GET_TASK_FAILED_CAUSE_SHARD_OWNERSHIP_LOST: _ClassVar[GetTaskFailedCause]
    GET_TASK_FAILED_CAUSE_UNCATEGORIZED: _ClassVar[GetTaskFailedCause]
TASK_TYPE_INVALID: TaskType
TASK_TYPE_TRANSFER: TaskType
TASK_TYPE_TIMER: TaskType
TASK_TYPE_REPLICATION: TaskType
TASK_TYPE_CROSS_CLUSTER: TaskType
CROSS_CLUSTER_TASK_TYPE_INVALID: CrossClusterTaskType
CROSS_CLUSTER_TASK_TYPE_START_CHILD_EXECUTION: CrossClusterTaskType
CROSS_CLUSTER_TASK_TYPE_CANCEL_EXECUTION: CrossClusterTaskType
CROSS_CLUSTER_TASK_TYPE_SIGNAL_EXECUTION: CrossClusterTaskType
CROSS_CLUSTER_TASK_TYPE_RECORD_CHILD_WORKKLOW_EXECUTION_COMPLETE: CrossClusterTaskType
CROSS_CLUSTER_TASK_TYPE_APPLY_PARENT_CLOSE_POLICY: CrossClusterTaskType
CROSS_CLUSTER_TASK_FAILED_CAUSE_INVALID: CrossClusterTaskFailedCause
CROSS_CLUSTER_TASK_FAILED_CAUSE_DOMAIN_NOT_ACTIVE: CrossClusterTaskFailedCause
CROSS_CLUSTER_TASK_FAILED_CAUSE_DOMAIN_NOT_EXISTS: CrossClusterTaskFailedCause
CROSS_CLUSTER_TASK_FAILED_CAUSE_WORKFLOW_ALREADY_RUNNING: CrossClusterTaskFailedCause
CROSS_CLUSTER_TASK_FAILED_CAUSE_WORKFLOW_NOT_EXISTS: CrossClusterTaskFailedCause
CROSS_CLUSTER_TASK_FAILED_CAUSE_WORKFLOW_ALREADY_COMPLETED: CrossClusterTaskFailedCause
CROSS_CLUSTER_TASK_FAILED_CAUSE_UNCATEGORIZED: CrossClusterTaskFailedCause
GET_TASK_FAILED_CAUSE_INVALID: GetTaskFailedCause
GET_TASK_FAILED_CAUSE_SERVICE_BUSY: GetTaskFailedCause
GET_TASK_FAILED_CAUSE_TIMEOUT: GetTaskFailedCause
GET_TASK_FAILED_CAUSE_SHARD_OWNERSHIP_LOST: GetTaskFailedCause
GET_TASK_FAILED_CAUSE_UNCATEGORIZED: GetTaskFailedCause

class CrossClusterTaskInfo(_message.Message):
    __slots__ = ("domain_id", "workflow_execution", "task_type", "task_state", "task_id", "visibility_timestamp")
    DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    domain_id: str
    workflow_execution: _common_pb2.WorkflowExecution
    task_type: CrossClusterTaskType
    task_state: int
    task_id: int
    visibility_timestamp: _timestamp_pb2.Timestamp
    def __init__(self, domain_id: _Optional[str] = ..., workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., task_type: _Optional[_Union[CrossClusterTaskType, str]] = ..., task_state: _Optional[int] = ..., task_id: _Optional[int] = ..., visibility_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CrossClusterStartChildExecutionRequestAttributes(_message.Message):
    __slots__ = ("target_domain_id", "request_id", "initiated_event_id", "initiated_event_attributes", "target_run_id", "partition_config")
    class PartitionConfigEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    TARGET_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    INITIATED_EVENT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    TARGET_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PARTITION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    target_domain_id: str
    request_id: str
    initiated_event_id: int
    initiated_event_attributes: _history_pb2.StartChildWorkflowExecutionInitiatedEventAttributes
    target_run_id: str
    partition_config: _containers.ScalarMap[str, str]
    def __init__(self, target_domain_id: _Optional[str] = ..., request_id: _Optional[str] = ..., initiated_event_id: _Optional[int] = ..., initiated_event_attributes: _Optional[_Union[_history_pb2.StartChildWorkflowExecutionInitiatedEventAttributes, _Mapping]] = ..., target_run_id: _Optional[str] = ..., partition_config: _Optional[_Mapping[str, str]] = ...) -> None: ...

class CrossClusterStartChildExecutionResponseAttributes(_message.Message):
    __slots__ = ("run_id",)
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    run_id: str
    def __init__(self, run_id: _Optional[str] = ...) -> None: ...

class CrossClusterCancelExecutionRequestAttributes(_message.Message):
    __slots__ = ("target_domain_id", "target_workflow_execution", "request_id", "initiated_event_id", "child_workflow_only")
    TARGET_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_WORKFLOW_ONLY_FIELD_NUMBER: _ClassVar[int]
    target_domain_id: str
    target_workflow_execution: _common_pb2.WorkflowExecution
    request_id: str
    initiated_event_id: int
    child_workflow_only: bool
    def __init__(self, target_domain_id: _Optional[str] = ..., target_workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., request_id: _Optional[str] = ..., initiated_event_id: _Optional[int] = ..., child_workflow_only: bool = ...) -> None: ...

class CrossClusterCancelExecutionResponseAttributes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CrossClusterSignalExecutionRequestAttributes(_message.Message):
    __slots__ = ("target_domain_id", "target_workflow_execution", "request_id", "initiated_event_id", "child_workflow_only", "signal_name", "signal_input", "control")
    TARGET_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_WORKFLOW_ONLY_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_NAME_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_INPUT_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    target_domain_id: str
    target_workflow_execution: _common_pb2.WorkflowExecution
    request_id: str
    initiated_event_id: int
    child_workflow_only: bool
    signal_name: str
    signal_input: _common_pb2.Payload
    control: bytes
    def __init__(self, target_domain_id: _Optional[str] = ..., target_workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., request_id: _Optional[str] = ..., initiated_event_id: _Optional[int] = ..., child_workflow_only: bool = ..., signal_name: _Optional[str] = ..., signal_input: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., control: _Optional[bytes] = ...) -> None: ...

class CrossClusterSignalExecutionResponseAttributes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class CrossClusterRecordChildWorkflowExecutionCompleteRequestAttributes(_message.Message):
    __slots__ = ("target_domain_id", "target_workflow_execution", "initiated_event_id", "completion_event")
    TARGET_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    TARGET_WORKFLOW_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    INITIATED_EVENT_ID_FIELD_NUMBER: _ClassVar[int]
    COMPLETION_EVENT_FIELD_NUMBER: _ClassVar[int]
    target_domain_id: str
    target_workflow_execution: _common_pb2.WorkflowExecution
    initiated_event_id: int
    completion_event: _history_pb2.HistoryEvent
    def __init__(self, target_domain_id: _Optional[str] = ..., target_workflow_execution: _Optional[_Union[_common_pb2.WorkflowExecution, _Mapping]] = ..., initiated_event_id: _Optional[int] = ..., completion_event: _Optional[_Union[_history_pb2.HistoryEvent, _Mapping]] = ...) -> None: ...

class CrossClusterRecordChildWorkflowExecutionCompleteResponseAttributes(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ApplyParentClosePolicyAttributes(_message.Message):
    __slots__ = ("child_domain_id", "child_workflow_id", "child_run_id", "parent_close_policy")
    CHILD_DOMAIN_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    CHILD_RUN_ID_FIELD_NUMBER: _ClassVar[int]
    PARENT_CLOSE_POLICY_FIELD_NUMBER: _ClassVar[int]
    child_domain_id: str
    child_workflow_id: str
    child_run_id: str
    parent_close_policy: _workflow_pb2.ParentClosePolicy
    def __init__(self, child_domain_id: _Optional[str] = ..., child_workflow_id: _Optional[str] = ..., child_run_id: _Optional[str] = ..., parent_close_policy: _Optional[_Union[_workflow_pb2.ParentClosePolicy, str]] = ...) -> None: ...

class ApplyParentClosePolicyStatus(_message.Message):
    __slots__ = ("completed", "failed_cause")
    COMPLETED_FIELD_NUMBER: _ClassVar[int]
    FAILED_CAUSE_FIELD_NUMBER: _ClassVar[int]
    completed: bool
    failed_cause: CrossClusterTaskFailedCause
    def __init__(self, completed: bool = ..., failed_cause: _Optional[_Union[CrossClusterTaskFailedCause, str]] = ...) -> None: ...

class ApplyParentClosePolicyRequest(_message.Message):
    __slots__ = ("child", "status")
    CHILD_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    child: ApplyParentClosePolicyAttributes
    status: ApplyParentClosePolicyStatus
    def __init__(self, child: _Optional[_Union[ApplyParentClosePolicyAttributes, _Mapping]] = ..., status: _Optional[_Union[ApplyParentClosePolicyStatus, _Mapping]] = ...) -> None: ...

class CrossClusterApplyParentClosePolicyRequestAttributes(_message.Message):
    __slots__ = ("children",)
    CHILDREN_FIELD_NUMBER: _ClassVar[int]
    children: _containers.RepeatedCompositeFieldContainer[ApplyParentClosePolicyRequest]
    def __init__(self, children: _Optional[_Iterable[_Union[ApplyParentClosePolicyRequest, _Mapping]]] = ...) -> None: ...

class ApplyParentClosePolicyResult(_message.Message):
    __slots__ = ("child", "failed_cause")
    CHILD_FIELD_NUMBER: _ClassVar[int]
    FAILED_CAUSE_FIELD_NUMBER: _ClassVar[int]
    child: ApplyParentClosePolicyAttributes
    failed_cause: CrossClusterTaskFailedCause
    def __init__(self, child: _Optional[_Union[ApplyParentClosePolicyAttributes, _Mapping]] = ..., failed_cause: _Optional[_Union[CrossClusterTaskFailedCause, str]] = ...) -> None: ...

class CrossClusterApplyParentClosePolicyResponseAttributes(_message.Message):
    __slots__ = ("children_status",)
    CHILDREN_STATUS_FIELD_NUMBER: _ClassVar[int]
    children_status: _containers.RepeatedCompositeFieldContainer[ApplyParentClosePolicyResult]
    def __init__(self, children_status: _Optional[_Iterable[_Union[ApplyParentClosePolicyResult, _Mapping]]] = ...) -> None: ...

class CrossClusterTaskRequest(_message.Message):
    __slots__ = ("task_info", "start_child_execution_attributes", "cancel_execution_attributes", "signal_execution_attributes", "record_child_workflow_execution_complete_request_attributes", "apply_parent_close_policy_request_attributes")
    TASK_INFO_FIELD_NUMBER: _ClassVar[int]
    START_CHILD_EXECUTION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CANCEL_EXECUTION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_EXECUTION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    RECORD_CHILD_WORKFLOW_EXECUTION_COMPLETE_REQUEST_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    APPLY_PARENT_CLOSE_POLICY_REQUEST_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    task_info: CrossClusterTaskInfo
    start_child_execution_attributes: CrossClusterStartChildExecutionRequestAttributes
    cancel_execution_attributes: CrossClusterCancelExecutionRequestAttributes
    signal_execution_attributes: CrossClusterSignalExecutionRequestAttributes
    record_child_workflow_execution_complete_request_attributes: CrossClusterRecordChildWorkflowExecutionCompleteRequestAttributes
    apply_parent_close_policy_request_attributes: CrossClusterApplyParentClosePolicyRequestAttributes
    def __init__(self, task_info: _Optional[_Union[CrossClusterTaskInfo, _Mapping]] = ..., start_child_execution_attributes: _Optional[_Union[CrossClusterStartChildExecutionRequestAttributes, _Mapping]] = ..., cancel_execution_attributes: _Optional[_Union[CrossClusterCancelExecutionRequestAttributes, _Mapping]] = ..., signal_execution_attributes: _Optional[_Union[CrossClusterSignalExecutionRequestAttributes, _Mapping]] = ..., record_child_workflow_execution_complete_request_attributes: _Optional[_Union[CrossClusterRecordChildWorkflowExecutionCompleteRequestAttributes, _Mapping]] = ..., apply_parent_close_policy_request_attributes: _Optional[_Union[CrossClusterApplyParentClosePolicyRequestAttributes, _Mapping]] = ...) -> None: ...

class CrossClusterTaskResponse(_message.Message):
    __slots__ = ("task_id", "task_type", "task_state", "failed_cause", "start_child_execution_attributes", "cancel_execution_attributes", "signal_execution_attributes", "record_child_workflow_execution_complete_request_attributes", "apply_parent_close_policy_response_attributes")
    TASK_ID_FIELD_NUMBER: _ClassVar[int]
    TASK_TYPE_FIELD_NUMBER: _ClassVar[int]
    TASK_STATE_FIELD_NUMBER: _ClassVar[int]
    FAILED_CAUSE_FIELD_NUMBER: _ClassVar[int]
    START_CHILD_EXECUTION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    CANCEL_EXECUTION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    SIGNAL_EXECUTION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    RECORD_CHILD_WORKFLOW_EXECUTION_COMPLETE_REQUEST_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    APPLY_PARENT_CLOSE_POLICY_RESPONSE_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    task_id: int
    task_type: CrossClusterTaskType
    task_state: int
    failed_cause: CrossClusterTaskFailedCause
    start_child_execution_attributes: CrossClusterStartChildExecutionResponseAttributes
    cancel_execution_attributes: CrossClusterCancelExecutionResponseAttributes
    signal_execution_attributes: CrossClusterSignalExecutionResponseAttributes
    record_child_workflow_execution_complete_request_attributes: CrossClusterRecordChildWorkflowExecutionCompleteResponseAttributes
    apply_parent_close_policy_response_attributes: CrossClusterApplyParentClosePolicyResponseAttributes
    def __init__(self, task_id: _Optional[int] = ..., task_type: _Optional[_Union[CrossClusterTaskType, str]] = ..., task_state: _Optional[int] = ..., failed_cause: _Optional[_Union[CrossClusterTaskFailedCause, str]] = ..., start_child_execution_attributes: _Optional[_Union[CrossClusterStartChildExecutionResponseAttributes, _Mapping]] = ..., cancel_execution_attributes: _Optional[_Union[CrossClusterCancelExecutionResponseAttributes, _Mapping]] = ..., signal_execution_attributes: _Optional[_Union[CrossClusterSignalExecutionResponseAttributes, _Mapping]] = ..., record_child_workflow_execution_complete_request_attributes: _Optional[_Union[CrossClusterRecordChildWorkflowExecutionCompleteResponseAttributes, _Mapping]] = ..., apply_parent_close_policy_response_attributes: _Optional[_Union[CrossClusterApplyParentClosePolicyResponseAttributes, _Mapping]] = ...) -> None: ...

class CrossClusterTaskRequests(_message.Message):
    __slots__ = ("task_requests",)
    TASK_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    task_requests: _containers.RepeatedCompositeFieldContainer[CrossClusterTaskRequest]
    def __init__(self, task_requests: _Optional[_Iterable[_Union[CrossClusterTaskRequest, _Mapping]]] = ...) -> None: ...
