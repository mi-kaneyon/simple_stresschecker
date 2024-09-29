import time

def stress_memory(duration=60):
    big_data = []
    start_time = time.time()

    print(f"Running memory stress test for {duration} seconds.")
    
    # 大量のデータをメモリに保持して負荷をかける
    try:
        while time.time() - start_time < duration:
            # 約10MBのリストを確保し続ける
            big_data.append([0] * (10**6))  
    except MemoryError:
        print("MemoryError: Could not allocate more memory.")

    # メモリを解放
    del big_data
    print("Memory stress test completed.")

if __name__ == "__main__":
    stress_memory(duration=60)
