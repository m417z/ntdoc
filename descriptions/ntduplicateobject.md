Allows copying handles across process boundaries and opening additional handles pointing to the same underlying kernel object. This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-zwduplicateobject).

# Parameters
 - `SourceProcessHandle` - a handle to the source process. This can be the `NtCurrentProcess` pseudo-handle or a handle granting `PROCESS_DUP_HANDLE` access.
 - `SourceHandle` - the source handle to duplicate. This value is meaningful in the context of the source process.
 - `TargetProcessHandle` - a handle to the target process. This can be the `NtCurrentProcess` pseudo-handle or a handle granting `PROCESS_DUP_HANDLE` access.
 - `TargetHandle` - an optional pointer to a variable that receives the new handle. This value is meaningful in the context of the target process.
 - `DesiredAccess` - the access mask to grant on the new handle.
 - `HandleAttributes` - the object attribute flags to set on the new handle. Supported flags are `OBJ_INHERIT` and `OBJ_PROTECT_CLOSE`.
 - `Options` - the flags that control the behavior of the function described below.

# Supported flags
 - `DUPLICATE_CLOSE_SOURCE` - instructs the system to close the source handle. Note that this occurs regardless of any error status returned. The target handle parameter becomes optional when using this flag.
 - `DUPLICATE_SAME_ACCESS` - instructs the system to ignore the `DesiredAccess` parameter and copy the access mask from the source handle.
 - `DUPLICATE_SAME_ATTRIBUTES` - instructs the system to ignore the `HandleAttributes` parameter and copy the handle attributes from the source handle.

# Remarks
This function offers a wide range of modes of operation:

1. Duplicate or reopen handles within the calling process. This function allows making copies of existing handles with different access/attributes.
2. Copying handles from other processes.
3. Copying handles into other processes.
4. Closing handles in other processes.

Note that this function performs an access check against the security descriptor of the source handle only when the `Options` parameter does not include the `DUPLICATE_SAME_ACCESS` flag.

# Related Win32 API
 - [`DuplicateHandle`](https://learn.microsoft.com/en-us/windows/win32/api/handleapi/nf-handleapi-duplicatehandle)

# See also
 - `NtClose`
 - `NtQueryObject`
 - `NtSetInformationObject`
