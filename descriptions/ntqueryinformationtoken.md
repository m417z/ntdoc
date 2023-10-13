Queries various information about the specified token. This function is partially documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryinformationtoken) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryinformationtoken).

# Parameters
 - `TokenHandle` - a handle to the token or one of the supported pseudo-handles (see below). For most information classes, the handle must grant `TOKEN_QUERY` access.
 - `TokenInformationClass` - the type of information to retrieve.
 - `TokenInformation` - a pointer to a user-allocated buffer that receives the requested information.
 - `TokenInformationLength` - the size of the provided buffer in bytes.
 - `ReturnLength` - an optional pointer to a variable that receives the number of bytes written when the function succeeds or the number of bytes requires when the buffer is too small.

# Information classes
For the list of supported info classes and required token access, see `TOKEN_INFORMATION_CLASS`.

# Pseudo-handles
This function supports the following pseudo-handle values **on Windows 8 and above**:
 - `NtCurrentProcessToken` - performs the query on the primary token of the calling process.
 - `NtCurrentThreadToken` - performs the query on the impersonation token of the calling thread. The function fails if the thread is not impersonating.
 - `NtCurrentThreadEffectiveToken` - performs the query on the impersonation token of the calling thread, if present. Otherwise, the function uses the primary token of the calling process.

# Notable return values
 - `STATUS_BUFFER_TOO_SMALL` and `STATUS_INFO_LENGTH_MISMATCH` indicate that the requested information does not fit into the provided buffer.
 - `STATUS_CANT_OPEN_ANONYMOUS` indicates that the caller attempted to query information about the current thread token while impersonating an anonymous token.

# Related Win32 API
 - [`GetTokenInformation`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-gettokeninformation)

# See also
 - `NtSetInformationToken`
 - `NtQuerySecurityAttributesToken`
 - `NtOpenProcessToken`
 - `NtOpenThreadToken`
 - `NtDuplicateToken`
 - `NtCompareTokens`
