Searches the installed signature catalogs for an entry that matches the supplied file hash and verifies the signature on the containing catalog. This is how Code Integrity validates files that are not signed inline, such as most Windows system binaries whose signatures live in `\SystemRoot\System32\CatRoot`.

# Parameters
 - `Hash` - a pointer to the file digest to look up in the catalogs.
 - `HashSize` - the size of the digest in bytes.
 - `AlgorithmId` - the algorithm used to compute the digest, such as `CALG_SHA1` or `CALG_SHA_256`. Only catalog entries indexed with the same algorithm are considered.
 - `ReloadCatalogs` - when non-zero, forces the Code Integrity subsystem to rescan the catalog store before performing the lookup. Use this to pick up catalogs that were installed after the module was first loaded.
 - `SecureProcess` - when non-zero, requests stricter policy that is appropriate for protected-process image loads; the exact semantics are a superset of the normal driver policy.
 - `AcceptRoots` - a bit mask of `MINCRYPT_POLICY_*_ROOT` values identifying which root authorities are acceptable for the catalog signer. Passing zero restricts verification to the default set for the current policy.
 - `PolicyInfo` - an optional pointer to a `MINCRYPT_POLICY_INFO` structure that receives information about the catalog signer, including the certificate chain and the matched root authority. The caller must release it with `CiFreePolicyInfo` when it is no longer needed. Before calling, set the `Size` field to `sizeof(MINCRYPT_POLICY_INFO)`.
 - `CatalogName` - an optional pointer to a `UNICODE_STRING` that receives the full path of the catalog file that contained the matching hash. The buffer is allocated by the callee and must be released with `RtlFreeUnicodeString`.
 - `SigningTime` - an optional pointer that receives the counter-signed time of signing, when available.
 - `TimeStampPolicyInfo` - an optional pointer to a `MINCRYPT_POLICY_INFO` structure that receives information about the timestamping authority, with the same ownership and release rules as `PolicyInfo`.

# Return value
Returns `STATUS_SUCCESS` if a matching catalog entry is found and the catalog itself carries a valid signature that chains to an accepted root. A failure `NTSTATUS` is returned when no catalog contains the hash or when the catalog signature does not verify.

# Remarks
This function is exported from `ci.dll`. It is used together with `CiCheckSignedFile`: callers typically call `CiCheckSignedFile` first to look for an embedded signature and fall back to `CiVerifyHashInCatalog` when no embedded signature is present.

Prior to Windows 7 SP1 with KB 2775511 (build 6.1.7601.18519), the function had a legacy prototype that only accepted SHA-1 hashes and did not take explicit size and algorithm parameters; the current prototype replaces it on all supported systems.

# See also
 - `CiCheckSignedFile`
 - `CiValidateFileObject`
 - `CiFreePolicyInfo`
 - `MINCRYPT_POLICY_INFO`
