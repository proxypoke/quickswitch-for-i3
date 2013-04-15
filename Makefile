.PHONY: clean
clean:
	rm *.tar.*

.PHONY: dist
dist:
	py setup.py sdist upload

.PHONY: arch-source
arch-source:
	makepkg --source
