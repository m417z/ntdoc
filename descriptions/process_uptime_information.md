This structure describes the uptime statistics for the process.

# Applicable to
 - `NtQueryInformationProcess` with `ProcessUptimeInformation` (88)

# Members

## QueryInterruptTime
The number of 100-nanosecond intervals passed since boot to the time of the query.

## QueryUnbiasedTime
The number of 100-nanosecond intervals the system was active since boot to the time of the query.

## EndInterruptTime
The number of 100-nanosecond intervals passed since boot to process termination.

## TimeSinceCreation
The number of 100-nanosecond intervals passed since process creation to the time of the query.

## Uptime
The number of 100-nanosecond intervals the process spent unfrozen.

## SuspendedTime
The number of 100-nanosecond intervals that the process spent in a deep-frozen state. Note that despite the name, this field does **not** include time spent in suspended and regular (non-deep) frozen state.

## HangCount
The number of times the UI threads of the process hang.

## GhostCount
The number of times the UI threads of the process triggered window ghosting.

## Crashed
The flag indicates whether the process has crashed.

## Terminated
The flag indicates whether the process has terminated.

# Required OS version
This structure was introduced in Windows 10 RS3 (1709).
