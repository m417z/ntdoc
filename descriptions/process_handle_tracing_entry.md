This structure contains a single process handle tracing entry.

# Applicable to
 - `PROCESS_HANDLE_TRACING_QUERY`

# Members

## Handle
The handle value on which the operation happened.

## ClientId
The pair of process and thread IDs that identifies the thread that performed the operation.

## Type
The type of the handle operation.

### Known values
 - `PROCESS_HANDLE_TRACE_TYPE_OPEN` - the handle was opened.
 - `PROCESS_HANDLE_TRACE_TYPE_CLOSE` - the handle was closed.
 - `PROCESS_HANDLE_TRACE_TYPE_BADREF` - the caller attempted to reference an object using the specified invalid handle value.

## Stacks
The stack trace of the operation.
