// Code generated by protoc-gen-gogo. DO NOT EDIT.
// source: uber/cadence/api/v1/query.proto

package apiv1

import (
	fmt "fmt"
	proto "github.com/gogo/protobuf/proto"
	io "io"
	math "math"
	math_bits "math/bits"
)

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.GoGoProtoPackageIsVersion3 // please upgrade the proto package

type QueryResultType int32

const (
	QueryResultType_QUERY_RESULT_TYPE_INVALID  QueryResultType = 0
	QueryResultType_QUERY_RESULT_TYPE_ANSWERED QueryResultType = 1
	QueryResultType_QUERY_RESULT_TYPE_FAILED   QueryResultType = 2
)

var QueryResultType_name = map[int32]string{
	0: "QUERY_RESULT_TYPE_INVALID",
	1: "QUERY_RESULT_TYPE_ANSWERED",
	2: "QUERY_RESULT_TYPE_FAILED",
}

var QueryResultType_value = map[string]int32{
	"QUERY_RESULT_TYPE_INVALID":  0,
	"QUERY_RESULT_TYPE_ANSWERED": 1,
	"QUERY_RESULT_TYPE_FAILED":   2,
}

func (x QueryResultType) String() string {
	return proto.EnumName(QueryResultType_name, int32(x))
}

func (QueryResultType) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_91769cfce21084c6, []int{0}
}

type QueryRejectCondition int32

const (
	QueryRejectCondition_QUERY_REJECT_CONDITION_INVALID QueryRejectCondition = 0
	// QUERY_REJECT_CONDITION_NOT_OPEN indicates that query should be rejected if workflow is not open.
	QueryRejectCondition_QUERY_REJECT_CONDITION_NOT_OPEN QueryRejectCondition = 1
	// QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY indicates that query should be rejected if workflow did not complete cleanly.
	QueryRejectCondition_QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY QueryRejectCondition = 2
)

var QueryRejectCondition_name = map[int32]string{
	0: "QUERY_REJECT_CONDITION_INVALID",
	1: "QUERY_REJECT_CONDITION_NOT_OPEN",
	2: "QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY",
}

var QueryRejectCondition_value = map[string]int32{
	"QUERY_REJECT_CONDITION_INVALID":               0,
	"QUERY_REJECT_CONDITION_NOT_OPEN":              1,
	"QUERY_REJECT_CONDITION_NOT_COMPLETED_CLEANLY": 2,
}

func (x QueryRejectCondition) String() string {
	return proto.EnumName(QueryRejectCondition_name, int32(x))
}

func (QueryRejectCondition) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_91769cfce21084c6, []int{1}
}

type QueryConsistencyLevel int32

const (
	QueryConsistencyLevel_QUERY_CONSISTENCY_LEVEL_INVALID QueryConsistencyLevel = 0
	// EVENTUAL indicates that query should be eventually consistent.
	QueryConsistencyLevel_QUERY_CONSISTENCY_LEVEL_EVENTUAL QueryConsistencyLevel = 1
	// STRONG indicates that any events that came before query should be reflected in workflow state before running query.
	QueryConsistencyLevel_QUERY_CONSISTENCY_LEVEL_STRONG QueryConsistencyLevel = 2
)

var QueryConsistencyLevel_name = map[int32]string{
	0: "QUERY_CONSISTENCY_LEVEL_INVALID",
	1: "QUERY_CONSISTENCY_LEVEL_EVENTUAL",
	2: "QUERY_CONSISTENCY_LEVEL_STRONG",
}

var QueryConsistencyLevel_value = map[string]int32{
	"QUERY_CONSISTENCY_LEVEL_INVALID":  0,
	"QUERY_CONSISTENCY_LEVEL_EVENTUAL": 1,
	"QUERY_CONSISTENCY_LEVEL_STRONG":   2,
}

func (x QueryConsistencyLevel) String() string {
	return proto.EnumName(QueryConsistencyLevel_name, int32(x))
}

func (QueryConsistencyLevel) EnumDescriptor() ([]byte, []int) {
	return fileDescriptor_91769cfce21084c6, []int{2}
}

type WorkflowQuery struct {
	QueryType            string   `protobuf:"bytes,1,opt,name=query_type,json=queryType,proto3" json:"query_type,omitempty"`
	QueryArgs            *Payload `protobuf:"bytes,2,opt,name=query_args,json=queryArgs,proto3" json:"query_args,omitempty"`
	XXX_NoUnkeyedLiteral struct{} `json:"-"`
	XXX_unrecognized     []byte   `json:"-"`
	XXX_sizecache        int32    `json:"-"`
}

