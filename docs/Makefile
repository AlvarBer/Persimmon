PDF := persimmon.pdf  # PDF Main Target
CSL := emerald-harvard.csl  # CSL file used for citations
TEMPLATE := template.tex  # LaTeX template for producing PDF
BIBLIOGRAPHY := persimmon.bib  # BibLaTeX bibliography
MARKDOWN := chapter0.md chapter1.md chapter2.md chapter3.md # Markdown files
GRAPHS := $(wildcard graphs/*.tex)
IMAGES := $(GRAPHS:.tex=.pdf)
LATEXHEADERS := latexheaders.tex

all: $(PDF)

$(PDF): $(MARKDOWN) $(BIBLIOGRAPHY) $(CSL) $(TEMPLATE) metadata.yaml
	pandoc --standalone --smart --latex-engine xelatex --template $(TEMPLATE) \
		--top-level-division chapter --bibliography $(BIBLIOGRAPHY) --csl $(CSL) \
		--include-in-header latexheaders.tex metadata.yaml $(MARKDOWN) -o $@

graphs/%.pdf: graphs/%.tex
	xelatex $<

travis:
	pandoc --standalone --smart --latex-engine xelatex --template $(TEMPLATE) \
		--chapters --bibliography $(BIBLIOGRAPHY) --csl $(CSL) \
		--include-in-header latexheaders.tex metadata.yaml $(MARKDOWN) -o $(PDF)


# Splitted creation (Not currently working)
CHAPTERS := $(MARKDOWN:.md=.tex)  # LaTeX Chapters
splitted: $(CHAPTERS) $(BIBLIOGRAPHY) $(CSL) $(TEMPLATE)
	pandoc --standalone --smart --latex-engine xelatex --template $(TEMPLATE) \
		--top-level-division chapter --bibliography $(BIBLIOGRAPHY) --csl $(CSL) \
	   	$(CHAPTERS) -o $(PDF)

%.tex: metadata.yaml %.md
	pandoc --no-tex-ligatures metadata.yaml $*.md -o $@

clean:
	rm -f *.pdf chapter?.tex *.log *.aux *.png

