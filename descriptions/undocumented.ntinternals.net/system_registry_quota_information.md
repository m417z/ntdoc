### RegistryQuotaAllowed

Allowed size of all currently loaded hives.

### RegistryQuotaUsed

Size of all currently loaded hives.

### PagedPoolSize

Paged Pool size. `RegistryQuotaAllowed` shouldn't be grater then 80 percent of `PagedPoolSize`.

---

Remember that registry size is always sum of all loaded hives. So if you call `NtSaveKey`, size of registry will have the highest point at the end of saving. \
`SYSTEM_REGISTRY_QUOTA_INFORMATION` don't need restart of system to change registry quota.

# Documented by

* Tomasz Nowak
* Sven B. Schreiber

# Requirements

Privilege: `SE_INCREASE_QUOTA_PRIVILEGE`

# See also

* `NtQuerySystemInformation`
* `NtRestoreKey`
* `NtSaveKey`
* `NtSetSystemInformation`
* `SYSTEM_INFORMATION_CLASS`
