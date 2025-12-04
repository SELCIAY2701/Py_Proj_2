# # charts.py
# import matplotlib.pyplot as plt
# import pandas as pd

# plt.rcParams.update({'figure.max_open_warning': 0})

# def marks_bar_with_avg(names, marks, title="Student Marks Analysis"):
#     plt.figure(figsize=(14,6))
#     # bar
#     plt.bar(names, marks, color="#90caf9")
#     plt.scatter(names, marks, s=160, facecolor="#0d47a1", edgecolor="white")
#     for name, m in zip(names, marks):
#         plt.text(name, m + 1.5, str(m), ha='center', fontsize=9, fontweight='bold')
#     avg = sum(marks) / len(marks)
#     plt.axhline(avg, linestyle='--', linewidth=2, label=f"Average {avg:.1f}")
#     plt.title(title, fontsize=16, fontweight='bold')
#     plt.ylim(0, 100)
#     plt.xticks(rotation=45, ha='right')
#     plt.legend()
#     plt.tight_layout()
#     plt.show()

# def course_wise_avg(df: pd.DataFrame):
#     if df.empty:
#         return
#     grouped = df.groupby("Course")["Marks"].mean().sort_values(ascending=False)
#     plt.figure(figsize=(8,5))
#     grouped.plot(kind='bar')
#     plt.title("Average Marks by Course")
#     plt.ylabel("Average Marks")
#     plt.ylim(0,100)
#     plt.tight_layout()
#     plt.show()

# def gender_performance(df):
#     if df.empty:
#         return
#     grp = df.groupby("Gender")["Marks"].mean()
#     plt.figure(figsize=(6,4))
#     grp.plot(kind='bar')
#     plt.title("Average Marks by Gender")
#     plt.ylim(0,100)
#     plt.tight_layout()
#     plt.show()

# def pass_fail_pie(df, pass_mark=40):
#     if df.empty:
#         return
#     passed = (df["Marks"] >= pass_mark).sum()
#     failed = (df["Marks"] < pass_mark).sum()
#     plt.figure(figsize=(5,5))
#     plt.pie([passed, failed], labels=[f"Pass ({passed})", f"Fail ({failed})"], autopct="%1.1f%%", startangle=140)
#     plt.title("Pass vs Fail")
#     plt.tight_layout()
#     plt.show()

# def histogram_marks(df):
#     if df.empty:
#         return
#     plt.figure(figsize=(8,5))
#     plt.hist(df["Marks"], bins=[0,20,40,60,80,100], edgecolor='black')
#     plt.title("Marks Distribution")
#     plt.xlabel("Marks")
#     plt.ylabel("Count")
#     plt.tight_layout()
#     plt.show()
import matplotlib.pyplot as plt

def marks_bar_with_avg(names, marks, title="Marks"):
    plt.figure(figsize=(10,6))
    avg = sum(marks)/len(marks) if marks else 0
    plt.bar(names, marks, color="#2196f3", edgecolor="black")
    plt.axhline(y=avg, color="red", linestyle="--", label=f"Average: {avg:.2f}")
    plt.title(title)
    plt.ylabel("Marks")
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()

def course_wise_avg(df):
    import pandas as pd
    grouped = df.groupby("Course")["Marks"].mean()
    plt.figure(figsize=(8,5))
    grouped.plot(kind="bar", color="#4caf50", edgecolor="black")
    plt.title("Average Marks by Course")
    plt.ylabel("Average Marks")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def gender_performance(df):
    import pandas as pd
    grouped = df.groupby("Gender")["Marks"].mean()
    plt.figure(figsize=(6,4))
    grouped.plot(kind="bar", color=["#2196f3","#ff4081"], edgecolor="black")
    plt.title("Average Marks by Gender")
    plt.ylabel("Average Marks")
    plt.tight_layout()
    plt.show()

def pass_fail_pie(df):
    import pandas as pd
    passed = df[df["Marks"]>=35].shape[0]
    failed = df[df["Marks"]<35].shape[0]
    plt.figure(figsize=(5,5))
    plt.pie([passed, failed], labels=["Pass","Fail"], autopct="%1.1f%%", colors=["#4caf50","#f44336"])
    plt.title("Pass/Fail Distribution")
    plt.show()

def histogram_marks(df):
    import pandas as pd
    plt.figure(figsize=(8,5))
    plt.hist(df["Marks"], bins=10, color="#2196f3", edgecolor="black")
    plt.title("Marks Distribution")
    plt.xlabel("Marks")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.show()
