Parses a DER-encoded certificate and returns the publisher name as a `UNICODE_STRING`. Typically used after a successful signature verification to obtain a human-readable signer name from the certificate chain returned in a `MINCRYPT_POLICY_INFO` structure.

# Parameters
 - `Certificate` - a pointer to a `CRYPT_DER_BLOB` that contains the DER-encoded certificate to parse. This is typically the `Certificate` field of one of the `MINCRYPT_CHAIN_ELEMENT` entries reached via `MINCRYPT_POLICY_INFO.ChainInfo.ChainElements` after a call to `CiCheckSignedFile`, `CiVerifyHashInCatalog`, or `CiValidateFileObject`.
 - `AllocateRoutine` - a pointer to a caller-supplied allocator that the function invokes to obtain the backing storage for the returned string.
 - `PublisherName` - a pointer to a `UNICODE_STRING` that receives the publisher name. The `Buffer` field is set to memory obtained from `AllocateRoutine` and becomes the caller's responsibility to free.

# Remarks
This function is exported from `ci.dll`.

The exact portion of the certificate that is returned (for example, the subject common name versus the full subject) is not covered by any public documentation known to us.

# See also
 - `CiValidateFileObject`
 - `CiCheckSignedFile`
 - `CiVerifyHashInCatalog`
 - `MINCRYPT_POLICY_INFO`
 - `MINCRYPT_CHAIN_ELEMENT`