func (m *WorkflowQuery) Reset()         { *m = WorkflowQuery{} }
func (m *WorkflowQuery) String() string { return proto.CompactTextString(m) }
func (*WorkflowQuery) ProtoMessage()    {}
func (*WorkflowQuery) Descriptor() ([]byte, []int) {
	return fileDescriptor_91769cfce21084c6, []int{0}
}
func (m *WorkflowQuery) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *WorkflowQuery) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_WorkflowQuery.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *WorkflowQuery) XXX_Merge(src proto.Message) {
	xxx_messageInfo_WorkflowQuery.Merge(m, src)
}
func (m *WorkflowQuery) XXX_Size() int {
	return m.Size()
}
func (m *WorkflowQuery) XXX_DiscardUnknown() {
	xxx_messageInfo_WorkflowQuery.DiscardUnknown(m)
}

var xxx_messageInfo_WorkflowQuery proto.InternalMessageInfo

func (m *WorkflowQuery) GetQueryType() string {
	if m != nil {
		return m.QueryType
	}
	return ""
}

func (m *WorkflowQuery) GetQueryArgs() *Payload {
	if m != nil {
		return m.QueryArgs
	}
	return nil
}

type WorkflowQueryResult struct {
	ResultType           QueryResultType `protobuf:"varint,1,opt,name=result_type,json=resultType,proto3,enum=uber.cadence.api.v1.QueryResultType" json:"result_type,omitempty"`
	Answer               *Payload        `protobuf:"bytes,2,opt,name=answer,proto3" json:"answer,omitempty"`
	ErrorMessage         string          `protobuf:"bytes,3,opt,name=error_message,json=errorMessage,proto3" json:"error_message,omitempty"`
	XXX_NoUnkeyedLiteral struct{}        `json:"-"`
	XXX_unrecognized     []byte          `json:"-"`
	XXX_sizecache        int32           `json:"-"`
}

func (m *WorkflowQueryResult) Reset()         { *m = WorkflowQueryResult{} }
func (m *WorkflowQueryResult) String() string { return proto.CompactTextString(m) }
func (*WorkflowQueryResult) ProtoMessage()    {}
func (*WorkflowQueryResult) Descriptor() ([]byte, []int) {
	return fileDescriptor_91769cfce21084c6, []int{1}
}
func (m *WorkflowQueryResult) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *WorkflowQueryResult) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_WorkflowQueryResult.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *WorkflowQueryResult) XXX_Merge(src proto.Message) {
	xxx_messageInfo_WorkflowQueryResult.Merge(m, src)
}
func (m *WorkflowQueryResult) XXX_Size() int {
	return m.Size()
}
func (m *WorkflowQueryResult) XXX_DiscardUnknown() {
	xxx_messageInfo_WorkflowQueryResult.DiscardUnknown(m)
}

var xxx_messageInfo_WorkflowQueryResult proto.InternalMessageInfo

func (m *WorkflowQueryResult) GetResultType() QueryResultType {
	if m != nil {
		return m.ResultType
	}
	return QueryResultType_QUERY_RESULT_TYPE_INVALID
}

func (m *WorkflowQueryResult) GetAnswer() *Payload {
	if m != nil {
		return m.Answer
	}
	return nil
}

func (m *WorkflowQueryResult) GetErrorMessage() string {
	if m != nil {
		return m.ErrorMessage
	}
	return ""
}

type QueryRejected struct {
	CloseStatus          WorkflowExecutionCloseStatus `protobuf:"varint,1,opt,name=close_status,json=closeStatus,proto3,enum=uber.cadence.api.v1.WorkflowExecutionCloseStatus" json:"close_status,omitempty"`
	XXX_NoUnkeyedLiteral struct{}                     `json:"-"`
	XXX_unrecognized     []byte                       `json:"-"`
	XXX_sizecache        int32                        `json:"-"`
}

