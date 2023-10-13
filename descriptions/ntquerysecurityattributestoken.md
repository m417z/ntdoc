Queries details about one or more token security attributes by name.

# Parameters
 - `TokenHandle` - a handle to the token or one of the supported pseudo-handles (see below). The handle must grant `TOKEN_QUERY` access.
 - `Attributes` - a pointer to an array attribute names to retrieve.
 - `NumberOfAttributes` - the number of names passed in the `Attributes` parameter.
 - `Buffer` - a pointer to a user-allocated buffer that receives the attribute information.
 - `Length` - the size of the provided buffer in bytes.
 - `ReturnLength` - an optional pointer to a variable that receives the number of bytes written when the function succeeds or the number of bytes requires when the buffer is too small.

# Pseudo-handles
This function supports the following pseudo-handle values **on Windows 8 and above**:
 - `NtCurrentProcessToken` - performs the query on the primary token of the calling process.
 - `NtCurrentThreadToken` - performs the query on the impersonation token of the calling thread. The function fails if the thread is not impersonating.
 - `NtCurrentThreadEffectiveToken` - performs the query on the impersonation token of the calling thread, if present. Otherwise, the function uses the primary token of the calling process.

# Notable return values
 - `STATUS_BUFFER_TOO_SMALL` and `STATUS_INFO_LENGTH_MISMATCH` indicate that the requested information does not fit into the provided buffer.
 - `STATUS_CANT_OPEN_ANONYMOUS` - the caller attempted to query information about the current thread token while impersonating an anonymous token.
 - `STATUS_NOT_FOUND` - one or more attribute names were not found in the token.

# Remarks
The names of attributes are case-insensitive.

This function has a **bug/inconsistency** and might succeed without returning any attributes (i.e., returning an array with zero entries) when the provided token has no associated security attributes. Therefore, it is recommended to check the `AttributeCount` field in the returned buffer before accessing the rest of the data.

To enumerate all security attributes associated with a token, use `NtQueryInformationToken` with `TokenSecurityAttributes` info class.

# See also
 - `NtQueryInformationToken`
 - `NtSetInformationToken`
 - `NtOpenProcessToken`
 - `NtOpenThreadToken`
 - `NtDuplicateToken`
