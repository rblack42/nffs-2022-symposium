.PHONY: all
all:	jb-build

.PHONY: venv
venv:
	echo 'layout python3' > .envrc && \
		direnv allow

.PHONY: reqs
reqs:
	pip install -U pip
	pip install -r requirements.txt
	cp ~/_data/tikzmagic.py .direnv/python-3.9.9/lib/python3.9/site-packages/

.PHONY: tex
tex:
	cd tex && \
	pdflatex main &&  \
	python main.sympy && \
	bibtex main && \
	pdflatex main && \
	pdflatex main

.PHONY: pub
pub:
	cd tex && \
	cp main.pdf ../docs/article.pdf && \
	pandoc main.tex -o ../docs/article.docx

.PHONY: clean
clean:
	cd tex && \
		rm -f *.aux *.bbc *.bbl *.fls *.log *.out *.sympy *.sout *.fdb_latexmk
	jupyter-book clean book/ --all

.PHONY: outline
outline:
	cd tex && pdflatex outline

.PHONY: nb
nb:
	cd book && jupyter notebook

.PHONY: jb-build
jb-build:
	jb build book
	cp -r book/_build/html/* docs
