Queues a user-mode Asynchronous Procedure Call (APC) on the specified thread.

# Parameters
 - `ThreadHandle` - a handle the the thread granting the `THREAD_SET_CONTEXT` access.
 - `ReserveHandle` - an optional handle to the reserve object (see `NtAllocateReserveObject`) or a `QUEUE_USER_APC_SPECIAL_USER_APC` constant.
 - `ApcRoutine` - the address of the function to invoke.
 - `ApcArgument1` - the first argument to pass to the APC routine.
 - `ApcArgument2` - the second argument to pass to the APC routine.
 - `ApcArgument3` - the third argument to pass to the APC routine.

# Remarks
This function has three modes of operation:

1. When `ReserveHandle` is `NULL`, the function behaves identically to `NtQueueApcThread`. To execute the APC, the thread must first enter an alertable wait via `NtDelayExecution` (or a similar function) or call `NtTestAlert`.
2. When `ReserveHandle` is a handle to the reserve object, the function uses this object to avoid additional memory allocations. Otherwise, the behavior is identical to option 1.
3. When `ReserveHandle` is the `QUEUE_USER_APC_SPECIAL_USER_APC` value, the function queues a *special user-mode APC* that does not require the thread to enter an alertable state. The APC will be executed on the next thread's transition to user mode. This flag is supported on Windows 10 RS5 (1809) and above. Because execution of special APCs is not synchronized with the target thread

To queue a WoW64 APC, encode the `ApcRoutine` parameter using the `Wow64EncodeApcRoutine` macro or use `RtlQueueApcWow64Thread`.

Note that user APCs on the Native API level have three parameters in contrast with the [Win32 APCs](https://learn.microsoft.com/en-us/windows/win32/api/winnt/nc-winnt-papcfunc) that only have one.

# Related Win32 API
 - [`QueueUserAPC2`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-queueuserapc2)

# See also
 - `NtQueueApcThread`
 - `NtQueueApcThreadEx2`
 - `RtlQueueApcWow64Thread`
 - `NtOpenThread`
 - `NtTestAlert`
