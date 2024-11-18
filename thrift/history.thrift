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

include "shared.thrift"
include "replicator.thrift"

namespace java com.uber.cadence.history

exception EventAlreadyStartedError {
  1: required string message
}

exception ShardOwnershipLostError {
  10: optional string message
  20: optional string owner
}

struct ParentExecutionInfo {
  10: optional string domainUUID
  15: optional string domain
  20: optional shared.WorkflowExecution execution
  30: optional i64 (js.type = "Long") initiatedId
}

struct StartWorkflowExecutionRequest {
  10: optional string domainUUID
  20: optional shared.StartWorkflowExecutionRequest startRequest
  30: optional ParentExecutionInfo parentExecutionInfo
  40: optional i32 attempt
  50: optional i64 (js.type = "Long") expirationTimestamp
  55: optional shared.ContinueAsNewInitiator continueAsNewInitiator
  56: optional string continuedFailureReason
  57: optional binary continuedFailureDetails
  58: optional binary lastCompletionResult
  60: optional i32 firstDecisionTaskBackoffSeconds
  62: optional map<string, string> partitionConfig
}

struct DescribeMutableStateRequest{
  10: optional string domainUUID
  20: optional shared.WorkflowExecution execution
}

struct DescribeMutableStateResponse{
  30: optional string mutableStateInCache
  40: optional string mutableStateInDatabase
}

struct GetMutableStateRequest {
  10: optional string domainUUID
  20: optional shared.WorkflowExecution execution
  30: optional i64 (js.type = "Long") expectedNextEventId
  40: optional binary currentBranchToken
  50: optional shared.VersionHistoryItem versionHistoryItem
}

struct GetMutableStateResponse {
  10: optional shared.WorkflowExecution execution
  20: optional shared.WorkflowType workflowType
  30: optional i64 (js.type = "Long") NextEventId
  35: optional i64 (js.type = "Long") PreviousStartedEventId
  40: optional i64 (js.type = "Long") LastFirstEventId
  50: optional shared.TaskList taskList
  60: optional shared.TaskList stickyTaskList
  70: optional string clientLibraryVersion
  80: optional string clientFeatureVersion
  90: optional string clientImpl
  //TODO: isWorkflowRunning is deprecating. workflowState is going replace this field
  100: optional bool isWorkflowRunning
  110: optional i32 stickyTaskListScheduleToStartTimeout
  120: optional i32 eventStoreVersion
  130: optional binary currentBranchToken
  // TODO: when migrating to gRPC, make this a enum
  // TODO: when migrating to gRPC, unify internal & external representation
  // NOTE: workflowState & workflowCloseState are the same as persistence representation
  150: optional i32 workflowState
  160: optional i32 workflowCloseState
  170: optional shared.VersionHistories versionHistories
  180: optional bool isStickyTaskListEnabled
  190: optional i64 (js.type = "Long") historySize
  200: optional shared.VersionHistoryItem versionHistoryItem
}

struct PollMutableStateRequest {
  10: optional string domainUUID
  20: optional shared.WorkflowExecution execution
  30: optional i64 (js.type = "Long") expectedNextEventId
  40: optional binary currentBranchToken
}

struct PollMutableStateResponse {
  10: optional shared.WorkflowExecution execution
  20: optional shared.WorkflowType workflowType
  30: optional i64 (js.type = "Long") NextEventId
  35: optional i64 (js.type = "Long") PreviousStartedEventId
  40: optional i64 (js.type = "Long") LastFirstEventId
  50: optional shared.TaskList taskList
  60: optional shared.TaskList stickyTaskList
  70: optional string clientLibraryVersion
  80: optional string clientFeatureVersion
  90: optional string clientImpl
  100: optional i32 stickyTaskListScheduleToStartTimeout
  110: optional binary currentBranchToken
  130: optional shared.VersionHistories versionHistories
  // TODO: when migrating to gRPC, make this a enum
  // TODO: when migrating to gRPC, unify internal & external representation
  // NOTE: workflowState & workflowCloseState are the same as persistence representation
  140: optional i32 workflowState
  150: optional i32 workflowCloseState
}

