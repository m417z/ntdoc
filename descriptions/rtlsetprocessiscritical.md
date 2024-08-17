Adjusts the critical state of the current process. Termination of a critical process causes a BSOD. Calling this function requires `SeDebugPrivilege`.

# Parameters
 - `NewValue` - a boolean indicating whether to set or to clear the critical flag.
 - `OldValue` - an optional pointer to a boolean indicating whether the critical flag was previously set.
 - `CheckFlag` - a boolean indicating whether the function should honor the `FLG_ENABLE_SYSTEM_CRIT_BREAKS` global flag.

# Notable return values
 - `STATUS_UNSUCCESSFUL` - the caller specified `CheckFlag` and the global flags indicate the use of critical processes is disabled.
 - `STATUS_PRIVILEGE_NOT_HELD` - the caller doesn't have the `SeDebugPrivilege` enabled in the token.

# Implementation details
This function uses `NtQueryInformationProcess` and `NtSetInformationProcess` with the `PROCESSINFOCLASS` value of `ProcessBreakOnTermination` (29) on the current process.

# See also
 - `NtTerminateProcess`
 - `NtQueryInformationProcess`
 - `NtSetInformationProcess`
 - `PROCESSINFOCLASS`
