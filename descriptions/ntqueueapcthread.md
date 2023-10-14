Queues a user-mode Asynchronous Procedure Call (APC) on the specified thread.

# Parameters
 - `ThreadHandle` - a handle the the thread granting the `THREAD_SET_CONTEXT` access.
 - `ApcRoutine` - the address of the function to invoke.
 - `ApcArgument1` - the first argument to pass to the APC routine.
 - `ApcArgument2` - the second argument to pass to the APC routine.
 - `ApcArgument3` - the third argument to pass to the APC routine.

# Remarks
To execute the APC, the thread must first enter an alertable wait via `NtDelayExecution` (or a similar function) or call `NtTestAlert`.

To queue a WoW64 APC, encode the `ApcRoutine` parameter using the `Wow64EncodeApcRoutine` macro or use `RtlQueueApcWow64Thread`.

To specify the reserve object or use special user-mode APCs, see `NtQueueApcThreadEx` and `NtQueueApcThreadEx2`.

Note that user APCs on the Native API level have three parameters in contrast with the [Win32 APCs](https://learn.microsoft.com/en-us/windows/win32/api/winnt/nc-winnt-papcfunc) that only have one.

# Related Win32 API
 - [`QueueUserAPC`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-queueuserapc)

# See also
 - `NtQueueApcThreadEx`
 - `NtQueueApcThreadEx2`
 - `RtlQueueApcWow64Thread`
 - `NtOpenThread`
 - `NtTestAlert`
