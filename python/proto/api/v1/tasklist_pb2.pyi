from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskListKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_LIST_KIND_INVALID: _ClassVar[TaskListKind]
    TASK_LIST_KIND_NORMAL: _ClassVar[TaskListKind]
    TASK_LIST_KIND_STICKY: _ClassVar[TaskListKind]
    TASK_LIST_KIND_EPHEMERAL: _ClassVar[TaskListKind]

class TaskListType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TASK_LIST_TYPE_INVALID: _ClassVar[TaskListType]
    TASK_LIST_TYPE_DECISION: _ClassVar[TaskListType]
    TASK_LIST_TYPE_ACTIVITY: _ClassVar[TaskListType]
TASK_LIST_KIND_INVALID: TaskListKind
TASK_LIST_KIND_NORMAL: TaskListKind
TASK_LIST_KIND_STICKY: TaskListKind
TASK_LIST_KIND_EPHEMERAL: TaskListKind
TASK_LIST_TYPE_INVALID: TaskListType
TASK_LIST_TYPE_DECISION: TaskListType
TASK_LIST_TYPE_ACTIVITY: TaskListType

class TaskList(_message.Message):
    __slots__ = ("name", "kind")
    NAME_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    name: str
    kind: TaskListKind
    def __init__(self, name: _Optional[str] = ..., kind: _Optional[_Union[TaskListKind, str]] = ...) -> None: ...

class TaskListMetadata(_message.Message):
    __slots__ = ("max_tasks_per_second",)
    MAX_TASKS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    max_tasks_per_second: _wrappers_pb2.DoubleValue
    def __init__(self, max_tasks_per_second: _Optional[_Union[_wrappers_pb2.DoubleValue, _Mapping]] = ...) -> None: ...

class TaskListPartitionMetadata(_message.Message):
    __slots__ = ("key", "owner_host_name")
    KEY_FIELD_NUMBER: _ClassVar[int]
    OWNER_HOST_NAME_FIELD_NUMBER: _ClassVar[int]
    key: str
    owner_host_name: str
    def __init__(self, key: _Optional[str] = ..., owner_host_name: _Optional[str] = ...) -> None: ...

class IsolationGroupMetrics(_message.Message):
    __slots__ = ("new_tasks_per_second", "poller_count")
    NEW_TASKS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    POLLER_COUNT_FIELD_NUMBER: _ClassVar[int]
    new_tasks_per_second: float
    poller_count: int
    def __init__(self, new_tasks_per_second: _Optional[float] = ..., poller_count: _Optional[int] = ...) -> None: ...

class TaskListStatus(_message.Message):
    __slots__ = ("backlog_count_hint", "read_level", "ack_level", "rate_per_second", "task_id_block", "isolation_group_metrics", "new_tasks_per_second", "empty")
    class IsolationGroupMetricsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: IsolationGroupMetrics
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[IsolationGroupMetrics, _Mapping]] = ...) -> None: ...
    BACKLOG_COUNT_HINT_FIELD_NUMBER: _ClassVar[int]
    READ_LEVEL_FIELD_NUMBER: _ClassVar[int]
    ACK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    RATE_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    TASK_ID_BLOCK_FIELD_NUMBER: _ClassVar[int]
    ISOLATION_GROUP_METRICS_FIELD_NUMBER: _ClassVar[int]
    NEW_TASKS_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    EMPTY_FIELD_NUMBER: _ClassVar[int]
    backlog_count_hint: int
    read_level: int
    ack_level: int
    rate_per_second: float
    task_id_block: TaskIDBlock
    isolation_group_metrics: _containers.MessageMap[str, IsolationGroupMetrics]
    new_tasks_per_second: float
    empty: bool
    def __init__(self, backlog_count_hint: _Optional[int] = ..., read_level: _Optional[int] = ..., ack_level: _Optional[int] = ..., rate_per_second: _Optional[float] = ..., task_id_block: _Optional[_Union[TaskIDBlock, _Mapping]] = ..., isolation_group_metrics: _Optional[_Mapping[str, IsolationGroupMetrics]] = ..., new_tasks_per_second: _Optional[float] = ..., empty: bool = ...) -> None: ...

class TaskIDBlock(_message.Message):
    __slots__ = ("start_id", "end_id")
    START_ID_FIELD_NUMBER: _ClassVar[int]
    END_ID_FIELD_NUMBER: _ClassVar[int]
    start_id: int
    end_id: int
    def __init__(self, start_id: _Optional[int] = ..., end_id: _Optional[int] = ...) -> None: ...

class PollerInfo(_message.Message):
    __slots__ = ("last_access_time", "identity", "rate_per_second")
    LAST_ACCESS_TIME_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    RATE_PER_SECOND_FIELD_NUMBER: _ClassVar[int]
    last_access_time: _timestamp_pb2.Timestamp
    identity: str
    rate_per_second: float
    def __init__(self, last_access_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., identity: _Optional[str] = ..., rate_per_second: _Optional[float] = ...) -> None: ...

class StickyExecutionAttributes(_message.Message):
    __slots__ = ("worker_task_list", "schedule_to_start_timeout")
    WORKER_TASK_LIST_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TO_START_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    worker_task_list: TaskList
    schedule_to_start_timeout: _duration_pb2.Duration
    def __init__(self, worker_task_list: _Optional[_Union[TaskList, _Mapping]] = ..., schedule_to_start_timeout: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class TaskListPartition(_message.Message):
    __slots__ = ("isolation_groups",)
    ISOLATION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    isolation_groups: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, isolation_groups: _Optional[_Iterable[str]] = ...) -> None: ...

class TaskListPartitionConfig(_message.Message):
    __slots__ = ("version", "num_read_partitions", "num_write_partitions", "read_partitions", "write_partitions")
    class ReadPartitionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TaskListPartition
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TaskListPartition, _Mapping]] = ...) -> None: ...
    class WritePartitionsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: TaskListPartition
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[TaskListPartition, _Mapping]] = ...) -> None: ...
    VERSION_FIELD_NUMBER: _ClassVar[int]
    NUM_READ_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    NUM_WRITE_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    READ_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    WRITE_PARTITIONS_FIELD_NUMBER: _ClassVar[int]
    version: int
    num_read_partitions: int
    num_write_partitions: int
    read_partitions: _containers.MessageMap[int, TaskListPartition]
    write_partitions: _containers.MessageMap[int, TaskListPartition]
    def __init__(self, version: _Optional[int] = ..., num_read_partitions: _Optional[int] = ..., num_write_partitions: _Optional[int] = ..., read_partitions: _Optional[_Mapping[int, TaskListPartition]] = ..., write_partitions: _Optional[_Mapping[int, TaskListPartition]] = ...) -> None: ...
