from setuptools import setup
from setuptools.command.install import install
import subprocess
import platform

class CustomInstallCommand(install):
    def run(self):
        install.run(self)
        if platform.system() == "Windows":
            subprocess.run(['cmd', '/C', 'scripts\\setup_cli.bat'])
        else:
            subprocess.run(['bash', 'scripts/setup_cli.sh'])

setup(
    cmdclass={'install': CustomInstallCommand}
)
