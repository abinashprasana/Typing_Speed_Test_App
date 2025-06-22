# ⌨️ Typing Speed Test App

A terminal-based **Typing Speed Test App** built in Python that challenges users to measure their typing speed and accuracy. This app provides a fun way to test your **Words Per Minute (WPM)** and **typing precision**, using randomly selected sentences from a text file.

---

## 🧠 Description

This program displays a sentence on the screen for the user to type. It measures:
- How fast the user types (in WPM)
- How accurate the user was (percentage match)

It includes a set of predefined sentences loaded from a `.txt` file (`sentences.txt`).

---

## 🔧 Features

- 📄 Loads sentences dynamically from an external file
- ⏱️ Calculates and displays Words Per Minute (WPM)
- 🎯 Shows typing accuracy in percentage
- ❌ Detects mistakes and gives detailed feedback
- 🖥️ Clean terminal interface for practice

---

## 📚 Concepts Used

- File Handling (Reading from `sentences.txt`)
- String manipulation and comparison
- Random module for sentence selection
- Time tracking using `time.time()`
- Input/output operations
- Exception handling

---

## ▶️ How to Run

1. Clone the repository or download the files  
2. Make sure both `main.py` and `sentences.txt` are in the same folder  
3. Run the script using Python:

```bash
python main.py
```

---

## 💻 Sample Output

```bash
Typing Speed Test Started...

Type the following:
The quick brown fox jumps over the lazy dog

Your Input:
The quick brown fix jumps over the lazy dog

WPM: 38.7
Accuracy: 88.57%
```

---

## 📁 Folder Structure

```
Typing_Speed_Test_App/
└── Typing Speed Test Program/
    ├── main.py
    └── sentences.txt
```

---

## 👨‍💻 Author

**Abinash Prasana**

This project is part of my intermediate-level Python learning journey. 🚀
