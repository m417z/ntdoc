NtSetDefaultHardErrorPort is typically called only \
once. After call, kernel set BOOLEAN flag named \
\_ExReadyForErrors to TRUE, and all other tries to \
change default port are broken with STATUS\_UNSUCCESSFUL \
error code. \
PortHandle HANDLE to named Port \
Object. \
Listener of default HardError port receive HARDERROR\_MSG \
LPC messages when any process call NtRaiseHardError \
function.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib \
Privileges: SE\_TCB\_PRIVILEGE

See also: \
HARDERROR\_MSG \
NtRaiseHardError
