Function NtLoadKey is used to make avaiable registry \
keys and values stored in Hive File. Hive file can be \
created by calling \
NtSaveKey. If loaded Hive is no longer needed \(for \
example when user logout for HKCU Hive\), it can be udloaded \
by call \
NtUnloadKey. \
DestinationKeyName Pointer to \
OBJECT\_ATTRIBUTES structure contains destination key name \
and HANDLE to root key. Root can be \\REGISTRY\\machine or \\REGISTRY\\user. All other keys are invalid. \
HiveFileName Pointer to \
OBJECT\_ATTRIBUTES structure contains Hive file path \
and name.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib \
Privilege: SE\_RESTORE\_PRIVILEGE

See also: \
NtLoadKey2 \
NtSaveKey \
NtUnloadKey
