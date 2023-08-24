Retrieves various information about kernel handles and the objects they point to. This function is partially documented in Windows Driver Kit [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntqueryobject) and [here](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwqueryobject).

# Parameters
 - `Handle` - a kernel handle to query information about. The handle does not need to grant any specific access.
 - `ObjectInformationClass` - the type of information to retrieve.
 - `ObjectInformation` - a pointer to a user-allocated buffer that receives the requested information.
 - `ObjectInformationLength` - the size of the provided buffer in bytes.
 - `ReturnLength` - an optional pointer to a variable that receives the number of bytes written when the function succeeds or the number of bytes requires when the buffer is too small.

# Information classes
For the list of supported information classes, see `OBJECT_INFORMATION_CLASS`.

# Notable return values
 - `STATUS_BUFFER_TOO_SMALL` and `STATUS_INFO_LENGTH_MISMATCH` indicate that the requested information does not fit into the provided buffer.

# Related Win32 API
 - [`GetHandleInformation`](https://learn.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-gethandleinformation)

# See also
 - `NtSetInformationObject`
 - `NtQuerySecurityObject`
