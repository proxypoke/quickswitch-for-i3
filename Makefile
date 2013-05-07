.PHONY: clean
clean:
	# This will remove EVERYTHING that's not tracked by git. Use with care.
	git clean -df

.PHONY: dist
dist:
	python setup.py sdist upload

.PHONY: arch-source
arch-source:
	makepkg --source
