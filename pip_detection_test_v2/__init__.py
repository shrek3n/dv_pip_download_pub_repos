import base64
import subprocess

cmd = base64.b64encode(b"notepad.exe").decode()
decoded = base64.b64decode(cmd).decode()

subprocess.Popen(["cmd.exe", "/c", decoded], shell=True)
