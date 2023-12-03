This enumeration defines types of information that can be queried or set for processes.

# Applicable to
 - `NtQueryInformationProcess`
 - `NtSetInformationProcess`

# Members

## ProcessBasicInformation (0)
Retrieves various information about the process, such as its ID, its parent ID, exit status, and `PEB` address.

|                 | Query                                                               | Set
| --------------- | ------------------------------------------------------------------- | ---
| Type            | `PROCESS_BASIC_INFORMATION` or `PROCESS_EXTENDED_BASIC_INFORMATION` | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION`                                 | N/A

### Remarks
The extended structure was introduced in Windows 8.

### Related Win32 API
 - [`GetExitCodeProcess`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getexitcodeprocess)
 - [`GetProcessId`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessid)

## ProcessQuotaLimits (1)
Retrieves or adjusts quota limits for the process.

|                    | Query                               | Set
| ------------------ | ----------------------------------- | ---
| Type               | `QUOTA_LIMITS` or `QUOTA_LIMITS_EX` | `QUOTA_LIMITS` or `QUOTA_LIMITS_EX`
| Required access    | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_QUOTA`
| Required privilege | None                                | `SeIncreaseBasePriorityPrivilege` or `SeIncreaseWorkingSetPrivilege`

### Related Win32 API
 - [`GetProcessWorkingSetSizeEx`](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-getprocessworkingsetsizeex)
 - [`SetProcessWorkingSetSizeEx`](https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-setprocessworkingsetsizeex)

## ProcessIoCounters (2)
Retrieves I/O operation statistics for the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `IO_COUNTERS`                       | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A

## ProcessVmCounters (3)
Retrieves virtual memory statistics for the process.

|                 | Query                                                 | Set
| --------------- | ----------------------------------------------------- | ---
| Type            | `VM_COUNTERS`, `VM_COUNTERS_EX`, or `VM_COUNTERS_EX2` | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION`                   | N/A

## ProcessTimes (4)
Retrieves combined timing information for all threads in the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `KERNEL_USER_TIMES`                 | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A

### Related Win32 API
 - [`GetProcessTimes`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocesstimes)

### See also
 - `ProcessCycleTime` (38)
 - `ProcessUptimeInformation` (88)

## ProcessBasePriority (5)
Sets the base priority for all threads in the process.

|                    | Query | Set
| ------------------ | ----- | ---
| Type               | N/A   | `KPRIORITY`
| Required access    | N/A   | `PROCESS_SET_INFORMATION`
| Required privilege | N/A   | `SeIncreaseBasePriorityPrivilege`

### Remarks
The highest order bit specifies the memory priority; the rest specify the scheduling priority.

## ProcessRaisePriority (6)
Increases the base priority for all threads in the process by the specified amount, up to the maximum non-realtime priority.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `ULONG`
| Required access | N/A   | `PROCESS_SET_INFORMATION`

## ProcessDebugPort (7)
Determined if the process is being debugged.

|                 | Query                       | Set
| --------------- | --------------------------- | ---
| Type            | `LONG_PTR`                  | N/A
| Required access | `PROCESS_QUERY_INFORMATION` | N/A

### Remarks
The query returns `-1` if the process has an associated debug object and `0` otherwise.

### Related Win32 API
 - [`CheckRemoteDebuggerPresent`](https://learn.microsoft.com/en-us/windows/win32/api/debugapi/nf-debugapi-checkremotedebuggerpresent)

## ProcessExceptionPort (8)

|                    | Query | Set
| ------------------ | ----- | ---
| Type               | N/A   | `PROCESS_EXCEPTION_PORT`
| Required access    | N/A   | `PROCESS_SUSPEND_RESUME` + no specific access on the port handle
| Required privilege | N/A   | `SeTcbPrivilege`

## ProcessAccessToken (9)
Replaces the primary token of the process.

|                    | Query | Set
| ------------------ | ----- | ---
| Type               | N/A   | `PROCESS_ACCESS_TOKEN`
| Required access    | N/A   | `PROCESS_SET_INFORMATION` + `TOKEN_ASSIGN_PRIMARY` on the token
| Required privilege | N/A   | `SeAssignPrimaryTokenPrivilege`

### Notable return values
 - `STATUS_BAD_TOKEN_TYPE` - the caller provided an impersonation token while the operation requires a primary token.
 - `STATUS_NOT_SUPPORTED` - the caller attempted to replace a token on a process that has already started executing or has more than one thread. The operation only works on newly created suspended processes.
 - `STATUS_TOKEN_ALREADY_IN_USE` - the caller provided a token that is already assigned as a primary token for another process.

### Remarks
The privilege is required when the specified token is not a child or a sibling of the caller's token or has a higher integrity level.

### See also
 - `NtSetInformationThread` with `THREADINFOCLASS` value of `ThreadImpersonationToken` (5)

## ProcessLdtInformation (10)
Retrieves or modifies Local Descriptor Table information for the process. This information class has no effect on modern versions of Windows.

|                 | Query                                          | Set
| --------------- | ---------------------------------------------- | ---
| Type            | `PROCESS_LDT_INFORMATION`                      | `PROCESS_LDT_INFORMATION`
| Required access | `PROCESS_QUERY_INFORMATION \| PROCESS_VM_READ` | `PROCESS_SET_INFORMATION \| PROCESS_VM_WRITE`

## ProcessLdtSize (11)
Adjusts the size of the Local Descriptor Table for the process. This information class has no effect on modern versions of Windows.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `PROCESS_LDT_SIZE`
| Required access | N/A   | `PROCESS_SET_INFORMATION \| PROCESS_VM_WRITE`

## ProcessDefaultHardErrorMode (12)
Retrieves or sets the default mode for handling hard errors.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `ULONG`                             | `ULONG`
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_INFORMATION`

