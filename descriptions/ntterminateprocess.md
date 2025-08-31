Forces the process to terminate. This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntddk/nf-ntddk-zwterminateprocess).

# Parameters
 - `ProcessHandle` - an optional handle to a process granting `PROCESS_TERMINATE` access or the `NtCurrentProcess` pseudo-handle. The `NULL` value indicates the current process.
 - `ExitStatus` - the exit code to use for the process.

# Remarks
Note that specifying `NULL` as a process handle has a different semantic compared to using `NtCurrentProcess`. `NtCurrentProcess` immediately terminates the current process (without returning from the function) while `NULL` terminates all threads except for the calling, sets the exit status, and marks the process for self-delete. A second call to `NtTerminateProcess` with `NULL` completes termination.

To exit the current process gracefully, use `RtlExitUserProcess`.

Setting `ExitStatus` to `DBG_TERMINATE_PROCESS` automatically clears the process's debug object.

The process object becomes signalled after termination.

# Related Win32 API
 - [`TerminateProcess`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-terminateprocess)

# See also
 - `NtOpenProcess`
 - `NtCreateProcess`
 - `NtCreateUserProcess`
 - `RtlExitUserProcess`
 - `RtlExitUserThread`
 - `NtTerminateThread`
 - `NtWaitForSingleObject`
