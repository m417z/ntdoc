Adjusts the state of a process via a process state object. This function offers a more resilient alternative mechanism to suspending processes, tying the duration of the operation to the lifetime of the state object.

# Parameters
 - `ProcessStateChangeHandle` - a handle to the process state object created via `NtCreateProcessStateChange`. The handle must grant `PROCESS_STATE_CHANGE_STATE` access.
 - `ProcessHandle` - a handle to the associated process which state should be changed. For suspend and resume operations, this handle must grant `PROCESS_SUSPEND_RESUME` access.
 - `StateChangeType` - the type of the operation to perform.
 - `ExtendedInformation` - an optional pointer to a buffer with request-specific information. Currently unused.
 - `ExtendedInformationLength` - the size of the provided buffer. Currently unused.
 - `Reserved` - this parameter is unused and should be set to zero.

# Operation types
For the list of supported operations, see `PROCESS_STATE_CHANGE_TYPE`.

# Remarks
Closing the process state object handle via `NtClose` releases the reference. When the reference counter drops to zero, the system automatically undoes the effect of the state changes on the associated process.

# Related Win32 API
This functionality is not exposed in Win32 API.

# Required OS version
This function was introduced in Windows 11.

# See also
 - `NtCreateProcessStateChange`
 - `NtOpenProcess`
 - `NtSuspendProcess`
 - `NtResumeProcess`
 - `NtChangeThreadState`
