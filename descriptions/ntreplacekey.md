Function NtReplaceKey save specified hive key to \
file, and starts use this file instread of original hive file. \
Original hive file contents is replaced with contents of third hive \
file, specified below. \
NewHiveFileName Pointer to \
OBJECT\_ATTRIBUTES structure containing name of third file \
\(file with new contents\). \
KeyHandle HANDLE to Key Object. \
Backuped and replaced are all keys from hive whith contains key \
specified by KeyHandle \
parameter. \
BackupHiveFileName Pointer to \
OBJECT\_ATTRIBUTES structure containing name of first file \
\(new hive file\). \
Example: \
NewHiveFile \-&gt; \
OrginalHiveFile \-&gt; BackupHiveFile \
Before call to NtReplaceKey system \
uses OriginalHiveFile. \
After call, system use BackupHiveFile.

Documented by: \
Tomasz Nowak \
Requirements:

Library: ntdll.lib

See also: \
NtLoadKey \
NtLoadKey2 \
NtRestoreKey \
NtSaveKey \
NtUnloadKey
