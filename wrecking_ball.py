import subprocess

#payload = "cmd.exe /c powershell.exe"
#subprocess.Popen("wmic process call create '" + payload + "'", shell=True)

import pywinpty

(master_fd, slave_fd) = pywinpty.open()

pid, handle = pywinpty.spawn("cmd.exe", master_fd=master_fd)

output = pywinpty.read(master_fd)
print(output.decode())

pywinpty.write(master_fd, "dir\n")
output = pywinpty.read(master_fd)
print(output.decode())

pywinpty.close(master_fd, slave_fd, pid, handle)