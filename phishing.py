import tkinter as tk
from tkinter import messagebox

def check_email():
    warning = """
⚠ PHISHING DETECTED!

Warning Signs:
1. Suspicious sender email address
2. Urgent language ("Act Now!")
3. Requests for personal information
4. Untrusted links

Tips:
✔ Verify the sender
✔ Check the URL carefully
✔ Never share passwords
✔ Report suspicious emails
"""
    messagebox.showinfo("Phishing Awareness", warning)

# Main Window
root = tk.Tk()
root.title("Phishing Attack Awareness Simulator")
root.geometry("600x400")

title = tk.Label(
    root,
    text="Phishing Attack Awareness Simulator",
    font=("Arial", 16, "bold"),
    fg="red"
)
title.pack(pady=10)

email_frame = tk.Frame(root, bd=2, relief="solid", padx=10, pady=10)
email_frame.pack(pady=20)

email_text = """
From: support@secure-bank-login.com

Dear Customer,

Your account has been temporarily locked.
Click the button below to verify your account immediately.

Failure to respond within 24 hours may result
in permanent account suspension.
"""

label = tk.Label(email_frame, text=email_text, justify="left")
label.pack()

btn = tk.Button(
    root,
    text="Verify Account",
    command=check_email,
    bg="red",
    fg="white",
    font=("Arial", 12)
)
btn.pack(pady=20)

root.mainloop()