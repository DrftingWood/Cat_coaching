# Render shortcuts for Manim.
# Usage:
#   make preview FILE=videos/quant/arithmetic/001_percentages_basics/scenes.py SCENE=Intro
#   make high    FILE=videos/quant/arithmetic/001_percentages_basics/scenes.py SCENE=Intro
#   make fourk   FILE=videos/quant/arithmetic/001_percentages_basics/scenes.py SCENE=Intro
#   make clean

FILE  ?=
SCENE ?=

.PHONY: preview high fourk clean check

check:
	@if [ -z "$(FILE)" ] || [ -z "$(SCENE)" ]; then \
		echo "usage: make <target> FILE=path/to/scenes.py SCENE=ClassName"; \
		exit 2; \
	fi

preview: check
	manim -pql $(FILE) $(SCENE)

high: check
	manim -pqh $(FILE) $(SCENE)

fourk: check
	manim -pqk $(FILE) $(SCENE)

clean:
	rm -rf media/
