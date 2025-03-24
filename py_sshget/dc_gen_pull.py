import os
import pprint
from pathlib import Path

import logging

from lib.xlsx_parser import xlsxAccessFile2JSON

def dcGenAndPull(serversAccessXlsxFile=None) -> None:
    hostsDict = xlsxAccessFile2JSON(serversAccessXlsxFile)
    pprint.pprint(hostsDict)

if __name__ == "__main__":
    thisPath = Path(__file__).absolute().parent
    accessFile = Path(thisPath).joinpath("access_info.xlsx")
    dcGenAndPull(serversAccessXlsxFile=accessFile)