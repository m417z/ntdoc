Determines whether the specified handle is a handle to the current thread.

# Parameters
 - `ThreadHandle` - a thread handle. The handle does not need to grant any specific access mask.

# Implementation details
This function is a wrapper over `NtCompareObjects`.

# Related Win32 API
This functionality is not exposed in Win32 API.

# See also
 - `NtCompareObjects`
 - `NtOpenThread`
 - `RtlIsCurrentProcess`
