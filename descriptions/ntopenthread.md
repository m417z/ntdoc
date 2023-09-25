Opens a handle to an existing thread. This function is [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/devnotes/ntopenthread).

# Parameters
 - `ThreadHandle` - a pointer to a variable that receives a handle to the thread.
 - `DesiredAccess` - the requested access mask.
 - `ObjectAttributes` - a pointer to an `OBJECT_ATTRIBUTES` structure that specifies attributes of the handle. Use `InitializeObjectAttributes` to initialize this structure.
 - `ClientId` - a pointer to the variable that indicates the client ID of the thread to open. You can omit the process part of the structure by specifying `NULL` in `UniqueProcess`.

# Access masks

Access mask                        | Use
---------------------------------- | -----
`THREAD_TERMINATE`                 | Allows terminating the thread via `NtTerminateThread`.
`THREAD_SUSPEND_RESUME`            | Allows suspending and resuming the thread via `NtSuspendThread` and `NtResumeThread`, respectively.
`THREAD_ALERT`                     | Allows waking the thread from an alertable wait via `NtAlertThread`.
`THREAD_GET_CONTEXT`               | Allows retrieving the context (set of registers) of the thread via `NtGetContextThread`.
`THREAD_SET_CONTEXT`               | Allows changing the context of the thread via `NtSetContextThread` and queuing APCs via `NtQueueApcThread`.
`THREAD_SET_INFORMATION`           | Allows setting most information classes via `NtSetInformationThread`.
`THREAD_QUERY_INFORMATION`         | Allows querying most information classes via `NtQueryInformationThread`.
`THREAD_SET_THREAD_TOKEN`          | Allows setting thread impersonation token via `NtSetInformationThread` with `ThreadImpersonationToken`.
`THREAD_IMPERSONATE`               | Allows using the thread as a server during direct impersonation via `NtImpersonateThread`.
`THREAD_DIRECT_IMPERSONATION`      | Allows using the thread as a client during direct impersonation via `NtImpersonateThread`.
`THREAD_SET_LIMITED_INFORMATION`   | Allows setting some information classes via `NtSetInformationThread`. The system automatically includes this right if the caller requested `THREAD_SET_INFORMATION`.
`THREAD_QUERY_LIMITED_INFORMATION` | Allows querying some information classes via `NtQueryInformationThread`. The system automatically includes this right if the caller requested `THREAD_QUERY_INFORMATION`.
`THREAD_RESUME`                    | Allows resuming the thread via `NtResumeThread`. The system automatically includes this right if the caller requested `THREAD_SUSPEND_RESUME`.
`THREAD_ALL_ACCESS`                | All of the above plus standard rights.

# Remarks
This function bypasses some access checks if the caller has the `SeDebugPrivilege` enabled.

To avoid retaining unused resources, call `NtClose` to close the returned handle when it is no longer required.

Instead of opening the current thread, consider using the `NtCurrentThread` pseudo-handle.

# Related Win32 API
 - [`OpenThread`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openthread)

# See also
 - `NtCurrentThread`
 - `NtQueryInformationThread`
 - `NtSetInformationThread`
 - `NtResumeThread`
 - `NtSuspendThread`
 - `NtCreateThreadEx`
