This enumeration defines types of operations that can be performed on process state objects.

# Applicable to
 - `NtChangeProcessState`

# Members

## ProcessStateChangeSuspend (0)
Suspends (freezes) the associated process.

|                 | Change
| --------------- | ------
| Extra buffer    | void (zero size)
| Required access | `PROCESS_SUSPEND_RESUME`

### Remarks


### See also
 - `NtSuspendProcess`
 - `THREAD_CREATE_FLAGS_BYPASS_PROCESS_FREEZE`
 - `JOBOBJECT_FREEZE_INFORMATION`

## ProcessStateChangeResume (1)
Resumes (thaws) the associated process.

|                 | Change
| --------------- | ------
| Extra buffer    | void (zero size)
| Required access | `PROCESS_SUSPEND_RESUME`

### See also
 - `NtResumeProcess`
