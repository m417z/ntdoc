Routine RtlGetCallersAddress is usefull in program \
debugging or exceptions control. It returns address of calling \
instruction. \
CallersAddress Returns address in body \
of function that call RtlGetCallersAddress. \
CallersCaller Returns address in \
function's calling function that call \
RtlGetCallersAddress body. \
Supported on system versions: \
NT 4.0,Win 2000,Win XP/2003

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
RtlCaptureStackBackTrace
