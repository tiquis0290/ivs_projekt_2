

# all musi byt prvni, (přeloží projekt – včetně programu pro profiling) – při zvolení skriptovacího jazyka využijte pro stažení závislostí, případně volte variantu níže
all: venv
# help (vypíše nápovědu s popisem, co je potřeba udělat před spuštěním programu)
help:
# run (spustí program)
run: gui
install: venv

#profile (při zvolení skriptovacího jazyka využijte pro stažení závislostí, případně volte variantu níže
profile: profiling.py
	python3 ./profiling.py
venv:
	( \
	  cd ..; \
	  virtualenv venv; \
      source ./venv/bin/activate; \
      pip3 install -r ./requirements.txt; \
    )
#doc (spustí generování dokumentace)
doc:
	doxygen Doxyfile -w dox.css
gui:
	python3 ./gui.py
testq: ./test/math_lib_test.py
	pytest -rAq --tb=no ./test/math_lib_test.py
#test (spustí testy matematické knihovny)
test:
	pytest -rAq ./test/math_lib_test.py
clean:
	rm -r ../venv
	rm -r ../program_documentation

# pack (zabalí projekt tak, aby mohl být odevzdán)
pack: doc
	rm -rf ../pro_odevzdani
	rm -rf ../xlogin01_xlogin02_xlogin03_xlogin04.zip
	# doc
	mkdir ../pro_odevzdani
	mv ../program_documentation ../pro_odevzdani/doc
	rm -rf ../program_documentation
	# working dir
	cp -r ../../ivs_projekt_2 ../../tmp && mv ../../tmp ../pro_odevzdani/repo
	# installator
	mkdir ../pro_odevzdani/install
	cp ./dist/stddev.exe ../pro_odevzdani/install
	cp ./Output/calculator_setup.exe ../pro_odevzdani/install
	zip -r ../xlogin01_xlogin02_xlogin03_xlogin04.zip ../pro_odevzdani
	rm -rf ../pro_odevzdani

passlist_test:
	python -m doctest -v passlist.py

save_requirements: #without SUDO !!!! or global python will be used
	( \
	source ../venv/bin/activate;\
	#pip3 install --upgrade pip;\
	pip3 freeze > ../requirements.txt;\
	)
FORCE: ;
