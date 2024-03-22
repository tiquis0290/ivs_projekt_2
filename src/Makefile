

install:
	pip install -r ../requirements.txt
doc:
	doxygen Doxyfile

testq:
	pytest -rAq --tb=no ./test/math_lib_test.py
test: FORCE
	pytest -rAq ./test/math_lib_test.py

clean:
pack:
	zip *

FORCE: ;
