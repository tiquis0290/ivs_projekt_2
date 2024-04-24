

# all musi byt prvni, (přeloží projekt – včetně programu pro profiling) – při zvolení skriptovacího jazyka využijte pro stažení závislostí, případně volte variantu níže
all: venv
# help (vypíše nápovědu s popisem, co je potřeba udělat před spuštěním programu)
help:
# run (spustí program)
run: gui
profile: all #stahne závislosti
venv: # source ../venv/bin/activate;
	virtualenv ../venv
	../venv/bin/pip install pytest
	../venv/bin/pip3 install -r ../requirements.txt

#doc (spustí generování dokumentace)
doc:
	doxygen Doxyfile -w dox.css
gui:
	python3 ./gui.py
testq: ./test/math_lib_test.py
	pytest -rAq --tb=no ./test/math_lib_test.py
#test (spustí testy matematické knihovny)
test: FORCE
	pytest -rAq ./test/math_lib_test.py
clean:
	rm -r ../venv
	rm -r ../program_documentation

# pack (zabalí projekt tak, aby mohl být odevzdán)
pack: doc
	rm -rf ../pro_odevzdani
	rm -rf ../xmaslom00_xsloboa00_xhyzari00_xjanecv00.zip
	# doc
	mkdir ../pro_odevzdani
	mv ../program_documentation ../pro_odevzdani/doc
	rm -rf ../program_documentation
	# working dir
	cp -r ../../ivs_projekt_2 ../../tmp && mv ../../tmp ../pro_odevzdani/repo
	# installator
	mkdir ../pro_odevzdani/install
	cp ./Output/stddev_setup.exe ../pro_odevzdani/install
	cp ./Output/calculator_setup.exe ../pro_odevzdani/install
	zip -r ../xmaslom00_xsloboa00_xhyzari00_xjanecv00.zip ../pro_odevzdani
	rm -rf ../pro_odevzdani

passlist_test:
	python -m doctest -v passlist.py

save_requirements: #without SUDO !!!! or global python will be used
	../venv/bin/pip3 freeze > ../requirements.txt;
FORCE: ;
