# utils.py
import re

def is_valid_name(name: str) -> bool:
    # allow spaces and alphabets
    return bool(re.fullmatch(r"[A-Za-z ]{2,50}", name.strip()))

def is_valid_mobile(mobile: str) -> bool:
    return mobile.isdigit() and len(mobile) == 10

def is_valid_marks(marks: str) -> bool:
    if not marks.isdigit():
        return False
    m = int(marks)
    return 0 <= m <= 100
