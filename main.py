"""Main class"""
import pathlib

from pip._vendor.distlib.compat import raw_input
from calc.utils.csvmanager import CsvManager

BASE_DIR = pathlib.Path().resolve()


class CalcCSV:
    """Main class for CSV"""

    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = raw_input("Enter your choice: ")
    print("fetching CSV file")
    CsvManager.csv_process(choice)
    print("CSV file processing")
