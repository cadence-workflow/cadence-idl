// Copyright (c) 2017 Uber Technologies, Inc.
//
// Permission is hereby granted, free of charge, to any person obtaining a copy
// of this software and associated documentation files (the "Software"), to deal
// in the Software without restriction, including without limitation the rights
// to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
// copies of the Software, and to permit persons to whom the Software is
// furnished to do so, subject to the following conditions:
//
// The above copyright notice and this permission notice shall be included in
// all copies or substantial portions of the Software.
//
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
// AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
// LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
// OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
// THE SOFTWARE.

namespace java com.uber.cadence.admin

include "shared.thrift"
include "replicator.thrift"
include "config.thrift"

/**
* AdminService provides advanced APIs for debugging and analysis with admin privilege
**/
service AdminService {
  /**
  * DescribeWorkflowExecution returns information about the internal states of workflow execution.
  **/
  DescribeWorkflowExecutionResponse DescribeWorkflowExecution(1: DescribeWorkflowExecutionRequest request)
    throws (
      1: shared.BadRequestError         badRequestError,
      2: shared.InternalServiceError    internalServiceError,
      3: shared.EntityNotExistsError    entityNotExistError,
      4: shared.AccessDeniedError       accessDeniedError,
    )

  /**
  * DescribeShardDistribution returns information about history shards within the cluster
  **/
  shared.DescribeShardDistributionResponse DescribeShardDistribution(1: shared.DescribeShardDistributionRequest request)
    throws (
      1: shared.InternalServiceError internalServiceError,
    )

  /**
  * DescribeHistoryHost returns information about the internal states of a history host
  **/
  shared.DescribeHistoryHostResponse DescribeHistoryHost(1: shared.DescribeHistoryHostRequest request)
    throws (
      1: shared.BadRequestError       badRequestError,
      2: shared.InternalServiceError  internalServiceError,
      3: shared.AccessDeniedError     accessDeniedError,
    )

  void CloseShard(1: shared.CloseShardRequest request)
    throws (
      1: shared.BadRequestError       badRequestError,
      2: shared.InternalServiceError  internalServiceError,
      3: shared.AccessDeniedError     accessDeniedError,
    )

  void RemoveTask(1: shared.RemoveTaskRequest request)
    throws (
      1: shared.BadRequestError       badRequestError,
      2: shared.InternalServiceError  internalServiceError,
      3: shared.AccessDeniedError     accessDeniedError,
    )

  void ResetQueue(1: shared.ResetQueueRequest request)
    throws (
      1: shared.BadRequestError       badRequestError,
      2: shared.InternalServiceError  internalServiceError,
      3: shared.AccessDeniedError     accessDeniedError,
    )

  shared.DescribeQueueResponse DescribeQueue(1: shared.DescribeQueueRequest request)
    throws (
      1: shared.BadRequestError       badRequestError,
      2: shared.InternalServiceError  internalServiceError,
      3: shared.AccessDeniedError     accessDeniedError,
    )

  /**
  * Returns the raw history of specified workflow execution.  It fails with 'EntityNotExistError' if speficied workflow
  * execution in unknown to the service.
  * StartEventId defines the beginning of the event to fetch. The first event is inclusive.
  * EndEventId and EndEventVersion defines the end of the event to fetch. The end event is exclusive.
  **/
  GetWorkflowExecutionRawHistoryV2Response GetWorkflowExecutionRawHistoryV2(1: GetWorkflowExecutionRawHistoryV2Request getRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ServiceBusyError serviceBusyError,
    )

  replicator.GetReplicationMessagesResponse GetReplicationMessages(1: replicator.GetReplicationMessagesRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.LimitExceededError limitExceededError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
    )

  replicator.GetDomainReplicationMessagesResponse GetDomainReplicationMessages(1: replicator.GetDomainReplicationMessagesRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.LimitExceededError limitExceededError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
    )

  replicator.GetDLQReplicationMessagesResponse GetDLQReplicationMessages(1: replicator.GetDLQReplicationMessagesRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.ServiceBusyError serviceBusyError,
    )

  /**
  * ReapplyEvents applies stale events to the current workflow and current run
  **/
  void ReapplyEvents(1: shared.ReapplyEventsRequest reapplyEventsRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.DomainNotActiveError domainNotActiveError,
      4: shared.LimitExceededError limitExceededError,
      5: shared.ServiceBusyError serviceBusyError,
      6: shared.EntityNotExistsError entityNotExistError,
    )

  /**
  * AddSearchAttribute whitelist search attribute in request.
  **/
  void AddSearchAttribute(1: AddSearchAttributeRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.ServiceBusyError serviceBusyError,
    )

  /**
  * DescribeCluster returns information about cadence cluster
  **/
  DescribeClusterResponse DescribeCluster()
    throws (
      1: shared.InternalServiceError internalServiceError,
      2: shared.ServiceBusyError serviceBusyError,
    )

  /**
  * ReadDLQMessages returns messages from DLQ
  **/
  replicator.ReadDLQMessagesResponse ReadDLQMessages(1: replicator.ReadDLQMessagesRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.ServiceBusyError serviceBusyError,
      4: shared.EntityNotExistsError entityNotExistError,
    )

  /**
  * PurgeDLQMessages purges messages from DLQ
  **/
  void PurgeDLQMessages(1: replicator.PurgeDLQMessagesRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.ServiceBusyError serviceBusyError,
      4: shared.EntityNotExistsError entityNotExistError,
    )

  /**
  * MergeDLQMessages merges messages from DLQ
  **/
  replicator.MergeDLQMessagesResponse MergeDLQMessages(1: replicator.MergeDLQMessagesRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.ServiceBusyError serviceBusyError,
      4: shared.EntityNotExistsError entityNotExistError,
    )

  /**
  * RefreshWorkflowTasks refreshes all tasks of a workflow
  **/
  void RefreshWorkflowTasks(1: shared.RefreshWorkflowTasksRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.DomainNotActiveError domainNotActiveError,
      3: shared.ServiceBusyError serviceBusyError,
      4: shared.EntityNotExistsError entityNotExistError,
    )

  /**
  * ResendReplicationTasks requests replication tasks from remote cluster and apply tasks to current cluster
  **/
  void ResendReplicationTasks(1: ResendReplicationTasksRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.ServiceBusyError serviceBusyError,
      3: shared.EntityNotExistsError entityNotExistError,
    )

  /**
  * GetCrossClusterTasks fetches cross cluster tasks
  **/
  shared.GetCrossClusterTasksResponse GetCrossClusterTasks(1: shared.GetCrossClusterTasksRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.ServiceBusyError serviceBusyError,
    )

  /**
  * RespondCrossClusterTasksCompleted responds the result of processing cross cluster tasks
  **/
  shared.RespondCrossClusterTasksCompletedResponse RespondCrossClusterTasksCompleted(1: shared.RespondCrossClusterTasksCompletedRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.ServiceBusyError serviceBusyError,
    )

  /**
  * GetDynamicConfig returns values associated with a specified dynamic config parameter.
  **/
  GetDynamicConfigResponse GetDynamicConfig(1: GetDynamicConfigRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
    )

  void UpdateDynamicConfig(1: UpdateDynamicConfigRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
    )

  void RestoreDynamicConfig(1: RestoreDynamicConfigRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
    )

  ListDynamicConfigResponse ListDynamicConfig(1: ListDynamicConfigRequest request)
    throws (
      1: shared.InternalServiceError internalServiceError,
    )

  GetOperationalDynamicConfigResponse GetOperationalDynamicConfig(1: GetOperationalDynamicConfigRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
    )

  void UpdateOperationalDynamicConfig(1: UpdateOperationalDynamicConfigRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
    )

  void RestoreOperationalDynamicConfig(1: RestoreOperationalDynamicConfigRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
    )

  ListOperationalDynamicConfigResponse ListOperationalDynamicConfig(1: ListOperationalDynamicConfigRequest request)
    throws (
      1: shared.InternalServiceError internalServiceError,
    )

  AdminDeleteWorkflowResponse DeleteWorkflow(1: AdminDeleteWorkflowRequest request)
    throws (
      1: shared.BadRequestError         badRequestError,
      2: shared.EntityNotExistsError    entityNotExistError,
      3: shared.InternalServiceError    internalServiceError,
    )

  AdminMaintainWorkflowResponse MaintainCorruptWorkflow(1: AdminMaintainWorkflowRequest request)
    throws (
      1: shared.BadRequestError         badRequestError,
      2: shared.EntityNotExistsError    entityNotExistError,
      3: shared.InternalServiceError    internalServiceError,
    )

  GetGlobalIsolationGroupsResponse GetGlobalIsolationGroups(1: GetGlobalIsolationGroupsRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
    )

  UpdateGlobalIsolationGroupsResponse UpdateGlobalIsolationGroups(1: UpdateGlobalIsolationGroupsRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
    )

  GetDomainIsolationGroupsResponse GetDomainIsolationGroups(1: GetDomainIsolationGroupsRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
    )

  UpdateDomainIsolationGroupsResponse UpdateDomainIsolationGroups(1: UpdateDomainIsolationGroupsRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
    )


  GetDomainAsyncWorkflowConfiguratonResponse GetDomainAsyncWorkflowConfiguraton(1: GetDomainAsyncWorkflowConfiguratonRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
    )

  UpdateDomainAsyncWorkflowConfiguratonResponse UpdateDomainAsyncWorkflowConfiguraton(1: UpdateDomainAsyncWorkflowConfiguratonRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
    )
}

