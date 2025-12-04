# db.py
import os
import pandas as pd

FILE_NAME = "students.csv"
DEFAULT_COLUMNS = ["ID", "Name", "Mobile", "Course", "Marks", "Gender"]

def ensure_csv():
    if not os.path.exists(FILE_NAME):
        df = pd.DataFrame(columns=DEFAULT_COLUMNS)
        df.to_csv(FILE_NAME, index=False)

def read_all():
    ensure_csv()
    df = pd.read_csv(FILE_NAME)
    return df

def append_student(record: dict):
    """
    record = {"ID":..., "Name":..., "Mobile":..., "Course":..., "Marks":..., "Gender":...}
    """
    df = read_all()
    df = pd.concat([df, pd.DataFrame([record])], ignore_index=True)
    df.to_csv(FILE_NAME, index=False)

def update_student(student_id: str, updated: dict):
    df = read_all()
    idx = df.index[df["ID"] == student_id]
    if len(idx) == 0:
        return False
    for k, v in updated.items():
        if k in df.columns:
            df.loc[idx, k] = v
    df.to_csv(FILE_NAME, index=False)
    return True

def delete_student(student_id: str):
    df = read_all()
    df = df[df["ID"] != student_id]
    df.to_csv(FILE_NAME, index=False)

def clear_all():
    df = pd.DataFrame(columns=DEFAULT_COLUMNS)
    df.to_csv(FILE_NAME, index=False)

def next_id():
    df = read_all()
    if df.empty:
        return "ST1001"
    last = df["ID"].iloc[-1]
    try:
        num = int(last.replace("ST", ""))
    except:
        num = 1000
    return f"ST{num+1}"
