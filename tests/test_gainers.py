import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # kudos for the use of os.path and using insert to put 
                                                                                    # the inserted path up front.
                                                                                    # So the `..` works?  Wouldn't that put in the path two levels above?
                                                                                    # If it works it works, just struck me as odd since Ohhhhhh wait
                                                                                    # maybe it's got something to do with the use of os.path... 
                                                                                    # the other more simplistic call just used `append('.')`... ok, I think I see it now

from bin.gainers.yahoo import GainerDownloadYahoo, GainerProcessYahoo
from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ

# would be good to put a small description on the tests, would you give a Given/When/Then block a try on the tests?
def test_yahoo_download():
    downloader = GainerDownloadYahoo()
    assert downloader.url == "https://finance.yahoo.com/gainers"

def test_wsj_download():
    downloader = GainerDownloadWSJ()
    assert downloader.url == "https://www.wsj.com/gainers"
