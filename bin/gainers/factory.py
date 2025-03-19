"""
Factory class for creating downloader and processor instances.
"""

from .wsj import GainerDownloadWSJ, GainerProcessWSJ
from .yahoo import GainerDownloadYahoo, GainerProcessYahoo

class GainerFactory:
    """Factory class to generate GainerDownload and GainerProcess instances."""

    def __init__(self, choice):
        """Initialize the factory with a data source choice."""
        assert choice in ["yahoo", "wsj"], f"Unrecognized gainer type {choice}"
        self.choice = choice

    def get_downloader(self):
        """Return the appropriate downloader instance based on the choice."""
        if self.choice == "yahoo":
            return GainerDownloadYahoo()
        return GainerDownloadWSJ()  # No unnecessary elif

    def get_processor(self):
        """Return the appropriate processor instance based on the choice."""
        if self.choice == "yahoo":
            return GainerProcessYahoo()
        return GainerProcessWSJ()  # No unnecessary elif
