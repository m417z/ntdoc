This structure defines basic information about the process.

# Applicable to
 - `NtQueryInformationProcess` with `ProcessBasicInformation` (0)

# Members

## ExitStatus
The exit code of the process. If the process has not exited, this field contains `STATUS_PENDING`.

### See also
 - `RtlExitUserProcess`
 - `NtTerminateProcess`

## PebBaseAddress
The address of the Process Environment Block. See `PEB` for more details. To query the address of the 32-bit `PEB32`, use `ProcessWow64Information` (26).

## AffinityMask
The bit mask indicating on which processors the threads from the process are allowed to run.

### See also
 - `PROCESSINFOCLASS` value of `ProcessAffinityMask` (21)

## BasePriority
The base priority for the threads in the process.

### See also
 - `PROCESSINFOCLASS` value of `ProcessBasePriority` (5)

## UniqueProcessId
The PID of the process.

### See also
 - `CLIENT_ID`

## InheritedFromUniqueProcessId
The PID of the process's parent from which it inherits various attributes.

### See also
 - `PS_ATTRIBUTE_PARENT_PROCESS`

# See also
 - `PROCESS_EXTENDED_BASIC_INFORMATION`