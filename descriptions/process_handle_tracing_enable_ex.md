This structure enables handle tracing for the process.

# Applicable to
 - `NtSetInformationProcess` with `ProcessHandleTracing` (32)

# Members

## Flags
This value is unused.

## TotalSlots
The number of slots to allocate for storing handle tracing entries. The system rounds the specified value up to the closest power of two between 0x80 and 0x20000. Specifying a zero value defaults it to 0x1000.

## See also
 - `PROCESS_HANDLE_TRACING_ENABLE`
 - `PROCESS_HANDLE_TRACING_QUERY`
