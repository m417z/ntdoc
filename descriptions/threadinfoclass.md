This enumeration defines types of information that can be queried or set for threads.

# Applicable to
 - `NtQueryInformationThread`
 - `NtSetInformationThread`

# Members

## ThreadBasicInformation (0)
Retrieves basic information about the thread such as its exit status, `TEB` address, and `CLIENT_ID`.

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `THREAD_BASIC_INFORMATION`         | N/A
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | N/A

### Related Win32 API
 - [`GetExitCodeThread`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getexitcodethread)
 - [`GetThreadId`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadid)
 - [`GetProcessIdOfThread`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessidofthread)
 - [`GetThreadPriority`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadpriority)

### See also
 - `NtCurrentTeb`

## ThreadTimes (1)
Retrieves creation and executions times for the thread.

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `KERNEL_USER_TIMES`                | N/A
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | N/A

### Related Win32 API
 - [`GetThreadTimes`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreadtimes)

## ThreadPriority (2)
Adjusts the priority of the thread.

|                    | Query | Set
| ------------------ | ----- | ---
| Type               | N/A   | `KPRIORITY`
| Required access    | N/A   | `THREAD_SET_LIMITED_INFORMATION`
| Required privilege | None  | `SeIncreaseBasePriorityPrivilege`

## ThreadBasePriority (3)
Adjusts the base priority of the thread.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `KPRIORITY`
| Required access | N/A   | `THREAD_SET_LIMITED_INFORMATION`

## ThreadAffinityMask (4)
Limits on which processors the thread is allowed to run.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `KAFFINITY`
| Required access | N/A   | `THREAD_SET_LIMITED_INFORMATION`

## ThreadImpersonationToken (5)
Sets thread impersonation token. Note that if the token of the target process does not have `SeImpersonatePrivilege` enabled, the system might downgrade the assigned token to the identification level of impersonation.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | Token `HANDLE` with `TOKEN_IMPERSONATE` access
| Required access | N/A   | `THREAD_SET_THREAD_TOKEN`

### Related Win32 API
 - [`SetThreadToken`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadtoken)

### See also
 - `NtOpenThreadToken`

## ThreadDescriptorTableEntry (6)

|                 | Query                                                      | Set
| --------------- | ---------------------------------------------------------- | ---
| Type            | `DESCRIPTOR_TABLE_ENTRY` or `WOW64_DESCRIPTOR_TABLE_ENTRY` | N/A
| Required access | `THREAD_QUERY_INFORMATION`                                 | N/A

## ThreadEnableAlignmentFaultFixup (7)

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `BOOLEAN`
| Required access | N/A   | `THREAD_SET_INFORMATION`

## ThreadEventPair (8)

## ThreadQuerySetWin32StartAddress (9)
Retrieves the start address of a Win32 thread.

|                 | Query                      | Set
| --------------- | -------------------------- | ---
| Type            | `PVOID` or `ULONG_PTR`     | N/A
| Required access | `THREAD_QUERY_INFORMATION` | N/A

## ThreadZeroTlsCell (10)
Zeros out the specified TLS cell indicated by index.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `ULONG`
| Required access | N/A   | `THREAD_SET_INFORMATION`

## ThreadPerformanceCount (11)

|                 | Query                      | Set
| --------------- | -------------------------- | ---
| Type            | `LARGE_INTEGER`            | N/A
| Required access | `THREAD_QUERY_INFORMATION` | N/A

## ThreadAmILastThread (12)
Determines if the thread is the only one in the process.

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `ULONG` or `BOOL`                  | N/A
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | N/A

## ThreadIdealProcessor (13)
Adjusts the number of the ideal (preferred) processor for the thread. This info class only supports the current processor group. To set the ideal processor from another group, use `ThreadIdealProcessorEx` (info class 33).

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `ULONG`
| Required access | N/A   | `THREAD_SET_INFORMATION`

### Related Win32 API
 - [`SetThreadIdealProcessor`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadidealprocessor)

## ThreadPriorityBoost (14)
Queries, enables, or disables priority boosting for the thread

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `ULONG` or `BOOL`                  | `ULONG` or `BOOL`
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | `THREAD_SET_LIMITED_INFORMATION`

### Related Win32 API
 - [`SetThreadPriorityBoost`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadpriorityboost)

## ThreadSetTlsArrayAddress (15)

## ThreadIsIoPending (16)
Determines if the thread has any pending I/O requests.

