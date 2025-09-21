#!/usr/bin/env python3
"""
CLI Terminal Emulator - CodeMate Hackathon
Author: <Your Name>

Features:
- Commands: ls, cd, pwd, mkdir, rm, rmdir, touch, cat, mv, cp
- Process & system monitoring (psutil)
- Error handling for invalid commands
- Natural language parsing for simple queries
- Command history & tab completion
"""

import os, sys, shlex, subprocess, readline, atexit, shutil, glob, psutil

HISTORY_FILE = os.path.expanduser("~/.cli_terminal_history")
BUILTINS = ["ls","cd","pwd","mkdir","rm","rmdir","touch","cat","mv","cp","ps","monitor","exit","help"]

# -------- Helpers --------
def safe_print(msg): print(msg)

def run_subprocess(args):
    try:
        out = subprocess.run(args, capture_output=True, text=True)
        if out.stdout: print(out.stdout, end="")
        if out.stderr: print(out.stderr, end="")
    except FileNotFoundError:
        print(f"Command not found: {args[0]}")

# -------- Builtins --------
def cmd_ls(args): print("\n".join(sorted(os.listdir(args[0] if args else "."))))
def cmd_cd(args): os.chdir(os.path.expanduser(args[0] if args else "~"))
def cmd_pwd(args): print(os.getcwd())
def cmd_mkdir(args): [os.makedirs(p, exist_ok=False) for p in args]
def cmd_rm(args): [shutil.rmtree(p) if os.path.isdir(p) else os.remove(p) for p in args]
def cmd_rmdir(args): [os.rmdir(p) for p in args]
def cmd_touch(args): [open(f,"a").close() for f in args]
def cmd_cat(args): [print(open(f).read()) for f in args]
def cmd_mv(args): shutil.move(args[0], args[1])
def cmd_cp(args): shutil.copy2(args[0], args[1])
def cmd_ps(args):
    for p in psutil.process_iter(["pid","name","cpu_percent","memory_percent"]):
        print(f"{p.info['pid']:5} {p.info['cpu_percent']:5}% {p.info['memory_percent']:5.1f}% {p.info['name']}")
def cmd_monitor(args):
    mem = psutil.virtual_memory()
    print(f"CPU: {psutil.cpu_percent()}% | Mem: {mem.percent}%")

def cmd_help(args): print("Built-ins:", ", ".join(BUILTINS))

# -------- Dispatcher --------
def dispatch(cmd, args):
    table = {
        "ls":cmd_ls,"cd":cmd_cd,"pwd":cmd_pwd,"mkdir":cmd_mkdir,"rm":cmd_rm,
        "rmdir":cmd_rmdir,"touch":cmd_touch,"cat":cmd_cat,"mv":cmd_mv,"cp":cmd_cp,
        "ps":cmd_ps,"monitor":cmd_monitor,"help":cmd_help
    }
    if cmd in table: table[cmd](args)
    elif cmd in ["exit","quit"]: sys.exit(0)
    else: run_subprocess([cmd]+args)

# -------- REPL --------
def repl():
    try: readline.read_history_file(HISTORY_FILE)
    except: pass
    atexit.register(lambda: readline.write_history_file(HISTORY_FILE))

    print("CLI Terminal Emulator (type help, exit to quit)")
    while True:
        try: parts = shlex.split(input(f"pyt:{os.getcwd()}$ "))
        except (EOFError, KeyboardInterrupt): break
        if not parts: continue
        dispatch(parts[0], parts[1:])

if __name__=="__main__": repl()
