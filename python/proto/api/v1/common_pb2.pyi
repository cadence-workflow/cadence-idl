from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EncodingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENCODING_TYPE_INVALID: _ClassVar[EncodingType]
    ENCODING_TYPE_THRIFTRW: _ClassVar[EncodingType]
    ENCODING_TYPE_JSON: _ClassVar[EncodingType]
    ENCODING_TYPE_PROTO3: _ClassVar[EncodingType]

class IsolationGroupState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ISOLATION_GROUP_STATE_INVALID: _ClassVar[IsolationGroupState]
    ISOLATION_GROUP_STATE_HEALTHY: _ClassVar[IsolationGroupState]
    ISOLATION_GROUP_STATE_DRAINED: _ClassVar[IsolationGroupState]

class ActiveClusterSelectionStrategy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTIVE_CLUSTER_SELECTION_STRATEGY_INVALID: _ClassVar[ActiveClusterSelectionStrategy]
    ACTIVE_CLUSTER_SELECTION_STRATEGY_REGION_STICKY: _ClassVar[ActiveClusterSelectionStrategy]
    ACTIVE_CLUSTER_SELECTION_STRATEGY_EXTERNAL_ENTITY: _ClassVar[ActiveClusterSelectionStrategy]
ENCODING_TYPE_INVALID: EncodingType
ENCODING_TYPE_THRIFTRW: EncodingType
ENCODING_TYPE_JSON: EncodingType
ENCODING_TYPE_PROTO3: EncodingType
ISOLATION_GROUP_STATE_INVALID: IsolationGroupState
ISOLATION_GROUP_STATE_HEALTHY: IsolationGroupState
ISOLATION_GROUP_STATE_DRAINED: IsolationGroupState
ACTIVE_CLUSTER_SELECTION_STRATEGY_INVALID: ActiveClusterSelectionStrategy
ACTIVE_CLUSTER_SELECTION_STRATEGY_REGION_STICKY: ActiveClusterSelectionStrategy
ACTIVE_CLUSTER_SELECTION_STRATEGY_EXTERNAL_ENTITY: ActiveClusterSelectionStrategy

class WorkflowExecution(_message.Message):
    __slots__ = ("workflow_id", "run_id")
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    RUN_ID_FIELD_NUMBER: _ClassVar[int]
    workflow_id: str
    run_id: str
    def __init__(self, workflow_id: _Optional[str] = ..., run_id: _Optional[str] = ...) -> None: ...

class WorkflowType(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ActivityType(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class Payload(_message.Message):
    __slots__ = ("data",)
    DATA_FIELD_NUMBER: _ClassVar[int]
    data: bytes
    def __init__(self, data: _Optional[bytes] = ...) -> None: ...

class Failure(_message.Message):
    __slots__ = ("reason", "details")
    REASON_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    reason: str
    details: bytes
    def __init__(self, reason: _Optional[str] = ..., details: _Optional[bytes] = ...) -> None: ...

class Memo(_message.Message):
    __slots__ = ("fields",)
    class FieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Payload
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Payload, _Mapping]] = ...) -> None: ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.MessageMap[str, Payload]
    def __init__(self, fields: _Optional[_Mapping[str, Payload]] = ...) -> None: ...

class Header(_message.Message):
    __slots__ = ("fields",)
    class FieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Payload
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Payload, _Mapping]] = ...) -> None: ...
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.MessageMap[str, Payload]
    def __init__(self, fields: _Optional[_Mapping[str, Payload]] = ...) -> None: ...

class SearchAttributes(_message.Message):
    __slots__ = ("indexed_fields",)
    class IndexedFieldsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: Payload
        def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[Payload, _Mapping]] = ...) -> None: ...
    INDEXED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    indexed_fields: _containers.MessageMap[str, Payload]
    def __init__(self, indexed_fields: _Optional[_Mapping[str, Payload]] = ...) -> None: ...

class DataBlob(_message.Message):
    __slots__ = ("encoding_type", "data")
    ENCODING_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    encoding_type: EncodingType
    data: bytes
    def __init__(self, encoding_type: _Optional[_Union[EncodingType, str]] = ..., data: _Optional[bytes] = ...) -> None: ...

class WorkerVersionInfo(_message.Message):
    __slots__ = ("impl", "feature_version")
    IMPL_FIELD_NUMBER: _ClassVar[int]
    FEATURE_VERSION_FIELD_NUMBER: _ClassVar[int]
    impl: str
    feature_version: str
    def __init__(self, impl: _Optional[str] = ..., feature_version: _Optional[str] = ...) -> None: ...

