Function `NtCreateProfile` creates Profile Object.

Profile Objects are used for application profiling. There're *24* profile counters defined in `KPROFILE_SOURCE` enumeration type. Single Profile Object can be used to get information from one performance counter.

### ProfileHandle

Result of call - `HANDLE` to Profile Object.

### Process

`HANDLE` to Process Object to profile. Not required if profiled code is placed in Kernel address space (above *0x80000000*).

### ImageBase

Start address of profiling.

### ImageSize

Size of profiled memory block.

### BucketSize

*- ???* (cannot be less than *2* ).

### Buffer

Caller's allocated buffer for data.

### BufferSize

Size of buffer, in bytes.

### ProfileSource

Identifier of performance counter. See `KPROFILE_SOURCE` enumeration type for possible values.

### Affinity

Processor affinity mask. It defines processors to ask about performance counter.

# Documented by

* Tomasz Nowak

# Requirements

Privilege for UserMode: `SE_PROF_SINGLE_PROCESS_PRIVILEGE`
Privilege for KernelMode: `SE_SYSTEM_PROFILE_PRIVILEGE`

# See also

* `KPROFILE_SOURCE`
* `NtQueryIntervalProfile`
* `NtSetIntervalProfile`
* `NtStartProfile`
* `NtStopProfile`
