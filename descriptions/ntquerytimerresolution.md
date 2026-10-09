Retrieves the range of supported system timer resolutions and the current resolution. All values are intervals between timer ticks in 100-nanosecond units, so a smaller value means a finer resolution.

# Parameters
 - `MaximumTime` - a pointer to a variable that receives the longest supported interval, i.e., the coarsest resolution. This value is typically 156,250 (15.625 ms).
 - `MinimumTime` - a pointer to a variable that receives the shortest supported interval, i.e., the finest resolution. This value is typically 5,000 (0.5 ms).
 - `CurrentTime` - a pointer to a variable that receives the current interval. This is the finest resolution among active requests from processes (see `NtSetTimerResolution`) and drivers (see `ExSetTimerResolution`), or `MaximumTime` if there are no requests.

# Related Win32 API
This functionality is not exposed in Win32 API.

# See also
 - `NtSetTimerResolution`
 - `ExQueryTimerResolution`
 - `NtDelayExecution`