struct DescribeWorkflowExecutionRequest {
  10: optional string                       domain
  20: optional shared.WorkflowExecution     execution
}

struct DescribeWorkflowExecutionResponse {
  10: optional string shardId
  20: optional string historyAddr
  40: optional string mutableStateInCache
  50: optional string mutableStateInDatabase
}

/**
  * StartEventId defines the beginning of the event to fetch. The first event is exclusive.
  * EndEventId and EndEventVersion defines the end of the event to fetch. The end event is exclusive.
  **/
struct GetWorkflowExecutionRawHistoryV2Request {
  10: optional string domain
  20: optional shared.WorkflowExecution execution
  30: optional i64 (js.type = "Long") startEventId
  40: optional i64 (js.type = "Long") startEventVersion
  50: optional i64 (js.type = "Long") endEventId
  60: optional i64 (js.type = "Long") endEventVersion
  70: optional i32 maximumPageSize
  80: optional binary nextPageToken
}

struct GetWorkflowExecutionRawHistoryV2Response {
  10: optional binary nextPageToken
  20: optional list<shared.DataBlob> historyBatches
  30: optional shared.VersionHistory versionHistory
}

struct AddSearchAttributeRequest {
  10: optional map<string, shared.IndexedValueType> searchAttribute
  20: optional string securityToken
}

