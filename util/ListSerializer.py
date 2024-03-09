from typing import List

def dump(list: List[str], file_name: str) -> None:
    with open(file_name, "w") as f:
        for line in list:
            f.write(line + "\n")

def load(file: str) -> List[str]:
    lines = []
    with open(file, "r") as f:
        for line in f:
            lines.append(line)
    return lines