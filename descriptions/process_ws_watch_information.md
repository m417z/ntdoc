This structure defines a Working Set Watch entry.

# Applicable to
 - `NtQueryInformationProcess` with `ProcessWorkingSetWatch` (15)
 - `PROCESS_WS_WATCH_INFORMATION_EX`

# Members

## FaultingPc
The instruction pointer at the moment of the page fault.

## FaultingVa
The virtual address that triggered the page fault.
