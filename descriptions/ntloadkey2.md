Function `NtLoadKey2` loads Hive file into registry structure.

### DestinationKeyName

Pointer to `OBJECT_ATTRIBUTES` structure contains name of loaded key and virtual parent key (**"machine"** or **"user"**).

### HiveFileName

Pointer to `OBJECT_ATTRIBUTES` structure specifing Hive file.

### Flags

**(?)** Only values *0x0000* and *0x0004* are valid. If caller set `Flags` to 0x0000, function works as `NtLoadKey`.

# Documented by

* Tomasz Nowak

# Requirements

Privilege: `SE_RESTORE_PRIVILEGE`

# See also

* `NtLoadKey`
* `NtSaveKey`
* `NtUnloadKey`
