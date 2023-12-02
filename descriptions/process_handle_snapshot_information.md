This structure defines a snapshot of handles opened by the process.

# Applicable to
 - `NtQueryInformationProcess` with `ProcessHandleInformation` (51)

# Members

## NumberOfHandles
The number of entries returned in the `Handles` field.

## Reserved
This value is unused.

## Handles
An array of entries with information about each handle. See `PROCESS_HANDLE_TABLE_ENTRY_INFO` for more details.

# Required OS version
This structure was introduced in Windows 8.
