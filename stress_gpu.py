import torch
import time
import subprocess

def log_and_display_gpu_status(step, logfile):
    with open(logfile, "a") as f:
        try:
            # nvidia-smiを使ってGPUのステータスを取得
            result = subprocess.check_output("nvidia-smi --query-gpu=temperature.gpu,utilization.gpu,memory.used,power.draw --format=csv,noheader,nounits", shell=True)
            gpu_status = result.decode("utf-8").strip()
            log_message = f"Step {step}, {time.strftime('%Y-%m-%d %H:%M:%S')}, {gpu_status}\n"
            f.write(log_message)
            print(log_message)  # 画面に表示
        except Exception as e:
            f.write(f"Error collecting GPU status: {e}\n")
            print(f"Error collecting GPU status: {e}")

def stress_gpu_stepwise(total_duration=60, step_duration=10, log_interval=5):
    logfile = "gpu_test/gpu_stress_log_stepwise.txt"
    
    # ログファイルの初期化
    with open(logfile, "w") as f:
        f.write("Step, Time, Temperature (C), GPU Utilization (%), Memory Used (MB), Power Draw (W)\n")
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Running stepwise GPU stress test for a total of {total_duration} seconds on {device}")
    
    num_steps = total_duration // step_duration
    start_time = time.time()

    for step in range(1, num_steps + 1):
        step_start_time = time.time()
        print(f"Starting Step {step}/{num_steps}")
        
        # ステップごとの負荷を増加させる（計算量を増やす）
        while time.time() - step_start_time < step_duration:
            x = torch.rand((1000 * step, 1000 * step), device=device)  # ステップごとにテンソルサイズを増やす
            y = torch.matmul(x, x)

            # 指定された間隔ごとにGPUのステータスを記録
            if int(time.time() - start_time) % log_interval == 0:
                log_and_display_gpu_status(step, logfile)

        print(f"Step {step} completed")

    print("Stepwise GPU stress test completed.")

if __name__ == "__main__":
    # 60秒間テストし、10秒ごとに負荷を増加させる
    stress_gpu_stepwise(total_duration=60, step_duration=10, log_interval=5)
