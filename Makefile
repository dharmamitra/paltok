all: build

submodule.lock:
	git submodule update --init --recursive
	touch submodule.lock

venv/venv.lock: requirements.txt
	test -d venv || python3 -m venv venv 
	sed -i '/include-system-site-packages/s/false/true/' venv/pyvenv.cfg
	. venv/bin/activate && \
	pip install --user -r requirements.txt 
	touch venv/venv.lock

fastText/fasttext: submodule.lock 
	cd fastText && make

build: venv/venv.lock fastText/fasttext
	. venv/bin/activate && \
	echo $${PATH} && \
	cd src && bash train_models.sh


clean:
	rm -rf output

fclean: clean
	rm -rf venv
	rm -rf segmented-pali/*