func (m *QueryRejected) Reset()         { *m = QueryRejected{} }
func (m *QueryRejected) String() string { return proto.CompactTextString(m) }
func (*QueryRejected) ProtoMessage()    {}
func (*QueryRejected) Descriptor() ([]byte, []int) {
	return fileDescriptor_91769cfce21084c6, []int{2}
}
func (m *QueryRejected) XXX_Unmarshal(b []byte) error {
	return m.Unmarshal(b)
}
func (m *QueryRejected) XXX_Marshal(b []byte, deterministic bool) ([]byte, error) {
	if deterministic {
		return xxx_messageInfo_QueryRejected.Marshal(b, m, deterministic)
	} else {
		b = b[:cap(b)]
		n, err := m.MarshalToSizedBuffer(b)
		if err != nil {
			return nil, err
		}
		return b[:n], nil
	}
}
func (m *QueryRejected) XXX_Merge(src proto.Message) {
	xxx_messageInfo_QueryRejected.Merge(m, src)
}
func (m *QueryRejected) XXX_Size() int {
	return m.Size()
}
func (m *QueryRejected) XXX_DiscardUnknown() {
	xxx_messageInfo_QueryRejected.DiscardUnknown(m)
}

var xxx_messageInfo_QueryRejected proto.InternalMessageInfo

func (m *QueryRejected) GetCloseStatus() WorkflowExecutionCloseStatus {
	if m != nil {
		return m.CloseStatus
	}
	return WorkflowExecutionCloseStatus_WORKFLOW_EXECUTION_CLOSE_STATUS_INVALID
}

func init() {
	proto.RegisterEnum("uber.cadence.api.v1.QueryResultType", QueryResultType_name, QueryResultType_value)
	proto.RegisterEnum("uber.cadence.api.v1.QueryRejectCondition", QueryRejectCondition_name, QueryRejectCondition_value)
	proto.RegisterEnum("uber.cadence.api.v1.QueryConsistencyLevel", QueryConsistencyLevel_name, QueryConsistencyLevel_value)
	proto.RegisterType((*WorkflowQuery)(nil), "uber.cadence.api.v1.WorkflowQuery")
	proto.RegisterType((*WorkflowQueryResult)(nil), "uber.cadence.api.v1.WorkflowQueryResult")
	proto.RegisterType((*QueryRejected)(nil), "uber.cadence.api.v1.QueryRejected")
}

func init() { proto.RegisterFile("uber/cadence/api/v1/query.proto", fileDescriptor_91769cfce21084c6) }

