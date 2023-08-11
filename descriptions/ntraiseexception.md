Function NtRaiseException is typically used inside \
KiUserExceptionDispatcher \
function for inform system about exception in current process. \
ExceptionRecord Pointer to \
EXCEPTION\_RECORD structure containing typical \
information about error. \
ThreadContext Pointer to \
CONTEXT structure. \
HandleException If not set, calling \
process is killed. If set, system tries to execute actually enabled \
Exception Handler procedure with parameters specified aa \
ExceptionRecord and ThreadContext.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
KiUserExceptionDispatcher \
NtGetContextThread \
NtRaiseHardError
