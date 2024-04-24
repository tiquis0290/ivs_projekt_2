cd profiling
python3 generate.py
cd ..
echo "10 numbers" > profiling/output.txt
python3 profiling.py < profiling/numbers0.txt >> profiling/output.txt
echo "100 numbers" >> profiling/output.txt
python3 profiling.py < profiling/numbers1.txt >> profiling/output.txt
echo "1 000 000 numbers" >> profiling/output.txt
python3 profiling.py < profiling/numbers2.txt >> profiling/output.txt
