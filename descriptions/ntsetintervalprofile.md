Function `NtSetIntervalProfile` sets delay between performance counter's ticks. Setting profile's interval has global effect for all running processes.

User can set interval only for software performance counters. To determine if counter is software or not, call `NtQueryIntervalProfile`. If returned interval is zero, queried counter is hardware counter (build in CPU).

### Interval

New interval, in ms.

### Source

Performance counter's identifier, defined in `KPROFILE_SOURCE` enumeration type.

# Documented by

* Tomasz Nowak

# See also

* `KPROFILE_SOURCE`
* `NtCreateProfile`
* `NtQueryIntervalProfile`
