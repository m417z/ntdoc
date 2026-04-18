Searches the installed signature catalogs for an entry that matches the supplied file hash and verifies the signature on the containing catalog.

# Parameters
 - `Hash` - a pointer to the file digest to look up in the catalogs.
 - `HashSize` - the size of the digest in bytes.
 - `AlgorithmId` - the algorithm used to compute the digest, such as `CALG_SHA1` or `CALG_SHA_256`.
 - `ReloadCatalogs` - controls whether the Code Integrity subsystem rescans the catalog store before performing the lookup. The precise semantics of non-zero values are not publicly documented.
 - `SecureProcess` - selects a stricter verification policy when non-zero. The precise semantics are not publicly documented.
 - `AcceptRoots` - additional bits controlling which root authorities are acceptable for the catalog signer. The precise encoding is not publicly documented; typical values are drawn from the `MINCRYPT_POLICY_*_ROOT` flags.
 - `PolicyInfo` - an optional pointer to a `MINCRYPT_POLICY_INFO` structure that receives information about the catalog signer. The caller must release it with `CiFreePolicyInfo` when it is no longer needed.
 - `CatalogName` - an optional pointer to a `UNICODE_STRING` that receives the full path of the catalog file that contained the matching hash. The buffer is allocated by the callee and must be released with `RtlFreeUnicodeString`.
 - `SigningTime` - an optional pointer that receives the counter-signed time of signing, when available.
 - `TimeStampPolicyInfo` - an optional pointer to a `MINCRYPT_POLICY_INFO` structure that receives information about the timestamping authority, with the same ownership and release rules as `PolicyInfo`.

# Remarks
This function is exported from `ci.dll`.

Prior to build 6.1.7601.18519, the function had a legacy prototype that only accepted SHA-1 hashes and did not take explicit size and algorithm parameters.

The meaning of the `ReloadCatalogs`, `SecureProcess`, and `AcceptRoots` parameters described above is inferred from their names; they are not covered by any public documentation known to us.

# See also
 - `CiCheckSignedFile`
 - `CiValidateFileObject`
 - `CiFreePolicyInfo`
 - `MINCRYPT_POLICY_INFO`
