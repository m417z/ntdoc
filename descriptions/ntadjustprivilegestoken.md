Enables, disables, or removes privileges from the token.

# Parameters
 - `TokenHandle` - a handle to the token. The handle must grant `TOKEN_ADJUST_PRIVILEGES` access. Additionally, the handle must grant `TOKEN_QUERY` when the caller provides the `PreviousState` buffer.
 - `DisableAllPrivileges` - a boolean indicating if the function should disable all privileges present in the token.
 - `NewState` - an optional pointer to a collection of privilege LUIDs with their desired states, such as `SE_PRIVILEGE_DISABLED` (`0`), `SE_PRIVILEGE_ENABLED`, or `SE_PRIVILEGE_REMOVED`.
 - `BufferLength` - the size of the `PreviousState` buffer in bytes.
 - `PreviousState` - an optional pointer to a user-allocated buffer that receives the state of token privileges prior to adjustment.
 - `ReturnLength` - an optional pointer to a variable that receives the number of bytes written to the `PreviousState` buffer when the function succeeds or the number of bytes requires when the buffer is too small.

# Notable return values
 - `STATUS_NOT_ALL_ASSIGNED` - this successful status indicates that not all of the requested privileges were adjusted, such as when they are not present or cannot be enabled.
 - `STATUS_BUFFER_TOO_SMALL` - the previous state data does not fit into the provided buffer.

# Remarks
Disabled privileges are not taken into account during access checks. Some privileges cannot be enabled when token integrity level is too low. Removing privileges in an irreversible operation because this function can only enable privileges that are already present in the token.

Note that this function does not support token pseudo-handles such as `NtCurrentProcessToken`. If you want to adjust the current process/thread token, you need to open it first.

# Related Win32 API
 - [`AdjustTokenPrivileges`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-adjusttokenprivileges)

# See also
 - `NtFilterToken`
 - `NtAdjustGroupsToken`
 - `RtlRemovePrivileges`
 - `NtOpenProcessToken`
 - `NtOpenThreadToken`
