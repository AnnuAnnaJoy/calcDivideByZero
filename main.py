"""Main class"""
from pip._vendor.distlib.compat import raw_input

from calc.calculation.csvcalculation import CsvCalc
from calc.utils.csvmanager import CsvManager


class CalcCSV:
    """Main class for CSV"""

    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    choice = int(raw_input("Enter your choice: "))
    print("fetching CSV file")
    cv = CsvManager()
    df = cv.read_csv()
    print("CSV file processing")
    df1 = CsvCalc.csvprocess(df, choice)
    if choice == 1:
        cv.write_csv(df1, "add")
    elif choice == 2:
        cv.write_csv(df1, "sub")
    elif choice == 3:
        cv.write_csv(df1, "mul")
    else:
        cv.write_csv(df1, "div")


class AutoCalcCSV:
    """Main class for auto calc CSV"""
    print("Reading CSV")
    cv = CsvManager()
    df = cv.read_csv()
    print("CSV processing..")
    for i in range(1, 5, 1):
        df1 = CsvCalc.csvprocess(df, i)
        if i == 1:
            cv.write_csv(df1, "addition")
        elif i == 2:
            cv.write_csv(df1, "subtraction")
        elif i == 3:
            cv.write_csv(df1, "multiplication")
        else:
            cv.write_csv(df1, "division")

    print("CSV results generated")
