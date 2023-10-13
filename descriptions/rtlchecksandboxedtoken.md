Determines if a token is considered sandboxed (i.e., has integrity level below medium).

# Parameters
 - `TokenHandle` - a handle to the token or one of the supported pseudo-handles (see below). The handle must grant `TOKEN_QUERY` access.
 - `IsSandboxed` - a pointer to a variable that receives a boolean indicating whether the token is sandboxed.

# Pseudo-handles
This function supports the following pseudo-handle values:
 - `NtCurrentProcessToken` - performs the query on the primary token of the calling process.
 - `NtCurrentThreadToken` - performs the query on the impersonation token of the calling thread. The function fails if the thread is not impersonating.
 - `NtCurrentThreadEffectiveToken` - performs the query on the impersonation token of the calling thread, if present. Otherwise, the function uses the primary token of the calling process.

# Implementation details
On modern versions of Windows, this function calls `NtQueryInformationToken` with `TokenIsSandboxed` info class. Previously, it used to create a security descriptor with a medium mandatory label and perform an access check against it via `NtAccessCheck`.

# Required OS version
This function was introduced in Windows 10 TH1 (1507).

# See also
 - `NtOpenProcessToken`
 - `NtOpenThreadToken`