var fileDescriptor_91769cfce21084c6 = []byte{
	// 549 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x02, 0xff, 0x8c, 0x53, 0xc1, 0x6e, 0xd3, 0x40,
	0x14, 0x64, 0x83, 0x54, 0xd1, 0x4d, 0x03, 0xd6, 0x16, 0x44, 0x88, 0xda, 0x34, 0x4a, 0x7b, 0xa8,
	0x22, 0x64, 0x93, 0xc2, 0xad, 0x27, 0xd7, 0x59, 0x90, 0x91, 0x6b, 0xbb, 0xb6, 0x93, 0x2a, 0x5c,
	0x2c, 0xc7, 0x59, 0x82, 0x69, 0xe2, 0x35, 0xbb, 0x76, 0x42, 0x7e, 0x80, 0x3b, 0x5f, 0xc3, 0x2f,
	0x70, 0xe4, 0x13, 0x50, 0xbe, 0x04, 0xd9, 0x71, 0x48, 0x4a, 0x5c, 0xd4, 0xdb, 0xf3, 0xbc, 0x19,
	0xcf, 0x8c, 0x56, 0x0f, 0x1e, 0x25, 0x03, 0xc2, 0x24, 0xdf, 0x1b, 0x92, 0xd0, 0x27, 0x92, 0x17,
	0x05, 0xd2, 0xb4, 0x2d, 0x7d, 0x49, 0x08, 0x9b, 0x8b, 0x11, 0xa3, 0x31, 0x45, 0xfb, 0x29, 0x41,
	0xcc, 0x09, 0xa2, 0x17, 0x05, 0xe2, 0xb4, 0x5d, 0x6b, 0x14, 0xa9, 0x7c, 0x3a, 0x99, 0xd0, 0x70,
	0x29, 0xab, 0x35, 0x8b, 0x18, 0x33, 0xca, 0x6e, 0x3e, 0x8e, 0xe9, 0x6c, 0xc9, 0x69, 0xde, 0xc0,
	0xca, 0x75, 0x8e, 0x5c, 0xa5, 0x8e, 0xe8, 0x10, 0xc2, 0xcc, 0xda, 0x8d, 0xe7, 0x11, 0xa9, 0x82,
	0x06, 0x38, 0xdd, 0xb5, 0x76, 0x33, 0xc4, 0x99, 0x47, 0x04, 0x9d, 0xaf, 0xd6, 0x1e, 0x1b, 0xf1,
	0x6a, 0xa9, 0x01, 0x4e, 0xcb, 0x67, 0x07, 0x62, 0x41, 0x3e, 0xd1, 0xf4, 0xe6, 0x63, 0xea, 0x0d,
	0x73, 0xb1, 0xcc, 0x46, 0xbc, 0xf9, 0x03, 0xc0, 0xfd, 0x5b, 0x6e, 0x16, 0xe1, 0xc9, 0x38, 0x46,
	0x18, 0x96, 0x59, 0x36, 0xad, 0x4d, 0x1f, 0x9f, 0x9d, 0x14, 0xfe, 0x75, 0x43, 0x96, 0xe6, 0xb1,
	0x20, 0xfb, 0x3b, 0xa3, 0x37, 0x70, 0xc7, 0x0b, 0xf9, 0x8c, 0xb0, 0x7b, 0xe5, 0xca, 0xb9, 0xe8,
	0x18, 0x56, 0x08, 0x63, 0x94, 0xb9, 0x13, 0xc2, 0xb9, 0x37, 0x22, 0xd5, 0x87, 0x59, 0xe7, 0xbd,
	0x0c, 0xbc, 0x5c, 0x62, 0x4d, 0x02, 0x2b, 0xb9, 0xf3, 0x67, 0xe2, 0xc7, 0x64, 0x88, 0x1c, 0xb8,
	0xe7, 0x8f, 0x29, 0x27, 0x2e, 0x8f, 0xbd, 0x38, 0xe1, 0x79, 0xe6, 0x76, 0xa1, 0xe3, 0xaa, 0x32,
	0xfe, 0x4a, 0xfc, 0x24, 0x0e, 0x68, 0xa8, 0xa4, 0x4a, 0x3b, 0x13, 0x5a, 0x65, 0x7f, 0xfd, 0xd1,
	0x0a, 0xe1, 0x93, 0x7f, 0x0a, 0xa2, 0x43, 0xf8, 0xe2, 0xaa, 0x8b, 0xad, 0xbe, 0x6b, 0x61, 0xbb,
	0xab, 0x39, 0xae, 0xd3, 0x37, 0xb1, 0xab, 0xea, 0x3d, 0x59, 0x53, 0x3b, 0xc2, 0x03, 0x54, 0x87,
	0xb5, 0xed, 0xb5, 0xac, 0xdb, 0xd7, 0xd8, 0xc2, 0x1d, 0x01, 0xa0, 0x03, 0x58, 0xdd, 0xde, 0xbf,
	0x95, 0x55, 0x0d, 0x77, 0x84, 0x52, 0xeb, 0x3b, 0x80, 0x4f, 0x37, 0x7a, 0x29, 0x34, 0x1c, 0x06,
	0x69, 0x40, 0xd4, 0x84, 0xf5, 0x95, 0xec, 0x3d, 0x56, 0x1c, 0x57, 0x31, 0xf4, 0x8e, 0xea, 0xa8,
	0x86, 0xbe, 0x61, 0x7d, 0x0c, 0x8f, 0xee, 0xe0, 0xe8, 0x86, 0xe3, 0x1a, 0x26, 0xd6, 0x05, 0x80,
	0x5e, 0xc1, 0x97, 0xff, 0x21, 0x29, 0xc6, 0xa5, 0xa9, 0x61, 0x07, 0x77, 0x5c, 0x45, 0xc3, 0xb2,
	0xae, 0xf5, 0x85, 0x52, 0xeb, 0x1b, 0x80, 0xcf, 0xb2, 0x4c, 0x0a, 0x0d, 0x79, 0xc0, 0x63, 0x12,
	0xfa, 0x73, 0x8d, 0x4c, 0xc9, 0x78, 0x6d, 0xa8, 0x18, 0xba, 0xad, 0xda, 0x0e, 0xd6, 0x95, 0xbe,
	0xab, 0xe1, 0x1e, 0xd6, 0x36, 0x52, 0x9d, 0xc0, 0xc6, 0x5d, 0x24, 0xdc, 0xc3, 0xba, 0xd3, 0x95,
	0x35, 0x01, 0xac, 0xfb, 0x6d, 0xb3, 0x6c, 0xc7, 0x32, 0xf4, 0x77, 0x42, 0xe9, 0x62, 0xf0, 0x73,
	0x51, 0x07, 0xbf, 0x16, 0x75, 0xf0, 0x7b, 0x51, 0x07, 0xf0, 0xb9, 0x4f, 0x27, 0x45, 0xaf, 0x7b,
	0xf1, 0x48, 0x8e, 0x02, 0x33, 0xbd, 0x25, 0x13, 0x7c, 0x90, 0x46, 0x41, 0xfc, 0x29, 0x19, 0x88,
	0x3e, 0x9d, 0x48, 0xb7, 0x8e, 0x4f, 0x1c, 0x91, 0x50, 0xca, 0x2e, 0x2e, 0xbf, 0xc3, 0x73, 0x2f,
	0x0a, 0xa6, 0xed, 0xc1, 0x4e, 0x86, 0xbd, 0xfe, 0x13, 0x00, 0x00, 0xff, 0xff, 0xa7, 0xde, 0x5a,
	0x02, 0x03, 0x04, 0x00, 0x00,
}

