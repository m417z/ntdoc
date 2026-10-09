Requests or releases a system timer resolution on behalf of the calling process. A finer resolution increases the precision of waits and timers at the cost of higher power consumption.

# Parameters
 - `DesiredTime` - the requested interval between timer ticks, in 100-nanosecond units. Values outside the range reported by `NtQueryTimerResolution` are clamped to it. This parameter is ignored when `SetResolution` is `FALSE`.
 - `SetResolution` - whether to set (`TRUE`) or release (`FALSE`) the request of the calling process.
 - `ActualTime` - a pointer to a variable that receives the resulting timer resolution, in 100-nanosecond units. See the remarks for its limitations.

# Notable return values
 - `STATUS_TIMER_RESOLUTION_NOT_SET` - `SetResolution` is `FALSE`, but the calling process does not have an active request.

# Remarks
Each process can have at most one active request. Calling the function with `SetResolution` set to `TRUE` replaces the previous request instead of adding another one, and a single call with `FALSE` releases it. The system releases the request automatically when the process exits.

The system uses the finest resolution among all active requests from processes and drivers (see `ExSetTimerResolution`). To check the resulting resolution, use the `CurrentTime` value from `NtQueryTimerResolution`. On recent versions of Windows, the value returned in `ActualTime` can differ from it.

Starting with Windows 10 version 2004, Windows does not guarantee a finer resolution for processes that did not request one. See the remarks for [`timeBeginPeriod`](https://learn.microsoft.com/en-us/windows/win32/api/timeapi/nf-timeapi-timebeginperiod) for more details.

Requests from processes with `PROCESS_POWER_THROTTLING_IGNORE_TIMER_RESOLUTION` enabled (see `ProcessPowerThrottlingState`) succeed but do not affect the system timer resolution.

# Related Win32 API
 - [`timeBeginPeriod`](https://learn.microsoft.com/en-us/windows/win32/api/timeapi/nf-timeapi-timebeginperiod)
 - [`timeEndPeriod`](https://learn.microsoft.com/en-us/windows/win32/api/timeapi/nf-timeapi-timeendperiod)

# See also
 - `NtQueryTimerResolution`
 - `ExSetTimerResolution`
 - `NtDelayExecution`
 - `ProcessPowerThrottlingState`
