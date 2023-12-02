The enumeration defines the strength and type of the signature for the process

# Known values
 - `PsProtectedSignerNone` (0) - the process has no signature that grants it protection.
 - `PsProtectedSignerAuthenticode` (1) - the process has an Authenticode signature.
 - `PsProtectedSignerCodeGen` (2) - the process has a Code Generation signature.
 - `PsProtectedSignerAntimalware` (3) - the process has an Antimalware signature.
 - `PsProtectedSignerLsa` (4) - the process has an LSA signature.
 - `PsProtectedSignerWindows` (5) - the process has a Windows signature.
 - `PsProtectedSignerWinTcb` (6) - the process has an WinTCB (trusted computer base) signature.
 - `PsProtectedSignerWinSystem` (7) - the process has an WinSystem signature.
 - `PsProtectedSignerApp` (8) - the process has a Store Application signature.

# See also
 - `PS_PROTECTION`
