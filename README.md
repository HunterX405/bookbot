# 📘 BookBot

A simple command-line program that analyzes a text file and prints useful statistics such as:

* Total word count
* Character frequency (sorted by most common)

This project is part of the **Boot.dev Guided Project** curriculum.

---

## 🚀 Features

### ✅ Word Count

Counts how many words appear in a given book or text file.

### ✅ Character Frequency

Reports how often each character (a–z) appears, case-insensitive.

### ✅ Sorted Output

Character frequency is automatically sorted from most common → least common.

---

## 📂 Project Structure

```
.
├── main.py        # Entry point for the program
├── stats.py       # Helper functions for analysis
└── README.md      # Project documentation
```

---

## 🛠 How It Works

### `main.py`

* Reads the book file passed as a command-line argument
* Calls helper functions from `stats.py`
* Prints results in clean, organized sections

### `stats.py`

Contains the core logic:

* `get_num_words(text)` — counts total words
* `get_char_frequency(text)` — counts the frequency of each character
* `sort_dictionary(dictionary)` — sorts character counts by frequency

---

## 🧪 Example Usage

Run BookBot from the command line:

```bash
python3 main.py books/frankenstein.txt
```

Sample Output:

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 78345 total words
--------- Character Count -------
e: 41565
t: 30321
a: 24887
o: 24411
...
============= END ===============
```

---

## 📌 Requirements

* Python 3.10+ recommended
* A text file (plain `.txt`) to analyze

---

## 🧠 What I Learned

This guided project helped me practice:

* Working with command-line arguments
* Reading and processing text files
* Using dictionaries for frequency counts
* Sorting custom data structures
* Building small but functional Python CLI tools

---
