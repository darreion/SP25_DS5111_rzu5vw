import sys
import platform

def test_os():
    assert platform.system() == "Linux", "Tests must run on Linux"

def test_python_version():
    assert sys.version_info[:2] in [(3, 10), (3, 11)], "Python version must be 3.10 or 3.11"
