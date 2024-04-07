cd profiling
python3 generate.py
cd ..
python3 profiling.py < profiling/numbers0.txt > profiling/output.txt
python3 profiling.py < profiling/numbers1.txt >> profiling/output.txt
python3 profiling.py < profiling/numbers2.txt >> profiling/output.txt
