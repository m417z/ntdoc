TimerHandle HANDLE to Timer \
Object opened with TIMER\_MODIFY\_STATE access. \
DueTime Time when timer should be set, \
in 100ns units. If it is negative value, it means relative \
time. \
TimerApcRoutine User's APC routine, \
defined as follows: \
        typedef void \(\*PTIMER\_APC\_ROUTINE\)\( \
                        IN PVOID TimerContext, \
                        IN ULONG TimerLowValue, \
                        IN LONG TimerHighValue \
                        \);
