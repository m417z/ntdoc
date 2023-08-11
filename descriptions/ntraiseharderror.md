This function sends HARDERROR\_MSG \
LPC message to listener \(typically CSRSS.EXE\). See \
NtSetDefaultHardErrorPort for more information. \
ErrorStatus Error code. \
NumberOfParameters Number of optional \
parameters in Parameters \
array. \
UnicodeStringParameterMask Optional \
string parameter \(can be only one per error code\). \
\*Parameters Array of DWORD \
parameters for use in error message string. \
ResponseOption See \
HARDERROR\_RESPONSE\_OPTION for possible values description. \
Response Pointer to HARDERROR\_RESPONSE \
enumeration. \
NtRaiseHardError is easy way to display message in \
GUI without loading Win32 API libraries.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
HARDERROR\_MSG \
HARDERROR\_RESPONSE \
HARDERROR\_RESPONSE\_OPTION \
NtSetDefaultHardErrorPort