struct ResetStickyTaskListRequest {
  10: optional string domainUUID
  20: optional shared.WorkflowExecution execution
}

struct ResetStickyTaskListResponse {
  // The reason to keep this response is to allow returning
  // information in the future.
}

struct RespondDecisionTaskCompletedRequest {
  10: optional string domainUUID
  20: optional shared.RespondDecisionTaskCompletedRequest completeRequest
}

struct RespondDecisionTaskCompletedResponse {
  10: optional RecordDecisionTaskStartedResponse startedResponse
  20: optional map<string,shared.ActivityLocalDispatchInfo> activitiesToDispatchLocally
}

struct RespondDecisionTaskFailedRequest {
  10: optional string domainUUID
  20: optional shared.RespondDecisionTaskFailedRequest failedRequest
}

struct RecordActivityTaskHeartbeatRequest {
  10: optional string domainUUID
  20: optional shared.RecordActivityTaskHeartbeatRequest heartbeatRequest
}

struct RespondActivityTaskCompletedRequest {
  10: optional string domainUUID
  20: optional shared.RespondActivityTaskCompletedRequest completeRequest
}

struct RespondActivityTaskFailedRequest {
  10: optional string domainUUID
  20: optional shared.RespondActivityTaskFailedRequest failedRequest
}

struct RespondActivityTaskCanceledRequest {
  10: optional string domainUUID
  20: optional shared.RespondActivityTaskCanceledRequest cancelRequest
}

struct RefreshWorkflowTasksRequest {
  10: optional string domainUIID
  20: optional shared.RefreshWorkflowTasksRequest request
}

struct RecordActivityTaskStartedRequest {
  10: optional string domainUUID
  20: optional shared.WorkflowExecution workflowExecution
  30: optional i64 (js.type = "Long") scheduleId
  40: optional i64 (js.type = "Long") taskId
  45: optional string requestId // Unique id of each poll request. Used to ensure at most once delivery of tasks.
  50: optional shared.PollForActivityTaskRequest pollRequest
}

struct RecordActivityTaskStartedResponse {
  20: optional shared.HistoryEvent scheduledEvent
  30: optional i64 (js.type = "Long") startedTimestamp
  40: optional i64 (js.type = "Long") attempt
  50: optional i64 (js.type = "Long") scheduledTimestampOfThisAttempt
  60: optional binary heartbeatDetails
  70: optional shared.WorkflowType workflowType
  80: optional string workflowDomain
}

struct RecordDecisionTaskStartedRequest {
  10: optional string domainUUID
  20: optional shared.WorkflowExecution workflowExecution
  30: optional i64 (js.type = "Long") scheduleId
  40: optional i64 (js.type = "Long") taskId
  45: optional string requestId // Unique id of each poll request. Used to ensure at most once delivery of tasks.
  50: optional shared.PollForDecisionTaskRequest pollRequest
}

struct RecordDecisionTaskStartedResponse {
  10: optional shared.WorkflowType workflowType
  20: optional i64 (js.type = "Long") previousStartedEventId
  30: optional i64 (js.type = "Long") scheduledEventId
  40: optional i64 (js.type = "Long") startedEventId
  50: optional i64 (js.type = "Long") nextEventId
  60: optional i64 (js.type = "Long") attempt
  70: optional bool stickyExecutionEnabled
  80: optional shared.TransientDecisionInfo decisionInfo
  90: optional shared.TaskList WorkflowExecutionTaskList
  100: optional i32 eventStoreVersion
  110: optional binary branchToken
  120: optional i64 (js.type = "Long") scheduledTimestamp
  130: optional i64 (js.type = "Long") startedTimestamp
  140: optional map<string, shared.WorkflowQuery> queries
  150: optional i64 (js.type = "Long") historySize
}

struct SignalWorkflowExecutionRequest {
  10: optional string domainUUID
  20: optional shared.SignalWorkflowExecutionRequest signalRequest
  // workflow execution that requests this signal, for making sure
  // the workflow being signaled is actually a child of the workflow
  // making the request
  30: optional shared.WorkflowExecution externalWorkflowExecution
  40: optional bool childWorkflowOnly
}

