Adjusts various information common to all types of kernel handles.

# Parameters
 - `Handle` - a handle to set information on. The handle does not need to grant any specific access.
 - `ObjectInformationClass` - the type of information to set.
 - `ObjectInformation` - a pointer to the buffer with the data specific to the request.
 - `ObjectInformationLength` - the size of the provided buffer in bytes.

# Information classes
For the list of supported information classes, see `OBJECT_INFORMATION_CLASS`.

# Related Win32 API
 - [`SetHandleInformation`](https://learn.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-sethandleinformation)

# See also
 - `NtQueryObject`
 - `NtSetSecurityObject`
 - `OBJ_INHERIT`
 - `OBJ_PROTECT_CLOSE`
