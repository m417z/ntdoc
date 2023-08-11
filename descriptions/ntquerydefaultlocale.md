Function NtQueryDefaultLocale returns current Locale \
Identifier. Locale Identifier if defined as DWORD value, and \
contains locale code, sublocale etc. For more information about \
LCID see Microsoft SDK. \
UserProfile If set, function returns \
UserMode default locale. If not, result is system \
locale. \
DefaultLocaleId Pointer to LCID \
value receiving current locale.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtSetDefaultLocale
