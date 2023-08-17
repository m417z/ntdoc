### TimerHandle

`HANDLE` to Timer Object opened with `TIMER_MODIFY_STATE` access.

### DueTime

Time when timer should be set, in *100ns* units. If it is negative value, it means relative time.

### TimerApcRoutine

User's APC routine, defined as follows:

```cpp
typedef void (*PTIMER_APC_ROUTINE)(
        IN PVOID TimerContext,
        IN ULONG TimerLowValue,
        IN LONG TimerHighValue
        );
```

### TimerContext

Optional parameter to `TimerApcRoutine`.

### ResumeTimer

If set, Power Management restores system to normal mode when timer is signaled.

### Period

If zero, timer is set only once. Else will be set periodic in time intervals defined in `Period` value (in *100ms* units).

### PreviousState

Optional pointer to value receiving state of Timer Object before `NtSetTimer` call.

# Documented by

* Tomasz Nowak

# See also

* `NtCancelTimer`
* `NtCreateTimer`
* `NtOpenTimer`
* `NtQueryTimer`
