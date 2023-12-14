
import os
import signal
import sys
import threading

def cleanup_leaked_semaphores():
    # Get the process ID of the current process
    current_pid = os.getpid()

    # Iterate over all threads and release semaphores forcibly
    for thread_id, thread_obj in threading._active.items():
        if hasattr(thread_obj, "_semaphore_tracker"):
            semaphores = thread_obj._semaphore_tracker._semaphores
            for semaphore in semaphores:
                try:
                    # Release the semaphore forcibly
                    semaphore._Semaphore__count = 0
                except Exception as e:
                    print(f"Failed to release semaphore: {e}")

    # Terminate the current process to clean up any remaining resources
    os.kill(current_pid, signal.SIGKILL)

if __name__ == "__main__":
    # Call the cleanup function if this script is run directly
    cleanup_leaked_semaphores()