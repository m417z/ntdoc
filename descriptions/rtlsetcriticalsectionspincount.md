Sets the specified spin count for the provided critical section object. On single-processor systems, the `SpinCount` is ignored and automatically set to 0.

# Parameters
- `CrticalSection` - A pointer to the critical section object
- `SpinCount` - Spin Count to be set for the provided critical section object

# Related Win32 API
- [`SetCriticalSectionSpinCount`](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-setcriticalsectionspincount)
- [`InitializeCriticalSectionAndSpinCount`](https://learn.microsoft.com/en-us/windows/win32/api/synchapi/nf-synchapi-initializecriticalsectionandspincount)

# See Also
- `RtlEnterCriticalSection`
- `RtlEnterCriticalSection`
- `RtlInitializeCriticalSection`
- `RtlInitializeCriticalSectionAndSpinCount`
- `RtlDeleteCriticalSection`
- `RtlInitializeCriticalSectionEx`
