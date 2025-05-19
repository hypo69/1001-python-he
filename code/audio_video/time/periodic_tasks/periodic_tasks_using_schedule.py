import schedule
import threading
import time
import tkinter as tk
from tkinter import scrolledtext

# משתנים גלובליים
running = True
scheduler_active_1 = False
scheduler_active_2 = False

def do_something():
    log_message("לחייך 😊")

def do_something_else():
    log_message("לנופף ביד 👋")

# פונקציה לרישום הודעות
log_text = None  # יאותחל בהמשך
def log_message(message):
    if log_text:
        log_text.insert(tk.END, message + "\n")
        log_text.yview(tk.END)

# פונקציה להפעלת המתזמן
def run_scheduler():
    while running:
        if scheduler_active_1:
            schedule.run_pending()
        if scheduler_active_2:
            schedule.run_pending()
        time.sleep(0.1)

# הפעלת המתזמן באשכול נפרד
scheduler_thread = threading.Thread(target=run_scheduler, daemon=True)
scheduler_thread.start()

# פונקציות שליטה

def start_task_1():
    global scheduler_active_1
    scheduler_active_1 = True
    schedule.every(1).seconds.do(do_something).tag("task1")
    log_message("המשימה הראשונה הופעלה.")

def stop_task_1():
    global scheduler_active_1
    scheduler_active_1 = False
    schedule.clear("task1")
    log_message("המשימה הראשונה הופסקה.")

def start_task_2():
    global scheduler_active_2
    scheduler_active_2 = True
    schedule.every(1).seconds.do(do_something_else).tag("task2")
    log_message("המשימה השנייה הופעלה.")

def stop_task_2():
    global scheduler_active_2
    scheduler_active_2 = False
    schedule.clear("task2")
    log_message("המשימה השנייה הופסקה.")

def remove_task_1():
    schedule.clear("task1")
    log_message("המשימה הראשונה הוסרה.")

def remove_task_2():
    schedule.clear("task2")
    log_message("המשימה השנייה הוסרה.")

def list_tasks():
    log_message("משימות מתוזמנות:")
    for job in schedule.jobs:
        log_message(str(job))

# יצירת ממשק המשתמש הגרפי
root = tk.Tk()
root.title("Task Scheduler")
root.geometry("500x300")

main_frame = tk.Frame(root)
main_frame.pack(pady=10, fill=tk.BOTH, expand=True)

button_frame = tk.Frame(main_frame)
button_frame.pack(side=tk.LEFT, padx=10, pady=10)

log_frame = tk.Frame(main_frame)
log_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

start_btn_1 = tk.Button(button_frame, text="Start 1", command=start_task_1)
stop_btn_1 = tk.Button(button_frame, text="Stop 1", command=stop_task_1)
remove_btn_1 = tk.Button(button_frame, text="Remove 1", command=remove_task_1)
start_btn_2 = tk.Button(button_frame, text="Start 2", command=start_task_2)
stop_btn_2 = tk.Button(button_frame, text="Stop 2", command=stop_task_2)
remove_btn_2 = tk.Button(button_frame, text="Remove 2", command=remove_task_2)
list_btn = tk.Button(button_frame, text="List Tasks", command=list_tasks)

start_btn_1.pack(fill=tk.X, pady=2)
stop_btn_1.pack(fill=tk.X, pady=2)
remove_btn_1.pack(fill=tk.X, pady=2)
start_btn_2.pack(fill=tk.X, pady=2)
stop_btn_2.pack(fill=tk.X, pady=2)
remove_btn_2.pack(fill=tk.X, pady=2)
list_btn.pack(fill=tk.X, pady=2)

log_text = scrolledtext.ScrolledText(log_frame, height=10, width=60)
log_text.pack(pady=10, fill=tk.BOTH, expand=True)

# הפעלת ממשק המשתמש הגרפי
root.mainloop()

running = False