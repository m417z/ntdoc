This prototype defines the function to use as an [APC](https://learn.microsoft.com/en-us/windows/win32/sync/asynchronous-procedure-calls) routine.

# Applicable to
 - `NtQueueApcThread`
 - `NtQueueApcThreadEx`
 - `NtQueueApcThreadEx2`
 - `RtlQueueApcWow64Thread`

# Remarks
Note that user APCs on the Native API level have three parameters in contrast with the [Win32 APCs](https://learn.microsoft.com/en-us/windows/win32/api/winnt/nc-winnt-papcfunc) that only have one.
