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

namespace java com.uber.cadence

/**
* WorkflowService API is exposed to provide support for long running applications.  Application is expected to call
* StartWorkflowExecution to create an instance for each instance of long running workflow.  Such applications are expected
* to have a worker which regularly polls for DecisionTask and ActivityTask from the WorkflowService.  For each
* DecisionTask, application is expected to process the history of events for that session and respond back with next
* decisions.  For each ActivityTask, application is expected to execute the actual logic for that task and respond back
* with completion or failure.  Worker is expected to regularly heartbeat while activity task is running.
**/
service WorkflowService {
  /**
  * RegisterDomain creates a new domain which can be used as a container for all resources.  Domain is a top level
  * entity within Cadence, used as a container for all resources like workflow executions, tasklists, etc.  Domain
  * acts as a sandbox and provides isolation for all resources within the domain.  All resources belongs to exactly one
  * domain.
  **/
  void RegisterDomain(1: shared.RegisterDomainRequest registerRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.DomainAlreadyExistsError domainExistsError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      6: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * DescribeDomain returns the information and configuration for a registered domain.
  **/
  shared.DescribeDomainResponse DescribeDomain(1: shared.DescribeDomainRequest describeRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      6: shared.AccessDeniedError accessDeniedError,
    )

  /**
    * ListDomains returns the information and configuration for all domains.
    **/
    shared.ListDomainsResponse ListDomains(1: shared.ListDomainsRequest listRequest)
      throws (
        1: shared.BadRequestError badRequestError,
        3: shared.EntityNotExistsError entityNotExistError,
        4: shared.ServiceBusyError serviceBusyError,
        5: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
        6: shared.AccessDeniedError accessDeniedError,
      )

  /**
  * UpdateDomain is used to update the information and configuration for a registered domain.
  **/
  shared.UpdateDomainResponse UpdateDomain(1: shared.UpdateDomainRequest updateRequest)
      throws (
        1: shared.BadRequestError badRequestError,
        3: shared.EntityNotExistsError entityNotExistError,
        4: shared.ServiceBusyError serviceBusyError,
        5: shared.DomainNotActiveError domainNotActiveError,
        6: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
        7: shared.AccessDeniedError accessDeniedError,
      )

  /**
  * DeprecateDomain us used to update status of a registered domain to DEPRECATED.  Once the domain is deprecated
  * it cannot be used to start new workflow executions.  Existing workflow executions will continue to run on
  * deprecated domains.
  **/
  void DeprecateDomain(1: shared.DeprecateDomainRequest deprecateRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      7: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * DeleteDomain permanently removes a domain record. This operation:
  * - Requires domain to be in DEPRECATED status
  * - Cannot be performed on domains with running workflows
  * - Is irreversible and removes all domain data
  * - Requires proper permissions and security token
  **/
  void DeleteDomain(1: shared.DeleteDomainRequest deleteRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.ServiceBusyError serviceBusyError,
      3: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      4: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * RestartWorkflowExecution restarts a previous workflow
  * If the workflow is currently running it will terminate and restart
  **/
  shared.RestartWorkflowExecutionResponse RestartWorkflowExecution(1: shared.RestartWorkflowExecutionRequest restartRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.ServiceBusyError serviceBusyError,
      3: shared.DomainNotActiveError domainNotActiveError,
      4: shared.LimitExceededError limitExceededError,
      5: shared.EntityNotExistsError entityNotExistError,
      6: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      7: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * DiagnoseWorkflowExecution diagnoses a previous workflow execution
  **/
  shared.DiagnoseWorkflowExecutionResponse DiagnoseWorkflowExecution(1: shared.DiagnoseWorkflowExecutionRequest diagnoseRequest)
    throws (
      1: shared.DomainNotActiveError domainNotActiveError,
      2: shared.ServiceBusyError serviceBusyError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      5: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * StartWorkflowExecution starts a new long running workflow instance.  It will create the instance with
  * 'WorkflowExecutionStarted' event in history and also schedule the first DecisionTask for the worker to make the
  * first decision for this instance.  It will return 'WorkflowExecutionAlreadyStartedError', if an instance already
  * exists with same workflowId.
  **/
  shared.StartWorkflowExecutionResponse StartWorkflowExecution(1: shared.StartWorkflowExecutionRequest startRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.WorkflowExecutionAlreadyStartedError sessionAlreadyExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.EntityNotExistsError entityNotExistError,
      8: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      9: shared.AccessDeniedError accessDeniedError,
    )
  /**
  * StartWorkflowExecutionAsync starts a new long running workflow instance asynchronously. It will push a StartWorkflowExecutionRequest to a queue
  * and immediately return a response. The request will be processed by a separate consumer eventually.
  **/
  shared.StartWorkflowExecutionAsyncResponse StartWorkflowExecutionAsync(1: shared.StartWorkflowExecutionAsyncRequest startRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.WorkflowExecutionAlreadyStartedError sessionAlreadyExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.EntityNotExistsError entityNotExistError,
      8: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      9: shared.AccessDeniedError accessDeniedError,
    )
  /**
  * Returns the history of specified workflow execution.  It fails with 'EntityNotExistError' if speficied workflow
  * execution in unknown to the service.
  **/
  shared.GetWorkflowExecutionHistoryResponse GetWorkflowExecutionHistory(1: shared.GetWorkflowExecutionHistoryRequest getRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      6: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * PollForDecisionTask is called by application worker to process DecisionTask from a specific taskList.  A
  * DecisionTask is dispatched to callers for active workflow executions, with pending decisions.
  * Application is then expected to call 'RespondDecisionTaskCompleted' API when it is done processing the DecisionTask.
  * It will also create a 'DecisionTaskStarted' event in the history for that session before handing off DecisionTask to
  * application worker.
  **/
  shared.PollForDecisionTaskResponse PollForDecisionTask(1: shared.PollForDecisionTaskRequest pollRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.ServiceBusyError serviceBusyError,
      4: shared.LimitExceededError limitExceededError,
      5: shared.EntityNotExistsError entityNotExistError,
      6: shared.DomainNotActiveError domainNotActiveError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * RespondDecisionTaskCompleted is called by application worker to complete a DecisionTask handed as a result of
  * 'PollForDecisionTask' API call.  Completing a DecisionTask will result in new events for the workflow execution and
  * potentially new ActivityTask being created for corresponding decisions.  It will also create a DecisionTaskCompleted
  * event in the history for that session.  Use the 'taskToken' provided as response of PollForDecisionTask API call
  * for completing the DecisionTask.
  * The response could contain a new decision task if there is one or if the request asking for one.
  **/
  shared.RespondDecisionTaskCompletedResponse RespondDecisionTaskCompleted(1: shared.RespondDecisionTaskCompletedRequest completeRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.DomainNotActiveError domainNotActiveError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
      9: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * RespondDecisionTaskFailed is called by application worker to indicate failure.  This results in
  * DecisionTaskFailedEvent written to the history and a new DecisionTask created.  This API can be used by client to
  * either clear sticky tasklist or report any panics during DecisionTask processing.  Cadence will only append first
  * DecisionTaskFailed event to the history of workflow execution for consecutive failures.
  **/
  void RespondDecisionTaskFailed(1: shared.RespondDecisionTaskFailedRequest failedRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.DomainNotActiveError domainNotActiveError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
      9: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * PollForActivityTask is called by application worker to process ActivityTask from a specific taskList.  ActivityTask
  * is dispatched to callers whenever a ScheduleTask decision is made for a workflow execution.
  * Application is expected to call 'RespondActivityTaskCompleted' or 'RespondActivityTaskFailed' once it is done
  * processing the task.
  * Application also needs to call 'RecordActivityTaskHeartbeat' API within 'heartbeatTimeoutSeconds' interval to
  * prevent the task from getting timed out.  An event 'ActivityTaskStarted' event is also written to workflow execution
  * history before the ActivityTask is dispatched to application worker.
  **/
  shared.PollForActivityTaskResponse PollForActivityTask(1: shared.PollForActivityTaskRequest pollRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.ServiceBusyError serviceBusyError,
      4: shared.LimitExceededError limitExceededError,
      5: shared.EntityNotExistsError entityNotExistError,
      6: shared.DomainNotActiveError domainNotActiveError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * RecordActivityTaskHeartbeat is called by application worker while it is processing an ActivityTask.  If worker fails
  * to heartbeat within 'heartbeatTimeoutSeconds' interval for the ActivityTask, then it will be marked as timedout and
  * 'ActivityTaskTimedOut' event will be written to the workflow history.  Calling 'RecordActivityTaskHeartbeat' will
  * fail with 'EntityNotExistsError' in such situations.  Use the 'taskToken' provided as response of
  * PollForActivityTask API call for heartbeating.
  **/
  shared.RecordActivityTaskHeartbeatResponse RecordActivityTaskHeartbeat(1: shared.RecordActivityTaskHeartbeatRequest heartbeatRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.DomainNotActiveError domainNotActiveError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
      9: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * RecordActivityTaskHeartbeatByID is called by application worker while it is processing an ActivityTask.  If worker fails
  * to heartbeat within 'heartbeatTimeoutSeconds' interval for the ActivityTask, then it will be marked as timedout and
  * 'ActivityTaskTimedOut' event will be written to the workflow history.  Calling 'RecordActivityTaskHeartbeatByID' will
  * fail with 'EntityNotExistsError' in such situations.  Instead of using 'taskToken' like in RecordActivityTaskHeartbeat,
  * use Domain, WorkflowID and ActivityID
  **/
  shared.RecordActivityTaskHeartbeatResponse RecordActivityTaskHeartbeatByID(1: shared.RecordActivityTaskHeartbeatByIDRequest heartbeatRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.DomainNotActiveError domainNotActiveError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
      9: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * RespondActivityTaskCompleted is called by application worker when it is done processing an ActivityTask.  It will
  * result in a new 'ActivityTaskCompleted' event being written to the workflow history and a new DecisionTask
  * created for the workflow so new decisions could be made.  Use the 'taskToken' provided as response of
  * PollForActivityTask API call for completion. It fails with 'EntityNotExistsError' if the taskToken is not valid
  * anymore due to activity timeout.
  **/
  void  RespondActivityTaskCompleted(1: shared.RespondActivityTaskCompletedRequest completeRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.DomainNotActiveError domainNotActiveError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
      9: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * RespondActivityTaskCompletedByID is called by application worker when it is done processing an ActivityTask.
  * It will result in a new 'ActivityTaskCompleted' event being written to the workflow history and a new DecisionTask
  * created for the workflow so new decisions could be made.  Similar to RespondActivityTaskCompleted but use Domain,
  * WorkflowID and ActivityID instead of 'taskToken' for completion. It fails with 'EntityNotExistsError'
  * if the these IDs are not valid anymore due to activity timeout.
  **/
  void  RespondActivityTaskCompletedByID(1: shared.RespondActivityTaskCompletedByIDRequest completeRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.DomainNotActiveError domainNotActiveError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
      9: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * RespondActivityTaskFailed is called by application worker when it is done processing an ActivityTask.  It will
  * result in a new 'ActivityTaskFailed' event being written to the workflow history and a new DecisionTask
  * created for the workflow instance so new decisions could be made.  Use the 'taskToken' provided as response of
  * PollForActivityTask API call for completion. It fails with 'EntityNotExistsError' if the taskToken is not valid
  * anymore due to activity timeout.
  **/
  void  RespondActivityTaskFailed(1: shared.RespondActivityTaskFailedRequest failRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.DomainNotActiveError domainNotActiveError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
      9: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * RespondActivityTaskFailedByID is called by application worker when it is done processing an ActivityTask.
  * It will result in a new 'ActivityTaskFailed' event being written to the workflow history and a new DecisionTask
  * created for the workflow instance so new decisions could be made.  Similar to RespondActivityTaskFailed but use
  * Domain, WorkflowID and ActivityID instead of 'taskToken' for completion. It fails with 'EntityNotExistsError'
  * if the these IDs are not valid anymore due to activity timeout.
  **/
  void  RespondActivityTaskFailedByID(1: shared.RespondActivityTaskFailedByIDRequest failRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.DomainNotActiveError domainNotActiveError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
      9: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * RespondActivityTaskCanceled is called by application worker when it is successfully canceled an ActivityTask.  It will
  * result in a new 'ActivityTaskCanceled' event being written to the workflow history and a new DecisionTask
  * created for the workflow instance so new decisions could be made.  Use the 'taskToken' provided as response of
  * PollForActivityTask API call for completion. It fails with 'EntityNotExistsError' if the taskToken is not valid
  * anymore due to activity timeout.
  **/
  void RespondActivityTaskCanceled(1: shared.RespondActivityTaskCanceledRequest canceledRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.DomainNotActiveError domainNotActiveError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
      9: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * RespondActivityTaskCanceledByID is called by application worker when it is successfully canceled an ActivityTask.
  * It will result in a new 'ActivityTaskCanceled' event being written to the workflow history and a new DecisionTask
  * created for the workflow instance so new decisions could be made.  Similar to RespondActivityTaskCanceled but use
  * Domain, WorkflowID and ActivityID instead of 'taskToken' for completion. It fails with 'EntityNotExistsError'
  * if the these IDs are not valid anymore due to activity timeout.
  **/
  void RespondActivityTaskCanceledByID(1: shared.RespondActivityTaskCanceledByIDRequest canceledRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.DomainNotActiveError domainNotActiveError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ServiceBusyError serviceBusyError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
      9: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * RequestCancelWorkflowExecution is called by application worker when it wants to request cancellation of a workflow instance.
  * It will result in a new 'WorkflowExecutionCancelRequested' event being written to the workflow history and a new DecisionTask
  * created for the workflow instance so new decisions could be made. It fails with 'EntityNotExistsError' if the workflow is not valid
  * anymore due to completion or doesn't exist.
  **/
  void RequestCancelWorkflowExecution(1: shared.RequestCancelWorkflowExecutionRequest cancelRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.CancellationAlreadyRequestedError cancellationAlreadyRequestedError,
      5: shared.ServiceBusyError serviceBusyError,
      6: shared.DomainNotActiveError domainNotActiveError,
      7: shared.LimitExceededError limitExceededError,
      8: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      9: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
      10: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * SignalWorkflowExecution is used to send a signal event to running workflow execution.  This results in
  * WorkflowExecutionSignaled event recorded in the history and a decision task being created for the execution.
  **/
  void SignalWorkflowExecution(1: shared.SignalWorkflowExecutionRequest signalRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
      9: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * SignalWithStartWorkflowExecution is used to ensure sending signal to a workflow.
  * If the workflow is running, this results in WorkflowExecutionSignaled event being recorded in the history
  * and a decision task being created for the execution.
  * If the workflow is not running or not found, this results in WorkflowExecutionStarted and WorkflowExecutionSignaled
  * events being recorded in history, and a decision task being created for the execution
  **/
  shared.StartWorkflowExecutionResponse SignalWithStartWorkflowExecution(1: shared.SignalWithStartWorkflowExecutionRequest signalWithStartRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.WorkflowExecutionAlreadyStartedError workflowAlreadyStartedError,
      8: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      9: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * SignalWithStartWorkflowExecutionAsync is used to ensure sending signal to a workflow asynchronously.  It will push a SignalWithStartWorkflowExecutionRequest to a queue
  * and immediately return a response. The request will be processed by a separate consumer eventually.
  **/
  shared.SignalWithStartWorkflowExecutionAsyncResponse SignalWithStartWorkflowExecutionAsync(1: shared.SignalWithStartWorkflowExecutionAsyncRequest signalWithStartRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.WorkflowExecutionAlreadyStartedError sessionAlreadyExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.EntityNotExistsError entityNotExistError,
      8: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      9: shared.AccessDeniedError accessDeniedError,
    )
  /**
    * ResetWorkflowExecution reset an existing workflow execution to DecisionTaskCompleted event(exclusive).
    * And it will immediately terminating the current execution instance.
    **/
  shared.ResetWorkflowExecutionResponse ResetWorkflowExecution(1: shared.ResetWorkflowExecutionRequest resetRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * TerminateWorkflowExecution terminates an existing workflow execution by recording WorkflowExecutionTerminated event
  * in the history and immediately terminating the execution instance.
  **/
  void TerminateWorkflowExecution(1: shared.TerminateWorkflowExecutionRequest terminateRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.DomainNotActiveError domainNotActiveError,
      6: shared.LimitExceededError limitExceededError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
      9: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * ListOpenWorkflowExecutions is a visibility API to list the open executions in a specific domain.
  **/
  shared.ListOpenWorkflowExecutionsResponse ListOpenWorkflowExecutions(1: shared.ListOpenWorkflowExecutionsRequest listRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.LimitExceededError limitExceededError,
      6: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      7: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * ListClosedWorkflowExecutions is a visibility API to list the closed executions in a specific domain.
  **/
  shared.ListClosedWorkflowExecutionsResponse ListClosedWorkflowExecutions(1: shared.ListClosedWorkflowExecutionsRequest listRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      6: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * ListWorkflowExecutions is a visibility API to list workflow executions in a specific domain.
  **/
  shared.ListWorkflowExecutionsResponse ListWorkflowExecutions(1: shared.ListWorkflowExecutionsRequest listRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      6: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * ListArchivedWorkflowExecutions is a visibility API to list archived workflow executions in a specific domain.
  **/
  shared.ListArchivedWorkflowExecutionsResponse ListArchivedWorkflowExecutions(1: shared.ListArchivedWorkflowExecutionsRequest listRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      6: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * ScanWorkflowExecutions is a visibility API to list large amount of workflow executions in a specific domain without order.
  **/
  shared.ListWorkflowExecutionsResponse ScanWorkflowExecutions(1: shared.ListWorkflowExecutionsRequest listRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      6: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * CountWorkflowExecutions is a visibility API to count of workflow executions in a specific domain.
  **/
  shared.CountWorkflowExecutionsResponse CountWorkflowExecutions(1: shared.CountWorkflowExecutionsRequest countRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      6: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * GetSearchAttributes is a visibility API to get all legal keys that could be used in list APIs
  **/
  shared.GetSearchAttributesResponse GetSearchAttributes()
    throws (
      2: shared.ServiceBusyError serviceBusyError,
      3: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      4: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * RespondQueryTaskCompleted is called by application worker to complete a QueryTask (which is a DecisionTask for query)
  * as a result of 'PollForDecisionTask' API call. Completing a QueryTask will unblock the client call to 'QueryWorkflow'
  * API and return the query result to client as a response to 'QueryWorkflow' API call.
  **/
  void RespondQueryTaskCompleted(1: shared.RespondQueryTaskCompletedRequest completeRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.LimitExceededError limitExceededError,
      5: shared.ServiceBusyError serviceBusyError,
      6: shared.DomainNotActiveError domainNotActiveError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.AccessDeniedError accessDeniedError,
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
  shared.ResetStickyTaskListResponse ResetStickyTaskList(1: shared.ResetStickyTaskListRequest resetRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.LimitExceededError limitExceededError,
      5: shared.ServiceBusyError serviceBusyError,
      6: shared.DomainNotActiveError domainNotActiveError,
      7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      8: shared.WorkflowExecutionAlreadyCompletedError workflowExecutionAlreadyCompletedError,
      9: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * QueryWorkflow returns query result for a specified workflow execution
  **/
  shared.QueryWorkflowResponse QueryWorkflow(1: shared.QueryWorkflowRequest queryRequest)
	throws (
	  1: shared.BadRequestError badRequestError,
	  3: shared.EntityNotExistsError entityNotExistError,
	  4: shared.QueryFailedError queryFailedError,
	  5: shared.LimitExceededError limitExceededError,
	  6: shared.ServiceBusyError serviceBusyError,
	  7: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
    8: shared.AccessDeniedError accessDeniedError,
	)

  /**
  * DescribeWorkflowExecution returns information about the specified workflow execution.
  **/
  shared.DescribeWorkflowExecutionResponse DescribeWorkflowExecution(1: shared.DescribeWorkflowExecutionRequest describeRequest)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.LimitExceededError limitExceededError,
      5: shared.ServiceBusyError serviceBusyError,
      6: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      7: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * DescribeTaskList returns information about the target tasklist, right now this API returns the
  * pollers which polled this tasklist in last few minutes.
  **/
  shared.DescribeTaskListResponse DescribeTaskList(1: shared.DescribeTaskListRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.LimitExceededError limitExceededError,
      5: shared.ServiceBusyError serviceBusyError,
      6: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      7: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * GetClusterInfo returns information about cadence cluster
  **/
  shared.ClusterInfo GetClusterInfo()
    throws (
      1: shared.InternalServiceError internalServiceError,
      2: shared.ServiceBusyError serviceBusyError,
      3: shared.AccessDeniedError accessDeniedError,
    )

  /**
  * GetTaskListsByDomain returns the list of all the task lists for a domainName.
  **/
  shared.GetTaskListsByDomainResponse GetTaskListsByDomain(1: shared.GetTaskListsByDomainRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      2: shared.EntityNotExistsError entityNotExistError,
      3: shared.LimitExceededError limitExceededError,
      4: shared.ServiceBusyError serviceBusyError,
      5: shared.ClientVersionNotSupportedError clientVersionNotSupportedError,
      6: shared.AccessDeniedError accessDeniedError,
    )

   /**
   * ReapplyEvents applies stale events to the current workflow and current run
   **/
  shared.ListTaskListPartitionsResponse ListTaskListPartitions(1: shared.ListTaskListPartitionsRequest request)
    throws (
      1: shared.BadRequestError badRequestError,
      3: shared.EntityNotExistsError entityNotExistError,
      4: shared.LimitExceededError limitExceededError,
      5: shared.ServiceBusyError serviceBusyError,
      6: shared.AccessDeniedError accessDeniedError,
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
      5: shared.AccessDeniedError accessDeniedError,
    )
}
