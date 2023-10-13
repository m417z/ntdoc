Determines if the specified SID is a capability SID.

# Parameters
 - `Sid` - a SID to check.

# Implementation details
The function checks if the SID belongs to `SECURITY_APP_PACKAGE_AUTHORITY` (15) with `SECURITY_CAPABILITY_BASE_RID` (3). In other words, it accepts `S-1-15-3-*` SIDs.

# Required OS version
This function was introduced in Windows 8.

# See also
 - `RtlDeriveCapabilitySidsFromName`
 - `NtCreateLowBoxToken`