|                 | Query                      | Set
| --------------- | -------------------------- | ---
| Type            | `ULONG` or `BOOL`          | N/A
| Required access | `THREAD_QUERY_INFORMATION` | N/A

## ThreadHideFromDebugger (17)
Queries or enables suppression of debug events generated on the thread. Threads that do not generate debug events are essentially invisible to debuggers.

|                 | Query                      | Set
| --------------- | -------------------------- | ---
| Type            | `BOOLEAN`                  | void (zero-size)
| Required access | `THREAD_QUERY_INFORMATION` | `THREAD_SET_INFORMATION`

### See also
 - `THREAD_CREATE_FLAGS_HIDE_FROM_DEBUGGER`
 - `NtWaitForDebugEvent`

## ThreadBreakOnTermination (18)
Marks the thread as critical, causing a BSOD if it terminates.

|                    | Query                      | Set
| ------------------ | -------------------------- | ---
| Type               | `ULONG` or `BOOL`          | `ULONG` or `BOOL`
| Required access    | `THREAD_QUERY_INFORMATION` | `THREAD_SET_INFORMATION`
| Required privilege | None                       | `SeDebugPrivilege`

### See also
 - `RtlSetThreadIsCritical`
 - `NtRaiseHardError`

## ThreadSwitchLegacyState (19)

## ThreadIsTerminated (20)
Determines if the thread has already terminated. The result is similar to a no-timeout wait on the handle via `NtWaitForSingleObject` but requires a different access mask.

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `ULONG` or `BOOL`                  | N/A
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | N/A

### See also
 - `NtWaitForSingleObject`
 - `NtTerminateThread`
 - `NtTerminateProcess`

## ThreadLastSystemCall (21)
Queries the information about the last syscall performed by the thread.

|                 | Query                             | Set
| --------------- | --------------------------------- | ---
| Type            | `THREAD_LAST_SYSCALL_INFORMATION` | N/A
| Required access | `THREAD_GET_CONTEXT`              | N/A

## ThreadIoPriority (22)
Determines or adjusts I/O priority for the thread.

|                    | Query                              | Set
| ------------------ | ---------------------------------- | ---
| Type               | `IO_PRIORITY_HINT`                 | `IO_PRIORITY_HINT`
| Required access    | `THREAD_QUERY_LIMITED_INFORMATION` | `THREAD_SET_INFORMATION`
| Required privilege | None                               | `SeIncreaseBasePriorityPrivilege`

## ThreadCycleTime (23)
Determines the number of cycles spent by the thread.

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `THREAD_QUERY_LIMITED_INFORMATION` | N/A
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | N/A

## ThreadPagePriority (24)
Determines or adjusts paging priority for the thread.

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `PAGE_PRIORITY_INFORMATION`        | `PAGE_PRIORITY_INFORMATION`
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | `THREAD_SET_INFORMATION`

## ThreadActualBasePriority (25)
Adjusts the base priority of the thread.

|                    | Query | Set
| ------------------ | ----- | ---
| Type               | N/A   | `LONG`
| Required access    | N/A   | `THREAD_SET_LIMITED_INFORMATION`
| Required privilege | None  | `SeIncreaseBasePriorityPrivilege`

## ThreadTebInformation (26)
Allows reading a portion of the thread's TEB.

|                 | Query                                       | Set
| --------------- | ------------------------------------------- | ---
| Type            | `THREAD_TEB_INFORMATION`                    | N/A
| Required access | `THREAD_GET_CONTEXT` + `THREAD_SET_CONTEXT` | N/A

## ThreadCSwitchMon (27)

## ThreadCSwitchPmu (28)

## ThreadWow64Context (29)
Gets and sets the WoW64 context (set of registers) for 32-bit threads running on 64-bit systems.

|                 | Query                | Set
| --------------- | -------------------- | ---
| Type            | `WOW64_CONTEXT`      | `WOW64_CONTEXT`
| Required access | `THREAD_GET_CONTEXT` | `THREAD_SET_CONTEXT`

