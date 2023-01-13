import os
import servicemanager
import shutil
import subprocess
import sys

import win32event
import win32service
import win32serviceutil

SRCDIR = 'C:\\Users\\rupnat0120a\\Desktop\\Wrecking Ball'
TGTDIR = 'C:\\Windows\\TEMP'

class Win32ServerSvc(win32serviceutil.ServiceFramework):
    _svc_name_ = ""