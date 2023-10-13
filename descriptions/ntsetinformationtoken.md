Sets various information about the specified token. This function is partially documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntsetinformationtoken) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwsetinformationtoken).

# Parameters
 - `TokenHandle` - a handle to the token. For most information classes, the handle must grant `TOKEN_ADJUST_DEFAULT` access.
 - `TokenInformationClass` - the type of information to set.
 - `TokenInformation` - a pointer to the buffer with the data specific to the request.
 - `TokenInformationLength` - the size of the provided buffer in bytes.

# Information classes
For the list of supported info classes and required token access, see `TOKEN_INFORMATION_CLASS`.

# Notable return values
 - `STATUS_TOKEN_ALREADY_IN_USE` indicates that the specified type of information cannot be changed for a token that is currently used as a primary token for a process.

# Remarks
Note that as opposed to `NtQueryInformationToken`, this function does not support token pseudo-handles.

# Related Win32 API
 - [`SetTokenInformation`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-settokeninformation)

# See also
 - `NtQueryInformationToken`
 - `NtFilterToken`
 - `NtAdjustPrivilegesToken`
 - `NtAdjustGroupsToken`
 - `NtOpenProcessToken`
 - `NtOpenThreadToken`
