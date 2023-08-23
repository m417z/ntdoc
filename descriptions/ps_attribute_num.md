This enumeration defines indexes for process and thread creation attributes. The `PsAttributeValue` macro is used convert them into usable attribute values.

# Known attributes
 - `PS_ATTRIBUTE_PARENT_PROCESS` - specifies the handle to the parent process during process creation.
 - `PS_ATTRIBUTE_DEBUG_OBJECT` - specifies the handle to the debug object to attach to the new process.
 - `PS_ATTRIBUTE_TOKEN` - specifies the token to the use as the primary token of the new process.
 - `PS_ATTRIBUTE_CLIENT_ID` - allows retrieving the client ID of the new/initial thread.
 - `PS_ATTRIBUTE_TEB_ADDRESS` - allows retrieving the `TEB` address of the new/initial thread.
 - `PS_ATTRIBUTE_IMAGE_NAME` - provides an NT filename of the executable image to use for the new process.
 - `PS_ATTRIBUTE_IMAGE_INFO` - allows retrieving information about the executable image used during process creation.
 - `PS_ATTRIBUTE_MEMORY_RESERVE`
 - `PS_ATTRIBUTE_PRIORITY_CLASS`
 - `PS_ATTRIBUTE_ERROR_MODE` - sets the default error mode for the process.
 - `PS_ATTRIBUTE_STD_HANDLE_INFO` - specifies which standard (console) handles to inherit in the new process.
 - `PS_ATTRIBUTE_HANDLE_LIST` - indicates a subset of inheritable handles to be inherited by the new process.
 - `PS_ATTRIBUTE_GROUP_AFFINITY`
 - `PS_ATTRIBUTE_PREFERRED_NODE`
 - `PS_ATTRIBUTE_IDEAL_PROCESSOR` - allows specifying the ideal processor for new thread.
 - `PS_ATTRIBUTE_UMS_THREAD` - controls user-mode thread scheduling.
 - `PS_ATTRIBUTE_MITIGATION_OPTIONS` - controls which mitigation policies should be applied to the new process.
 - `PS_ATTRIBUTE_PROTECTION_LEVEL` - specifies which the protection level to use when creating protected/PPL processes.
 - `PS_ATTRIBUTE_SECURE_PROCESS`
 - `PS_ATTRIBUTE_JOB_LIST` - specifies the list of handles to job objects to put the new process into.
 - `PS_ATTRIBUTE_CHILD_PROCESS_POLICY` - specifies whether the new process should be allowed to create child processes.
 - `PS_ATTRIBUTE_ALL_APPLICATION_PACKAGES_POLICY` - specifies whether the new process should run in LPAC sandbox.
 - `PS_ATTRIBUTE_WIN32K_FILTER`
 - `PS_ATTRIBUTE_SAFE_OPEN_PROMPT_ORIGIN_CLAIM` - specifies safe origin claims; used by SmartScreen.
 - `PS_ATTRIBUTE_BNO_ISOLATION` - controls BNO isolation for the new process.
 - `PS_ATTRIBUTE_DESKTOP_APP_POLICY`
 - `PS_ATTRIBUTE_CHPE` - controls CHPE settings on ARM machines.
 - `PS_ATTRIBUTE_MITIGATION_AUDIT_OPTIONS`
 - `PS_ATTRIBUTE_MACHINE_TYPE`
 - `PS_ATTRIBUTE_COMPONENT_FILTER`
 - `PS_ATTRIBUTE_ENABLE_OPTIONAL_XSTATE_FEATURES` - controls extended thread context features.

Check the corresponding pages for more details.

# See also
 - `PS_ATTRIBUTE`
 - `PS_ATTRIBUTE_LIST`
 - `NtCreateThreadEx`
 - `NtCreateUserProcess`
