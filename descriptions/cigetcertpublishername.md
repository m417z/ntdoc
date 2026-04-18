Parses a DER-encoded X.509 certificate and extracts the publisher (subject common name) as a `UNICODE_STRING`. This is a convenience routine that callers can invoke after a successful signature verification to obtain a human-readable signer name from the certificate chain returned in a `MINCRYPT_POLICY_INFO` structure.

# Parameters
 - `Certificate` - a pointer to a `CRYPT_DER_BLOB` that contains the DER-encoded certificate to parse. This is typically the `Certificate` field of one of the `MINCRYPT_CHAIN_ELEMENT` entries reached via `MINCRYPT_POLICY_INFO.ChainInfo.ChainElements` after a call to `CiCheckSignedFile`, `CiVerifyHashInCatalog`, or `CiValidateFileObject`.
 - `AllocateRoutine` - a pointer to a caller-supplied allocator that the function invokes to obtain the backing storage for the returned string. The allocator is called with the number of bytes required and must return a pointer to memory that the caller will later release.
 - `PublisherName` - a pointer to a `UNICODE_STRING` that receives the publisher name. The `Buffer` field is set to memory obtained from `AllocateRoutine` and becomes the caller's responsibility to free.

# Return value
Returns `STATUS_SUCCESS` on success. A failure `NTSTATUS` is returned if the certificate cannot be parsed, the subject common name is missing, or the allocator returns `NULL`.

# Remarks
This function is exported from `ci.dll`. The allocator is parameterized so that the routine can be used both from contexts that allocate from the non-paged pool (such as a driver reacting to a process-creation notification) and from contexts that prefer the paged pool; the function itself runs at `PASSIVE_LEVEL`.

# See also
 - `CiValidateFileObject`
 - `CiCheckSignedFile`
 - `CiVerifyHashInCatalog`
 - `MINCRYPT_POLICY_INFO`
 - `MINCRYPT_CHAIN_ELEMENT`
