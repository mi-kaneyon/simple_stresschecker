import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import os

# 各ストレステストの実行関数
def run_cpu_test():
    result = subprocess.run(['python', 'cpu_test/stress_cpu.py'], capture_output=True, text=True)
    messagebox.showinfo("CPU Test Result", result.stdout)

def run_gpu_test():
    result = subprocess.run(['python', 'gpu_test/stress_gpu.py'], capture_output=True, text=True)
    messagebox.showinfo("GPU Test Result", result.stdout)

def run_memory_test():
    result = subprocess.run(['python', 'memory_test/stress_memory.py'], capture_output=True, text=True)
    messagebox.showinfo("Memory Test Result", result.stdout)

# GUIメニュー
def create_gui():
    root = tk.Tk()
    root.title("総合ストレステストメニュー")

    label = tk.Label(root, text="実行するストレステストを選択してください")
    label.pack(pady=10)

    cpu_button = tk.Button(root, text="CPU負荷テスト", command=lambda: threading.Thread(target=run_cpu_test).start())
    cpu_button.pack(pady=5)

    gpu_button = tk.Button(root, text="GPU負荷テスト", command=lambda: threading.Thread(target=run_gpu_test).start())
    gpu_button.pack(pady=5)

    memory_button = tk.Button(root, text="memory負荷テスト", command=lambda: threading.Thread(target=run_memory_test).start())
    memory_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    # スクリプトのルートディレクトリであることを確認
    if not os.path.exists("cpu_test") or not os.path.exists("gpu_test") or not os.path.exists("memory_test"):
        messagebox.showerror("Error", "テストディレクトリが存在しません")
    else:
        create_gui()
