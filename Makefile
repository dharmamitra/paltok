all: build

venv/venv-lock: requirements.txt
	test -d venv || python3 -m venv venv 
	sed -i '/include-system-site-packages/s/false/true/' venv/pyvenv.cfg
	. venv/bin/activate && \
	pip install --user -r requirements.txt 
	touch venv/venv-lock

build: venv/venv-lock
	. venv/bin/activate && \
	echo $${PATH} && \
	cd src && bash train_models.sh

clone-src:
	git submodule update --init --recursive

clean:
	rm -rf output

fclean: clean
	rm -rf venv
	rm -rf segmented-pali/*