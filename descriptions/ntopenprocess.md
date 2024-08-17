Opens a handle to an existing process. This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-ntopenprocess) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwopenprocess).

# Parameters
 - `ProcessHandle` - a pointer to a variable that receives a handle to the process.
 - `DesiredAccess` - the requested access mask.
 - `ObjectAttributes` - a pointer to an `OBJECT_ATTRIBUTES` structure that specifies attributes of the handle. Use `InitializeObjectAttributes` to initialize this structure.
 - `ClientId` - a pointer to the variable that indicates the client ID of the process to open. Specify the PID in `UniqueProcess` and set `UniqueThread` field to `NULL`.

# Access masks

Access mask                         | Use
----------------------------------- | -----
`PROCESS_TERMINATE`                 | Terminating the process via `NtTerminateProcess`.
`PROCESS_CREATE_THREAD`             | Creating threads in the process via `NtCreateThread` and `NtCreateThreadEx`.
`PROCESS_SET_SESSIONID`             | Unused
`PROCESS_VM_OPERATION`              | Performing various memory operations such as `NtAllocateVirtualMemory`, `NtProtectVirtualMemory`, `NtMapViewOfSection`.
`PROCESS_VM_READ`                   | Reading the process's memory via `NtReadVirtualMemory`
`PROCESS_VM_WRITE`                  | Writing to the process's memory via `NtWriteVirtualMemory`
`PROCESS_DUP_HANDLE`                | Duplicating and closing process handles via `NtDuplicateObject`.
`PROCESS_CREATE_PROCESS`            | Specifying the process as the parent in `NtCreateProcess` and `NtCreateUserProcess`.
`PROCESS_SET_QUOTA`                 | Adjusting  quota limits via `NtSetInformationProcess`.
`PROCESS_SET_INFORMATION`           | Setting most information classes via `NtSetInformationProcess`.
`PROCESS_QUERY_INFORMATION`         | Querying most information classes via `NtQueryInformationProcess` and `NtQueryVirtualMemory`.
`PROCESS_SUSPEND_RESUME`            | Suspending and resuming all threads in the process via `NtSuspendProcess` and `NtResumeThread`.
`PROCESS_QUERY_LIMITED_INFORMATION` | Querying some information classes via `NtQueryInformationProcess` and `NtQueryVirtualMemory`. The system automatically includes this right if the caller requests `PROCESS_QUERY_INFORMATION`.
`PROCESS_SET_LIMITED_INFORMATION`   | Setting some information classes via `NtSetInformationProcess`. The system automatically includes this right if the caller requests `PROCESS_SET_INFORMATION`.
`PROCESS_ALL_ACCESS`                | All of the above plus standard rights.

# Remarks
This function bypasses some access checks if the caller has the `SeDebugPrivilege` enabled.

To avoid retaining unused resources, call `NtClose` to close the returned handle when it is no longer required.

Instead of opening the current process, consider using the `NtCurrentProcess` pseudo-handle.

# Related Win32 API
 - [`OpenProcess`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocess)
 
# See also
 - `CLIENT_ID`
 - `NtGetNextProcess`
 - `NtCreateProcess`
 - `NtCreateUserProcess`
 - `NtQueryInformationProcess`
 - `NtSetInformationProcess`
 - `NtOpenThread`
