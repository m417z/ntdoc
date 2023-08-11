Function NtLoadKey2 loads Hive file into registry \
structure. \
DestinationKeyName Pointer to \
OBJECT\_ATTRIBUTES structure contains name of loaded key and \
virtual parent key \("machine" or \
"user"\). \
HiveFileName Pointer to \
OBJECT\_ATTRIBUTES structure specifing Hive file. \
Flags \(?\) Only values \
0x0000 and 0x0004 are valid. If caller set \
Flags to 0x0000, function works \
as \
NtLoadKey.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib \
Privilege: SE\_RESTORE\_PRIVILEGE

See also: \
NtLoadKey \
NtSaveKey \
NtUnloadKey