func (m *WorkflowQuery) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *WorkflowQuery) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *WorkflowQuery) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if m.XXX_unrecognized != nil {
		i -= len(m.XXX_unrecognized)
		copy(dAtA[i:], m.XXX_unrecognized)
	}
	if m.QueryArgs != nil {
		{
			size, err := m.QueryArgs.MarshalToSizedBuffer(dAtA[:i])
			if err != nil {
				return 0, err
			}
			i -= size
			i = encodeVarintQuery(dAtA, i, uint64(size))
		}
		i--
		dAtA[i] = 0x12
	}
	if len(m.QueryType) > 0 {
		i -= len(m.QueryType)
		copy(dAtA[i:], m.QueryType)
		i = encodeVarintQuery(dAtA, i, uint64(len(m.QueryType)))
		i--
		dAtA[i] = 0xa
	}
	return len(dAtA) - i, nil
}

func (m *WorkflowQueryResult) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *WorkflowQueryResult) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *WorkflowQueryResult) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if m.XXX_unrecognized != nil {
		i -= len(m.XXX_unrecognized)
		copy(dAtA[i:], m.XXX_unrecognized)
	}
	if len(m.ErrorMessage) > 0 {
		i -= len(m.ErrorMessage)
		copy(dAtA[i:], m.ErrorMessage)
		i = encodeVarintQuery(dAtA, i, uint64(len(m.ErrorMessage)))
		i--
		dAtA[i] = 0x1a
	}
	if m.Answer != nil {
		{
			size, err := m.Answer.MarshalToSizedBuffer(dAtA[:i])
			if err != nil {
				return 0, err
			}
			i -= size
			i = encodeVarintQuery(dAtA, i, uint64(size))
		}
		i--
		dAtA[i] = 0x12
	}
	if m.ResultType != 0 {
		i = encodeVarintQuery(dAtA, i, uint64(m.ResultType))
		i--
		dAtA[i] = 0x8
	}
	return len(dAtA) - i, nil
}

func (m *QueryRejected) Marshal() (dAtA []byte, err error) {
	size := m.Size()
	dAtA = make([]byte, size)
	n, err := m.MarshalToSizedBuffer(dAtA[:size])
	if err != nil {
		return nil, err
	}
	return dAtA[:n], nil
}

func (m *QueryRejected) MarshalTo(dAtA []byte) (int, error) {
	size := m.Size()
	return m.MarshalToSizedBuffer(dAtA[:size])
}

func (m *QueryRejected) MarshalToSizedBuffer(dAtA []byte) (int, error) {
	i := len(dAtA)
	_ = i
	var l int
	_ = l
	if m.XXX_unrecognized != nil {
		i -= len(m.XXX_unrecognized)
		copy(dAtA[i:], m.XXX_unrecognized)
	}
	if m.CloseStatus != 0 {
		i = encodeVarintQuery(dAtA, i, uint64(m.CloseStatus))
		i--
		dAtA[i] = 0x8
	}
	return len(dAtA) - i, nil
}

