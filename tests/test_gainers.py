import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from bin.gainers.yahoo import GainerDownloadYahoo, GainerProcessYahoo
from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ

def test_yahoo_download():
    downloader = GainerDownloadYahoo()
    assert downloader.url == "https://finance.yahoo.com/gainers"

def test_wsj_download():
    downloader = GainerDownloadWSJ()
    assert downloader.url == "https://www.wsj.com/gainers"
