Sets the execution state for the current thread and manages the corresponding power requests that prevent the system from dimming the display or entering sleep.

# Parameters
 - `NewFlags` - a bit mask containing flags that
 - `PreviousFlags` - a pointer to a variable that receives the previous execution state.

# Supported flags
 - `ES_SYSTEM_REQUIRED` - prevents the system from going to sleep.
 - `ES_DISPLAY_REQUIRED` - forces the display to be on.
 - `ES_USER_PRESENT` - this flag is not supported.
 - `ES_AWAYMODE_REQUIRED` - enables the away mode that allows the computer appear to be sleeping while being active,
 - `ES_CONTINUOUS` - the state should remain in effect until the next call that uses this flag.

# Remarks
You can view the power requests created via this and other APIs via `powercfg /requests`.

# Related Win32 API
 - [`SetThreadExecutionState`](https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate

# See also
 - `NtPowerInformation`
