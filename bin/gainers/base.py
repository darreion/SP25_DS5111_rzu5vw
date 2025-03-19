"""
Base classes for gainers module.
"""

from abc import ABC, abstractmethod

class GainerDownload(ABC):
    """Abstract base class for downloading gainers data."""

    def __init__(self, url):
        """Initialize with a URL."""
        self.url = url

    @abstractmethod
    def download(self):
        """Abstract method to be implemented for downloading data."""

class GainerProcess(ABC):
    """Abstract base class for processing gainers data."""

    @abstractmethod
    def normalize(self):
        """Abstract method to normalize data."""

    @abstractmethod
    def save_with_timestamp(self):
        """Abstract method to save with timestamp."""

