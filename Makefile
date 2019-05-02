# LaTeX compiler
#TEXC := pdflatex
TEXC := xelatex

default: pdf

part01: stats_part01.md stats_part01.bib
	echo "Convert Markdown text file to tex file"
	multimarkdown -t beamer stats_part01.md > stats_part01.tex
	echo "Compile tex file with pdflatex"
	$(TEXC) stats_part01.tex
	bibtex stats_part01
	$(TEXC) stats_part01.tex
	$(TEXC) stats_part01.tex

part02: stats_part02.md
	echo "Convert Markdown text file to tex file"
	multimarkdown -t beamer stats_part02.md > stats_part02.tex
	echo "Compile tex file with pdflatex"
	$(TEXC) stats_part02.tex
	bibtex stats_part02
	$(TEXC) stats_part02.tex
	$(TEXC) stats_part02.tex

part03: stats_part03.md stats_part03.bib
	echo "Convert Markdown text file to tex file"
	multimarkdown -t beamer stats_part03.md > stats_part03.tex
	echo "Compile tex file with pdflatex"
	$(TEXC) stats_part03.tex
	bibtex stats_part03
	$(TEXC) stats_part03.tex
	$(TEXC) stats_part03.tex

part04: stats_part04.md
	echo "Convert Markdown text file to tex file"
	multimarkdown -t beamer stats_part04.md > stats_part04.tex
	echo "Compile tex file with pdflatex"
	$(TEXC) stats_part04.tex
	$(TEXC) stats_part04.tex

pdf: part01 part02 part03 part04

clean:
	rm -f *.out *.aux *.log *.toc *.snm *.nav *.bbl *.blg *.backup
