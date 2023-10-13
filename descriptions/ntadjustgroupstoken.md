Enables and disables groups in the token.

# Parameters
 - `TokenHandle` - a handle to the token. The handle must grant `TOKEN_ADJUST_GROUPS` access. Additionally, the handle must grant `TOKEN_QUERY` when the caller provides the `PreviousState` buffer.
 - `ResetToDefault` - a boolean indicating if the function should reset group states to their defaults based on the presence of `SE_GROUP_ENABLED_BY_DEFAULT` flag.
 - `NewState` - an optional pointer to a collection of group SIDs with their desired states, such as `SE_GROUP_DISABLED` (`0`) or `SE_GROUP_ENABLED`.
 - `BufferLength` - the size of the `PreviousState` buffer in bytes.
 - `PreviousState` - an optional pointer to a user-allocated buffer that receives the state of token groups prior to adjustment.
 - `ReturnLength` - an optional pointer to a variable that receives the number of bytes written to the `PreviousState` buffer when the function succeeds or the number of bytes requires when the buffer is too small.

# Notable return values
 - `STATUS_CANT_ENABLE_DENY_ONLY` - the caller attempted to enable a group that has `SE_GROUP_USE_FOR_DENY_ONLY` flag set.
 - `STATUS_CANT_DISABLE_MANDATORY` - the caller attempted to disable a group that has `SE_GROUP_MANDATORY` flag set.
 - `STATUS_NOT_ALL_ASSIGNED` - this successful status indicates that not all of the requested groups were adjusted, such as when they are not present.
 - `STATUS_BUFFER_TOO_SMALL` - the previous state data does not fit into the provided buffer.

# Remarks
Groups are taken into account for granting access checks when they have `SE_GROUP_ENABLED` flag set. Groups are taken into account for denying access checks when they have either `SE_GROUP_ENABLED` or `SE_GROUP_USE_FOR_DENY_ONLY` flags set.                                                                                                                                                                       

Note that this function does not support token pseudo-handles such as `NtCurrentProcessToken`. If you want to adjust the current process/thread token, you need to open it first.

# Related Win32 API
 - [`AdjustTokenGroups`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-adjusttokengroups)

# See also
 - `NtFilterToken`
 - `NtAdjustPrivilegesToken`
 - `NtOpenProcessToken`
 - `NtOpenThreadToken`
