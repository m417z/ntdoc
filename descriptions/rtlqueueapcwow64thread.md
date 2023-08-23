Queues a WoW64 user-mode Asynchronous Procedure Call (APC) on the specified thread.

# Parameters
 - `ThreadHandle` - a handle the the thread granting the `THREAD_SET_CONTEXT` access.
 - `ApcRoutine` - the WoW64 address of the function to invoke.
 - `ApcArgument1` - the first argument to pass to the APC routine.
 - `ApcArgument2` - the second argument to pass to the APC routine.
 - `ApcArgument3` - the third argument to pass to the APC routine.

# Remarks
To execute the APC, the thread must first enter an alertable wait via `NtDelayExecution` (or a similar function) or call `NtTestAlert`. Note that user APCs on the Native API level have three parameters in contrast with the Win32 APCs that only have one.

To specify the reserve object or use special user-mode APCs, see `NtQueueApcThreadEx` and `NtQueueApcThreadEx2`.

Note that user APCs on the Native API level have three parameters in contrast with the [Win32 APCs](https://learn.microsoft.com/en-us/windows/win32/api/winnt/nc-winnt-papcfunc) that only have one.

# Implementation details
This function uses `Wow64EncodeApcRoutine` and then calls `NtQueueApcThread`.

# Related Win32 API
 - [`QueueUserAPC`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-queueuserapc)

# See also
 - `NtQueueApcThread`
 - `NtQueueApcThreadEx`
 - `NtQueueApcThreadEx2`
 - `NtOpenThread`
 - `NtTestAlert`
