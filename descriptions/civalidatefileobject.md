Performs end-to-end Authenticode validation of a file given only a `FILE_OBJECT`. The routine maps the file into system address space, parses its PE headers, computes the Authenticode digest, and then verifies the signature either from the embedded security directory or from a matching catalog entry. On success it optionally returns the digest it computed so that the caller does not have to read the file a second time.

# Parameters
 - `FileObject` - a pointer to the `FILE_OBJECT` of the image to validate. The caller must hold a reference on the object for the duration of the call.
 - `PolicyFlags` - a bit mask of `CI_POLICY_*` flags controlling the verification policy (for example `CI_POLICY_CHECK_PROTECTED_PROCESS_EKU`, `CI_POLICY_FORCE_PROTECTED_PROCESS_POLICY`, `CI_POLICY_ACCEPT_ANY_ROOT_CERTIFICATE`). Flags outside `CI_POLICY_VALID_FLAGS` are rejected.
 - `LevelCheck` - an `SE_SIGNING_LEVEL` value describing the minimum signing level that must be satisfied, for example `SE_SIGNING_LEVEL_WINDOWS` or `SE_SIGNING_LEVEL_ANTIMALWARE`.
 - `PolicyInfo` - a pointer to a `MINCRYPT_POLICY_INFO` structure that receives information about the signer. The caller must release it with `CiFreePolicyInfo` when it is no longer needed. Before calling, set the `Size` field to `sizeof(MINCRYPT_POLICY_INFO)`.
 - `TimeStampPolicyInfo` - a pointer to a `MINCRYPT_POLICY_INFO` structure that receives information about the timestamping authority, with the same ownership and release rules as `PolicyInfo`.
 - `SigningTime` - a pointer that receives the counter-signed time of signing, when available.
 - `Thumbprint` - a buffer that receives the Authenticode digest that was used to perform the verification. May be `NULL` together with a zero `*ThumbprintSize` if the digest is not needed.
 - `ThumbprintSize` - on input, the size of the `Thumbprint` buffer in bytes; on output, the number of bytes written. On insufficient buffer, the function returns `STATUS_BUFFER_TOO_SMALL` with the required size written back.
 - `ThumbprintAlgorithm` - a pointer that receives the algorithm identifier (an `ALG_ID` such as `CALG_SHA_256`) used to compute the returned digest.

# Return value
Returns `STATUS_SUCCESS` if the file is signed and the signature satisfies the requested policy. A failure `NTSTATUS` is returned otherwise; in that case the `VerificationStatus` and `PolicyBits` fields of the `MINCRYPT_POLICY_INFO` structures indicate the specific failure reason.

# Remarks
This function is exported from `ci.dll` and is the preferred entry point for drivers that do not need to pre-hash the image themselves. It applies a stricter policy than `CiCheckSignedFile`, which means that some images that `CiCheckSignedFile` would accept can be rejected here.

Internally it tries the embedded Authenticode signature first and falls back to the catalog store (equivalent to `CiVerifyHashInCatalog`) when no embedded signature is present.

Within the kernel, `CiValidateFileObject` is reached through the Code Integrity function table that `ntoskrnl.exe` populates during `CiInitialize`; it underlies the signing-level enforcement performed by `SeCodeIntegrity` routines when protected processes and signed drivers are loaded.

For more details, see [Code Integrity in the Kernel: A Look Into ci.dll](https://www.cybereason.com/blog/code-integrity-in-the-kernel-a-look-into-cidll) by Liron Zuarets and Ido Moshe.

# See also
 - `CiCheckSignedFile`
 - `CiVerifyHashInCatalog`
 - `CiFreePolicyInfo`
 - `CiGetCertPublisherName`
 - `MINCRYPT_POLICY_INFO`
 - `SE_SIGNING_LEVEL`
