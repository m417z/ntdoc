Performs end-to-end Authenticode validation of a file given only a `FILE_OBJECT`. The routine maps the file into system address space, computes the Authenticode digest, and verifies the signature. On success it optionally returns the digest it computed so that the caller does not have to hash the file a second time.

# Parameters
 - `FileObject` - a pointer to the `FILE_OBJECT` of the image to validate.
 - `PolicyFlags` - a bit mask of `CI_POLICY_*` flags controlling the verification policy (for example `CI_POLICY_CHECK_PROTECTED_PROCESS_EKU`, `CI_POLICY_FORCE_PROTECTED_PROCESS_POLICY`, `CI_POLICY_ACCEPT_ANY_ROOT_CERTIFICATE`).
 - `LevelCheck` - an `SE_SIGNING_LEVEL` value passed to the verifier as part of the requested policy.
 - `PolicyInfo` - a pointer to a `MINCRYPT_POLICY_INFO` structure that receives information about the signer. The caller must release it with `CiFreePolicyInfo` when it is no longer needed.
 - `TimeStampPolicyInfo` - a pointer to a `MINCRYPT_POLICY_INFO` structure that receives information about the timestamping authority, with the same ownership and release rules as `PolicyInfo`.
 - `SigningTime` - a pointer that receives the counter-signed time of signing, when available.
 - `Thumbprint` - a buffer that receives the Authenticode digest that was used to perform the verification.
 - `ThumbprintSize` - on input, the size of the `Thumbprint` buffer in bytes; on output, the number of bytes written.
 - `ThumbprintAlgorithm` - a pointer that receives the algorithm identifier (an `ALG_ID` such as `CALG_SHA_256`) used to compute the returned digest.

# Remarks
This function is exported from `ci.dll` and is the preferred entry point for drivers that do not need to pre-hash the image themselves. It applies a stricter policy than `CiCheckSignedFile`, which means that some images that `CiCheckSignedFile` would accept can be rejected here.

For more details, see [Code Integrity in the Kernel: A Look Into ci.dll](https://www.cybereason.com/blog/code-integrity-in-the-kernel-a-look-into-cidll) by Liron Zuarets and Ido Moshe.

# See also
 - `CiCheckSignedFile`
 - `CiVerifyHashInCatalog`
 - `CiFreePolicyInfo`
 - `CiGetCertPublisherName`
 - `MINCRYPT_POLICY_INFO`
 - `SE_SIGNING_LEVEL`
