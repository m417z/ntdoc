This function allows iterating over threads in a process without incurring any race conditions inherent to enumerating or opening threads by ID. Call this function repeatedly to open threads one by one.

# Parameters
 - `ProcessHandle` - a handle to the process which threads should be enumerated. This can either be the `NtCurrentProcess` pseudo-handle or a handle with `PROCESS_QUERY_INFORMATION` access.
 - `ThreadHandle` - a handle to the previous thread to continue enumeration from or `NULL` to restart enumeration.
 - `DesiredAccess` - the thread access mask expected on the opened handle.
 - `HandleAttributes` - flags that control the property of the handle, such as its inheritance (`OBJ_INHERIT`).
 - `Flags` - this parameter is unused and should be set to zero.
 - `NewThreadHandle` - a pointer to a variable that receives a handle to the opened thread.

# Access masks
For the list of thread-specific access masks, see `NtOpenThread`.

# Notable return values
 - `STATUS_SUCCESS` - the function opened the next thread.
 - `STATUS_NO_MORE_ENTRIES` - the function failed because there are no more accessible threads to enumerate.

# Remarks
`NtGetNextThread` automatically skips inaccessible threads. In other words, it only enumerates threads for which it can return handles with the specified desired access. However, if there are no threads that can be returned at the start of enumeration (when the input handle is `NULL`), the function returns the error accordingly (usually `STATUS_ACCESS_DENIED`) instead of `STATUS_NO_MORE_ENTRIES`.

To avoid retaining unused resources, call `NtClose` to close the returned handles when they are no longer required.

This function bypasses some access checks if the caller has the `SeDebugPrivilege` enabled.

# Related Win32 API
This functionality is not exposed in Win32 API.

# See also
 - `NtGetNextProcess`
 - `NtOpenProcess`
 - `NtOpenThread`
