# ui.py
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import datetime

# safe import for db module (db.py or database.py)
try:
    import database as db_mod
except Exception:
    try:
        import database as db_mod
    except Exception:
        raise ImportError("Could not import 'db' or 'database' module. Make sure one exists and has required functions.")

import charts
import exporter
import utils

# ---------- Theme / Constants ----------
BG = "#F7F8FA"
CARD_BG = "#FFFFFF"
ACCENT = "#1976D2"  # blue
TEXT = "#222222"
FONT_TITLE = ("Bookman", 18, "bold")
FONT_LABEL = ("Bookman", 11)
BTN_WIDTH = 14
BTN_HEIGHT = 1

# ---------- Build UI function (exposed) ----------
def build_ui(root):
    root.configure(bg=BG)
    root.title("Student Management — Light Professional")
    try:
        root.geometry("1150x740")
    except Exception:
        pass

    # ---- Top header ----
    header = tk.Frame(root, bg=BG)
    header.pack(fill="x", padx=18, pady=(12, 6))

    title_lbl = tk.Label(header, text="Student Management Dashboard", font=FONT_TITLE, bg=BG, fg=TEXT)
    title_lbl.pack(side="left", padx=(10,0))

    dt_lbl = tk.Label(header, text=datetime.datetime.now().strftime("%b %d, %Y  %I:%M %p"),
                      font=("Bookman", 10), bg=BG, fg="#555555")
    dt_lbl.pack(side="right", padx=(0,10))

    # ---- Summary cards ----
    summary_frame = tk.Frame(root, bg=BG)
    summary_frame.pack(fill="x", padx=18, pady=(0,12))

    def make_card(parent, heading, initial_text):
        card = tk.Frame(parent, bg=CARD_BG, bd=0, relief="ridge")
        card.pack(side="left", padx=8, ipadx=12, ipady=10, expand=True, fill="x")
        tk.Label(card, text=heading, font=("Bookman", 10), bg=CARD_BG, fg="#666666").pack(anchor="w")
        val = tk.Label(card, text=initial_text, font=("Bookman", 14, "bold"), bg=CARD_BG, fg=TEXT)
        val.pack(anchor="w", pady=(6,0))
        return val

    total_label = make_card(summary_frame, "Total Students", "0")
    avg_label   = make_card(summary_frame, "Average Marks", "0")
    male_label  = make_card(summary_frame, "Male", "0")
    female_label= make_card(summary_frame, "Female", "0")

    # ---- Main horizontal area: left form, right table ----
    main_frame = tk.Frame(root, bg=BG)
    main_frame.pack(fill="both", expand=True, padx=18, pady=(0,12))

    # --- Left: Form & quick actions ---
    left_frame = tk.Frame(main_frame, bg=BG)
    left_frame.pack(side="left", fill="y", padx=(0,12), ipadx=6)

    form_card = tk.Frame(left_frame, bg=CARD_BG)
    form_card.pack(fill="x", pady=(0,10))

    tk.Label(form_card, text="Add / Edit Student", font=("Bookman", 13, "bold"), bg=CARD_BG, fg=TEXT).pack(anchor="w", padx=12, pady=(10,4))

    # Form fields
    form_inner = tk.Frame(form_card, bg=CARD_BG)
    form_inner.pack(fill="both", padx=12, pady=6)

    tk.Label(form_inner, text="Name", font=FONT_LABEL, bg=CARD_BG).grid(row=0, column=0, sticky="w", pady=6)
    name_entry = tk.Entry(form_inner, width=28, bg="#F1F3F5", font=FONT_LABEL, relief="flat", insertbackground='black')
    name_entry.grid(row=0, column=1, pady=6, padx=(8,0))

    tk.Label(form_inner, text="Mobile", font=FONT_LABEL, bg=CARD_BG).grid(row=1, column=0, sticky="w", pady=6)
    mobile_entry = tk.Entry(form_inner, width=28, bg="#F1F3F5", font=FONT_LABEL, relief="flat", insertbackground='black')
    mobile_entry.grid(row=1, column=1, pady=6, padx=(8,0))

    tk.Label(form_inner, text="Course", font=FONT_LABEL, bg=CARD_BG).grid(row=2, column=0, sticky="w", pady=6)
    course_combo = ttk.Combobox(form_inner, values=("ECE","MCA","CSE","IT","MTX","EEE"), width=26)
    course_combo.current(0)
    course_combo.grid(row=2, column=1, pady=6, padx=(8,0))

    tk.Label(form_inner, text="Marks", font=FONT_LABEL, bg=CARD_BG).grid(row=3, column=0, sticky="w", pady=6)
    marks_entry = tk.Entry(form_inner, width=28, bg="#F1F3F5", font=FONT_LABEL, relief="flat", insertbackground='black')
    marks_entry.grid(row=3, column=1, pady=6, padx=(8,0))

    tk.Label(form_inner, text="Gender", font=FONT_LABEL, bg=CARD_BG).grid(row=4, column=0, sticky="w", pady=6)
    gender_var = tk.StringVar(value="")
    gender_frame = tk.Frame(form_inner, bg=CARD_BG)
    gender_frame.grid(row=4, column=1, sticky="w", pady=6, padx=(8,0))
    tk.Radiobutton(gender_frame, text="Male", variable=gender_var, value="Male", bg=CARD_BG).pack(side="left")
    tk.Radiobutton(gender_frame, text="Female", variable=gender_var, value="Female", bg=CARD_BG).pack(side="left", padx=(8,0))

    # Buttons under form
    form_btn_frame = tk.Frame(form_card, bg=CARD_BG)
    form_btn_frame.pack(fill="x", pady=(6,12), padx=12)
    submit_btn = tk.Button(form_btn_frame, text="Submit", width=BTN_WIDTH, bg=ACCENT, fg="white", relief="flat")
    submit_btn.pack(side="left", padx=(0,8))
    clear_btn  = tk.Button(form_btn_frame, text="Clear", width=BTN_WIDTH, bg="#9E9E9E", fg="white", relief="flat")
    clear_btn.pack(side="left", padx=(0,8))

    # Quick analytics buttons
    quick_card = tk.Frame(left_frame, bg=CARD_BG)
    quick_card.pack(fill="x", pady=(0,10))
    tk.Label(quick_card, text="Analytics", font=("Bookman", 12, "bold"), bg=CARD_BG).pack(anchor="w", padx=12, pady=(10,0))
    qf = tk.Frame(quick_card, bg=CARD_BG)
    qf.pack(padx=12, pady=10)
    tk.Button(qf, text="Marks (sorted)", width=18, command=lambda: analyze_marks()).grid(row=0, column=0, pady=6, padx=4)
    tk.Button(qf, text="Course Avg", width=18, command=lambda: charts.course_wise_avg(db_mod.read_all())).grid(row=0, column=1, pady=6, padx=4)
    tk.Button(qf, text="Gender Avg", width=18, command=lambda: charts.gender_performance(db_mod.read_all())).grid(row=1, column=0, pady=6, padx=4)
    tk.Button(qf, text="Pass/Fail", width=18, command=lambda: charts.pass_fail_pie(db_mod.read_all())).grid(row=1, column=1, pady=6, padx=4)
    tk.Button(qf, text="Distribution", width=37, command=lambda: charts.histogram_marks(db_mod.read_all())).grid(row=2, column=0, columnspan=2, pady=6)

    # Export & utilities
    util_card = tk.Frame(left_frame, bg=CARD_BG)
    util_card.pack(fill="x", pady=(0,10))
    tk.Label(util_card, text="Utilities", font=("Bookman", 12, "bold"), bg=CARD_BG).pack(anchor="w", padx=12, pady=(10,0))
    uf = tk.Frame(util_card, bg=CARD_BG)
    uf.pack(padx=12, pady=10)
    tk.Button(uf, text="Top 5", width=18, command=lambda: show_top5()).grid(row=0, column=0, padx=6, pady=4)
    tk.Button(uf, text="Export Excel", width=18, command=lambda: do_export("excel")).grid(row=0, column=1, padx=6, pady=4)
    tk.Button(uf, text="Export CSV", width=18, command=lambda: do_export("csv")).grid(row=1, column=0, padx=6, pady=4)
    tk.Button(uf, text="Clear DB", width=18, command=lambda: clear_database()).grid(row=1, column=1, padx=6, pady=4)

    # --- Right: Table and bottom actions ---
    right_frame = tk.Frame(main_frame, bg=BG)
    right_frame.pack(side="left", fill="both", expand=True)

    # Search bar above table
    search_frame = tk.Frame(right_frame, bg=BG)
    search_frame.pack(fill="x", pady=(0,8))
    search_var = tk.StringVar()
    search_entry = tk.Entry(search_frame, textvariable=search_var, width=38)
    search_entry.pack(side="left", padx=(0,8))
    tk.Button(search_frame, text="Search", width=12, command=lambda: search()).pack(side="left")
    tk.Button(search_frame, text="Reset", width=12, command=lambda: refresh_tree()).pack(side="left", padx=(8,0))

    # Table card
    table_card = tk.Frame(right_frame, bg=CARD_BG)
    table_card.pack(fill="both", expand=True)
    cols = ("ID","Name","Mobile","Course","Marks","Gender")
    tree = ttk.Treeview(table_card, columns=cols, show="headings", height=14)
    for c in cols:
        tree.heading(c, text=c)
        tree.column(c, width=120, anchor="center")
    vsb = ttk.Scrollbar(table_card, orient="vertical", command=tree.yview)
    tree.configure(yscroll=vsb.set)
    tree.pack(side="left", fill="both", expand=True, padx=(12,0), pady=12)
    vsb.pack(side="right", fill="y", pady=12)

    # bottom action buttons (below table)
    action_frame = tk.Frame(right_frame, bg=BG)
    action_frame.pack(fill="x", pady=(8,12))
    tk.Button(action_frame, text="Edit Selected", width=14, command=lambda: edit_selected()).pack(side="left", padx=6)
    tk.Button(action_frame, text="Delete Selected", width=14, command=lambda: delete_selected()).pack(side="left", padx=6)
    tk.Button(action_frame, text="Analyze Selected", width=14, command=lambda: analyze_selected()).pack(side="left", padx=6)

    # --- Helper functions (UI behavior) ---
    def refresh_tree():
        for i in tree.get_children():
            tree.delete(i)
        df = db_mod.read_all()
        if df is None or df.empty:
            update_summary()
            return
        for idx, r in df.iterrows():
            tag = "even" if idx%2==0 else "odd"
            tree.insert("", "end", values=(r["ID"], r["Name"], r["Mobile"], r["Course"], int(r["Marks"]), r["Gender"]), tags=(tag,))
        tree.tag_configure("even", background="#FBFBFB")
        tree.tag_configure("odd", background="#FFFFFF")
        update_summary()

    def update_summary():
        df = db_mod.read_all()
        total = len(df) if df is not None else 0
        total_marks = int(df["Marks"].sum()) if total>0 else 0
        avg = round(total_marks/total,2) if total>0 else 0
        male = int((df["Gender"]=="Male").sum()) if total>0 else 0
        female = int((df["Gender"]=="Female").sum()) if total>0 else 0
        total_label.config(text=str(total))
        avg_label.config(text=str(avg))
        male_label.config(text=str(male))
        female_label.config(text=str(female))

    def clear_form():
        name_entry.delete(0, "end")
        mobile_entry.delete(0, "end")
        marks_entry.delete(0, "end")
        course_combo.current(0)
        gender_var.set("")
        name_entry.focus_set()

    def submit_action():
        name = name_entry.get().strip()
        mobile = mobile_entry.get().strip()
        course = course_combo.get()
        marks = marks_entry.get().strip()
        gender = gender_var.get()
        if not utils.is_valid_name(name):
            messagebox.showerror("Invalid", "Name must be alphabets and spaces (2-50 chars)."); return
        if not utils.is_valid_mobile(mobile):
            messagebox.showerror("Invalid", "Mobile must be 10 digits."); return
        if not utils.is_valid_marks(marks):
            messagebox.showerror("Invalid", "Marks must be integer 0-100."); return
        if gender == "":
            messagebox.showerror("Invalid", "Select gender."); return
        sid = db_mod.next_id()
        db_mod.append_student({"ID": sid, "Name": name, "Mobile": mobile, "Course": course, "Marks": int(marks), "Gender": gender})
        clear_form()
        refresh_tree()
        messagebox.showinfo("Saved", f"Student {name} saved (ID: {sid})")

    def search():
        q = search_var.get().strip()
        if not q:
            refresh_tree()
            return
        df = db_mod.read_all()
        if df is None or df.empty:
            messagebox.showinfo("Search", "No data available")
            return
        res = df[df.apply(lambda r: q.lower() in str(r["Name"]).lower() or q.lower() in str(r["ID"]).lower() or q.lower() in str(r["Course"]).lower(), axis=1)]
        for i in tree.get_children():
            tree.delete(i)
        for idx, r in res.iterrows():
            tree.insert("", "end", values=(r["ID"], r["Name"], r["Mobile"], r["Course"], int(r["Marks"]), r["Gender"]))
        update_summary()

    def edit_selected():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Select", "Select a record to edit")
            return
        vals = tree.item(sel[0], "values")
        sid = vals[0]
        df = db_mod.read_all()
        row = df[df["ID"]==sid].iloc[0]
        # popup edit window
        ew = tk.Toplevel(root)
        ew.title("Edit Student")
        ew.geometry("420x360")
        ew.configure(bg=BG)
        tk.Label(ew, text=f"Edit — {sid}", font=("Bookman", 12, "bold"), bg=BG).pack(pady=10)
        ef = tk.Frame(ew, bg=BG)
        ef.pack(padx=12, pady=6)
        tk.Label(ef, text="Name", bg=BG).grid(row=0, column=0, sticky="w")
        e_name = tk.Entry(ef, width=34); e_name.grid(row=0, column=1, pady=6); e_name.insert(0, row["Name"])
        tk.Label(ef, text="Mobile", bg=BG).grid(row=1, column=0, sticky="w")
        e_mob = tk.Entry(ef, width=34); e_mob.grid(row=1, column=1, pady=6); e_mob.insert(0, row["Mobile"])
        tk.Label(ef, text="Course", bg=BG).grid(row=2, column=0, sticky="w")
        e_course = ttk.Combobox(ef, values=("ECE","MCA","CSE","IT","MTX","EEE"), width=32); e_course.grid(row=2, column=1, pady=6); e_course.set(row["Course"])
        tk.Label(ef, text="Marks", bg=BG).grid(row=3, column=0, sticky="w")
        e_marks = tk.Entry(ef, width=34); e_marks.grid(row=3, column=1, pady=6); e_marks.insert(0, str(row["Marks"]))
        tk.Label(ef, text="Gender", bg=BG).grid(row=4, column=0, sticky="w")
        e_gender = tk.StringVar(value=row["Gender"])
        gframe = tk.Frame(ef, bg=BG); gframe.grid(row=4, column=1, pady=6, sticky="w")
        tk.Radiobutton(gframe, text="Male", variable=e_gender, value="Male", bg=BG).pack(side="left")
        tk.Radiobutton(gframe, text="Female", variable=e_gender, value="Female", bg=BG).pack(side="left", padx=8)

        def save_edit():
            name2 = e_name.get().strip(); mob2 = e_mob.get().strip(); course2 = e_course.get(); marks2 = e_marks.get().strip(); gender2 = e_gender.get()
            if not utils.is_valid_name(name2):
                messagebox.showerror("Invalid","Name invalid"); return
            if not utils.is_valid_mobile(mob2):
                messagebox.showerror("Invalid","Mobile invalid"); return
            if not utils.is_valid_marks(marks2):
                messagebox.showerror("Invalid","Marks invalid"); return
            db_mod.update_student(sid, {"Name": name2, "Mobile": mob2, "Course": course2, "Marks": int(marks2), "Gender": gender2})
            ew.destroy()
            refresh_tree()
            messagebox.showinfo("Updated", f"{sid} updated.")

        btnf = tk.Frame(ew, bg=BG); btnf.pack(pady=12)
        tk.Button(btnf, text="Save", width=14, command=save_edit).pack(side="left", padx=6)
        tk.Button(btnf, text="Cancel", width=14, command=ew.destroy).pack(side="left", padx=6)

    def delete_selected():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Select", "Select a record to delete")
            return
        vals = tree.item(sel[0], "values")
        sid = vals[0]
        if messagebox.askyesno("Confirm", f"Delete {sid}?"):
            db_mod.delete_student(sid)
            refresh_tree()

    def clear_database():
        if messagebox.askyesno("Confirm", "Delete all records?"):
            db_mod.clear_all()
            refresh_tree()

    def do_export(kind="excel"):
        try:
            if kind == "excel":
                p = exporter.export_to_excel()
            else:
                p = exporter.export_to_csv()
            messagebox.showinfo("Exported", f"Saved: {p}")
        except Exception as e:
            messagebox.showerror("Export Failed", str(e))

    def show_top5():
        df = db_mod.read_all()
        if df is None or df.empty:
            messagebox.showinfo("Top 5", "No data")
            return
        top = df.sort_values(by="Marks", ascending=False).head(5)
        w = tk.Toplevel(root); w.title("Top 5 Students"); w.geometry("420x260")
        tv = ttk.Treeview(w, columns=("Name","Marks","Course"), show="headings", height=6)
        tv.heading("Name", text="Name"); tv.heading("Marks", text="Marks"); tv.heading("Course", text="Course")
        for _, r in top.iterrows():
            tv.insert("", "end", values=(r["Name"], int(r["Marks"]), r["Course"]))
        tv.pack(fill="both", expand=True, padx=10, pady=10)

    def analyze_marks():
        df = db_mod.read_all()
        if df is None or df.empty:
            messagebox.showinfo("Analyze", "No data to analyze")
            return
        df_sorted = df.sort_values(by="Marks", ascending=False)
        charts.marks_bar_with_avg(df_sorted["Name"].tolist(), df_sorted["Marks"].tolist(), title="Marks (High → Low)")

    def analyze_selected():
        sel = tree.selection()
        if not sel:
            messagebox.showwarning("Select", "Select a record")
            return
        vals = tree.item(sel[0], "values")
        # show simple single-student bar (or highlight)
        name = vals[1]; marks_v = int(vals[4])
        charts.marks_bar_with_avg([name], [marks_v], title=f"{name} — Marks")

    # Bind buttons
    submit_btn.config(command=submit_action)
    clear_btn.config(command=clear_form)

    # init db + tree
    try:
        db_mod.ensure_csv()
    except Exception:
        pass
    refresh_tree()

    # Return a small API for external use (if needed)
    return {
        "root": root,
        "refresh": refresh_tree,
        "submit": submit_action,
    }

# ---------- start_app() to be imported by main.py ----------
def start_app():
    root = tk.Tk()
    app = build_ui(root)
    root.mainloop()

# If run directly, start
if __name__ == "__main__":
    start_app()



