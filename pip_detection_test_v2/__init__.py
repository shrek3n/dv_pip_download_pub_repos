import subprocess

subprocess.Popen(
  ["cmd.exe", "/c", "echo PIP DETECTION CHILD PROCESS"],
  shell=True
)
