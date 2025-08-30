This function allows iterating over processes on the system without incurring any race conditions inherent to enumerating or opening processes by ID. Call this function repeatedly to open processes one by one.

# Parameters
 - `ProcessHandle` - a handle to the previous process to continue enumeration from or `NULL` to restart enumeration. The handle doesn't need to grant any particular access.
 - `DesiredAccess` - the process access mask expected on the opened handle.
 - `HandleAttributes` - flags that control the property of the handle, such as its inheritance (`OBJ_INHERIT`).
 - `Flags` - the bit mask that controls the operation. See below for known values.
 - `NewProcessHandle` - a pointer to a variable that receives a handle to the opened process.

# Known flags
 - `PROCESS_GET_NEXT_FLAGS_PREVIOUS_PROCESS` - reverses enumeration order by opening the previous process instead of the next one.

# Access masks
For the list of process-specific access masks, see `NtOpenProcess`.

# Notable return values
 - `STATUS_SUCCESS` - the function opened the next/previous process.
 - `STATUS_NO_MORE_ENTRIES` - the function failed because there are no more accessible processes to enumerate.

# Remarks
`NtGetNextProcess` automatically skips inaccessible processes. In other words, it only enumerates processes for which it can return handles with the specified desired access. However, if there are no processes that satisfy this criterion at the start of enumeration (when the input handle is `NULL`), the function returns the error accordingly (usually `STATUS_ACCESS_DENIED`) instead of `STATUS_NO_MORE_ENTRIES`.

To avoid retaining unused resources, call `NtClose` to close the returned handles when they are no longer required.

This function bypasses some access checks if the caller has the `SeDebugPrivilege` enabled.

# Related Win32 API
This functionality is not exposed in Win32 API.

# See also
 - `NtGetNextThread`
 - `NtOpenProcess`
 - `NtOpenThread`
