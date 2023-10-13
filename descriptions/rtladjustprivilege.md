Enables or disables a single privilege in the current process or thread token.

# Parameters
 - `Privilege` - the LUID of the privilege to adjust.
 - `Enable` - a boolean indicating whether to enable or disable the privilege.
 - `Client` - a boolean indicating whether to perform the operation on the current process (`FALSE`) or thread (`TRUE`) token.
 - `WasEnabled` - a pointer to a to a variable that receives the previous state of the privilege.

# Notable return values
 - `STATUS_PRIVILEGE_NOT_HELD` - the privilege is not present in the token.
 - `STATUS_NO_TOKEN` - the caller requested to adjust a thread token, but the thread is not impersonating at the moment.

# Remarks
Disabled privileges are not taken into account during access checks. Some privileges cannot be enabled when token integrity level is too low.

# Implementation details
This function is a wrapper over `NtAdjustPrivilegesToken`.

# See also
 - `NtFilterToken`
 - `NtAdjustPrivilegesToken`
 - `NtOpenProcessToken`
 - `NtOpenThreadToken`
