### KeyHandle

### FileHandle

`HANDLE` to any file created with write access.

Before use `FileHandle` in other registry function without closing it, call `NtFlushKey` with `KeyHandle` \
as param.

# Requirements

Privilege: `SE_BACKUP_NAME`

# See also

* `NtOpenKey`
* `NtRestoreKey`