struct HostInfo {
  10: optional string Identity
}

struct RingInfo {
  10: optional string role
  20: optional i32 memberCount
  30: optional list<HostInfo> members
}

struct MembershipInfo {
  10: optional HostInfo currentHost
  20: optional list<string> reachableMembers
  30: optional list<RingInfo> rings
}

struct PersistenceSetting {
  10: optional string key
  20: optional string value
}

struct PersistenceFeature {
  10: optional string key
  20: optional bool enabled
}

struct PersistenceInfo {
  10: optional string backend
  20: optional list<PersistenceSetting> settings
  30: optional list<PersistenceFeature> features
}

struct DescribeClusterResponse {
  10: optional shared.SupportedClientVersions supportedClientVersions
  20: optional MembershipInfo membershipInfo
  30: optional map<string,PersistenceInfo> persistenceInfo
}

struct ResendReplicationTasksRequest {
  10: optional string domainID
  20: optional string workflowID
  30: optional string runID
  40: optional string remoteCluster
  50: optional i64 (js.type = "Long") startEventID
  60: optional i64 (js.type = "Long") startVersion
  70: optional i64 (js.type = "Long") endEventID
  80: optional i64 (js.type = "Long") endVersion
}

struct GetDynamicConfigRequest {
  10: optional string configName
  20: optional list<config.DynamicConfigFilter> filters
}