struct SignalWithStartWorkflowExecutionRequest {
  10: optional string domainUUID
  20: optional shared.SignalWithStartWorkflowExecutionRequest signalWithStartRequest
  30: optional map<string, string> partitionConfig
}

struct RemoveSignalMutableStateRequest {
  10: optional string domainUUID
  20: optional shared.WorkflowExecution workflowExecution
  30: optional string requestId
}

struct TerminateWorkflowExecutionRequest {
  10: optional string domainUUID
  20: optional shared.TerminateWorkflowExecutionRequest terminateRequest
  // workflow execution that requests this termination, for making sure
  // the workflow being terminated is actually a child of the workflow
  // making the request
  30: optional shared.WorkflowExecution externalWorkflowExecution
  40: optional bool childWorkflowOnly
}

struct ResetWorkflowExecutionRequest {
  10: optional string domainUUID
  20: optional shared.ResetWorkflowExecutionRequest resetRequest
}

struct RequestCancelWorkflowExecutionRequest {
  10: optional string domainUUID
  20: optional shared.RequestCancelWorkflowExecutionRequest cancelRequest
  // workflow execution that requests this cancellation, for making sure
  // the workflow being cancelled is actually a child of the workflow
  // making the request
  30: optional i64 (js.type = "Long") externalInitiatedEventId
  40: optional shared.WorkflowExecution externalWorkflowExecution
  50: optional bool childWorkflowOnly
}

struct ScheduleDecisionTaskRequest {
  10: optional string domainUUID
  20: optional shared.WorkflowExecution workflowExecution
  30: optional bool isFirstDecision
}

struct DescribeWorkflowExecutionRequest {
  10: optional string domainUUID
  20: optional shared.DescribeWorkflowExecutionRequest request
}

/**
* RecordChildExecutionCompletedRequest is used for reporting the completion of child execution to parent workflow
* execution which started it.  When a child execution is completed it creates this request and calls the
* RecordChildExecutionCompleted API with the workflowExecution of parent.  It also sets the completedExecution of the
* child as it could potentially be different than the ChildExecutionStartedEvent of parent in the situation when
* child creates multiple runs through ContinueAsNew before finally completing.
**/
struct RecordChildExecutionCompletedRequest {
  10: optional string domainUUID
  20: optional shared.WorkflowExecution workflowExecution
  30: optional i64 (js.type = "Long") initiatedId
  40: optional shared.WorkflowExecution completedExecution
  50: optional shared.HistoryEvent completionEvent
  60: optional i64 (js.type = "Long") startedId
}

struct ReplicateEventsV2Request {
  10: optional string domainUUID
  20: optional shared.WorkflowExecution workflowExecution
  30: optional list<shared.VersionHistoryItem> versionHistoryItems
  40: optional shared.DataBlob events
  // new run events does not need version history since there is no prior events
  60: optional shared.DataBlob newRunEvents
}

struct SyncShardStatusRequest {
  10: optional string sourceCluster
  20: optional i64 (js.type = "Long") shardId
  30: optional i64 (js.type = "Long") timestamp
}

struct SyncActivityRequest {
  10: optional string domainId
  20: optional string workflowId
  30: optional string runId
  40: optional i64 (js.type = "Long") version
  50: optional i64 (js.type = "Long") scheduledId
  60: optional i64 (js.type = "Long") scheduledTime
  70: optional i64 (js.type = "Long") startedId
  80: optional i64 (js.type = "Long") startedTime
  90: optional i64 (js.type = "Long") lastHeartbeatTime
  100: optional binary details
  110: optional i32 attempt
  120: optional string lastFailureReason
  130: optional string lastWorkerIdentity
  140: optional binary lastFailureDetails
  150: optional shared.VersionHistory versionHistory
}

struct QueryWorkflowRequest {
  10: optional string domainUUID
  20: optional shared.QueryWorkflowRequest request
}

struct QueryWorkflowResponse {
  10: optional shared.QueryWorkflowResponse response
}

struct ReapplyEventsRequest {
  10: optional string domainUUID
  20: optional shared.ReapplyEventsRequest request
}

struct FailoverMarkerToken {
  10: optional list<i32> shardIDs
  20: optional replicator.FailoverMarkerAttributes failoverMarker
}

