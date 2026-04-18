Releases the resources referenced by a `MINCRYPT_POLICY_INFO` structure populated by one of the Code Integrity signature verification routines (such as `CiCheckSignedFile`, `CiVerifyHashInCatalog`, or `CiValidateFileObject`).

# Parameters
 - `PolicyInfo` - a pointer to the `MINCRYPT_POLICY_INFO` structure to release. The structure itself is owned by the caller; the inner certificate chain information buffer is freed. The routine is safe to call on a structure that was not populated (for example, when the preceding verification call failed).

# Remarks
This function is exported from `ci.dll`, the kernel-mode Code Integrity module.

For more details, see [Code Integrity in the Kernel: A Look Into ci.dll](https://www.cybereason.com/blog/code-integrity-in-the-kernel-a-look-into-cidll) by Liron Zuarets and Ido Moshe.

# See also
 - `MINCRYPT_POLICY_INFO`
 - `CiCheckSignedFile`
 - `CiVerifyHashInCatalog`
 - `CiValidateFileObject`
