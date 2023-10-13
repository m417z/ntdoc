This macro defines a pseudo-handle that allows querying information about the primary token of the calling process without explicitly opening it.

# Applicable to
 - `NtQueryInformationToken`
 - `NtQuerySecurityAttributesToken`

# Remarks
Note that as opposed to `NtCurrentProcess` and `NtCurrentThread`, the system does not accept token pseudo-handles outside of the token-querying function.

# Required OS version
This macro was introduced in Windows 8.

# See also
 - `NtCurrentThreadToken`
 - `NtCurrentThreadEffectiveToken`
 - `NtOpenProcessToken`
 - `NtOpenProcessTokenEx`
