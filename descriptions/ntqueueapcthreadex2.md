Queues a user-mode Asynchronous Procedure Call (APC) on the specified thread.

# Parameters
 - `ThreadHandle` - a handle the the thread granting the `THREAD_SET_CONTEXT` access.
 - `ReserveHandle` - an optional handle to the reserve object (see `NtAllocateReserveObject`) to avoid memory allocations.
 - `ApcFlags` - the flags that control properties of the APC.
 - `ApcRoutine` - the address of the function to invoke.
 - `ApcArgument1` - the first argument to pass to the APC routine.
 - `ApcArgument2` - the second argument to pass to the APC routine.
 - `ApcArgument3` - the third argument to pass to the APC routine.

# Supported flags
 - `QUEUE_USER_APC_FLAGS_NONE` - indicates that none of the flags listed below are used. The behavior defaults to regular APCs that require the thread to first enter an alertable wait via `NtDelayExecution` (or a similar function) or call `NtTestAlert`.
 - `QUEUE_USER_APC_FLAGS_SPECIAL_USER_APC` - queue a *special user-mode APC* that does not require the thread to enter an alertable state. The APC will be executed on the next thread's transition to user mode.
 - `QUEUE_USER_APC_FLAGS_CALLBACK_DATA_CONTEXT` - let the callback routine receive the context (set of registers) that was interrupted when the thread was directed to call the APC function.

# Remarks
To queue a WoW64 APC, encode the `ApcRoutine` parameter using the `Wow64EncodeApcRoutine` macro or use `RtlQueueApcWow64Thread`.

Note that user APCs on the Native API level have three parameters in contrast with the [Win32 APCs](https://learn.microsoft.com/en-us/windows/win32/api/winnt/nc-winnt-papcfunc) that only have one.

# Related Win32 API
 - [`QueueUserAPC2`](https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-queueuserapc2)

# Required OS version
This function was introduced in Windows 11.

# See also
 - `NtQueueApcThread`
 - `NtQueueApcThreadEx`
 - `RtlQueueApcWow64Thread`
 - `NtOpenThread`
 - `NtTestAlert`
