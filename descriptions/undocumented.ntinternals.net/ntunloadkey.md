Function `NtUnloadKey` unloads previously loaded *Hive* file from registry structure. All changes made to keys and values under this Hive are stored.

### DestinationKeyName

Pointer to `OBJECT_ATTRIBUTES` structure contains path and name of *Hive* root key.

# Documented by

* Tomasz Nowak

# Requirements

Privilege: `SE_RESTORE_PRIVILEGE`

# See also

* `NtLoadKey`
* `NtLoadKey2`
