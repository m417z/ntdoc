This flags indicates the use of a *special user-mode APC* that does not require the thread to enter an alertable state. The APC will be executed on the next thread's transition to user mode.

# Applicable to
 - `NtQueueApcThreadEx2`

# Related flags
 - `QUEUE_USER_APC_FLAGS_NONE`
 - `QUEUE_USER_APC_FLAGS_CALLBACK_DATA_CONTEXT`

# Remarks
For the introduction to special user-mode APCs, see [this blog post](https://repnz.github.io/posts/apc/user-apc/#ntqueueapcthreadex-meet-special-user-apc).

Because execution of special APCs is not synchronized with the target thread (which might happen to acquire locks), it is crucial to keep the amount and complexity of the code invoked by the special APC routine to a minimum.

# Required OS version
This flag was introduced in Windows 11.
