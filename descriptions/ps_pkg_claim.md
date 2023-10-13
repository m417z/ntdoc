This structure stores various properties of token package identity.

# Applicable to
 - `RtlQueryPackageClaims`
 - `RtlQueryPackageIdentityEx`

# Members

## Flags
Defines a bit mask of various package identity flags:
 - `PSM_ACTIVATION_TOKEN_PACKAGED_APPLICATION`
 - `PSM_ACTIVATION_TOKEN_SHARED_ENTITY`
 - `PSM_ACTIVATION_TOKEN_FULL_TRUST`
 - `PSM_ACTIVATION_TOKEN_NATIVE_SERVICE`
 - `PSM_ACTIVATION_TOKEN_DEVELOPMENT_APP`
 - `PSM_ACTIVATION_TOKEN_BREAKAWAY_INHIBITED`
 - `PSM_ACTIVATION_TOKEN_RUNTIME_BROKER`
 - `PSM_ACTIVATION_TOKEN_UNIVERSAL_CONSOLE`
 - `PSM_ACTIVATION_TOKEN_WIN32ALACARTE_PROCESS`

## Origin
Defines the origin of the package. The underlying enumeration is [`PackageOrigin`](https://learn.microsoft.com/en-us/windows/win32/api/appmodel/ne-appmodel-packageorigin), which is documented in Windows SDK:
 - `PackageOrigin_Unknown` (0)
 - `PackageOrigin_Unsigned` (1)
 - `PackageOrigin_Inbox` (2)
 - `PackageOrigin_Store` (3)
 - `PackageOrigin_DeveloperUnsigned` (4)
 - `PackageOrigin_DeveloperSigned` (5)
 - `PackageOrigin_LineOfBusiness` (6)

# Required OS version
Package identities were introduced in Windows 8.
