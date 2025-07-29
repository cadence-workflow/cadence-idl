from google.protobuf import timestamp_pb2 as _timestamp_pb2
from uber.cadence.api.v1 import workflow_pb2 as _workflow_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IndexedValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INDEXED_VALUE_TYPE_INVALID: _ClassVar[IndexedValueType]
    INDEXED_VALUE_TYPE_STRING: _ClassVar[IndexedValueType]
    INDEXED_VALUE_TYPE_KEYWORD: _ClassVar[IndexedValueType]
    INDEXED_VALUE_TYPE_INT: _ClassVar[IndexedValueType]
    INDEXED_VALUE_TYPE_DOUBLE: _ClassVar[IndexedValueType]
    INDEXED_VALUE_TYPE_BOOL: _ClassVar[IndexedValueType]
    INDEXED_VALUE_TYPE_DATETIME: _ClassVar[IndexedValueType]
INDEXED_VALUE_TYPE_INVALID: IndexedValueType
INDEXED_VALUE_TYPE_STRING: IndexedValueType
INDEXED_VALUE_TYPE_KEYWORD: IndexedValueType
INDEXED_VALUE_TYPE_INT: IndexedValueType
INDEXED_VALUE_TYPE_DOUBLE: IndexedValueType
INDEXED_VALUE_TYPE_BOOL: IndexedValueType
INDEXED_VALUE_TYPE_DATETIME: IndexedValueType

class WorkflowExecutionFilter(_message.Message):
    __slots__ = ("workflow_id", "run_id")
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    workflow_id: str
    run_id: str
    def __init__(self, workflow_id: _Optional[str] = ..., run_id: _Optional[str] = ...) -> None: ...

class WorkflowTypeFilter(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class StartTimeFilter(_message.Message):
    __slots__ = ("earliest_time", "latest_time")
    EARLIEST_TIME_FIELD_NUMBER: _ClassVar[int]
    LATEST_TIME_FIELD_NUMBER: _ClassVar[int]
    earliest_time: _timestamp_pb2.Timestamp
    latest_time: _timestamp_pb2.Timestamp
    def __init__(self, earliest_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., latest_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class StatusFilter(_message.Message):
    __slots__ = ("status",)
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: _workflow_pb2.WorkflowExecutionCloseStatus
    def __init__(self, status: _Optional[_Union[_workflow_pb2.WorkflowExecutionCloseStatus, str]] = ...) -> None: ...