struct NotifyFailoverMarkersRequest {
  10: optional list<FailoverMarkerToken> failoverMarkerTokens
}

struct ProcessingQueueStates {
  10: optional map<string, list<ProcessingQueueState>> statesByCluster
}

struct ProcessingQueueState {
  10: optional i32 level
  20: optional i64 ackLevel
  30: optional i64 maxLevel
  40: optional DomainFilter domainFilter
}

struct DomainFilter {
  10: optional list<string> domainIDs
  20: optional bool reverseMatch
}

struct GetFailoverInfoRequest {
  10: optional string domainID
}

struct GetFailoverInfoResponse {
  10: optional i32 completedShardCount
  20: optional list<i32> pendingShards
}

struct RatelimitUpdateRequest {
  /**
  * impl-specific data.
  *
  * likely some simple top-level keys and then either:
  *   - map<ratelimit-key-string, something>
  *   - list<something>
  *
  * this is a single blob rather than a collection to save on
  * repeated serialization of the type name, and to allow impls
  * to choose whatever structures are most-convenient for them.
  */
  10: optional shared.Any data
}

struct RatelimitUpdateResponse {
  /**
  * impl-specific data.
  *
  * likely some simple top-level keys and then either:
  *   - map<ratelimit-key-string, something>
  *   - list<something>
  *
  * this is a single blob rather than a collection to save on
  * repeated serialization of the type name, and to allow impls
  * to choose whatever structures are most-convenient for them.
  */
  10: optional shared.Any data
}

/**
* first impl of ratelimiting data, collected by limiters and sent to aggregators.
*
* used in an Any with ValueType: WeightedRatelimitUsageAnyType
*/
struct WeightedRatelimitUsage {
  /** unique, stable identifier of the calling host, to identify future data from the same host */
  10: required string caller
  /** milliseconds since last update call.  expected to be on the order of a few seconds or less. */
  20: required i32 elapsedMS
  /** per key, number of allowed vs rejected calls since last update. */
  30: required map<string, WeightedRatelimitCalls> calls
}

/** Any{ValueType} identifier for WeightedRatelimitUsage data */
const string WeightedRatelimitUsageAnyType = "cadence:loadbalanced:update_request"

/** fields are required to encourage compact serialization, zeros are expected */
struct WeightedRatelimitCalls {
  /**
  * number of allowed requests since last call.
  * assumed to be <1m or so, saturates at MAX_INT32.
  */
  10: required i32 allowed
  /**
  * number of rejected requests since last call.
  * assumed to be <1m or so, saturates at MAX_INT32.
  */
  20: required i32 rejected
}

/**
* first impl of ratelimiting data, result from aggregator to limiter.
*
* used in an Any with ValueType: WeightedRatelimitQuotasAnyType
*/
struct WeightedRatelimitQuotas {
  /** RPS-weights to allow per key */
  10: required map<string,double> quotas
}

/** Any{ValueType} identifier for WeightedRatelimitQuotas data */
const string WeightedRatelimitQuotasAnyType = "cadence:loadbalanced:update_response"

/**
* second impl, includes unused-RPS data so limiters can decide if they
* want to allow exceeding limits when there is free space.
*
* used in an Any with ValueType: WeightedRatelimitUsageQuotasAnyType
*/
struct WeightedRatelimitUsageQuotas {
  /** RPS weights and total usage per key */
  10: required map<string,WeightedRatelimitUsageQuotaEntry> quotas
}

struct WeightedRatelimitUsageQuotaEntry {
  /** Amount of the quota that the receiving host can use, between 0 and 1 */
  10: required double weight
  /** RPS estimated across the whole cluster */
  20: required double used
}

const string WeightedRatelimitUsageQuotasAnyType = "cadence:loadbalanced:update_response_used"

