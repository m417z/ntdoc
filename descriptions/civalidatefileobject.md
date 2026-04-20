Verifies the signature of a file object and returns the policy info along with the timestamp and signing time. The routine maps the file into system address space, computes the Authenticode digest, and verifies the signature. The computed digest is returned to the caller through the `Thumbprint` output parameters.

# Parameters
 - `FileObject` - a pointer to the `FILE_OBJECT` of the image to validate.
 - `PolicyFlags` - a bit mask of `CI_POLICY_*` flags controlling the verification policy (for example `CI_POLICY_CHECK_PROTECTED_PROCESS_EKU`, `CI_POLICY_FORCE_PROTECTED_PROCESS_POLICY`, `CI_POLICY_ACCEPT_ANY_ROOT_CERTIFICATE`).
 - `LevelCheck` - an `SE_SIGNING_LEVEL` value. The precise role of this parameter is not publicly documented; the name suggests it selects the signing level to enforce.
 - `PolicyInfo` - a pointer to a `MINCRYPT_POLICY_INFO` structure that receives information about the signer. The caller must release it with `CiFreePolicyInfo` when it is no longer needed.
 - `TimeStampPolicyInfo` - a pointer to a `MINCRYPT_POLICY_INFO` structure that receives information about the timestamping authority, with the same ownership and release rules as `PolicyInfo`.
 - `SigningTime` - a pointer that receives the time of signing, when available.
 - `Thumbprint` - a buffer that receives the Authenticode digest that was used to perform the verification.
 - `ThumbprintSize` - on input, the size of the `Thumbprint` buffer in bytes; on output, the number of bytes written.
 - `ThumbprintAlgorithm` - a pointer that receives the algorithm identifier (an `ALG_ID` such as `CALG_SHA_256`) used to compute the returned digest.

# Remarks
This function is exported from `ci.dll`. Unlike `CiCheckSignedFile`, it performs the mapping and hashing of the image itself. It also applies a stricter policy than `CiCheckSignedFile`, which means that some images that `CiCheckSignedFile` would accept can be rejected here.

In practice, several contributors have reported that with a zero `PolicyFlags` the function rejects images signed with non-Microsoft root certificates unless test-signing mode is enabled, and that setting `CI_POLICY_ACCEPT_ANY_ROOT_CERTIFICATE` (`0x20`) in `PolicyFlags` makes verification succeed on production systems. Reproduced on Windows 10 builds 19041 and 19045; see [CiDllDemo issue #5](https://github.com/Ido-Moshe-Github/CiDllDemo/issues/5).

In the same thread, contributors also report that the function returns `STATUS_INVALID_IMAGE_HASH` for PE images signed using ECDSA. An OSR forum analysis linked from the thread attributes this to a `MinCrypt_DisableEcdsa` routine invoked from `CipInitialize` during Code Integrity startup.

For more details, see [Code Integrity in the Kernel: A Look Into ci.dll](https://www.cybereason.com/blog/code-integrity-in-the-kernel-a-look-into-cidll) by Liron Zuarets and Ido Moshe.

# See also
 - `CiCheckSignedFile`
 - `CiVerifyHashInCatalog`
 - `CiFreePolicyInfo`
 - `CiGetCertPublisherName`
 - `MINCRYPT_POLICY_INFO`
 - `SE_SIGNING_LEVEL`
