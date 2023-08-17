### ThreadHandle

Caller supplied storage for the resulting handle.

### DesiredAccess

Specifies the allowed or desired access to the thread.

### ObjectAttributes

Initialized attributes for the object.

### ProcessHandle

Handle to the threads parent process.

### ClientId

Caller supplies storage for returned process id and thread id.

### ThreadContext

Initial processor context for the thread.

### InitialTeb

Initial user mode stack context for the thread.

### CreateSuspended

Specifies if the thread is ready for scheduling. See `NtContinue` for more information.

# Documented by

* ReactOS

# See also

* `INITIAL_TEB`
* `NtContinue`
* `NtCreateProcess`
* `NtTerminateThread`
* `NtAlertResumeThread`
