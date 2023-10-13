Removes all privileges from the token except for the specified ones.

# Parameters
 - `TokenHandle` - a handle to the token to modify. The handle must grant `TOKEN_QUERY | TOKEN_ADJUST_PRIVILEGES` access.
 - `PrivilegesToKeep` - a pointer to an array of privilege IDs to keep.
 - `PrivilegeCount` - the number of elements passed in the `PrivilegesToKeep` parameter.

# Notable return values
 - `STATUS_NOT_ALL_ASSIGNED` - this successful status indicates that not all of the requested privileges were adjusted, such as when they are not present.

# Remarks
Note that this function does not support token pseudo-handles such as `NtCurrentProcessToken`. If you want to adjust the current process/thread token, you need to open it first.

# Implementation details
This function enumerates available privileges via `NtQueryInformationToken` with `TokenPrivileges` and then modifies them via `NtAdjustPrivilegesToken`.

# See also
 - `NtAdjustPrivilegesToken`
 - `NtFilterToken`
 - `NtOpenProcessToken`
 - `NtOpenThreadToken`
