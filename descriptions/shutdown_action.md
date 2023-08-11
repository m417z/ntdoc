Enumeration type SHUTDOWN\_ACTION is used in a call to \
NtShutdownSystem \
function. \
ShutdownNoReboot Normal shutdown, after \
system closes, processor jump into infinite loop. \
ShutdownReboot BIOS Reset \
function is called, after system closes. \
ShutdownPowerOff BIOS Shutdown \
function is called after system closes. If hardware does not \
support this functionality, ShutdownReboot is automatically called.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtShutdownSystem
