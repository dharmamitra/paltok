CWD=$(shell pwd)
PY_VERSION=3.12.1
PY_BIN=python/bin/python3

all: build

submodule.lock:
	git submodule update --init --recursive
	touch submodule.lock

venv/venv.lock: python requirements.txt
	test -d venv || ${PY_BIN} -m venv venv 
	sed -i '/include-system-site-packages/s/false/true/' venv/pyvenv.cfg
	. venv/bin/activate && \
	echo $${PATH} && \
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

python:
	mkdir python
	cd python && \
	wget https://www.python.org/ftp/python/${PY_VERSION}/Python-${PY_VERSION}.tgz && \
	tar -xvf Python-${PY_VERSION}.tgz && \
	cd Python-${PY_VERSION} && \
	./configure --prefix=${CWD}/python && \
	make && \
	make install

test:
	echo 