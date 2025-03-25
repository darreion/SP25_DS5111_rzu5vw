"""
Main script to process gainers using the factory pattern.
"""

import sys
from bin.gainers.factory import GainerFactory

class ProcessGainer:
    """Handles downloading, normalizing, and saving gainers data."""

    def __init__(self, gainer_downloader, gainer_normalizer):
        """Initialize with downloader and normalizer instances."""
        self.downloader = gainer_downloader
        self.normalizer = gainer_normalizer

    def process(self):
        """Run the complete processing pipeline."""
        self.downloader.download()
        self.normalizer.normalize()
        self.normalizer.save_with_timestamp()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_gainer.py <yahoo|wsj>")
        sys.exit(1)

    choice = sys.argv[1]
    factory = GainerFactory(choice)
    downloader = factory.get_downloader()
    normalizer = factory.get_processor()

    runner = ProcessGainer(downloader, normalizer)
    runner.process()
