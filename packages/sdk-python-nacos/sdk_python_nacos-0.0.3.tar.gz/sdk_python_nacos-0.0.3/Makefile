clean:
	rm -rf build dist
build:
	python3 -m build
	#python3 setup.py sdist bdist_wheel
install:
	python3 setup.py install
check:
	twine check dist/*
upload:
	twine upload dist/*
all:clean build install check upload
