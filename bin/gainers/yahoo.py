"""
Yahoo-specific implementation of GainerDownload and GainerProcess.
"""

from .base import GainerDownload, GainerProcess
import pandas as pd
import datetime
import os

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
        self.df = pd.DataFrame({"Symbol": ["AAPL"], "Change": [5.2]})

    def save_with_timestamp(self):
        """Save Yahoo gainers data with a timestamp."""
        os.makedirs("data", exist_ok=True)
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filepath = f"data/yahoo_gainers_{timestamp}.csv"
        self.df.to_csv(filepath, index=False)
        print(f"Saved to {filepath}")
