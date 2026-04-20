Frees memory allocated by other Code Integrity signature verification functions and referenced from a `MINCRYPT_POLICY_INFO` structure.

# Parameters
 - `PolicyInfo` - a pointer to the `MINCRYPT_POLICY_INFO` structure to release. The structure itself is owned by the caller; the inner certificate chain information buffer is freed. The routine is safe to call on a structure that was not populated (for example, when the preceding verification call failed).

# Remarks
This function is exported from `ci.dll`, the kernel-mode Code Integrity module.

Per the FIPS 140-2 [Code Integrity Security Policy Document](https://csrc.nist.gov/CSRC/media/projects/cryptographic-module-validation-program/documents/security-policies/140sp3644.pdf) (Microsoft, Windows 10 1809 / Windows Server 2019), the function "frees memory allocated by the `CiVerifyHashInCatalog`, `CiCheckSignedFile`, `CiFindPageHashesInCatalog`, and `CiFindPageHashesInSignedFile` functions". The same release is used for the `MINCRYPT_POLICY_INFO` structures produced by `CiValidateFileObject`, as documented in the Cybereason write-up below.

For more details, see [Code Integrity in the Kernel: A Look Into ci.dll](https://www.cybereason.com/blog/code-integrity-in-the-kernel-a-look-into-cidll) by Liron Zuarets and Ido Moshe.

# See also
 - `MINCRYPT_POLICY_INFO`
 - `CiCheckSignedFile`
 - `CiVerifyHashInCatalog`
 - `CiValidateFileObject`
