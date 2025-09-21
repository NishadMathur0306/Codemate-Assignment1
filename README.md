# Codemate-Assignment1
The Python Terminal Emulator is a custom Python project replicating a system shell with file operations (ls, cd, mkdir, etc.), process monitoring via psutil, CLI with history/completion, and a Flask web version. It also supports simple natural language commands, showcasing system-level Python skills and innovation


# 🔹 Project Description

**Python Terminal Emulator** is a custom-built terminal environment designed in Python that mimics the behavior of a real system shell. It allows users to perform core file and directory operations, process management, and system monitoring directly from a Python backend.

The project is implemented in two modes:

* **CLI Terminal** – runs inside any terminal/IDE (like PyCharm) and provides a command-line interface with history and auto-completion.
* **Web Terminal** – a Flask-based interface that runs in the browser, enabling users to execute commands through a simple, responsive UI.

This project was developed as part of the **CodeMate Hackathon** to demonstrate problem-solving, system-level programming in Python, and the integration of monitoring tools.

---

##  Features

* **File & Directory Operations** – `ls`, `cd`, `pwd`, `mkdir`, `rm`, `touch`, `cat`, `mv`, `cp`
* **Error Handling** – graceful handling of invalid commands or paths
* **Process & Resource Monitoring** – view running processes, CPU, and memory usage (`ps`, `monitor`)
* **Natural Language Parsing** – supports simple English commands like *“create folder test”* or *“move file1.txt to data”*
* **CLI & Web Versions** – terminal can be used either in the console or via a Flask-powered browser UI
* **Command History & Auto-completion** – (in CLI mode, using `readline`)

---

##  Tech Stack

* **Python 3** (core backend)
* **Flask** (for web terminal UI)
* **psutil** (for process and system monitoring)

---

##  Use Cases

* A learning tool for understanding how terminals work behind the scenes.
* A lightweight terminal for executing commands in restricted environments.
* A demo project for showcasing Python’s ability to integrate system calls, monitoring, and web interfaces.


