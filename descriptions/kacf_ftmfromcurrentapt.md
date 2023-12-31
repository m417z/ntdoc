This application compatibility flag used to be documented in early Windows 10 EWDK.

# Applicable to
 - `PEB->AppCompatFlags`

# Meaning
If set, a DCOM Free-Threaded-Marshaled Object has its' stub parked in the apartment that the object is marshaled from instead of the Neutral-Apartment. Having to set this bit indicates a busted App that is not following the rules for FTM objects. The app probably has other subtle problems that NT 4 or Win9x didn't show. Blindly using the ATL wizard to enable using the FTM is usually the source of the bug.

# Related flags
 - `KACF_OLDGETSHORTPATHNAME`
 - `KACF_VERSIONLIE_NOT_USED`
 - `KACF_GETDISKFREESPACE`
 - `KACF_DISALLOWORBINDINGCHANGES`
 - `KACF_OLE32VALIDATEPTRS`
 - `KACF_DISABLECICERO`
 - `KACF_OLE32ENABLEASYNCDOCFILE`
 - `KACF_OLE32ENABLELEGACYEXCEPTIONHANDLING`
 - `KACF_RPCDISABLENDRCLIENTHARDENING`
 - `KACF_RPCDISABLENDRMAYBENULL_SIZEIS`
 - `KACF_DISABLEALLDDEHACK_NOT_USED`
 - `KACF_RPCDISABLENDR61_RANGE`
 - `KACF_RPC32ENABLELEGACYEXCEPTIONHANDLING`
 - `KACF_OLE32DOCFILEUSELEGACYNTFSFLAGS`
 - `KACF_RPCDISABLENDRCONSTIIDCHECK`
 - `KACF_USERDISABLEFORWARDERPATCH`
 - `KACF_OLE32DISABLENEW_WMPAINT_DISPATCH`
 - `KACF_ADDRESTRICTEDSIDINCOINITIALIZESECURITY`
 - `KACF_ALLOCDEBUGINFOFORCRITSECTIONS`
 - `KACF_OLEAUT32ENABLEUNSAFELOADTYPELIBRELATIVE`
 - `KACF_ALLOWMAXIMIZEDWINDOWGAMMA`
 - `KACF_DONOTADDTOCACHE`
