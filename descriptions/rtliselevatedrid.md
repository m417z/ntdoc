Determines if the specified SID and attributes represent an elevated (admin-equivalent) group.

# Parameters
 - `SidAttr` - a pointer to a SID and their attributes.

# Implementation details
The function checks for the following conditions:
 - The attributes do not include `SE_GROUP_USE_FOR_DENY_ONLY` and `SE_GROUP_INTEGRITY`.
 - The first sub-authority is not within the range from `SECURITY_MIN_BASE_RID` (80) to `SECURITY_MAX_BASE_RID` (111).
 - The last sub-authority belongs to one of the following 19 values:

Constant                                                  | Value
--------------------------------------------------------- | -----
`SECURITY_LOCAL_ACCOUNT_AND_ADMIN_RID`                    | 114 (0x72)
`DOMAIN_GROUP_RID_ENTERPRISE_READONLY_DOMAIN_CONTROLLERS` | 498 (0x200)
`DOMAIN_GROUP_RID_ADMINS`                                 | 512 (0x204)
`DOMAIN_GROUP_RID_CONTROLLERS`                            | 516 (0x209)
`DOMAIN_GROUP_RID_CERT_ADMINS`                            | 517 (0x1F2)
`DOMAIN_GROUP_RID_SCHEMA_ADMINS`                          | 518 (0x205)
`DOMAIN_GROUP_RID_ENTERPRISE_ADMINS`                      | 519 (0x206)
`DOMAIN_GROUP_RID_POLICY_ADMINS`                          | 520 (0x207)
`DOMAIN_GROUP_RID_READONLY_CONTROLLERS`                   | 521 (0x208)
`DOMAIN_ALIAS_RID_ADMINS`                                 | 544 (0x220)
`DOMAIN_ALIAS_RID_POWER_USERS`                            | 547 (0x223)
`DOMAIN_ALIAS_RID_ACCOUNT_OPS`                            | 548 (0x224)
`DOMAIN_ALIAS_RID_SYSTEM_OPS`                             | 549 (0x225)
`DOMAIN_ALIAS_RID_PRINT_OPS`                              | 550 (0x226)
`DOMAIN_ALIAS_RID_BACKUP_OPS`                             | 551 (0x227)
`DOMAIN_ALIAS_RID_RAS_SERVERS`                            | 553 (0x229)
`DOMAIN_ALIAS_RID_PREW2KCOMPACCESS`                       | 554 (0x22A)
`DOMAIN_ALIAS_RID_NETWORK_CONFIGURATION_OPS`              | 556 (0x22C)
`DOMAIN_ALIAS_RID_CRYPTO_OPERATORS`                       | 569 (0x239)

# See also
 - `NtFilterToken`
 - `TOKEN_INFORMATION_CLASS` (`TokenElevation`)
