Constructs SIDs for named capabilities.

# Parameters
 - `UnicodeString` - a pointer to string specifying the name of the capability.
 - `CapabilityGroupSid` - a pointer to a user-allocated buffer that receives the capability group SID. The buffer must be at least `RtlLengthRequiredSid(SECURITY_INSTALLER_GROUP_CAPABILITY_RID_COUNT)` bytes in size.
 - `CapabilitySid` - a pointer to a user-allocated buffer that receives the capability SID. The buffer must be at least `RtlLengthRequiredSid(SECURITY_INSTALLER_CAPABILITY_RID_COUNT)` bytes in size.

# Implementation details
`CapabilityGroupSid` always belongs to `SECURITY_NT_AUTHORITY` (5) with `SECURITY_INSTALLER_GROUP_CAPABILITY_BASE` (32) and has `SECURITY_INSTALLER_GROUP_CAPABILITY_RID_COUNT` (9) sub-authorities. In other words, the SID looks like `S-1-5-32-x-x-x-x-x-x-x-x`, where the values are taken from a SHA256 hash of the uppercased capability name.

The structure of `CapabilitySid` is more complex because it depends on the type of capability. The function recognizes three types: legacy, hash-based, and AppSilo.

## Legacy capabilities
Windows defines twelve legacy capabilities that were originally introduced in Windows 8:

Name                         | RID
---------------------------- | ---
`internetClient`             | `SECURITY_CAPABILITY_INTERNET_CLIENT` (1)
`internetClientServer`       | `SECURITY_CAPABILITY_INTERNET_CLIENT_SERVER` (2)
`privateNetworkClientServer` | `SECURITY_CAPABILITY_PRIVATE_NETWORK_CLIENT_SERVER` (3)
`picturesLibrary`            | `SECURITY_CAPABILITY_PICTURES_LIBRARY` (4)
`videosLibrary`              | `SECURITY_CAPABILITY_VIDEOS_LIBRARY` (5)
`musicLibrary`               | `SECURITY_CAPABILITY_MUSIC_LIBRARY` (6)
`documentsLibrary`           | `SECURITY_CAPABILITY_DOCUMENTS_LIBRARY` (7)
`enterpriseAuthentication`   | `SECURITY_CAPABILITY_ENTERPRISE_AUTHENTICATION` (8)
`sharedUserCertificates`     | `SECURITY_CAPABILITY_SHARED_USER_CERTIFICATES` (9)
`removableStorage`           | `SECURITY_CAPABILITY_REMOVABLE_STORAGE` (10)
`appointments`               | `SECURITY_CAPABILITY_APPOINTMENTS` (11)
`contacts`                   | `SECURITY_CAPABILITY_CONTACTS` (12)

For these names, the `CapabilitySid` parameter receives a short SID that belongs to `SECURITY_APP_PACKAGE_AUTHORITY` (15) with `SECURITY_CAPABILITY_BASE_RID` (3) and has `SECURITY_BUILTIN_CAPABILITY_RID_COUNT` (2) sub-authorities. In other words, the SID looks like `S-1-15-3-x`, where the value is taken from the table above.

## Hash-based capabilities
Most names result in `CapabilitySid` receiving a SID that belongs to `SECURITY_APP_PACKAGE_AUTHORITY` (15) with `SECURITY_CAPABILITY_BASE_RID` (3) followed by `SECURITY_CAPABILITY_APP_RID` (1024) and has `SECURITY_INSTALLER_CAPABILITY_RID_COUNT` (10) sub-authorities. In other words, the SID looks like `S-1-15-3-1024-x-x-x-x-x-x-x-x`, where the values are taken from a SHA256 hash of the uppercased capability name.

## AppSilo capabilities
Starting from Windows 11 22H2, the function handles names that start with `isolatedWin32-` differently. In this case, `CapabilitySid` receives a SID that belongs to `SECURITY_APP_PACKAGE_AUTHORITY` (15) with `SECURITY_CAPABILITY_BASE_RID` (3) followed by `SECURITY_CAPABILITY_APP_SILO_RID` (65536) and has `SECURITY_INSTALLER_CAPABILITY_RID_COUNT` (10) sub-authorities. In other words, the SID looks like `S-1-15-3-65536-x-x-x-x-x-x-x-x`, where the values are taken from a SHA256 hash of the uppercased capability name.

# Required OS version
This function was introduced in Windows 10 TH1 (1507).

# Related Win32 API
 - [`DeriveCapabilitySidsFromName`](https://learn.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-derivecapabilitysidsfromname)

# See also
 - `RtlIsCapabilitySid`
 - `NtCreateLowBoxToken`
