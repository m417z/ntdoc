Determines if two tokens are identical for the purpose of access checks. This function is [documented in Windows SDK](https://learn.microsoft.com/en-us/windows/win32/secauthz/ntcomparetokens).

# Parameters
 - `FirstTokenHandle` - a handle to the first token. The handle must grant `TOKEN_QUERY` access.
 - `SecondTokenHandle` - a handle to the second token. The handle must grant `TOKEN_QUERY` access.
 - `Equal` - a pointer to a variable that receives whether the two tokens are equal.

# Implementation details
The function compares the user, groups, restricting SIDs, privileges, trust level, mandatory policy, AppContainer SID, capabilities, claims, and security attributes.

Note that this function does not support token pseudo-handles such as `NtCurrentProcessToken`. If you want to compare the current process/thread token, you need to open it first.

# See also
 - `NtQueryInformationToken`
 - `NtDuplicateToken`
