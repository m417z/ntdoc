This function is [documented in Windows Driver Kit](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/ntifs/nf-ntifs-ntprivilegecheck).

---

Function `NtPrivilegeCheck` is used to check state of any privileges in Token Object. It's also described in *Microsoft SDK* as **PrivilegeCheck**.

### TokenHandle

`HANDLE` to Token Object opened with `TOKEN_QUERY` access.

### RequiredPrivileges

Pointer to `PRIVILEGE_SET` structure contains definitions of privileges to check.

### Result

Result of call - pointer to `BOOLEAN` value containing *TRUE* is all asked privileges are enabled.

# Documented by

* Tomasz Nowak

# See also

* `NtAdjustPrivilegesToken`
* `NtCreateToken`
* `NtOpenProcessToken`
* `NtOpenThreadToken`
* `PRIVILEGE_SET`
