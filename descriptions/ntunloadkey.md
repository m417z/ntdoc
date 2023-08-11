Function NtUnloadKey unloads previously loaded \
Hive file from registry structure. All changes made to keys \
and values under this Hive are stored. \
DestinationKeyName Pointer to \
OBJECT\_ATTRIBUTES structure contains path and name of \
Hive root key.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib \
Privileges: SE\_RESTORE\_PRIVILEGE

See also: \
NtLoadKey \
NtLoadKey2
