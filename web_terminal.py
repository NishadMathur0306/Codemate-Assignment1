from flask import Flask, render_template_string, request
import subprocess, shlex, os, psutil

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <title>Python Web Terminal</title>
  <style>
    body { font-family: monospace; background:#111; color:#0f0; }
    textarea { width:100%; height:400px; background:#000; color:#0f0; }
    input { width:80%; background:#222; color:#0f0; }
    button { padding:5px; }
  </style>
</head>
<body>
  <h2>Python Web Terminal</h2>
  <form method="POST">
    <input name="cmd" placeholder="Enter command">
    <button type="submit">Run</button>
  </form>
  <textarea readonly>{{output}}</textarea>
</body>
</html>
"""

@app.route("/", methods=["GET","POST"])
def index():
    output=""
    if request.method=="POST":
        cmd = request.form["cmd"]
        try:
            if cmd=="monitor":
                mem = psutil.virtual_memory()
                output = f"CPU: {psutil.cpu_percent()}% | MEM: {mem.percent}%"
            else:
                out = subprocess.run(shlex.split(cmd), capture_output=True, text=True)
                output = out.stdout + out.stderr
        except Exception as e:
            output = str(e)
    return render_template_string(TEMPLATE, output=output)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
