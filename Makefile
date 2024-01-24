all: clone-src
	cd src && bash train_models.sh

clone-src:
	git submodule update --init --recursive

clean:
	rm -rf output

fclean:
	rm -rf segmented-pali/*