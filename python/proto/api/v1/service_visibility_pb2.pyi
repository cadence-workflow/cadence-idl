from uber.cadence.api.v1 import visibility_pb2 as _visibility_pb2
from uber.cadence.api.v1 import workflow_pb2 as _workflow_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ListWorkflowExecutionsRequest(_message.Message):
    __slots__ = ("domain", "page_size", "next_page_token", "query")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    page_size: int
    next_page_token: bytes
    query: str
    def __init__(self, domain: _Optional[str] = ..., page_size: _Optional[int] = ..., next_page_token: _Optional[bytes] = ..., query: _Optional[str] = ...) -> None: ...

class ListWorkflowExecutionsResponse(_message.Message):
    __slots__ = ("executions", "next_page_token")
    EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    executions: _containers.RepeatedCompositeFieldContainer[_workflow_pb2.WorkflowExecutionInfo]
    next_page_token: bytes
    def __init__(self, executions: _Optional[_Iterable[_Union[_workflow_pb2.WorkflowExecutionInfo, _Mapping]]] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class ListOpenWorkflowExecutionsRequest(_message.Message):
    __slots__ = ("domain", "page_size", "next_page_token", "start_time_filter", "execution_filter", "type_filter")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FILTER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FILTER_FIELD_NUMBER: _ClassVar[int]
    domain: str
    page_size: int
    next_page_token: bytes
    start_time_filter: _visibility_pb2.StartTimeFilter
    execution_filter: _visibility_pb2.WorkflowExecutionFilter
    type_filter: _visibility_pb2.WorkflowTypeFilter
    def __init__(self, domain: _Optional[str] = ..., page_size: _Optional[int] = ..., next_page_token: _Optional[bytes] = ..., start_time_filter: _Optional[_Union[_visibility_pb2.StartTimeFilter, _Mapping]] = ..., execution_filter: _Optional[_Union[_visibility_pb2.WorkflowExecutionFilter, _Mapping]] = ..., type_filter: _Optional[_Union[_visibility_pb2.WorkflowTypeFilter, _Mapping]] = ...) -> None: ...

class ListOpenWorkflowExecutionsResponse(_message.Message):
    __slots__ = ("executions", "next_page_token")
    EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    executions: _containers.RepeatedCompositeFieldContainer[_workflow_pb2.WorkflowExecutionInfo]
    next_page_token: bytes
    def __init__(self, executions: _Optional[_Iterable[_Union[_workflow_pb2.WorkflowExecutionInfo, _Mapping]]] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class ListClosedWorkflowExecutionsRequest(_message.Message):
    __slots__ = ("domain", "page_size", "next_page_token", "start_time_filter", "execution_filter", "type_filter", "status_filter")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FILTER_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_FILTER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FILTER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FILTER_FIELD_NUMBER: _ClassVar[int]
    domain: str
    page_size: int
    next_page_token: bytes
    start_time_filter: _visibility_pb2.StartTimeFilter
    execution_filter: _visibility_pb2.WorkflowExecutionFilter
    type_filter: _visibility_pb2.WorkflowTypeFilter
    status_filter: _visibility_pb2.StatusFilter
    def __init__(self, domain: _Optional[str] = ..., page_size: _Optional[int] = ..., next_page_token: _Optional[bytes] = ..., start_time_filter: _Optional[_Union[_visibility_pb2.StartTimeFilter, _Mapping]] = ..., execution_filter: _Optional[_Union[_visibility_pb2.WorkflowExecutionFilter, _Mapping]] = ..., type_filter: _Optional[_Union[_visibility_pb2.WorkflowTypeFilter, _Mapping]] = ..., status_filter: _Optional[_Union[_visibility_pb2.StatusFilter, _Mapping]] = ...) -> None: ...

class ListClosedWorkflowExecutionsResponse(_message.Message):
    __slots__ = ("executions", "next_page_token")
    EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    executions: _containers.RepeatedCompositeFieldContainer[_workflow_pb2.WorkflowExecutionInfo]
    next_page_token: bytes
    def __init__(self, executions: _Optional[_Iterable[_Union[_workflow_pb2.WorkflowExecutionInfo, _Mapping]]] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class ListArchivedWorkflowExecutionsRequest(_message.Message):
    __slots__ = ("domain", "page_size", "next_page_token", "query")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    page_size: int
    next_page_token: bytes
    query: str
    def __init__(self, domain: _Optional[str] = ..., page_size: _Optional[int] = ..., next_page_token: _Optional[bytes] = ..., query: _Optional[str] = ...) -> None: ...

class ListArchivedWorkflowExecutionsResponse(_message.Message):
    __slots__ = ("executions", "next_page_token")
    EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    executions: _containers.RepeatedCompositeFieldContainer[_workflow_pb2.WorkflowExecutionInfo]
    next_page_token: bytes
    def __init__(self, executions: _Optional[_Iterable[_Union[_workflow_pb2.WorkflowExecutionInfo, _Mapping]]] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class ScanWorkflowExecutionsRequest(_message.Message):
    __slots__ = ("domain", "page_size", "next_page_token", "query")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    page_size: int
    next_page_token: bytes
    query: str
    def __init__(self, domain: _Optional[str] = ..., page_size: _Optional[int] = ..., next_page_token: _Optional[bytes] = ..., query: _Optional[str] = ...) -> None: ...

class ScanWorkflowExecutionsResponse(_message.Message):
    __slots__ = ("executions", "next_page_token")
    EXECUTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    executions: _containers.RepeatedCompositeFieldContainer[_workflow_pb2.WorkflowExecutionInfo]
    next_page_token: bytes
    def __init__(self, executions: _Optional[_Iterable[_Union[_workflow_pb2.WorkflowExecutionInfo, _Mapping]]] = ..., next_page_token: _Optional[bytes] = ...) -> None: ...

class CountWorkflowExecutionsRequest(_message.Message):
    __slots__ = ("domain", "query")
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    domain: str
    query: str
    def __init__(self, domain: _Optional[str] = ..., query: _Optional[str] = ...) -> None: ...

class CountWorkflowExecutionsResponse(_message.Message):
    __slots__ = ("count",)
    COUNT_FIELD_NUMBER: _ClassVar[int]
    count: int
    def __init__(self, count: _Optional[int] = ...) -> None: ...

class GetSearchAttributesRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetSearchAttributesResponse(_message.Message):
    __slots__ = ("keys",)
    class KeysEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _visibility_pb2.IndexedValueType
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_visibility_pb2.IndexedValueType, str]] = ...) -> None: ...
    KEYS_FIELD_NUMBER: _ClassVar[int]
    keys: _containers.ScalarMap[str, _visibility_pb2.IndexedValueType]
    def __init__(self, keys: _Optional[_Mapping[str, _visibility_pb2.IndexedValueType]] = ...) -> None: ...
