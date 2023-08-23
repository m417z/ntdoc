This enumeration defines types of operations that can be performed on thread state objects.

# Applicable to
 - `NtChangeThreadState`

# Members

## ThreadStateChangeSuspend (0)
Suspends the associated thread.

.               | Change
--------------- | ------
Extra bufffer   | void (zero size)
Required access | `THREAD_SUSPEND_RESUME`

### See also
 - `NtSuspendThread`

## ThreadStateChangeResume (1)
Resumes the associated thread.

.               | Change
--------------- | ------
Extra bufffer   | void (zero size)
Required access | `THREAD_SUSPEND_RESUME`

### See also
 - `NtResumeThread`
