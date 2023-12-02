This structure contains returned handle tracing records for the process.

# Applicable to
 - `NtQueryInformationProcess` with `ProcessHandleTracing` (32)

# Members

## Handle
On input, specifies an optional handle value to filter the returned entries. Set this field to `NULL` to disable filtering.

## TotalTraces
On output, contains the number of returned entries in the `HandleTrace` field.

## HandleTrace
On output, contains an array of handle tracing entries. See `PROCESS_HANDLE_TRACING_ENTRY` for more details.

# See also
 - `PROCESS_HANDLE_TRACING_ENABLE`
 - `PROCESS_HANDLE_TRACING_ENABLE_EX`
