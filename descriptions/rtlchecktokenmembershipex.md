Determines if a token can pass access checks against the specified SID.

# Parameters
 - `TokenHandle` - an optional handle to the token or one of the supported pseudo-handles (see below). The handle must grant `TOKEN_QUERY` access. The function uses (opens) the current thread's effective token if the caller passes `NULL` in this parameter.
 - `SidToCheck` - a SID to test for membership.
 - `Flags` - a bit mask that adjusts the behavior of the function. See below for supported values.
 - `IsMember` - a pointer to a variable that receives a boolean indicating whether the token has the SID.

# Flags
 - `CTMF_INCLUDE_APPCONTAINER` (0x01) - allow AppContainer tokens to pass the access check if that would be allowed otherwise.
 - `CTMF_INCLUDE_LPAC` (0x02) - allow Less Privileged AppContainers (LPAC) to pass the access check if it would be allowed otherwise. See `TOKEN_INFORMATION_CLASS` value `TokenIsLessPrivilegedAppContainer` for more details on LPAC. This flag was introduced in Windows 10 RS2 (1703).

# Pseudo-handles
This function supports the following pseudo-handle values:
 - `NtCurrentProcessToken` - performs the query on the primary token of the calling process.
 - `NtCurrentThreadToken` - performs the query on the impersonation token of the calling thread. The function fails if the thread is not impersonating.
 - `NtCurrentThreadEffectiveToken` - performs the query on the impersonation token of the calling thread, if present. Otherwise, the function uses the primary token of the calling process.

# Implementation details
This function creates a security descriptor with the owner set to the provided SID and a DACL that grants access to the SID. When the flag for including AppContainers is set, it also adds as access allowed ACE for `ALL APPLICATION PACKAGES` (`S-1-15-2-1`). When the LPAC flag is set, the function adds an access allowed ACE for `ALL RESTRICTED APPLICATION PACKAGES` (`S-1-15-2-2`). Then the function performs an access checks against it via `NtAccessCheck`. 

# Required OS version
This function was introduced in Windows 8.

# Related Win32 API
 - [`CheckTokenMembershipEx`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-checktokenmembershipex)

# See also
 - `RtlCheckTokenMembership`
 - `RtlCheckTokenCapability`
