import sys
import platform

def test_os():
    assert platform.system() == "Linux", "Tests must run on Linux"

def test_python_version(): # just a head's up that this will need to change to match the versions in validations.yml (3.12 and 3.13)
    assert sys.version_info[:2] in [(3, 10), (3, 11), (3, 12)], "Python version must be 3.10, 3.11, or 3.12"