func encodeVarintQuery(dAtA []byte, offset int, v uint64) int {
	offset -= sovQuery(v)
	base := offset
	for v >= 1<<7 {
		dAtA[offset] = uint8(v&0x7f | 0x80)
		v >>= 7
		offset++
	}
	dAtA[offset] = uint8(v)
	return base
}
func (m *WorkflowQuery) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	l = len(m.QueryType)
	if l > 0 {
		n += 1 + l + sovQuery(uint64(l))
	}
	if m.QueryArgs != nil {
		l = m.QueryArgs.Size()
		n += 1 + l + sovQuery(uint64(l))
	}
	if m.XXX_unrecognized != nil {
		n += len(m.XXX_unrecognized)
	}
	return n
}

func (m *WorkflowQueryResult) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	if m.ResultType != 0 {
		n += 1 + sovQuery(uint64(m.ResultType))
	}
	if m.Answer != nil {
		l = m.Answer.Size()
		n += 1 + l + sovQuery(uint64(l))
	}
	l = len(m.ErrorMessage)
	if l > 0 {
		n += 1 + l + sovQuery(uint64(l))
	}
	if m.XXX_unrecognized != nil {
		n += len(m.XXX_unrecognized)
	}
	return n
}

func (m *QueryRejected) Size() (n int) {
	if m == nil {
		return 0
	}
	var l int
	_ = l
	if m.CloseStatus != 0 {
		n += 1 + sovQuery(uint64(m.CloseStatus))
	}
	if m.XXX_unrecognized != nil {
		n += len(m.XXX_unrecognized)
	}
	return n
}

