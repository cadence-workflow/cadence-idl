from uber.cadence.api.v1 import common_pb2 as _common_pb2
from uber.cadence.api.v1 import workflow_pb2 as _workflow_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QueryResultType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUERY_RESULT_TYPE_INVALID: _ClassVar[QueryResultType]
    QUERY_RESULT_TYPE_ANSWERED: _ClassVar[QueryResultType]
    QUERY_RESULT_TYPE_FAILED: _ClassVar[QueryResultType]

class QueryRejectCondition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUERY_REJECT_CONDITION_INVALID: _ClassVar[QueryRejectCondition]
    QUERY_REJECT_CONDITION_NOT_OPEN: _ClassVar[QueryRejectCondition]
    QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY: _ClassVar[QueryRejectCondition]

class QueryConsistencyLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUERY_CONSISTENCY_LEVEL_INVALID: _ClassVar[QueryConsistencyLevel]
    QUERY_CONSISTENCY_LEVEL_EVENTUAL: _ClassVar[QueryConsistencyLevel]
    QUERY_CONSISTENCY_LEVEL_STRONG: _ClassVar[QueryConsistencyLevel]
QUERY_RESULT_TYPE_INVALID: QueryResultType
QUERY_RESULT_TYPE_ANSWERED: QueryResultType
QUERY_RESULT_TYPE_FAILED: QueryResultType
QUERY_REJECT_CONDITION_INVALID: QueryRejectCondition
QUERY_REJECT_CONDITION_NOT_OPEN: QueryRejectCondition
QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY: QueryRejectCondition
QUERY_CONSISTENCY_LEVEL_INVALID: QueryConsistencyLevel
QUERY_CONSISTENCY_LEVEL_EVENTUAL: QueryConsistencyLevel
QUERY_CONSISTENCY_LEVEL_STRONG: QueryConsistencyLevel

class WorkflowQuery(_message.Message):
    __slots__ = ("query_type", "query_args")
    QUERY_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUERY_ARGS_FIELD_NUMBER: _ClassVar[int]
    query_type: str
    query_args: _common_pb2.Payload
    def __init__(self, query_type: _Optional[str] = ..., query_args: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ...) -> None: ...

class WorkflowQueryResult(_message.Message):
    __slots__ = ("result_type", "answer", "error_message")
    RESULT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    result_type: QueryResultType
    answer: _common_pb2.Payload
    error_message: str
    def __init__(self, result_type: _Optional[_Union[QueryResultType, str]] = ..., answer: _Optional[_Union[_common_pb2.Payload, _Mapping]] = ..., error_message: _Optional[str] = ...) -> None: ...

class QueryRejected(_message.Message):
    __slots__ = ("close_status",)
    CLOSE_STATUS_FIELD_NUMBER: _ClassVar[int]
    close_status: _workflow_pb2.WorkflowExecutionCloseStatus
    def __init__(self, close_status: _Optional[_Union[_workflow_pb2.WorkflowExecutionCloseStatus, str]] = ...) -> None: ...
