# simple_stresschecker
## This checker is created due to resolve GPU train/inference shutdown system failure
- When I replaced new DIMM from 8GB to 18GB.
- After expanded memory, OS woerking very well. But GPU working time always system shutdown without error message.
- To create this script for resolve shut down issue.

# Normaly I recommend to use stress to your system below repository

https://github.com/mi-kaneyon/Ubuntu_loadpower

# function 
- CPU stress
- memory stress
- GPU stress
- No considering stress level.

## Generate directory tree shell
- you can create yourself tree 

```
stress_check$ tree
.
├── cpu_test
│   └── stress_cpu.py
├── create_stress_test_dirs.sh
├── gpu_test
│   ├── gpu_stress_log_stepwise.txt
│   ├── gpu_stress_log.txt
│   ├── stress_gpu.py
│   └── stress_gpu_stepwise.py
├── memory_test
│   └── stress_memory.py
└── stress_test_main.py

3 directories, 8 files

```


```
create_stress_test_dirs.sh

```
If you cannot exexute the shell , change permission first.

```
chmod +x create_stress_test_dirs.sh

```

# Example

```
python stress_test_main.py

```
![Test Image 3](/main.png)