struct GetDynamicConfigResponse {
  10: optional shared.DataBlob value
}

struct UpdateDynamicConfigRequest {
  10: optional string configName
  20: optional list<config.DynamicConfigValue> configValues
}

struct RestoreDynamicConfigRequest {
  10: optional string configName
  20: optional list<config.DynamicConfigFilter> filters
}

struct AdminDeleteWorkflowRequest {
  10: optional string                       domain
  20: optional shared.WorkflowExecution     execution
}

struct AdminDeleteWorkflowResponse {
  10: optional bool historyDeleted
  20: optional bool executionsDeleted
  30: optional bool visibilityDeleted
}

struct AdminMaintainWorkflowRequest {
  10: optional string                       domain
  20: optional shared.WorkflowExecution     execution
}

struct AdminMaintainWorkflowResponse {
  10: optional bool historyDeleted
  20: optional bool executionsDeleted
  30: optional bool visibilityDeleted
}

//Eventually remove configName and integrate this functionality into Get.
//GetDynamicConfigResponse would need to change as well.
struct ListDynamicConfigRequest {
  10: optional string configName
}

struct ListDynamicConfigResponse {
  10: optional list<config.DynamicConfigEntry> entries
}

struct GetOperationalDynamicConfigRequest {
  10: optional string configName
  20: optional list<config.DynamicConfigFilter> filters
}

struct GetOperationalDynamicConfigResponse {
  10: optional shared.DataBlob value
}

struct UpdateOperationalDynamicConfigRequest {
  10: optional string configName
  20: optional list<config.DynamicConfigValue> configValues
}

struct RestoreOperationalDynamicConfigRequest {
  10: optional string configName
  20: optional list<config.DynamicConfigFilter> filters
}

struct ListOperationalDynamicConfigRequest {
  10: optional string configName
}

struct ListOperationalDynamicConfigResponse {
  10: optional list<config.DynamicConfigEntry> entries
}

// global
struct GetGlobalIsolationGroupsRequest{}

struct GetGlobalIsolationGroupsResponse{
    10: optional shared.IsolationGroupConfiguration isolationGroups
}

struct UpdateGlobalIsolationGroupsRequest{
    10: optional shared.IsolationGroupConfiguration isolationGroups
}

struct UpdateGlobalIsolationGroupsResponse{}


// For domains
struct GetDomainIsolationGroupsRequest{
    10: optional string domain
}

struct GetDomainIsolationGroupsResponse{
    10: optional shared.IsolationGroupConfiguration isolationGroups
}

struct UpdateDomainIsolationGroupsRequest{
    10: optional string domain
    20: optional shared.IsolationGroupConfiguration isolationGroups
}

struct UpdateDomainIsolationGroupsResponse{}

// Async workflow configuration request/response payloads
struct GetDomainAsyncWorkflowConfiguratonRequest {
    10: optional string domain
}

struct GetDomainAsyncWorkflowConfiguratonResponse {
    10: optional shared.AsyncWorkflowConfiguration configuration
}

struct UpdateDomainAsyncWorkflowConfiguratonRequest {
    10: optional string domain
    20: optional shared.AsyncWorkflowConfiguration configuration
}

struct UpdateDomainAsyncWorkflowConfiguratonResponse {}
