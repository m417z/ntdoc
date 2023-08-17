Function `NtSetSystemTime` sets system time. See `NtQuerySystemTime` for detailed information.

### SystemTime

Pointer to `LARGE_INTEGER` contains *UTC* time to set.

### PreviousTime

Optionally receives time before change.

# Documented by

* Tomasz Nowak

# Requirements

Privilege: `SE_SYSTEMTIME_PRIVILEGE`

# See also

* `NtQuerySystemTime`
* `RtlTimeFieldsToTime`
* `RtlTimeToTimeFields`
