import winreg
import time
import uuid
import os

def write_artifact():
    paths = [
        r"C:\Users\Public",
        #os.environ.get("PROGRAMDATA", r"C:\ProgramData"),
        #os.environ.get("TEMP", r"C:\Temp")
    ]

    for base in paths:
        try:
            file_path = os.path.join(base, "pip_detection_test.txt")

            with open(file_path, "w") as f:
                f.write("PIP detection test executed\n")

            print(f"[+] File artifact created: {file_path}")
            return

        except Exception:
            continue

    print("[!] Unable to write artifact to any location")

write_artifact()



def registry_artifact_test():
    try:
        # Unique key name per execution
        unique_id = uuid.uuid4().hex[:8]
        key_path = fr"Software\PipDetectionTest\{unique_id}"

        print(f"[+] Creating registry key: HKCU\\{key_path}")

        # Create key
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)

        # Write benign value
        winreg.SetValueEx(
            key,
            "TestValue",
            0,
            winreg.REG_SZ,
            "PIP detection validation"
        )

        winreg.CloseKey(key)

        print("[+] Registry key created successfully")

        # Wait (for detection timing / correlation)
        time.sleep(30)

        print("[+] Cleaning up registry key")

        # Delete value and key
        winreg.DeleteKey(winreg.HKEY_CURRENT_USER, key_path)

        print("[+] Registry key removed")

    except Exception as e:
        print(f"[!] Registry test failed: {e}")


# Execute
# registry_artifact_test()
