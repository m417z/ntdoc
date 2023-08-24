Closes the specified kernel handle. This function is documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntclose) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/wdm/nf-wdm-zwclose).

# Parameters
 - `Handle` - a handle to a kernel object.

# Notable return values
 - `STATUS_INVALID_HANDLE` - an invalid handle value was specified.
 - `STATUS_HANDLE_NOT_CLOSABLE` - the provided handle is marked as protected from closing. See `OBJ_PROTECT_CLOSE` for more details.

# Remarks
`NtClose` is one the few Native API functions that can raise exceptions instead of returning an error status code. See the [exploit protection reference](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/exploit-protection-reference?view=o365-worldwide#validate-handle-usage) for a description of the mitigation that causes this behavior.

# Related Win32 API
 - [`CloseHandle`](https://learn.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-closehandle)

# See also
 - `OBJ_PROTECT_CLOSE`
 - `NtMakeTemporaryObject`
 - `NtDuplicateObject`
 - `NtQueryObject`
 - `NtSetInformationObject`
