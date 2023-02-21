import subprocess

#payload = "cmd.exe /c powershell.exe"
#subprocess.Popen("wmic process call create '" + payload + "'", shell=True)

import winpty
process = winpty.PtyProcess.spawn("cmd.exe")

output = winpty.PtyProcess.read(process)
print(output)

winpty.PtyProcess.write(process, "dir\n")
output = winpty.PtyProcess.read(process)
print(output)