func sovQuery(x uint64) (n int) {
	return (math_bits.Len64(x|1) + 6) / 7
}
func sozQuery(x uint64) (n int) {
	return sovQuery(uint64((x << 1) ^ uint64((int64(x) >> 63))))
}
func (m *WorkflowQuery) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowQuery
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: WorkflowQuery: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: WorkflowQuery: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		case 1:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field QueryType", wireType)
			}
			var stringLen uint64
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowQuery
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				stringLen |= uint64(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			intStringLen := int(stringLen)
			if intStringLen < 0 {
				return ErrInvalidLengthQuery
			}
			postIndex := iNdEx + intStringLen
			if postIndex < 0 {
				return ErrInvalidLengthQuery
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.QueryType = string(dAtA[iNdEx:postIndex])
			iNdEx = postIndex
		case 2:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field QueryArgs", wireType)
			}
			var msglen int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowQuery
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				msglen |= int(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if msglen < 0 {
				return ErrInvalidLengthQuery
			}
			postIndex := iNdEx + msglen
			if postIndex < 0 {
				return ErrInvalidLengthQuery
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			if m.QueryArgs == nil {
				m.QueryArgs = &Payload{}
			}
			if err := m.QueryArgs.Unmarshal(dAtA[iNdEx:postIndex]); err != nil {
				return err
			}
			iNdEx = postIndex
		default:
			iNdEx = preIndex
			skippy, err := skipQuery(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if (skippy < 0) || (iNdEx+skippy) < 0 {
				return ErrInvalidLengthQuery
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			m.XXX_unrecognized = append(m.XXX_unrecognized, dAtA[iNdEx:iNdEx+skippy]...)
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func (m *WorkflowQueryResult) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowQuery
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: WorkflowQueryResult: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: WorkflowQueryResult: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		case 1:
			if wireType != 0 {
				return fmt.Errorf("proto: wrong wireType = %d for field ResultType", wireType)
			}
			m.ResultType = 0
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowQuery
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				m.ResultType |= QueryResultType(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
		case 2:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field Answer", wireType)
			}
			var msglen int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowQuery
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				msglen |= int(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if msglen < 0 {
				return ErrInvalidLengthQuery
			}
			postIndex := iNdEx + msglen
			if postIndex < 0 {
				return ErrInvalidLengthQuery
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			if m.Answer == nil {
				m.Answer = &Payload{}
			}
			if err := m.Answer.Unmarshal(dAtA[iNdEx:postIndex]); err != nil {
				return err
			}
			iNdEx = postIndex
		case 3:
			if wireType != 2 {
				return fmt.Errorf("proto: wrong wireType = %d for field ErrorMessage", wireType)
			}
			var stringLen uint64
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowQuery
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				stringLen |= uint64(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			intStringLen := int(stringLen)
			if intStringLen < 0 {
				return ErrInvalidLengthQuery
			}
			postIndex := iNdEx + intStringLen
			if postIndex < 0 {
				return ErrInvalidLengthQuery
			}
			if postIndex > l {
				return io.ErrUnexpectedEOF
			}
			m.ErrorMessage = string(dAtA[iNdEx:postIndex])
			iNdEx = postIndex
		default:
			iNdEx = preIndex
			skippy, err := skipQuery(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if (skippy < 0) || (iNdEx+skippy) < 0 {
				return ErrInvalidLengthQuery
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			m.XXX_unrecognized = append(m.XXX_unrecognized, dAtA[iNdEx:iNdEx+skippy]...)
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func (m *QueryRejected) Unmarshal(dAtA []byte) error {
	l := len(dAtA)
	iNdEx := 0
	for iNdEx < l {
		preIndex := iNdEx
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return ErrIntOverflowQuery
			}
			if iNdEx >= l {
				return io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= uint64(b&0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		fieldNum := int32(wire >> 3)
		wireType := int(wire & 0x7)
		if wireType == 4 {
			return fmt.Errorf("proto: QueryRejected: wiretype end group for non-group")
		}
		if fieldNum <= 0 {
			return fmt.Errorf("proto: QueryRejected: illegal tag %d (wire type %d)", fieldNum, wire)
		}
		switch fieldNum {
		case 1:
			if wireType != 0 {
				return fmt.Errorf("proto: wrong wireType = %d for field CloseStatus", wireType)
			}
			m.CloseStatus = 0
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return ErrIntOverflowQuery
				}
				if iNdEx >= l {
					return io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				m.CloseStatus |= WorkflowExecutionCloseStatus(b&0x7F) << shift
				if b < 0x80 {
					break
				}
			}
		default:
			iNdEx = preIndex
			skippy, err := skipQuery(dAtA[iNdEx:])
			if err != nil {
				return err
			}
			if (skippy < 0) || (iNdEx+skippy) < 0 {
				return ErrInvalidLengthQuery
			}
			if (iNdEx + skippy) > l {
				return io.ErrUnexpectedEOF
			}
			m.XXX_unrecognized = append(m.XXX_unrecognized, dAtA[iNdEx:iNdEx+skippy]...)
			iNdEx += skippy
		}
	}

	if iNdEx > l {
		return io.ErrUnexpectedEOF
	}
	return nil
}
func skipQuery(dAtA []byte) (n int, err error) {
	l := len(dAtA)
	iNdEx := 0
	depth := 0
	for iNdEx < l {
		var wire uint64
		for shift := uint(0); ; shift += 7 {
			if shift >= 64 {
				return 0, ErrIntOverflowQuery
			}
			if iNdEx >= l {
				return 0, io.ErrUnexpectedEOF
			}
			b := dAtA[iNdEx]
			iNdEx++
			wire |= (uint64(b) & 0x7F) << shift
			if b < 0x80 {
				break
			}
		}
		wireType := int(wire & 0x7)
		switch wireType {
		case 0:
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return 0, ErrIntOverflowQuery
				}
				if iNdEx >= l {
					return 0, io.ErrUnexpectedEOF
				}
				iNdEx++
				if dAtA[iNdEx-1] < 0x80 {
					break
				}
			}
		case 1:
			iNdEx += 8
		case 2:
			var length int
			for shift := uint(0); ; shift += 7 {
				if shift >= 64 {
					return 0, ErrIntOverflowQuery
				}
				if iNdEx >= l {
					return 0, io.ErrUnexpectedEOF
				}
				b := dAtA[iNdEx]
				iNdEx++
				length |= (int(b) & 0x7F) << shift
				if b < 0x80 {
					break
				}
			}
			if length < 0 {
				return 0, ErrInvalidLengthQuery
			}
			iNdEx += length
		case 3:
			depth++
		case 4:
			if depth == 0 {
				return 0, ErrUnexpectedEndOfGroupQuery
			}
			depth--
		case 5:
			iNdEx += 4
		default:
			return 0, fmt.Errorf("proto: illegal wireType %d", wireType)
		}
		if iNdEx < 0 {
			return 0, ErrInvalidLengthQuery
		}
		if depth == 0 {
			return iNdEx, nil
		}
	}
	return 0, io.ErrUnexpectedEOF
}

var (
	ErrInvalidLengthQuery        = fmt.Errorf("proto: negative length found during unmarshaling")
	ErrIntOverflowQuery          = fmt.Errorf("proto: integer overflow")
	ErrUnexpectedEndOfGroupQuery = fmt.Errorf("proto: unexpected end of group")
)