/**
* HistoryService provides API to start a new long running workflow instance, as well as query and update the history
* of workflow instances already created.
**/
service HistoryService {
  /**
  * StartWorkflowExecution starts a new long running workflow instance.  It will create the instance with
  * 'WorkflowExecutionStarted' event in history and also schedule the first DecisionTask for the worker to make the
  * first decision for this instance.  It will return 'WorkflowExecutionAlreadyStartedError', if an instance already
  * exists with same workflowId.
  **/
  shared.StartWorkflowExecutionResponse StartWorkflowExecution(1: StartWorkflowExecutionRequest startRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.WorkflowExecutionAlreadyStartedError sessionAlreadyExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ServiceBusyError serviceBusyError,
    )

  /**
  * Returns the information from mutable state of workflow execution.
  * It fails with 'EntityNotExistError' if specified workflow execution in unknown to the service.
  * It returns CurrentBranchChangedError if the workflow version branch has changed.
  **/
  GetMutableStateResponse GetMutableState(1: GetMutableStateRequest getRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
      7: shared.CurrentBranchChangedError currentBranchChangedError,
    )

  /**
   * Returns the information from mutable state of workflow execution.
   * It fails with 'EntityNotExistError' if specified workflow execution in unknown to the service.
   * It returns CurrentBranchChangedError if the workflow version branch has changed.
   **/
   PollMutableStateResponse PollMutableState(1: PollMutableStateRequest pollRequest)
     throws (
       1: shared.BadRequestError badRequestError,
       2: shared.InternalServiceError internalServiceError,
       3: shared.EntityNotExistsError entityNotExistError,
       4: ShardOwnershipLostError shardOwnershipLostError,
       5: shared.LimitExceededError limitExceededError,
       6: shared.ServiceBusyError serviceBusyError,
       7: shared.CurrentBranchChangedError currentBranchChangedError,
     )

  /**
  * Reset the sticky tasklist related information in mutable state of a given workflow.
  * Things cleared are:
  * 1. StickyTaskList
  * 2. StickyScheduleToStartTimeout
  * 3. ClientLibraryVersion
  * 4. ClientFeatureVersion
  * 5. ClientImpl
  **/
  ResetStickyTaskListResponse ResetStickyTaskList(1: ResetStickyTaskListRequest resetRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
      7: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * RecordDecisionTaskStarted is called by the Matchingservice before it hands a decision task to the application worker in response to
  * a PollForDecisionTask call. It records in the history the event that the decision task has started. It will return 'EventAlreadyStartedError',
  * if the workflow's execution history already includes a record of the event starting.
  **/
  RecordDecisionTaskStartedResponse RecordDecisionTaskStarted(1: RecordDecisionTaskStartedRequest addRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: EventAlreadyStartedError eventAlreadyStartedError,
      4: shared.EntityNotExistsError entityNotExistError,
      5: ShardOwnershipLostError shardOwnershipLostError,
      6: shared.DomainNotActiveError domainNotActiveError,
      7: shared.LimitExceededError limitExceededError,
      8: shared.ServiceBusyError serviceBusyError,
      9: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * RecordActivityTaskStarted is called by the Matchingservice before it hands a decision task to the application worker in response to
  * a PollForActivityTask call. It records in the history the event that the decision task has started. It will return 'EventAlreadyStartedError',
  * if the workflow's execution history already includes a record of the event starting.
  **/
  RecordActivityTaskStartedResponse RecordActivityTaskStarted(1: RecordActivityTaskStartedRequest addRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: EventAlreadyStartedError eventAlreadyStartedError,
      4: shared.EntityNotExistsError entityNotExistError,
      5: ShardOwnershipLostError shardOwnershipLostError,
      6: shared.DomainNotActiveError domainNotActiveError,
      7: shared.LimitExceededError limitExceededError,
      8: shared.ServiceBusyError serviceBusyError,
      9: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * RespondDecisionTaskCompleted is called by application worker to complete a DecisionTask handed as a result of
  * 'PollForDecisionTask' API call.  Completing a DecisionTask will result in new events for the workflow execution and
  * potentially new ActivityTask being created for corresponding decisions.  It will also create a DecisionTaskCompleted
  * event in the history for that session.  Use the 'taskToken' provided as response of PollForDecisionTask API call
  * for completing the DecisionTask.
  **/
  RespondDecisionTaskCompletedResponse RespondDecisionTaskCompleted(1: RespondDecisionTaskCompletedRequest completeRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ServiceBusyError serviceBusyError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * RespondDecisionTaskFailed is called by application worker to indicate failure.  This results in
  * DecisionTaskFailedEvent written to the history and a new DecisionTask created.  This API can be used by client to
  * either clear sticky tasklist or report ny panics during DecisionTask processing.
  **/
  void RespondDecisionTaskFailed(1: RespondDecisionTaskFailedRequest failedRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ServiceBusyError serviceBusyError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * RecordActivityTaskHeartbeat is called by application worker while it is processing an ActivityTask.  If worker fails
  * to heartbeat within 'heartbeatTimeoutSeconds' interval for the ActivityTask, then it will be marked as timedout and
  * 'ActivityTaskTimedOut' event will be written to the workflow history.  Calling 'RecordActivityTaskHeartbeat' will
  * fail with 'EntityNotExistsError' in such situations.  Use the 'taskToken' provided as response of
  * PollForActivityTask API call for heartbeating.
  **/
  shared.RecordActivityTaskHeartbeatResponse RecordActivityTaskHeartbeat(1: RecordActivityTaskHeartbeatRequest heartbeatRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ServiceBusyError serviceBusyError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * RespondActivityTaskCompleted is called by application worker when it is done processing an ActivityTask.  It will
  * result in a new 'ActivityTaskCompleted' event being written to the workflow history and a new DecisionTask
  * created for the workflow so new decisions could be made.  Use the 'taskToken' provided as response of
  * PollForActivityTask API call for completion. It fails with 'EntityNotExistsError' if the taskToken is not valid
  * anymore due to activity timeout.
  **/
  void  RespondActivityTaskCompleted(1: RespondActivityTaskCompletedRequest completeRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ServiceBusyError serviceBusyError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * RespondActivityTaskFailed is called by application worker when it is done processing an ActivityTask.  It will
  * result in a new 'ActivityTaskFailed' event being written to the workflow history and a new DecisionTask
  * created for the workflow instance so new decisions could be made.  Use the 'taskToken' provided as response of
  * PollForActivityTask API call for completion. It fails with 'EntityNotExistsError' if the taskToken is not valid
  * anymore due to activity timeout.
  **/
  void RespondActivityTaskFailed(1: RespondActivityTaskFailedRequest failRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ServiceBusyError serviceBusyError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * RespondActivityTaskCanceled is called by application worker when it is successfully canceled an ActivityTask.  It will
  * result in a new 'ActivityTaskCanceled' event being written to the workflow history and a new DecisionTask
  * created for the workflow instance so new decisions could be made.  Use the 'taskToken' provided as response of
  * PollForActivityTask API call for completion. It fails with 'EntityNotExistsError' if the taskToken is not valid
  * anymore due to activity timeout.
  **/
  void RespondActivityTaskCanceled(1: RespondActivityTaskCanceledRequest canceledRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ServiceBusyError serviceBusyError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * SignalWorkflowExecution is used to send a signal event to running workflow execution.  This results in
  * WorkflowExecutionSignaled event recorded in the history and a decision task being created for the execution.
  **/
  void SignalWorkflowExecution(1: SignalWorkflowExecutionRequest signalRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.ServiceBusyError serviceBusyError,
      7: shared.LimitExceededError limitExceededError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * SignalWithStartWorkflowExecution is used to ensure sending a signal event to a workflow execution.
  * If workflow is running, this results in WorkflowExecutionSignaled event recorded in the history
  * and a decision task being created for the execution.
  * If workflow is not running or not found, it will first try start workflow with given WorkflowIDResuePolicy,
  * and record WorkflowExecutionStarted and WorkflowExecutionSignaled event in case of success.
  * It will return `WorkflowExecutionAlreadyStartedError` if start workflow failed with given policy.
  **/
  shared.StartWorkflowExecutionResponse SignalWithStartWorkflowExecution(1: SignalWithStartWorkflowExecutionRequest signalWithStartRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: ShardOwnershipLostError shardOwnershipLostError,
      4: shared.DomainNotActiveError domainNotActiveError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
      7: shared.WorkflowExecutionAlreadyStartedError workflowAlreadyStartedError,
    )

  /**
  * RemoveSignalMutableState is used to remove a signal request ID that was previously recorded.  This is currently
  * used to clean execution info when signal decision finished.
  **/
  void RemoveSignalMutableState(1: RemoveSignalMutableStateRequest removeRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ServiceBusyError serviceBusyError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * TerminateWorkflowExecution terminates an existing workflow execution by recording WorkflowExecutionTerminated event
  * in the history and immediately terminating the execution instance.
  **/
  void TerminateWorkflowExecution(1: TerminateWorkflowExecutionRequest terminateRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ServiceBusyError serviceBusyError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * ResetWorkflowExecution reset an existing workflow execution by a firstEventID of a existing event batch
  * in the history and immediately terminating the current execution instance.
  * After reset, the history will grow from nextFirstEventID.
  **/
  shared.ResetWorkflowExecutionResponse ResetWorkflowExecution(1: ResetWorkflowExecutionRequest resetRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ServiceBusyError serviceBusyError,
    )

  /**
  * RequestCancelWorkflowExecution is called by application worker when it wants to request cancellation of a workflow instance.
  * It will result in a new 'WorkflowExecutionCancelRequested' event being written to the workflow history and a new DecisionTask
  * created for the workflow instance so new decisions could be made. It fails with
  * 'WorkflowExecutionAlreadyCompletedError' if the workflow is not valid
  * anymore due to completion or with 'EntityNotExistsError' if worfklow doesn't exist.
  **/
  void RequestCancelWorkflowExecution(1: RequestCancelWorkflowExecutionRequest cancelRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.CancellationAlreadyRequestedError cancellationAlreadyRequestedError,
      6: shared.DomainNotActiveError domainNotActiveError,
      7: shared.LimitExceededError limitExceededError,
      8: shared.ServiceBusyError serviceBusyError,
      10: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * ScheduleDecisionTask is used for creating a decision task for already started workflow execution.  This is mainly
  * used by transfer queue processor during the processing of StartChildWorkflowExecution task, where it first starts
  * child execution without creating the decision task and then calls this API after updating the mutable state of
  * parent execution.
  **/
  void ScheduleDecisionTask(1: ScheduleDecisionTaskRequest scheduleRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ServiceBusyError serviceBusyError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * RecordChildExecutionCompleted is used for reporting the completion of child workflow execution to parent.
  * This is mainly called by transfer queue processor during the processing of DeleteExecution task.
  **/
  void RecordChildExecutionCompleted(1: RecordChildExecutionCompletedRequest completionRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ServiceBusyError serviceBusyError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
    )

  /**
  * DescribeWorkflowExecution returns information about the specified workflow execution.
  **/
  shared.DescribeWorkflowExecutionResponse DescribeWorkflowExecution(1: DescribeWorkflowExecutionRequest describeRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
    )

  void ReplicateEventsV2(1: ReplicateEventsV2Request replicateV2Request)
    throws (
        1: shared.BadRequestError badRequestError,
        2: shared.InternalServiceError internalServiceError,
        3: shared.EntityNotExistsError entityNotExistError,
        4: ShardOwnershipLostError shardOwnershipLostError,
        5: shared.LimitExceededError limitExceededError,
        6: shared.RetryTaskV2Error retryTaskError,
        7: shared.ServiceBusyError serviceBusyError,
    )

  /**
  * SyncShardStatus sync the status between shards
  **/
  void SyncShardStatus(1: SyncShardStatusRequest syncShardStatusRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
    )

  /**
  * SyncActivity sync the activity status
  **/
  void SyncActivity(1: SyncActivityRequest syncActivityRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.ServiceBusyError serviceBusyError,
      7: shared.RetryTaskV2Error retryTaskV2Error,
    )

  /**
  * DescribeMutableState returns information about the internal states of workflow mutable state.
  **/
  DescribeMutableStateResponse DescribeMutableState(1: DescribeMutableStateRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.AccessDeniedError accessDeniedError,
      5: ShardOwnershipLostError shardOwnershipLostError,
      6: shared.LimitExceededError limitExceededError,
    )

  /**
  * DescribeHistoryHost returns information about the internal states of a history host
  **/
  shared.DescribeHistoryHostResponse DescribeHistoryHost(1: shared.DescribeHistoryHostRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * CloseShard close the shard
  **/
  void CloseShard(1: shared.CloseShardRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * RemoveTask remove task based on type, taskid, shardid
  **/
  void RemoveTask(1: shared.RemoveTaskRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * ResetQueue reset processing queue state based on cluster name and type
  **/
  void ResetQueue(1: shared.ResetQueueRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * DescribeQueue return queue states based on cluster name and type
  **/
  shared.DescribeQueueResponse DescribeQueue(1: shared.DescribeQueueRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * GetReplicationMessages return replication messages based on the read level
  **/
  replicator.GetReplicationMessagesResponse GetReplicationMessages(1: replicator.GetReplicationMessagesRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.LimitExceededError limitExceededError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
    )

  /**
  * GetDLQReplicationMessages return replication messages based on dlq info
  **/
  replicator.GetDLQReplicationMessagesResponse GetDLQReplicationMessages(1: replicator.GetDLQReplicationMessagesRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.ServiceBusyError serviceBusyError,
      4: shared.EntityNotExistsError entityNotExistError,
    )

  /**
  * QueryWorkflow returns query result for a specified workflow execution
  **/
  QueryWorkflowResponse QueryWorkflow(1: QueryWorkflowRequest queryRequest)
	throws (
	  1: shared.BadRequestError badRequestError,
	  2: shared.InternalServiceError internalServiceError,
	  3: shared.EntityNotExistsError entityNotExistError,
	  4: shared.QueryFailedError queryFailedError,
	  5: shared.LimitExceededError limitExceededError,
	  6: shared.ServiceBusyError serviceBusyError,
	  7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
	)

  /**
  * ReapplyEvents applies stale events to the current workflow and current run
  **/
  void ReapplyEvents(1: ReapplyEventsRequest reapplyEventsRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.DomainNotActiveError domainNotActiveError,
      4: shared.LimitExceededError limitExceededError,
      5: shared.ServiceBusyError serviceBusyError,
      6: ShardOwnershipLostError shardOwnershipLostError,
      7: shared.EntityNotExistsError entityNotExistError,
    )

  /**
  * RefreshWorkflowTasks refreshes all tasks of a workflow
  **/
  void RefreshWorkflowTasks(1: RefreshWorkflowTasksRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.DomainNotActiveError domainNotActiveError,
      4: ShardOwnershipLostError shardOwnershipLostError,
      5: shared.ServiceBusyError serviceBusyError,
      6: shared.EntityNotExistsError entityNotExistError,
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
      5: ShardOwnershipLostError shardOwnershipLostError,
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
      5: ShardOwnershipLostError shardOwnershipLostError,
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
      5: ShardOwnershipLostError shardOwnershipLostError,
    )

  /**
  * NotifyFailoverMarkers sends failover marker to the failover coordinator
  **/
  void NotifyFailoverMarkers(1: NotifyFailoverMarkersRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.ServiceBusyError serviceBusyError,
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
      4: ShardOwnershipLostError shardOwnershipLostError,
    )

  /**
  * GetFailoverInfo responds the failover info about an on-going graceful failover
  **/
  GetFailoverInfoResponse GetFailoverInfo(1: GetFailoverInfoRequest request)
    throws (
      1: shared.InternalServiceError internalServiceError,
      2: shared.ServiceBusyError serviceBusyError,
      3: ShardOwnershipLostError shardOwnershipLostError,
      4: shared.EntityNotExistsError entityNotExistError,
    )

  /**
  * RatelimitUpdate pushes global-ratelimiting data to aggregating hosts,
  * and returns data describing how to update the caller's ratelimits.
  *
  * For more details, see github.com/uber/cadence/common/quotas/global documentation.
  *
  * Request and response structures are intentionally loosely defined, to allow plugging
  * in externally-defined algorithms without changing protocol-level details.
  **/
  RatelimitUpdateResponse RatelimitUpdate(1: RatelimitUpdateRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.InternalServiceError internalServiceError,
      3: shared.ServiceBusyError serviceBusyError,
      4: ShardOwnershipLostError shardOwnershipLostError,
    )
}
