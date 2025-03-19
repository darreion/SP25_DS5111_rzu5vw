"""
WSJ-specific implementation of GainerDownload and GainerProcess.
"""

from .base import GainerDownload, GainerProcess

# pylint: disable=too-few-public-methods
class GainerDownloadWSJ(GainerDownload):
    """Downloader class for WSJ gainers."""

    def __init__(self):
        """Initialize with WSJ URL."""
        super().__init__("https://www.wsj.com/gainers")

    def download(self):
        """Download WSJ gainers data."""
        print("Downloading WSJ gainers")

class GainerProcessWSJ(GainerProcess):
    """Processor class for WSJ gainers."""

    def normalize(self):
        """Normalize WSJ gainers data."""
        print("Normalizing WSJ gainers")

    def save_with_timestamp(self):
        """Save WSJ gainers data with a timestamp."""
        print("Saving WSJ gainers")
