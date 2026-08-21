#V0.00.01

from pathlib import Path

log_file = Path("data/sample.log")

with log_file.open("r") as file:
    for line in file:
        line = line.strip()

        if line:
            print(line)
