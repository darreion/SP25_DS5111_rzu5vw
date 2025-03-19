"""
Yahoo-specific implementation of GainerDownload and GainerProcess.
"""

from .base import GainerDownload, GainerProcess

# pylint: disable=too-few-public-methods
class GainerDownloadYahoo(GainerDownload):
    """Downloader class for Yahoo gainers."""

    def __init__(self):
        """Initialize with Yahoo URL."""
        super().__init__("https://finance.yahoo.com/gainers")

    def download(self):
        """Download Yahoo gainers data."""
        print("Downloading Yahoo gainers")

class GainerProcessYahoo(GainerProcess):
    """Processor class for Yahoo gainers."""

    def normalize(self):
        """Normalize Yahoo gainers data."""
        print("Normalizing Yahoo gainers")

    def save_with_timestamp(self):
        """Save Yahoo gainers data with a timestamp."""
        print("Saving Yahoo gainers")
