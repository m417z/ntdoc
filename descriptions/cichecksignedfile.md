Verifies an Authenticode signature against a precomputed file hash. The caller is responsible for mapping the image, parsing its PE headers, locating the `WIN_CERTIFICATE` in the security directory, and computing the Authenticode digest.

# Parameters
 - `Hash` - a pointer to the Authenticode digest of the file being verified.
 - `HashSize` - the size of the digest in bytes.
 - `AlgorithmId` - the algorithm that was used to compute the digest, such as `CALG_SHA1` or `CALG_SHA_256`. The verifier iterates over the signatures embedded in the `WIN_CERTIFICATE` blob and selects the one whose digest algorithm matches this value.
 - `Signature` - a pointer to the raw `WIN_CERTIFICATE` bytes read from the PE security directory.
 - `SignatureSize` - the size of the signature blob, in bytes.
 - `PolicyInfo` - an optional pointer to a `MINCRYPT_POLICY_INFO` structure that receives information about the signer, including the certificate chain and root authority. The caller must release it with `CiFreePolicyInfo` when it is no longer needed. Before calling, set the `Size` field to `sizeof(MINCRYPT_POLICY_INFO)`.
 - `SigningTime` - an optional pointer that receives the counter-signed time of signing, when available.
 - `TimeStampPolicyInfo` - an optional pointer to a `MINCRYPT_POLICY_INFO` structure that receives information about the timestamping authority, with the same ownership and release rules as `PolicyInfo`.

# Return value
Returns `STATUS_SUCCESS` when the digest is covered by a valid signature that chains to a trusted root. When verification fails, the function returns a failure `NTSTATUS` and, if `PolicyInfo` was provided, the `VerificationStatus` and `PolicyBits` fields indicate the specific reason (for example, `MINCRYPT_POLICY_NO_SIGNATURE`, `MINCRYPT_POLICY_BAD_SIGNATURE`, `MINCRYPT_POLICY_BAD_CHAIN`).

# Remarks
This function is exported from `ci.dll`. It is suitable for drivers that have already mapped and hashed the target image themselves, for instance to avoid remapping a file object that is already present in memory. `CiValidateFileObject` provides a higher-level alternative that performs the mapping and hashing for the caller but applies a stricter policy.

Prior to Windows 7 SP1 with KB 2775511 (build 6.1.7601.18519), the function had a legacy prototype that only accepted SHA-1 hashes and did not take explicit size and algorithm parameters; the current prototype replaces it on all supported systems.

For more details, see [Code Integrity in the Kernel: A Look Into ci.dll](https://www.cybereason.com/blog/code-integrity-in-the-kernel-a-look-into-cidll) by Liron Zuarets and Ido Moshe.

# See also
 - `CiFreePolicyInfo`
 - `CiValidateFileObject`
 - `CiVerifyHashInCatalog`
 - `MINCRYPT_POLICY_INFO`