class SupportedClientVersions(_message.Message):
    __slots__ = ("go_sdk", "java_sdk")
    GO_SDK_FIELD_NUMBER: _ClassVar[int]
    JAVA_SDK_FIELD_NUMBER: _ClassVar[int]
    go_sdk: str
    java_sdk: str
    def __init__(self, go_sdk: _Optional[str] = ..., java_sdk: _Optional[str] = ...) -> None: ...

class RetryPolicy(_message.Message):
    __slots__ = ("initial_interval", "backoff_coefficient", "maximum_interval", "maximum_attempts", "non_retryable_error_reasons", "expiration_interval")
    INITIAL_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    BACKOFF_COEFFICIENT_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_ATTEMPTS_FIELD_NUMBER: _ClassVar[int]
    NON_RETRYABLE_ERROR_REASONS_FIELD_NUMBER: _ClassVar[int]
    EXPIRATION_INTERVAL_FIELD_NUMBER: _ClassVar[int]
    initial_interval: _duration_pb2.Duration
    backoff_coefficient: float
    maximum_interval: _duration_pb2.Duration
    maximum_attempts: int
    non_retryable_error_reasons: _containers.RepeatedScalarFieldContainer[str]
    expiration_interval: _duration_pb2.Duration
    def __init__(self, initial_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., backoff_coefficient: _Optional[float] = ..., maximum_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., maximum_attempts: _Optional[int] = ..., non_retryable_error_reasons: _Optional[_Iterable[str]] = ..., expiration_interval: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ...) -> None: ...

class IsolationGroupPartition(_message.Message):
    __slots__ = ("name", "state")
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: IsolationGroupState
    def __init__(self, name: _Optional[str] = ..., state: _Optional[_Union[IsolationGroupState, str]] = ...) -> None: ...

class IsolationGroupConfiguration(_message.Message):
    __slots__ = ("isolation_groups",)
    ISOLATION_GROUPS_FIELD_NUMBER: _ClassVar[int]
    isolation_groups: _containers.RepeatedCompositeFieldContainer[IsolationGroupPartition]
    def __init__(self, isolation_groups: _Optional[_Iterable[_Union[IsolationGroupPartition, _Mapping]]] = ...) -> None: ...

class AsyncWorkflowConfiguration(_message.Message):
    __slots__ = ("enabled", "predefined_queue_name", "queue_type", "queue_config")
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    PREDEFINED_QUEUE_NAME_FIELD_NUMBER: _ClassVar[int]
    QUEUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUEUE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    enabled: bool
    predefined_queue_name: str
    queue_type: str
    queue_config: DataBlob
    def __init__(self, enabled: bool = ..., predefined_queue_name: _Optional[str] = ..., queue_type: _Optional[str] = ..., queue_config: _Optional[_Union[DataBlob, _Mapping]] = ...) -> None: ...

class ActiveClusterSelectionPolicy(_message.Message):
    __slots__ = ("strategy", "active_cluster_sticky_region_config", "active_cluster_external_entity_config")
    STRATEGY_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTER_STICKY_REGION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_CLUSTER_EXTERNAL_ENTITY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    strategy: ActiveClusterSelectionStrategy
    active_cluster_sticky_region_config: ActiveClusterStickyRegionConfig
    active_cluster_external_entity_config: ActiveClusterExternalEntityConfig
    def __init__(self, strategy: _Optional[_Union[ActiveClusterSelectionStrategy, str]] = ..., active_cluster_sticky_region_config: _Optional[_Union[ActiveClusterStickyRegionConfig, _Mapping]] = ..., active_cluster_external_entity_config: _Optional[_Union[ActiveClusterExternalEntityConfig, _Mapping]] = ...) -> None: ...

class ActiveClusterStickyRegionConfig(_message.Message):
    __slots__ = ("sticky_region",)
    STICKY_REGION_FIELD_NUMBER: _ClassVar[int]
    sticky_region: str
    def __init__(self, sticky_region: _Optional[str] = ...) -> None: ...

class ActiveClusterExternalEntityConfig(_message.Message):
    __slots__ = ("external_entity_type", "external_entity_key")
    EXTERNAL_ENTITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ENTITY_KEY_FIELD_NUMBER: _ClassVar[int]
    external_entity_type: str
    external_entity_key: str
    def __init__(self, external_entity_type: _Optional[str] = ..., external_entity_key: _Optional[str] = ...) -> None: ...
