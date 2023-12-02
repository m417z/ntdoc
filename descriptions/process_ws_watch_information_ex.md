This structure defines an extended Working Set Watch entry.

# Applicable to
 - `NtQueryInformationProcess` with `ProcessWorkingSetWatchEx` (42)

# Members

## BasicInfo
A nested `PROCESS_WS_WATCH_INFORMATION` structure with basic information about the page fault.

## FaultingThreadId
The ID of the thread that caused the page fault.

### See also
 - `CLIENT_ID`

## Flags
This field is currently unused.
