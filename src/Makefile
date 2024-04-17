
install: venv
venv:
	( \
	  cd ..; \
	  virtualenv venv; \
      source ./venv/bin/activate; \
      pip3 install -r ./requirements.txt; \
    )
doc:
	doxygen Doxyfile -w dox.css
gui:
	python3 ./gui.py
testq: ./test/math_lib_test.py
	pytest -rAq --tb=no ./test/math_lib_test.py
test: FORCE
	pytest -rAq ./test/math_lib_test.py
clean:
	rm -r ../venv
	rm -r ../program_documentation
pack:
	zip *
passlist_test:
	python -m doctest -v passlist.py

save_requirements: #without SUDO !!!! or global python wwill be used
	( \
	source ../venv/bin/activate;\
	#pip3 install --upgrade pip;\
	pip3 freeze > ../requirements.txt;\
	)
FORCE: ;
