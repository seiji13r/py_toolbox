import os
import pprint
from pathlib import Path

def main() -> None:
    print("Hello World!")
    input()

if __name__ == "__main__":
    thisPath = Path(__file__).absolute().parent
    main()
