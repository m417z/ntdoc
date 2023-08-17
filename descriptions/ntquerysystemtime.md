Function `NtQuerySystemTime` returns current time in Coordinated Universal Time (*UTC*) *8-bytes* format.

### SystemTime

Pointer to `LARGE_INTEGER` value receiving current time.

---

*UTC* time it's represented as *8* bytes length integer. This value means number of *100-nanosecond* units since `1600, 1 January`. 

Time is incremented *10.000.000* times per second. So *64-bit* counter overloads after about *58.426* years... (If you don't believe, check this).

# Documented by

* Tomasz Nowak

# See also

* `NtSetSystemTime`
* `RtlTimeFieldsToTime`
* `RtlTimeToTimeFields`
