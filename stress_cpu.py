import time
import psutil

def log_memory_status(logfile):
    with open(logfile, "a") as f:
        memory_info = psutil.virtual_memory()
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')}, Memory Usage: {memory_info.percent}%, Available: {memory_info.available / (1024**2)}MB\n")

def stress_memory(duration=60, log_interval=5):
    logfile = "memory_test/memory_stress_log.txt"

    # 初期化メッセージ
    with open(logfile, "w") as f:
        f.write("Time, Memory Usage (%), Available Memory (MB)\n")

    big_data = []
    start_time = time.time()

    print(f"Running memory stress test for {duration} seconds.")
    
    try:
        while time.time() - start_time < duration:
            # メモリを大量に確保
            big_data.append([0] * (10**6))  # 約10MBのメモリ確保

            # 指定された間隔ごとにメモリのステータスを記録
            if int(time.time() - start_time) % log_interval == 0:
                log_memory_status(logfile)
    except MemoryError:
        print("MemoryError: Could not allocate more memory.")
    
    # メモリを解放
    del big_data
    print("Memory stress test completed.")

if __name__ == "__main__":
    stress_memory(duration=60, log_interval=5)
