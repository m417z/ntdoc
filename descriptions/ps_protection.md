This structure defines the protection level for fully- and light-protected processes.

# Applicable to
 - `NtQueryInformationProcess` with `ProcessProtectionInformation` (61)
 - `PS_ATTRIBUTE_PROTECTION_LEVEL`
 - `RtlValidProcessProtection`
 - `RtlTestProtectedAccess`

# Members

## Level
The numerical value of the protection level. You can use the `PsProtectedValue` macro to construct this value from the underlying fields.

### Type
The type of protection applied to the process. The values for this field come from the `PS_PROTECTED_TYPE` enumeration.

#### Known values
 - `PsProtectedTypeNone` (0) - the process is not running as protected.
 - `PsProtectedTypeProtectedLight` (1) - the process is running as light-protected (PPL).
 - `PsProtectedTypeProtected` (2) - the process is running as fully-protected.

### Audit
This flag indicates that the system should audit the operation instead of applying protection.

### Signer
The strength and type of the signature for the process. The values for this field come from the `PS_PROTECTED_SIGNER` enumeration.

#### Known values
 - `PsProtectedSignerNone` (0) - the process has no signature that grants it protection.
 - `PsProtectedSignerAuthenticode` (1) - the process has an Authenticode signature.
 - `PsProtectedSignerCodeGen` (2) - the process has a Code Generation signature.
 - `PsProtectedSignerAntimalware` (3) - the process has an Antimalware signature.
 - `PsProtectedSignerLsa` (4) - the process has an LSA signature.
 - `PsProtectedSignerWindows` (5) - the process has a Windows signature.
 - `PsProtectedSignerWinTcb` (6) - the process has a WinTCB (trusted computer base) signature.
 - `PsProtectedSignerWinSystem` (7) - the process has a WinSystem signature.
 - `PsProtectedSignerApp` (8) - the process has a Store Application signature.

# See also
 - `InitializePsProtection`

# Required OS version
This structure was introduced in Windows 8.1.