### Related Win32 API
 - [`GetErrorMode`](https://learn.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-geterrormode)
 - [`SetErrorMode`](https://learn.microsoft.com/en-us/windows/win32/api/errhandlingapi/nf-errhandlingapi-seterrormode)

### See also
 - `NtRaiseHardError`

## ProcessIoPortHandlers (13)
Allows drivers to install a handler that traps I/O of a 16-bit process. This information class is not implemented on modern versions of Windows.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `PROCESS_IO_PORT_HANDLER_INFORMATION`
| Required access | N/A   | `PROCESS_SET_INFORMATION`
| Required mode   | N/A   | Kernel mode

## ProcessPooledUsageAndLimits (14)
Determines pool memory usage and limits for the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `POOLED_USAGE_AND_LIMITS`           | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A

## ProcessWorkingSetWatch (15)
Enables working set watch that allows monitoring page faults that occur in the specified process.

|                    | Query                            | Set
| ------------------ | -------------------------------- | ---
| Type               | `PROCESS_WS_WATCH_INFORMATION[]` | void (zero-size)
| Required access    | `PROCESS_QUERY_INFORMATION`      | `PROCESS_SET_INFORMATION`
| Required integrity | Medium                           | None

### Notable return values
 - `STATUS_PORT_ALREADY_SET` - the caller attempted to enable the working set watch while it is already enabled for the process.
 - `STATUS_UNSUCCESSFUL` - the caller attempted to query information when the working set watch is not enabled for the process.
 - `STATUS_NO_MORE_ENTRIES` - there are no new faults to query.

### Remarks
Once enabled, WS watch cannot be disabled.

When the Restrict-Kernel-Address-Leaks feature is enabled and the caller doesn't have `SeDebugPrivilege`, the system removes kernel addresses from the returned data.

### See also
 - `ProcessWorkingSetWatchEx` (42)

## ProcessUserModeIOPL (16)
Sets user-mode I/O privilege level for the process. This information class is not implemented on modern versions of Windows.

|                    | Query | Set
| ------------------ | ----- | ---
| Type               | N/A   | `ULONG`
| Required access    | N/A   | `PROCESS_SET_INFORMATION`
| Required privilege | N/A   | `SeTcbPrivilege`

## ProcessEnableAlignmentFaultFixup (17)
Enables or disables automatic memory alignment fixup on certain processor architectures for the process.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `BOOLEAN`
| Required access | N/A   | `PROCESS_SET_INFORMATION`

### Remarks
Using this information class is equivalent to setting or clearing the `SEM_NOALIGNMENTFAULTEXCEPT` flag via the `ProcessDefaultHardErrorMode` (12) info class.

## ProcessPriorityClass (18)
Retrieves or adjust the priority class for the process.

|                    | Query                               | Set
| ------------------ | ----------------------------------- | ---
| Type               | `PROCESS_PRIORITY_CLASS`            | `PROCESS_PRIORITY_CLASS`
| Required access    | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_INFORMATION`
| Required privilege | None                                | `SeIncreaseBasePriorityPrivilege`

### Known values
 - `PROCESS_PRIORITY_CLASS_UNKNOWN`
 - `PROCESS_PRIORITY_CLASS_IDLE`
 - `PROCESS_PRIORITY_CLASS_BELOW_NORMAL`
 - `PROCESS_PRIORITY_CLASS_NORMAL`
 - `PROCESS_PRIORITY_CLASS_ABOVE_NORMAL`
 - `PROCESS_PRIORITY_CLASS_HIGH`
 - `PROCESS_PRIORITY_CLASS_REALTIME`

### Remarks
The privilege is required only when setting the priority class to realtime.

The system ignores the request if the process's job object specifies a conflicting value via `JOB_OBJECT_LIMIT_PRIORITY_CLASS`.

### Related Win32 API
 - [`SetPriorityClass`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setpriorityclass)

### See also
 - `ProcessForegroundInformation` (25)
 - `ProcessPriorityClassEx` (108)

## ProcessWx86Information (19)
This information classes accesses the `EPROCESS->VdmAllowed` flag for the process.

|                    | Query                       | Set
| ------------------ | --------------------------- | ---
| Type               | `ULONG` or `BOOL`           | `ULONG` or `BOOL`
| Required access    | `PROCESS_QUERY_INFORMATION` | `PROCESS_SET_INFORMATION`
| Required privilege | None                        | `SeTcbPrivilege`

## ProcessHandleCount (20)
Determines the current and historical highest number of handles for the process.

|                 | Query                                   | Set
| --------------- | --------------------------------------- | ---
| Type            | `ULONG` or `PROCESS_HANDLE_INFORMATION` | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION`     | N/A

### Remarks
To retrieve handle values, use the `ProcessHandleInformation` (51) info class.

### Related Win32 API
 - [`GetProcessHandleCount`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocesshandlecount)

### See also
 - `NtQuerySystemInformation` with `SYSTEM_INFORMATION_CLASS` value of `SystemExtendedHandleInformation` (64)
 - `NtQueryObject` with `OBJECT_INFORMATION_CLASS` value of `ObjectTypeInformation` (2)

## ProcessAffinityMask (21)
Enumerates or limits on which processors the threads from the specified process are allowed to run.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `KAFFINITY` or `GROUP_AFFINITY`     | `KAFFINITY` or `GROUP_AFFINITY`
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_INFORMATION`

### Related Win32 API
 - [`SetProcessAffinityMask`](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setprocessaffinitymask)
 - [`SetProcessAffinityUpdateMode`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessaffinityupdatemode)

### See also
 - `ProcessAffinityUpdateMode` (45)
 - `THREADINFOCLASS` values `ThreadAffinityMask` (4) and `ThreadGroupInformation` (30)

## ProcessPriorityBoost (22)
Enables or disables priority boosting for the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `ULONG` or `BOOL`                   | `ULONG` or `BOOL`
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_INFORMATION`

### Related Win32 API
 - [`GetProcessPriorityBoost`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocesspriorityboost)
 - [`SetProcessPriorityBoost`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocesspriorityboost)

## ProcessDeviceMap (23)
Enumerates defined drives in the DOS Devices directory and allows replacing the device map directory for the process.

|                    | Query                                                                   | Set
| ------------------ | ----------------------------------------------------------------------- | ---
| Type               | `PROCESS_DEVICEMAP_INFORMATION` or `PROCESS_DEVICEMAP_INFORMATION_EX`   | `PROCESS_DEVICEMAP_INFORMATION` or `PROCESS_DEVICEMAP_INFORMATION_EX`
| Required access    | `PROCESS_QUERY_INFORMATION`                                             | `PROCESS_SET_INFORMATION` + `DIRECTORY_TRAVERSE` on the directory handle
| Required integrity | None                                                                    | Medium

### Remarks
But default, processes use per-logon session DOS Devices directories `\Sessions\0\DosDevices\{xxxxxxxx-xxxxxxxx}` with names derived from the token's logon session LUID.

When using `PROCESS_DEVICEMAP_INFORMATION_EX` to query information, the caller must initialize the `Flags` field first. See the documentation of the structure for more details.

### Related Win32 API
 - [`DriveType`](https://learn.microsoft.com/en-us/windows/win32/api/shlobj_core/nf-shlobj_core-drivetype)

### See also
 - `OBJ_IGNORE_IMPERSONATED_DEVICEMAP`

## ProcessSessionInformation (24)
Retrieves the session ID of the process. Changing the value is not supported on modern versions of Windows.

|                    | Query                               | Set
| ------------------ | ----------------------------------- | ---
| Type               | `PROCESS_SESSION_INFORMATION`       | `PROCESS_SESSION_INFORMATION`
| Required access    | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_INFORMATION \| PROCESS_SET_SESSIONID`
| Required privilege | None                                | `SeTcbPrivilege`

### Related Win32 API
 - [`ProcessIdToSessionId`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-processidtosessionid)

### See also
 - `NtQueryInformationToken` with `TOKEN_INFORMATION_CLASS` value of `TokenSessionId` (12)

## ProcessForegroundInformation (25)
Switches the process's priority class between foreground and background.

|                    | Query | Set
| ------------------ | ----- | ---
| Type               | N/A   | `PROCESS_FOREGROUND_BACKGROUND`
| Required access    | N/A   | `PROCESS_SET_LIMITED_INFORMATION`

### See also
 - `ProcessPriorityClass` (18)
 - `ProcessPriorityClassEx` (108)

## ProcessWow64Information (26)
Retrieves the address of the WoW64 `PEB` (`PEB32`) for the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `ULONG_PTR` or `PPEB32`             | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A

### Remarks
The system returns `NULL` if the target process is not running under WoW64.

### Related Win32 API
 - [`IsWow64Process`](https://learn.microsoft.com/en-us/windows/win32/api/wow64apiset/nf-wow64apiset-iswow64process)

### See also
 - `NtQuerySystemInformationEx` with `SYSTEM_INFORMATION_CLASS` values of `SystemSupportedProcessorArchitectures` (181) and `SystemSupportedProcessorArchitectures2` (230)

## ProcessImageFileName (27)
Retrieves the image filename associated with the process in the native format.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `UNICODE_STRING`                    | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A

### Remarks
The system populates this string by looking up the name from the file object during process creation and doesn’t track subsequent renames. The field holds `NULL` pointer if the system failed to retrieve the value.

### See also
 - `ProcessImageFileNameWin32` (43)
 - `NtQueryVirtualMemory` with `MEMORY_INFORMATION_CLASS` value of `MemoryMappedFilenameInformation` (2)

## ProcessLUIDDeviceMapsEnabled (28)
Determines if the LUID device maps are enabled for the process. This info class always returns `TRUE` on modern versions of Windows.

|                 | Query             | Set
| --------------- | ----------------- | ---
| Type            | `ULONG` or `BOOL` | N/A
| Required access | None              | N/A

## ProcessBreakOnTermination (29)
Retrieves or sets the critical status for the process. Termination of a critical process causes a BSOD.

|                    | Query                               | Set
| ------------------ | ----------------------------------- | ---
| Type               | `ULONG` or `BOOL`                   | `ULONG` or `BOOL`
| Required access    | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_INFORMATION`
| Required privilege | None                                | `SeDebugPrivilege`

### Related Win32 API
 - [`IsProcessCritical`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-isprocesscritical)
 
### See also
 - `RtlSetProcessIsCritical`

## ProcessDebugObjectHandle (30)
Opens a handle to process's debug port object.

|                 | Query                       | Set
| --------------- | --------------------------- | ---
| Type            | `HANDLE`                    | N/A
| Required access | `PROCESS_QUERY_INFORMATION` | N/A

### Notable return values
 - `STATUS_PORT_NOT_SET` - the process is not being debugged at the moment, so it has no associated debug object.
 - `STATUS_PROCESS_IS_PROTECTED` - the caller attempted to open a debug object of a process with a higher protection level.

### Remarks
Opening the debug object requires passing an access check on its security descriptor and will return `MAXIMUM_ALLOWED` access on the handle or fail with `STATUS_ACCESS_DENIED`.

## ProcessDebugFlags (31)
Retrieves or sets a bit mask of debugging-related flags for the process.

|                 | Query                       | Set
| --------------- | --------------------------- | ---
| Type            | `ULONG`                     | `ULONG`
| Required access | `PROCESS_QUERY_INFORMATION` | `PROCESS_SET_INFORMATION`

### Known flags
 - `PROCESS_INHERIT_DEBUG` - when set, makes child processes inherit debugging.

## ProcessHandleTracing (32)
Allows collecting handle tracing information for the process. The trace records open, close, and bad reference operations on handles.

|                    | Query                            | Set
| ------------------ | -------------------------------- | ---
| Type               | `PROCESS_HANDLE_TRACING_QUERY`   | `PROCESS_HANDLE_TRACING_ENABLE` or `PROCESS_HANDLE_TRACING_ENABLE_EX` or void (zero-sized buffer) to disable
| Required access    | `PROCESS_QUERY_INFORMATION`      | `PROCESS_SET_INFORMATION`
| Required integrity | Medium                           | None

### Remarks
The system rounds the specified number of slots up to the closest power of two between 0x80 and 0x20000. Specifying a zero value (do not confuse with providing a zero-sized buffer) defaults it to 0x1000.

When querying, the caller can specify a non-NULL value in the `Handle` field to filter the output.

When the Restrict-Kernel-Address-Leaks feature is enabled, querying handle tracing information requires `SeDebugPrivilege`.

### See also
 - `ProcessHandleInformation` (51)

## ProcessIoPriority (33)
Retrieves or sets the priority for I/O operations issued by the process.

|                    | Query                               | Set
| ------------------ | ----------------------------------- | ---
| Type               | `IO_PRIORITY_HINT`                  | `IO_PRIORITY_HINT`
| Required access    | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_INFORMATION`
| Required privilege | None                                | `SeIncreaseBasePriorityPrivilege`

### See also
 - `ProcessEffectiveIoPriority` (110)

## ProcessExecuteFlags (34)
Retrieves or modifies the bit mask of Data Execution Prevention (DEP) options for the process.

|                 | Query                       | Set
| --------------- | --------------------------- | ---
| Type            | `ULONG`                     | `ULONG`
| Required access | `PROCESS_QUERY_INFORMATION` | N/A (`NtCurrentProcess` only)

### Known values
 - `MEM_EXECUTE_OPTION_ENABLE`
 - `MEM_EXECUTE_OPTION_DISABLE`
 - `MEM_EXECUTE_OPTION_DISABLE_THUNK_EMULATION`
 - `MEM_EXECUTE_OPTION_PERMANENT`
 - `MEM_EXECUTE_OPTION_EXECUTE_DISPATCH_ENABLE`
 - `MEM_EXECUTE_OPTION_IMAGE_DISPATCH_ENABLE`
 - `MEM_EXECUTE_OPTION_DISABLE_EXCEPTION_CHAIN_VALIDATION`

### Remarks
Trying to modify the options when the permanent bit is already set fails the request with `STATUS_ACCESS_DENIED`.

### Related Win32 API
 - [`GetProcessMitigationPolicy`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessmitigationpolicy)

## ProcessTlsInformation (35)
This information class is not implemented on modern versions of Windows.

## ProcessCookie (36)
Retrieves the cookie value for the process.

|                 | Query              | Set
| --------------- | ------------------ | ---
| Type            | `ULONG`            | N/A
| Required access | `PROCESS_VM_WRITE` | N/A

### Remarks
If the value haven't been queried before, it will be initialized.

### Related Win32 API
 - [`DecodePointer`](https://learn.microsoft.com/en-us/previous-versions/bb432242(v%3Dvs.85))
 - [`EncodePointer`](https://learn.microsoft.com/en-us/previous-versions/bb432254(v=vs.85))

### See also
 - `RtlDecodePointer`
 - `RtlEncodePointer`
 - `RtlDecodeRemotePointer`
 - `RtlEncodeRemotePointer`

## ProcessImageInformation (37)
Retrieves information about the executable image section used to create the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `SECTION_IMAGE_INFORMATION`         | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A

### Related Win32 API
 - [`GetProcessVersion`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessversion)

### See also
 - `NtQuerySection` with `SECTION_INFORMATION_CLASS` value of `SectionImageInformation` (1)

## ProcessCycleTime (38)
Retrieves the number of cycles spent by all threads of the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `PROCESS_CYCLE_TIME_INFORMATION`    | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A

### Related Win32 API
 - [`QueryProcessCycleTime`](https://learn.microsoft.com/en-us/windows/win32/api/realtimeapiset/nf-realtimeapiset-queryprocesscycletime)

### See also
 - `ProcessTimes` (4)
 - `ProcessUptimeInformation` (88)

## ProcessPagePriority (39)
Retrieves or adjusts paging priority for the process

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `PAGE_PRIORITY_INFORMATION`         | `PAGE_PRIORITY_INFORMATION`
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_INFORMATION`

### Related Win32 API
 - [`GetProcessInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessinformation)
 - [`SetProcessInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessinformation)

### See also
 - `ProcessEffectivePagePriority` (111)

## ProcessInstrumentationCallback (40)
Sets the instrumentation callback for the process.

|                    | Query | Set
| ------------------ | ----- | ---
| Type               | N/A   | `PVOID` or `PROCESS_INSTRUMENTATION_CALLBACK_INFORMATION`
| Required access    | N/A   | `PROCESS_SET_INFORMATION`
| Required privilege | N/A   | `SeDebugPrivilege`

### Remarks
The instrumentation callback executes on every transition from kernel to user mode, such as on syscall returns. Instead of returning to the intended location, the thread jumps to the callback which receives the original target in the `r10` register. You can read more about using instrumentation callbacks [in this blog](https://splintercod3.blogspot.com/p/weaponizing-mapping-injection-with.html).

Installing the callback for the current process does not require any privileges.

## ProcessThreadStackAllocation (41)
Reserves memory for an additional thread stack in the current process.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `PROCESS_STACK_ALLOCATION_INFORMATION` or `PROCESS_STACK_ALLOCATION_INFORMATION_EX`
| Required access | N/A   | N/A (`NtCurrentProcess` only)

### See also
 - `NtAllocateVirtualMemory`

## ProcessWorkingSetWatchEx (42)
Enables working set watch that allows monitoring page faults that occur in the specified process.

|                    | Query                               | Set
| ------------------ | ----------------------------------- | ---
| Type               | `PROCESS_WS_WATCH_INFORMATION_EX[]` | void (zero-size)
| Required access    | `PROCESS_QUERY_INFORMATION`         | `PROCESS_SET_INFORMATION`
| Required integrity | Medium                              | None

### Notable return values
 - `STATUS_PORT_ALREADY_SET` - the caller attempted to enable the working set watch while it is already enabled for the process.
 - `STATUS_UNSUCCESSFUL` - the caller attempted to query information when the working set watch is not enabled for the process.
 - `STATUS_NO_MORE_ENTRIES` - there are no new faults to query.

### Remarks
Once enabled, WS watch cannot be disabled.

When the Restrict-Kernel-Address-Leaks feature is enabled and the caller doesn't have `SeDebugPrivilege`, the system removes kernel addresses from the returned data.

### See also
 - `ProcessWorkingSetWatch` (15)

## ProcessImageFileNameWin32 (43)
Retrieves the image filename associated with the process in the Win32 format.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `UNICODE_STRING`                    | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A

### Remarks
The system dynamically retrieves this string from the file object associated with the process. Therefore, it tracks rename operations. The query results in an error if the file doesn’t have a valid Win32 name or has been deleted.

### See also
 - `ProcessImageFileName` (27)
 - `NtQueryVirtualMemory` with `MEMORY_INFORMATION_CLASS` value of `MemoryMappedFilenameInformation` (2)

## ProcessImageFileMapping (44)
Checks if the file used to create the process is the same as the specified file.

|                 | Query                                                                   | Set
| --------------- | ----------------------------------------------------------------------- | ---
| Type            | `HANDLE` to a file                                                      | N/A
| Required access | `PROCESS_QUERY_INFORMATION` + `FILE_EXECUTE \| SYNCHRONIZE` on the file | N/A

### Notable return values
 - `STATUS_SUCCESS` - the specified handle points to the same the file used to create the process.
 - `STATUS_UNSUCCESSFUL` - the files differ or the original file of the process is not available anymore.

### Remarks
Despite being used with `NtQueryInformationProcess`, this information class reads the provided buffer and does not write anything back.

The files are considered the same if they share `SectionObjectPointer`.

## ProcessAffinityUpdateMode (45)
Retrieves or sets the affinity update mode for the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `PROCESS_AFFINITY_UPDATE_MODE`      | `PROCESS_AFFINITY_UPDATE_MODE`
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A (`NtCurrentProcess` only)

### Related Win32 API
 - [`QueryProcessAffinityUpdateMode`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-queryprocessaffinityupdatemode)

### See also
 - `ProcessAffinityMask` (21)

## ProcessMemoryAllocationMode (46)
Retrieves or sets the memory allocation mode for the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `PROCESS_MEMORY_ALLOCATION_MODE`    | `PROCESS_MEMORY_ALLOCATION_MODE`
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_INFORMATION`

## ProcessGroupInformation (47)
Retrieves thread affinity to processors and processor groups.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `USHORT[]`                          | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A

### Related Win32 API
 - [`GetProcessGroupAffinity`](https://learn.microsoft.com/en-us/windows/win32/api/processtopologyapi/nf-processtopologyapi-getprocessgroupaffinity)

## ProcessTokenVirtualizationEnabled (48)
Enables or disables UAC filesystem and registry virtualization on the process's primary token.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `ULONG` or `BOOL`
| Required access | N/A   | `PROCESS_SET_INFORMATION`

### Remarks
This information class does not require the caller to pass additional access checks on the token.

### See also
 - `NtSetInformationToken` with `TOKEN_INFORMATION_CLASS` value of `TokenVirtualizationEnabled` (24)

## ProcessConsoleHostProcess (49)
Retrieves or sets the PID of the associated console host for the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `ULONG_PTR`                         | `ULONG_PTR`
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A (`NtCurrentProcess` only)

### Remarks
The system uses the two lower bits of the PID as flags. The lowest bit must be set for the request to succeed.

This information class was previously known as `ProcessOwnerInformation`.

## ProcessWindowInformation (50)
Reads windows flags and title information from the process parameters (`RTL_USER_PROCESS_PARAMETERS`) from `PEB` of the specified process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `PROCESS_WINDOW_INFORMATION`        | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A

### Remarks
Note that this information class fails to parse denormalized process parameters (the ones that don't have the `RTL_USER_PROC_PARAMS_NORMALIZED` flag set).

## ProcessHandleInformation (51)
Enumerates the handle table of the process.

|                 | Query                                 | Set
| --------------- | ------------------------------------- | ---
| Type            | `PROCESS_HANDLE_SNAPSHOT_INFORMATION` | N/A
| Required access | `PROCESS_QUERY_INFORMATION`           | N/A
| Minimal version | Windows 8                             | N/A

### See also
 - `ProcessHandleCount` (20)
 - `NtQuerySystemInformation` with `SYSTEM_INFORMATION_CLASS` value of `SystemExtendedHandleInformation` (64)

## ProcessMitigationPolicy (52)
Retrieves or adjusts various mitigation policies for the process.

|                 | Query                                   | Set
| --------------- | --------------------------------------- | ---
| Type            | `PROCESS_MITIGATION_POLICY_INFORMATION` | `PROCESS_MITIGATION_POLICY_INFORMATION`
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION`     | `PROCESS_SET_INFORMATION` for `ProcessDynamicCodePolicy` and `NtCurrentProcess`-only otherwise
| Minimal version | Windows 8                               | Windows 8

### Remarks
See [Exploit Protection Reference](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/exploit-protection-reference) for more details on mitigation policies.

### Related Win32 API
 - [`GetProcessMitigationPolicy`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessmitigationpolicy)
 - [`SetProcessMitigationPolicy`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessmitigationpolicy)

## ProcessDynamicFunctionTableInformation (53)
Adds or removes dynamic function table entries for the current process.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `PROCESS_DYNAMIC_FUNCTION_TABLE_INFORMATION`
| Required access | N/A   | N/A (`NtCurrentProcess` only)
| Minimal version | N/A   | Windows 8

## ProcessHandleCheckingMode (54)
Retrieves or sets whether the system should generate exceptions on invalid handle operations for the process.

|                 | Query                       | Set
| --------------- | --------------------------- | ---
| Type            | `ULONG` or `BOOL`           | `ULONG` or `BOOL`
| Required access | `PROCESS_QUERY_INFORMATION` | `PROCESS_SET_INFORMATION`
| Minimal version | Windows 8                   | Windows 8

### Related Win32 API
 - [`SetProcessMitigationPolicy`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessmitigationpolicy)

### See also
 - `ProcessRaiseUMExceptionOnInvalidHandleClose` (71)

## ProcessKeepAliveCount (55)
Retrieves the wake (keep-alive) counter for the process.

|                 | Query                                 | Set
| --------------- | ------------------------------------- | ---
| Type            | `PROCESS_KEEPALIVE_COUNT_INFORMATION` | N/A
| Required access | `PROCESS_QUERY_INFORMATION`           | N/A
| Minimal version | Windows 8                             | N/A

## ProcessRevokeFileHandles (56)
Revokes file handles on the specified device from an AppContainer process,

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `PROCESS_REVOKE_FILE_HANDLES_INFORMATION`
| Required access | N/A   | `PROCESS_SET_LIMITED_INFORMATION`
| Minimal version | N/A   | Windows 8

### Remarks
Trying to perform file operations on a revoked handle fails with `STATUS_FILE_HANDLE_REVOKED`.

Handle revocation has no effect on non-AppContainer processes.

## ProcessWorkingSetControl (57)
Perform an operation on the working set of the process

|                    | Query | Set
| ------------------ | ----- | ---
| Type               | N/A   | `PROCESS_WORKING_SET_CONTROL`
| Required access    | N/A   | `PROCESS_SET_LIMITED_INFORMATION`
| Required privilege | N/A   | `SeDebugPrivilege`
| Minimal version    | N/A   | Windows 8

## ProcessHandleTable (58)
Enumerate handle values present in the handle table of the process.

|                 | Query                                             | Set
| --------------- | ------------------------------------------------- | ---
| Type            | `ULONG[]`                                         | N/A
| Required access | `PROCESS_QUERY_INFORMATION \| PROCESS_DUP_HANDLE` | N/A
| Minimal version | Windows 8.1                                       | N/A

### See also
 - `ProcessHandleCount` (20)
 - `ProcessHandleInformation` (51)
 - `NtQuerySystemInformation` with `SYSTEM_INFORMATION_CLASS` value of `SystemExtendedHandleInformation` (64)

## ProcessCheckStackExtentsMode (59)
Retrieve or set whether the system should verify that the stack pointer belongs to the stack on context changes for the process. This info class accesses the `KPROCESS->CheckStackExtents` field.

|                    | Query                       | Set
| ------------------ | --------------------------- | ---
| Type               | `ULONG` or `BOOL`           | `ULONG` or `BOOL`
| Required access    | `PROCESS_QUERY_INFORMATION` | `PROCESS_SET_INFORMATION`
| Required privilege | None                        | `SeDebugPrivilege`
| Minimal version    | Windows 8.1                 | Windows 8.1

## ProcessCommandLineInformation (60)
Reads the command line string from the process parameters (`RTL_USER_PROCESS_PARAMETERS`) from `PEB` of the specified process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `UNICODE_STRING`                    | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 8.1                         | N/A

### Remarks
Note that this information class fails to parse denormalized process parameters (the ones that don't have the `RTL_USER_PROC_PARAMS_NORMALIZED` flag set).

## ProcessProtectionInformation (61)
Retrieves protection level for the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `PS_PROTECTION`                     | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 8.1                         | N/A

### Related Win32 API
 - [`GetProcessInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessinformation)

### See also
 - `PS_ATTRIBUTE_PROTECTION_LEVEL`

## ProcessMemoryExhaustion (62)
Sets whether the system should terminate the process if it fails to commit memory.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `PROCESS_MEMORY_EXHAUSTION_INFO`
| Required access | N/A   | `PROCESS_SET_INFORMATION`
| Minimal version | N/A   | Windows 10 TH1 (1507)

### Related Win32 API
 - [`SetProcessInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessinformation)

## ProcessFaultInformation (63)
Reports the process crash.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `PROCESS_FAULT_INFORMATION`
| Required access | N/A   | `PROCESS_SET_INFORMATION`
| Minimal version | N/A   | Windows 10 TH1 (1507)

## ProcessTelemetryIdInformation (64)
Retrieves many various properties of the process for telemetry collection.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `PROCESS_TELEMETRY_ID_INFORMATION`  | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 10 TH1 (1507)               | N/A

### See also
 - `ProcessBasicInformation` (0)

## ProcessCommitReleaseInformation (65)
Retrieves or sets whether the process is eligible for automatic commit memory releasing.

|                 | Query                                | Set
| --------------- | ------------------------------------ | ---
| Type            | `PROCESS_COMMIT_RELEASE_INFORMATION` | `PROCESS_COMMIT_RELEASE_INFORMATION`
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION`  | `PROCESS_SET_LIMITED_INFORMATION \| PROCESS_TERMINATE`
| Minimal version | Windows 10 TH1 (1507)                | Windows 10 TH1 (1507)

## ProcessDefaultCpuSetsInformation (66)
Retrieves or sets the default CPU Sets assignment for threads in the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `SYSTEM_CPU_SET_INFORMATION[5]`     | `SYSTEM_CPU_SET_INFORMATION[5]`
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_LIMITED_INFORMATION`
| Minimal version | Windows 10 TH1 (1507)               | Windows 10 TH1 (1507)

### Related Win32 API
 - [`GetProcessDefaultCpuSetMasks`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessdefaultcpusetmasks)
 - [`SetProcessDefaultCpuSetMasks`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessdefaultcpusetmasks)
 - [`GetProcessDefaultCpuSets`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessdefaultcpusets)
 - [`SetProcessDefaultCpuSets`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessdefaultcpusets)

## ProcessAllowedCpuSetsInformation (67)
Retrieves or sets the allowed CPU Sets assignment for threads in the process.

|                    | Query                               | Set
| ------------------ | ----------------------------------- | ---
| Type               | `SYSTEM_CPU_SET_INFORMATION[5]`     | `SYSTEM_CPU_SET_INFORMATION[5]`
| Required access    | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_LIMITED_INFORMATION`
| Required privilege | N/A                                 | `SeIncreaseBasePriorityPrivilege`
| Minimal version    | Windows 10 TH1 (1507)               | Windows 10 TH1 (1507)

### Remarks
The system doesn't requires the caller to have the privilege if it can pass an access check against `ExpCpuSetSecurityDescriptor` which grants access to `NT AUTHORITY\SYSTEM` and `NT SERVICE\Audiosrv`.

## ProcessSubsystemProcess (68)
Marks the process as the Subsystem Process. This info class sets the `EPROCESS->SubsystemProcess` flag.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | void (zero-size)
| Required access | N/A   | `PROCESS_SET_INFORMATION`
| Minimal version | N/A   | Windows 10 TH1 (1507)

### Remarks
The caller must be the session master. Otherwise, the operation fails with `STATUS_PRIVILEGE_NOT_HELD`.

## ProcessJobMemoryInformation (69)
Retrieves memory statistics and limits from the process's job object.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `PROCESS_JOB_MEMORY_INFO`           | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 10 TH1 (1507)               | N/A

### Notable return values
 - `STATUS_ERROR_PROCESS_NOT_IN_JOB` - the process has no associated job objects.

## ProcessInPrivate (70)
Retrieves or sets whether trace sessions with `EVENT_ENABLE_PROPERTY_EXCLUDE_INPRIVATE` flag should drop all events from the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `BOOLEAN`                           | void (zero-size)
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_INFORMATION`
| Minimal version | Windows 10 TH2 (1511)               | Windows 10 TH2 (1511)

### Related Win32 API
 - [`GetProcessInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessinformation)
 - [`SetProcessInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessinformation)

## ProcessRaiseUMExceptionOnInvalidHandleClose (71)
Retrieves or sets whether the system should raise user-mode exceptions when the process attempts to close invalid handles.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `ULONG` or `BOOL`                   | `ULONG` or `BOOL`
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_INFORMATION`
| Minimal version | Windows 10 TH2 (1511)               | Windows 10 TH2 (1511)

### See also
 - `ProcessHandleCheckingMode` (54)

## ProcessIumChallengeResponse (72)

## ProcessChildProcessInformation (73)
Retrieves child process creation restriction from the process's primary token.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `PROCESS_CHILD_PROCESS_INFORMATION` | N/A
| Required access | `PROCESS_QUERY_INFORMATION`         | N/A
| Minimal version | Windows 10 TH2 (1511)               | N/A

### See also
 - `NtSetInformationToken` with `TOKEN_INFORMATION_CLASS` value of `TokenChildProcessFlags` (45)
 - `PS_ATTRIBUTE_CHILD_PROCESS_POLICY`

## ProcessHighGraphicsPriorityInformation (74)
Retrieves, enables, or disables high graphics priority for the process.

|                    | Query                               | Set
| ------------------ | ----------------------------------- | ---
| Type               | `BOOLEAN`                           | `BOOLEAN`
| Required access    | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_LIMITED_INFORMATION`
| Required privilege | None                                | `SeTcbPrivilege`
| Minimal version    | Windows 10 TH2 (1511)               | Windows 10 TH2 (1511)

## ProcessSubsystemInformation (75)
Retrieves the subsystem type used by the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `SUBSYSTEM_INFORMATION_TYPE`        | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 10 RS2 (1703)               | N/A

## ProcessEnergyValues (76)
Retrieves energy-related statistics for the process.

|                 | Query                                                       | Set
| --------------- | ----------------------------------------------------------- | ---
| Type            | `PROCESS_ENERGY_VALUES` or `PROCESS_EXTENDED_ENERGY_VALUES` | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION`                         | N/A
| Minimal version | Windows 10 RS2 (1703)                                       | N/A

## ProcessPowerThrottlingState (77)
Retrieves or adjusts power throttling settings for the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `POWER_THROTTLING_PROCESS_STATE`    | `POWER_THROTTLING_PROCESS_STATE`
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_LIMITED_INFORMATION`
| Minimal version | Windows 10 RS2 (1703)               | Windows 10 RS2 (1703)

### Related Win32 API
 - [`GetProcessInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessinformation)
 - [`SetProcessInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessinformation)

## ProcessReserved3Information (78)

## ProcessWin32kSyscallFilterInformation (79)
Retrieves the win32k syscall filter for the process.

|                 | Query                       | Set
| --------------- | --------------------------- | ---
| Type            | `WIN32K_SYSCALL_FILTER`     | N/A
| Required access | `PROCESS_QUERY_INFORMATION` | N/A
| Minimal version | Windows 10 RS2 (1703)       | N/A

### See also
 - `ProcessMitigationPolicy` (52)

## ProcessDisableSystemAllowedCpuSets (80)

|                    | Query | Set
| ------------------ | ----- | ---
| Type               | N/A   | `BOOLEAN`
| Required access    | N/A   | `PROCESS_SET_LIMITED_INFORMATION`
| Required privilege | N/A   | `SeIncreaseBasePriorityPrivilege`
| Minimal version    | N/A   | Windows 10 RS2 (1703)

### Remarks
The system doesn't requires the caller to have the privilege if it can pass an access check against `ExpCpuSetSecurityDescriptor` which grants access to `NT AUTHORITY\SYSTEM` and `NT SERVICE\Audiosrv`.

## ProcessWakeInformation (81)
Allocates wake notification channel for the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `PROCESS_WAKE_INFORMATION`          | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 10 RS2 (1703)               | N/A

## ProcessEnergyTrackingState (82)
Retrieves or sets energy tracking for the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `PROCESS_ENERGY_TRACKING_STATE`     | `PROCESS_ENERGY_TRACKING_STATE`
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_INFORMATION`
| Minimal version | Windows 10 RS2 (1703)               | Windows 10 RS2 (1703)

## ProcessManageWritesToExecutableMemory (83)

## ProcessCaptureTrustletLiveDump (84)

|                 | Query                                                                  | Set
| --------------- | ---------------------------------------------------------------------- | ---
| Type            | `ULONG`                                                                | N/A
| Required access | `PROCESS_QUERY_INFORMATION \| PROCESS_VM_OPERATION \| PROCESS_VM_READ` | N/A
| Minimal version | Windows 10 RS3 (1709)                                                  | N/A

## ProcessTelemetryCoverage (85)
Retrieves or adjusts ETW telemetry coverage for the process.

|                     | Query                               | Set
| ------------------- | ----------------------------------- | ---
| Type                | `TELEMETRY_COVERAGE_HEADER`         | `TELEMETRY_COVERAGE_POINT`
| Required access     | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_INFORMATION \| PROCESS_VM_WRITE`
| Required membership | `BUILTIN\Administrators`            | None
| Minimal version     | Windows 10 RS3 (1709)               | Windows 10 RS3 (1709)

### Related Win32 API
 - [`SetProcessInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessinformation)

### See also
 - `EtwCheckCoverage`
 - `PEB->TelemetryCoverageHeader`

## ProcessEnclaveInformation (86)

## ProcessEnableReadWriteVmLogging (87)
Retrieves, enables, or disables whether EtwTi should log virtual memory read/write operations for the process.

|                     | Query                                     | Set
| ------------------- | ----------------------------------------- | ---
| Type                | `PROCESS_READWRITEVM_LOGGING_INFORMATION` | `PROCESS_READWRITEVM_LOGGING_INFORMATION`
| Required access     | `PROCESS_QUERY_LIMITED_INFORMATION`       | `PROCESS_SET_LIMITED_INFORMATION`
| Required privilege  | None                                      | `SeDebugPrivilege` or `SeTcbPrivilege`
| Required protection | None                                      | PPL Antimalware (Windows 11 only)
| Minimal version     | Windows 10 RS3 (1709)                     | Windows 10 RS3 (1709)

### See also
 - `ProcessEnableLogging` (96)
 - `NtReadVirtualMemory`
 - `NtWriteVirtualMemory`

## ProcessUptimeInformation (88)
Retrieves the uptime statistics for the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `PROCESS_UPTIME_INFORMATION`        | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 10 RS3 (1709)               | N/A

### See also
 - `ProcessTimes` (4)
 - `ProcessCycleTime` (38)

## ProcessImageSection (89)
Opens a handle to the image section associated with the process.

|                 | Query                         | Set
| --------------- | ----------------------------- | ---
| Type            | `HANDLE`                      | N/A
| Required access | N/A (`NtCurrentProcess` only) | N/A
| Minimal version | Windows 10 RS3 (1709)         | N/A

### Remarks
The system requires the caller to pass an access check for `SECTION_QUERY | SECTION_MAP_READ` on the section object and returns a handle with the these rights.

## ProcessDebugAuthInformation (90)

## ProcessSystemResourceManagement (91)
Switches the process between foreground and background resource management.

|                    | Query | Set
| ------------------ | ----- | ---
| Type               | N/A   | `PROCESS_SYSTEM_RESOURCE_MANAGEMENT`
| Required access    | N/A   | `PROCESS_SET_LIMITED_INFORMATION`
| Required privilege | N/A   | `SeTcbPrivilege`
| Minimal version    | N/A   | Windows 10 RS4 (1803)

## ProcessSequenceNumber (92)
Retrieves the unique sequence number of the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `ULONGLONG`                         | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 10 RS4 (1803)               | N/A

## ProcessLoaderDetour (93)

## ProcessSecurityDomainInformation (94)
Retrieves the ID of the security domain for the process. Processes in different security domains are isolated from each other's side-channel attacks.

|                 | Query                                 | Set
| --------------- | ------------------------------------- | ---
| Type            | `PROCESS_SECURITY_DOMAIN_INFORMATION` | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION`   | N/A
| Minimal version | Windows 10 RS5 (1809)                 | N/A

### Notable return values
 - `STATUS_NO_TOKEN` - the security domain of the process is not yet established because its primary token has not been frozen.

### See also
 - `ProcessMitigationPolicy` (52)
 - `ProcessCombineSecurityDomainsInformation` (95)

## ProcessCombineSecurityDomainsInformation (95)
Combines security domains of two processes. Processes in different security domains are isolated from each other's side-channel attacks. This operation changes the security domain of the process passed in the `ProcessHandle` parameter to the security domain of the process passed in the `ProcessInformation` parameter.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `PROCESS_COMBINE_SECURITY_DOMAINS_INFORMATION`
| Required access | N/A   | `PROCESS_SET_LIMITED_INFORMATION` + `PROCESS_QUERY_LIMITED_INFORMATION` on the other.
| Minimal version | N/A   | Windows 10 RS5 (1809)

### Notable return values
 - `STATUS_NO_TOKEN` - the security domain of at least one of the processes is not yet established because its primary token has not been frozen.
 - `STATUS_INVALID_TOKEN` - either at least one of the processes has the `IsolateSecurityDomain` side-channel mitigation enabled or at least one of the processes cannot pass an access check against the other for `PROCESS_VM_OPERATION | PROCESS_VM_WRITE` access.

### See also
 - `ProcessSecurityDomainInformation` (94)

## ProcessEnableLogging (96)
Retrieves, enables, or disables EtwTi logging for various operations for the process.

|                     | Query                               | Set
| ------------------- | ----------------------------------- | ---
| Type                | `PROCESS_LOGGING_INFORMATION`       | `PROCESS_LOGGING_INFORMATION`
| Required access     | `PROCESS_QUERY_LIMITED_INFORMATION` | `PROCESS_SET_LIMITED_INFORMATION`
| Required privilege  | None                                | `SeDebugPrivilege` or `SeTcbPrivilege`
| Required protection | None                                | PPL Antimalware (Windows 11 only)
| Minimal version     | Windows 10 RS5 (1809)               | Windows 10 RS5 (1809)

### See also
 - `ProcessEnableReadWriteVmLogging` (87)
 - `NtReadVirtualMemory`
 - `NtWriteVirtualMemory`
 - `NtProtectVirtualMemory`
 - `NtSuspendProcess`
 - `NtResumeProcess`
 - `NtSuspendThread`
 - `NtResumeThread`

## ProcessLeapSecondInformation (97)
Retrieves or adjusts the leap second handling mode for the current process.

|                 | Query                             | Set
| --------------- | --------------------------------- | ---
| Type            | `PROCESS_LEAP_SECOND_INFORMATION` | `PROCESS_LEAP_SECOND_INFORMATION`
| Required access | N/A (`NtCurrentProcess` only)     | N/A (`NtCurrentProcess` only)
| Minimal version | Windows 10 RS5 (1809)             | Windows 10 RS5 (1809)

### Related Win32 API
 - [`GetProcessInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getprocessinformation)
 - [`SetProcessInformation`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessinformation)

### See also
 - `PEB->LeapSecondData`

## ProcessFiberShadowStackAllocation (98)
Allocates a shadow stack for a fiber in the current process.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `PROCESS_FIBER_SHADOW_STACK_ALLOCATION_INFORMATION`
| Required access | N/A   | N/A (`NtCurrentProcess` only)
| Minimal version | N/A   | Windows 10 19H1 (1903)

### Notable return values
 - `STATUS_NOT_SUPPORTED` - CET and shadow stacks are not supported by the processor.

## ProcessFreeFiberShadowStackAllocation (99)
Frees a shadow stack for a fiber in the current process.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `PROCESS_FREE_FIBER_SHADOW_STACK_ALLOCATION_INFORMATION`
| Required access | N/A   | N/A (`NtCurrentProcess` only)
| Minimal version | N/A   | Windows 10 19H1 (1903)

### Notable return values
 - `STATUS_NOT_SUPPORTED` - CET and shadow stacks are not supported by the processor.

## ProcessAltSystemCallInformation (100)
Changes the syscall provider for the process.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `PROCESS_SYSCALL_PROVIDER_INFORMATION`
| Required access | N/A   | `PROCESS_VM_WRITE`
| Minimal version | N/A   | Windows 10 20H1 (2004)

## ProcessDynamicEHContinuationTargets (101)
Sets dynamic exception handling continuation targets for the process.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `PROCESS_DYNAMIC_EH_CONTINUATION_TARGETS_INFORMATION`
| Required access | N/A   | `PROCESS_SET_INFORMATION`
| Minimal version | N/A   | Windows 10 20H1 (2004)

### Notable return values
 - `STATUS_NOT_SUPPORTED` - the process doesn't have the `CetUserShadowStacks` mitigation enabled.
 - `STATUS_ACCESS_DENIED` - the specified handle points to the current process or the process has the `CetDynamicApisOutOfProcOnly` mitigation enabled.

### Related Win32 API
 - [`SetProcessDynamicEHContinuationTargets`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessdynamicehcontinuationtargets)

## ProcessDynamicEnforcedCetCompatibleRanges (102)
Sets CET-compatible ranges where shadow stack violations are fatal for the process.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `PROCESS_DYNAMIC_ENFORCED_ADDRESS_RANGE_INFORMATION`
| Required access | N/A   | `PROCESS_SET_INFORMATION`
| Minimal version | N/A   | Windows 10 20H2 (2009)

### Notable return values
 - `STATUS_NOT_SUPPORTED` - the process doesn't have the `CetUserShadowStacks` mitigation enabled.
 - `STATUS_ACCESS_DENIED` - the specified handle points to the current process or the process has the `CetDynamicApisOutOfProcOnly` mitigation enabled.

### Related Win32 API
 - [`SetProcessDynamicEnforcedCetCompatibleRanges`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setprocessdynamicenforcedcetcompatibleranges)

## ProcessCreateStateChange (103)
This information class has been superseded by `NtCreateProcessStateChange`.

## ProcessApplyStateChange (104)
This information class has been superseded by `NtChangeProcessState`.

## ProcessEnableOptionalXStateFeatures (105)
Enables optional XState features for the process.

|                 | Query | Set
| --------------- | ----- | ---
| Type            | N/A   | `ULONG64`
| Required access | N/A   | `PROCESS_SET_INFORMATION`
| Minimal version | N/A   | Windows 11

### Related Win32 API
 - [`EnableProcessOptionalXStateFeatures`](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-enableprocessoptionalxstatefeatures)

## ProcessAltPrefetchParam (106)

## ProcessAssignCpuPartitions (107)

## ProcessPriorityClassEx (108)
Adjust the priority class for the process.

|                    | Query | Set
| ------------------ | ----- | ---
| Type               | N/A   | `PROCESS_PRIORITY_CLASS_EX`
| Required access    | N/A   | `PROCESS_SET_INFORMATION`
| Required privilege | N/A   | `SeIncreaseBasePriorityPrivilege`
| Minimal version    | N/A   | Windows 11 22H2

### Known values
 - `PROCESS_PRIORITY_CLASS_UNKNOWN`
 - `PROCESS_PRIORITY_CLASS_IDLE`
 - `PROCESS_PRIORITY_CLASS_NORMAL`
 - `PROCESS_PRIORITY_CLASS_HIGH`
 - `PROCESS_PRIORITY_CLASS_REALTIME`
 - `PROCESS_PRIORITY_CLASS_BELOW_NORMAL`
 - `PROCESS_PRIORITY_CLASS_ABOVE_NORMAL`

### Remarks
Only setting the priority class to realtime requires the privilege.

The system ignores the request if the process's job object specifies a conflicting value via `JOB_OBJECT_LIMIT_PRIORITY_CLASS`.

### Related Win32 API
 - [`GetPriorityClass`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-getpriorityclass)
 - [`SetPriorityClass`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-setpriorityclass)

### See also
 - `ProcessPriorityClass` (18)
 - `ProcessForegroundInformation` (25)

## ProcessMembershipInformation (109)
Retrieves the effective server silo ID for the process.

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `PROCESS_MEMBERSHIP_INFORMATION`    | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 11 22H2                     | N/A

### Remarks
This info class lies and returns zero if the calling thread is in a server silo.

## ProcessEffectiveIoPriority (110)
Determines the effective priority for I/O operations issued by the process (taking its job object into account).

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `IO_PRIORITY_HINT`                  | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 11 22H2                     | N/A

### See also
 - `ProcessIoPriority` (33)

## ProcessEffectivePagePriority (111)
Determines the effective paging priority for the process (taking its job object into account).

|                 | Query                               | Set
| --------------- | ----------------------------------- | ---
| Type            | `PAGE_PRIORITY_INFORMATION`         | N/A
| Required access | `PROCESS_QUERY_LIMITED_INFORMATION` | N/A
| Minimal version | Windows 11 22H2                     | N/A

### See also
 - `ProcessPagePriority` (39)
