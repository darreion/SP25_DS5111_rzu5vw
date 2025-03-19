import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bin.gainers.factory import GainerFactory
from bin.gainers.yahoo import GainerDownloadYahoo, GainerProcessYahoo
from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ

def test_factory_yahoo():
    factory = GainerFactory("yahoo")
    assert isinstance(factory.get_downloader(), GainerDownloadYahoo)
    assert isinstance(factory.get_processor(), GainerProcessYahoo)

def test_factory_wsj():
    factory = GainerFactory("wsj")
    assert isinstance(factory.get_downloader(), GainerDownloadWSJ)
    assert isinstance(factory.get_processor(), GainerProcessWSJ)
