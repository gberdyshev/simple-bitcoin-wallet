make: install

clean:
	rm -rf build dist __pycache__ *.egg-info

format:
	black *.py --line-length 100

dist: clean format
	python3 setup.py sdist bdist_wheel

upload: dist
	python3 -m twine upload dist/*

install: dist
	-pipx install --force --pip-args='--force-reinstall --no-deps' dist/*.whl; [ $$? -eq 127 ] && pip install --force-reinstall --no-deps dist/*.whl

.PHONY: clean dist upload install
