import os
import pprint
from pathlib import Path

def main() -> None:
    print("Hello World!")

if __name__ == "__main__":
    # for key, value in os.environ.items():
    #     print(f"{key}: {value}")
    thisPath = Path(__file__).absolute().parent
    testInputPath = Path(thisPath).joinpath("_testinputs")
    Path.mkdir(testInputPath, exist_ok=True)
    testResultPath = Path(thisPath).joinpath("_testresults")
    Path.mkdir(testResultPath, exist_ok=True)