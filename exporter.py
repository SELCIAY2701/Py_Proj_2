# exporter.py
import pandas as pd
from database import read_all
import os

def export_to_excel(path="students_export.xlsx"):
    df = read_all()
    df.to_excel(path, index=False)
    return os.path.abspath(path)

def export_to_csv(path="students_export.csv"):
    df = read_all()
    df.to_csv(path, index=False)
    return os.path.abspath(path)
