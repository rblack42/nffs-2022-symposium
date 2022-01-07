TEXDOC	= main
LATECXMK = latexmk -use-make

all: pdf

%.pdf:	%.tex %.pytxcode
		pythontex $*
		$(LATEXMK) -M -MP -MF $*.deps $*

%.pytxcode: $(TEXDOC).tex
		pdflatex -synctex=1 --interaction-nonstop -file-line-error -shell-escape -draftmode $*

_pythontex/%.pytxmcr: %.pytxcode
		pythontex $(notdor $*)

report:	$(TEXDOC).pdf

clean:
	rm -rf _pythontex
	latexmk -c
