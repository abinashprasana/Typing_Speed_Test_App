import tkinter as tk
from tkinter import ttk
import time
import random

def load_sentences(filename="sentences.txt"):
    try:
        with open(filename, "r") as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines
    except FileNotFoundError:
        return ["No sentence file found. Please add 'sentences.txt'"]

class TypingSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.sentences = load_sentences()
        self.sentence = random.choice(self.sentences)
        self.start_time = 0
        self.running = False
        self.timer_label_text = tk.StringVar(value="Time: 0s")

        # Title
        self.title = ttk.Label(root, text="Typing Speed Test", font=("Helvetica", 20, "bold"))
        self.title.pack(pady=10)

        # Sentence
        self.display_sentence = tk.Label(root, text=self.sentence, wraplength=650, font=("Helvetica", 14))
        self.display_sentence.pack(pady=10)

        # Text Input
        self.text_input = tk.Text(root, height=5, width=60, font=("Courier", 12))
        self.text_input.pack(pady=10)

        # Buttons
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.start_button = tk.Button(self.button_frame, text="Start Typing", command=self.start_test, font=("Helvetica", 12))
        self.start_button.grid(row=0, column=0, padx=10)

        self.done_button = tk.Button(self.button_frame, text="Done", command=self.end_test, state=tk.DISABLED, font=("Helvetica", 12))
        self.done_button.grid(row=0, column=1, padx=10)

        # Timer Label
        self.timer_label = ttk.Label(root, textvariable=self.timer_label_text, font=("Helvetica", 12))
        self.timer_label.pack(pady=5)

        # Result
        self.result_label = ttk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=10)

    def start_test(self):
        self.text_input.delete(1.0, tk.END)
        self.text_input.focus_set()
        self.start_time = time.time()
        self.running = True
        self.elapsed = 0
        self.update_timer()

        self.done_button.config(state=tk.NORMAL)
        self.start_button.config(state=tk.DISABLED)
        self.result_label.config(text="")

    def update_timer(self):
        if self.running:
            self.elapsed = int(time.time() - self.start_time)
            self.timer_label_text.set(f"Time: {self.elapsed}s")
            self.root.after(1000, self.update_timer)

    def end_test(self):
        self.running = False
        total_time = time.time() - self.start_time
        typed_text = self.text_input.get(1.0, tk.END).strip()

        word_count = len(typed_text.split())
        wpm = (word_count / total_time) * 60 if total_time > 0 else 0

        correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(self.sentence) and c == self.sentence[i])
        accuracy = (correct_chars / len(self.sentence)) * 100 if self.sentence else 0

        self.result_label.config(text=f"WPM: {wpm:.2f} | Accuracy: {accuracy:.2f}% | Duration: {int(total_time)}s")

        # Prepare next sentence
        self.sentence = random.choice(self.sentences)
        self.display_sentence.config(text=self.sentence)

        # Reset buttons
        self.start_button.config(state=tk.NORMAL)
        self.done_button.config(state=tk.DISABLED)

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()
