Function `NtSystemDebugControl` is used by some low-level debuggers written by *Microsoft* and available typically in *DDK*.

### Command

Command request for system. Command's codes are available in enumeration type `SYSDBG_COMMAND`.

### InputBuffer

User's allocated buffer with input data.

### InputBufferLength

Length of `InputBuffer`, in bytes.

### OutputBuffer

User's allocated buffer for output data.

### OutputBufferLength

Length of `OutputBuffer`, in bytes.

### ReturnLength

Pointer to `ULONG` value receiving required size of `OutputBuffer`.

# Documented by

* Tomasz Nowak

# See also

* `SYSDBG_COMMAND`
