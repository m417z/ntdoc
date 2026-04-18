Releases the resources referenced by a `MINCRYPT_POLICY_INFO` structure populated by one of the Code Integrity signature verification routines (such as `CiCheckSignedFile`, `CiVerifyHashInCatalog`, or `CiValidateFileObject`).

# Parameters
 - `PolicyInfo` - a pointer to the `MINCRYPT_POLICY_INFO` structure to release. The structure itself is owned by the caller; only the inner buffers (most notably the certificate chain information) are freed. The routine checks the structure for embedded allocations and does nothing if none are present, so it is safe to call on a zero-initialized structure or one whose verification failed.

# Remarks
Both the signer `MINCRYPT_POLICY_INFO` and the timestamping-authority `MINCRYPT_POLICY_INFO` populated by the verification APIs must be released by a separate call to this function. Failing to do so leaks the chain information buffer.

This function is exported from `ci.dll` (the kernel-mode Code Integrity module). It is loaded dynamically at runtime by drivers that need to validate image signatures, typically through `MmGetSystemRoutineAddress` or an import table exposed by `ntoskrnl.exe` via `SeCodeIntegrityQueryInformation` and related infrastructure.

For more details, see [Code Integrity in the Kernel: A Look Into ci.dll](https://www.cybereason.com/blog/code-integrity-in-the-kernel-a-look-into-cidll) by Liron Zuarets and Ido Moshe.

# See also
 - `MINCRYPT_POLICY_INFO`
 - `CiCheckSignedFile`
 - `CiVerifyHashInCatalog`
 - `CiValidateFileObject`
