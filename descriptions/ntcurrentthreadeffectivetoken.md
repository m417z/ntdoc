This macro defines a pseudo-handle that allows querying information about the effective token token of the calling thread without explicitly opening it. The effective token is the thread token when the thread is impersonating or the process token otherwise.

# Applicable to
 - `NtQueryInformationToken`
 - `NtQuerySecurityAttributesToken`

# Remarks
Note that as opposed to `NtCurrentProcess` and `NtCurrentThread`, the system does not accept token pseudo-handles outside of the token-querying function.

# Required OS version
This macro was introduced in Windows 8.

# See also
 - `NtCurrentThreadToken`
 - `NtCurrentProcessToken`
 - `NtOpenThreadToken`
 - `NtOpenThreadTokenEx`
 - `NtOpenProcessToken`
 - `NtOpenProcessTokenEx`