### Related Win32 API
 - [`Wow64GetThreadContext`](https://learn.microsoft.com/en-us/windows/win32/api/wow64apiset/nf-wow64apiset-wow64getthreadcontext)
 - [`Wow64SetThreadContext`](https://learn.microsoft.com/en-us/windows/win32/api/wow64apiset/nf-wow64apiset-wow64setthreadcontext)

### See also
 - `RtlWow64GetThreadContext`
 - `RtlWow64SetThreadContext`

## ThreadGroupInformation (30)
Queries or adjusts the processor group for the thread.

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `GROUP_AFFINITY`                   | `GROUP_AFFINITY`
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | `THREAD_SET_INFORMATION`

## ThreadUmsInformation (31)

## ThreadCounterProfiling (32)

## ThreadIdealProcessorEx (33)
Queries or the number of the ideal (preferred) processor for the thread.

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `PROCESSOR_NUMBER`                 | `PROCESSOR_NUMBER`
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | `THREAD_SET_INFORMATION`

### Related Win32 API
 - [`SetThreadIdealProcessorEx`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreadidealprocessorex)

## ThreadCpuAccountingInformation (34)

## ThreadSuspendCount (35)
Queries the current suspension counter of the thread. Note that the value is incremented by one for frozen threads. If the value is zero, the thread is allowed to run.

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `ULONG`                            | N/A
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 8.1                        | N/A

### See also
 - `NtSuspendThread`
 - `NtResumeThread`

## ThreadHeterogeneousCpuPolicy (36)
Determines heterogeneous (big.LITTLE) scheduling policy for the thread.

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `KHETERO_CPU_POLICY`               | N/A
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 10 TH1 (1507)              | N/A

## ThreadContainerId (37)
Queries the job container ID attached to the thread.

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `GUID`                             | N/A
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 10 TH1 (1507)              | N/A

## ThreadNameInformation (38)
Queries or sets the thread description string.

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `THREAD_NAME_INFORMATION`          | `THREAD_NAME_INFORMATION`
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | `THREAD_SET_LIMITED_INFORMATION`
| Minimal version | Windows 10 TH1 (1507)              | Windows 10 TH1 (1507)

### Related Win32 API
 - [`GetThreadDescription`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getthreaddescription)
 - [`SetThreadDescription`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setthreaddescription)

## ThreadSelectedCpuSets (39)

## ThreadSystemThreadInformation (40)
Queries various information (exit status, times, priority, etc.) for the thread, returning the same structure as used when enumerating processes/threads via `NtQuerySystemInformation`.

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `SYSTEM_THREAD_INFORMATION`        | N/A
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 10 TH1 (1507)              | N/A

## ThreadActualGroupAffinity (41)

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `GROUP_AFFINITY`                   | N/A
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 10 TH2 (1511)              | N/A

## ThreadDynamicCodePolicyInfo (42)
Checks or applies exemptions for dynamic code policy (the [Arbitrary Code Guard](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/exploit-protection-reference?view=o365-worldwide#arbitrary-code-guard) mitigation).

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `ULONG` or `BOOL`                  | `ULONG` or `BOOL`
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | N/A (`NtCurrentThread` only)
| Minimal version | Windows 10 TH2 (1511)              | Windows 10 TH2 (1511)

## ThreadExplicitCaseSensitivity (43)
Configures explicit case-sensitivity for the thread.

|                    | Query                              | Set
| ------------------ | ---------------------------------- | ---
| Type               | `ULONG` or `BOOL`                  | `ULONG` or `BOOL`
| Required access    | `THREAD_QUERY_LIMITED_INFORMATION` | `THREAD_SET_INFORMATION`
| Required privilege | None                               | `SeDebugPrivilege`
| Minimal version    | Windows 10 TH2 (1511)              | Windows 10 TH2 (1511)

## ThreadWorkOnBehalfTicket (44)

## ThreadSubsystemInformation (45)
Determines the subsystem of the thread.

|                 | Query                              | Set
| --------------- | ---------------------------------- | ---
| Type            | `SUBSYSTEM_INFORMATION_TYPE`       | N/A
| Required access | `THREAD_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 10 RS2 (1703)              | N/A

## ThreadDbgkWerReportActive (46)
Enables or disables Windows Error Reporting on the thread.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `ULONG` or `BOOL`
| Required access | N/A   | `THREAD_SET_INFORMATION`
| Minimal version | N/A   | Windows 10 RS2 (1703)

## ThreadAttachContainer (47)

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | Job `HANDLE` with `JOB_OBJECT_IMPERSONATE` access
| Required access | N/A   | N/A (`NtCurrentThread` only)
| Minimal version | N/A   | Windows 10 RS2 (1703)

## ThreadManageWritesToExecutableMemory (48)

## ThreadPowerThrottlingState (49)

## ThreadWorkloadClass (50)

## ThreadCreateStateChange (51)

## ThreadApplyStateChange (52)

## ThreadStrongerBadHandleChecks (53)

## ThreadEffectiveIoPriority (54)

## ThreadEffectivePagePriority (55)
