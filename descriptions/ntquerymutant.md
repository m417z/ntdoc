### MutantHandle

Handle to Mutant object.

### MutantInformationClass

Is defined as enum:

	<B><FONT COLOR="Blue">typedef enum</FONT></B> `_MUTANT_INFORMATION_CLASS` \
	{ \
		MutantBasicInformation

	} `MUTANT_INFORMATION_CLASS`, *`PMUTANT_INFORMATION_CLASS`;

### MutantInformation

Buffer for result. As long as only one information type is defined, set `MutantInformation` as a pointer to `MUTANT_BASIC_INFORMATION` structure.

### MutantInformationLength

Size of buffer.

### ResultLength

Number of bytes written to buffer.

# Documented by

* Tomasz Nowak
* Sven B. Schreiber

# See also

* `MUTANT_BASIC_INFORMATION`
* `NtCreateMutant`
* `NtOpenMutant`
