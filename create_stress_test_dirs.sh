#!/bin/bash

# ディレクトリ作成
mkdir -p ~/note/stress_check/cpu_test
mkdir -p ~/note/stress_check/gpu_test
mkdir -p ~/note/stress_check/memory_test

# サンプルファイル作成
touch ~/note/stress_check/cpu_test/stress_cpu.py
touch ~/note/stress_check/gpu_test/stress_gpu.py
touch ~/note/stress_check/memory_test/stress_memory.py

echo "ディレクトリとファイルを作成しました。"
