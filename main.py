import tkinter as tk
from tkinter import messagebox
import threading


class DisappearingTextApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Disappearing Text Application")
        self.root.configure(bg="#f0f0f0")

        self.text = ""
        self.timer = None
        self.time_remaining = 5

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        # Configure the font
        font_style = ("Helvetica", 14)

        self.text_label = tk.Label(self.root, text="Enter text (it will disappear after 5 seconds of inactivity):",
                                   bg="#f0f0f0", font=font_style)
        self.text_label.pack(pady=10)

        self.text_entry = tk.Text(self.root, height=10, width=50, font=("Helvetica", 12))
        self.text_entry.pack(pady=10)

        self.timer_label = tk.Label(self.root, text=f"Time remaining: {self.time_remaining} seconds", bg="#f0f0f0",
                                    font=font_style)
        self.timer_label.pack(pady=10)

        self.button_frame = tk.Frame(self.root, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(self.button_frame, text="Start", command=self.start, bg="#4CAF50", fg="white",
                                      font=font_style, padx=20, pady=10)
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(self.button_frame, text="Stop", command=self.stop, bg="#F44336", fg="white",
                                     font=font_style, padx=20, pady=10)
        self.stop_button.grid(row=0, column=1, padx=10)

    def start(self):
        self.text_entry.bind("<KeyRelease>", self.reset_timer)
        self.reset_timer()

    def stop(self):
        if self.timer is not None:
            self.timer.cancel()
        self.text_entry.unbind("<KeyRelease>")
        self.time_remaining = 5
        self.timer_label.config(text=f"Time remaining: {self.time_remaining} seconds")
        messagebox.showinfo("Info", "Timer stopped")

    def reset_timer(self, event=None):
        if self.timer is not None:
            self.timer.cancel()
        self.time_remaining = 5
        self.update_timer_label()
        self.timer = threading.Timer(1.0, self.decrement_timer)
        self.timer.start()

    def decrement_timer(self):
        self.time_remaining -= 1
        self.update_timer_label()
        if self.time_remaining <= 0:
            self.clear_text()
        else:
            self.timer = threading.Timer(1.0, self.decrement_timer)
            self.timer.start()

    def update_timer_label(self):
        self.timer_label.config(text=f"Time remaining: {self.time_remaining} seconds")

    def clear_text(self):
        self.text_entry.delete(1.0, tk.END)
        messagebox.showinfo("Info", "Text cleared due to inactivity.")
        self.time_remaining = 5
        self.update_timer_label()


if __name__ == "__main__":
    root = tk.Tk()
    app = DisappearingTextApp(root)
    root.mainloop()
