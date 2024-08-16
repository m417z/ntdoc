Creates a new process state object. This object offers a more resilient alternative to suspending processes, tying the duration of the operation to the lifetime of the state object. To change the state of the process state object, use `NtChangeProcessState`.

# Parameters
 - `ProcessStateChangeHandle` - a pointer to a variable that receives a handle to the new process state object.
 - `DesiredAccess` - the access mask to provide on the returned handle. This value is usually `PROCESS_STATE_ALL_ACCESS`.
 - `ObjectAttributes` - an optional pointer to an `OBJECT_ATTRIBUTES` structure that specifies attributes of the new object/handle.
 - `ProcessHandle` - a handle to the associated process. The handle must grant `PROCESS_SET_INFORMATION` access.
 - `Reserved` - this parameter is unused and should be set to zero.

# Remarks
To avoid retaining unused resources, call `NtClose` to close the returned handle when it is no longer required. When the reference counter on the process state object drops to zero, the system automatically undoes the effect of the state changes on the associated process.

# Related Win32 API
This functionality is not exposed in Win32 API.

# Required OS version
This function was introduced in Windows 11.

# See also
 - `NtChangeProcessState`
 - `NtOpenProcess`
 - `NtSuspendProcess`
 - `NtCreateThreadStateChange`
