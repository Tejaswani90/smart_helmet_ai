# ==================================================
# SMART HELMET - SAFETY CONFIRMATION
# ==================================================

import time
import threading


def wait_for_safety_confirmation(timeout=15):

    user_input = [None]

    def get_confirmation():

        user_input[0] = input(
            "\nType YES if you are safe: "
        )

    input_thread = threading.Thread(
        target=get_confirmation,
        daemon=True
    )

    input_thread.start()

    print(
        f"\nYou have {timeout} seconds "
        "to confirm that you are safe."
    )

    for remaining in range(timeout, 0, -1):

        if user_input[0] is not None:
            break

        print(
            f"Time remaining: {remaining} seconds"
        )

        time.sleep(1)

    if (
        user_input[0] is not None
        and user_input[0].strip().upper() == "YES"
    ):

        return True

    return False


if __name__ == "__main__":

    result = wait_for_safety_confirmation()

    if result:

        print("\nSafety confirmation received.")
        print("Emergency alert cancelled.")

    else:

        print("\nNo safety confirmation received.")
        print("Emergency alert triggered.")