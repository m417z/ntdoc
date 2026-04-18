For an input Authenticode file digest and an Authenticode signature, verifies that the digest is in the signature and that the signature validates. Optionally returns information about the signature. The caller is responsible for mapping the image, parsing its PE headers, locating the `WIN_CERTIFICATE` in the security directory, and computing the Authenticode digest.

# Parameters
 - `Hash` - a pointer to the Authenticode digest of the file being verified.
 - `HashSize` - the size of the digest in bytes.
 - `AlgorithmId` - the algorithm that was used to compute the digest, such as `CALG_SHA1` or `CALG_SHA_256`. The verifier iterates over the signatures embedded in the `WIN_CERTIFICATE` blob and selects the one whose digest algorithm matches this value.
 - `Signature` - a pointer to the raw `WIN_CERTIFICATE` bytes read from the PE security directory.
 - `SignatureSize` - the size of the signature blob, in bytes.
 - `PolicyInfo` - an optional pointer to a `MINCRYPT_POLICY_INFO` structure that receives information about the signer, including the certificate chain. The caller must release it with `CiFreePolicyInfo` when it is no longer needed.
 - `SigningTime` - an optional pointer that receives the time of signing, when available.
 - `TimeStampPolicyInfo` - an optional pointer to a `MINCRYPT_POLICY_INFO` structure that receives information about the timestamping authority, with the same ownership and release rules as `PolicyInfo`.

# Remarks
This function is exported from `ci.dll`. It is suitable for drivers that have already mapped and hashed the target image themselves. `CiValidateFileObject` provides a higher-level alternative that performs the mapping and hashing for the caller but applies a stricter policy.

Prior to build 6.1.7601.18519, the function had a legacy prototype that only accepted SHA-1 hashes and did not take explicit size and algorithm parameters.

For more details, see [Code Integrity in the Kernel: A Look Into ci.dll](https://www.cybereason.com/blog/code-integrity-in-the-kernel-a-look-into-cidll) by Liron Zuarets and Ido Moshe.

# See also
 - `CiFreePolicyInfo`
 - `CiValidateFileObject`
 - `CiVerifyHashInCatalog`
 - `MINCRYPT_POLICY_INFO`
