PDF := persimmon.pdf  # PDF Main Target
CSL := emerald-harvard.csl  # CSL file used for citations
TEMPLATE := template.tex  # LaTeX template for producing PDF
BIBLIOGRAPHY := persimmon.bib  # BibLaTeX bibliography
MARKDOWN := chapter0.md chapter1.md chapter2.md chapter3.md  # Markdown files
IMAGES := $(wildcard graphs/*.png)  # Standalone pictures to be inserted
LATEXHEADERS := latexheaders.tex  # Additional LaTeX headers
METADATA := metadata.yaml  # Metadata files (Author, Date, Title, etc..)

all: pdf

pdf: $(MARKDOWN) $(BIBLIOGRAPHY) $(CSL) $(TEMPLATE) $(IMAGES) $(METADATA)
	pandoc --standalone --smart --latex-engine xelatex --template $(TEMPLATE) \
		--top-level-division chapter --bibliography $(BIBLIOGRAPHY) --csl $(CSL) \
		--include-in-header $(LATEXHEADERS) $(METADATA) $(MARKDOWN) -o $(PDF)

travis:
	pandoc --standalone --smart --latex-engine xelatex --template $(TEMPLATE) \
		--chapters --bibliography $(BIBLIOGRAPHY) --csl $(CSL) \
		--include-in-header $(LATEXHEADERS) $(METADATA) $(MARKDOWN) -o $(PDF)


## Splitted creation (Not currently working)
#CHAPTERS := $(MARKDOWN:.md=.tex)  # LaTeX Chapters
#GRAPHS := $(wildcard graphs/*.tex)
#IMAGES += $(GRAPHS:.tex=.pdf)
#
##splitted: $(CHAPTERS) $(BIBLIOGRAPHY) $(CSL) $(TEMPLATE)
#	pandoc --standalone --smart --latex-engine xelatex --template $(TEMPLATE) \
#		--top-level-division chapter --bibliography $(BIBLIOGRAPHY) --csl $(CSL) \
#	   	$(CHAPTERS) -o $(PDF)
#
#%.tex: metadata.yaml %.md
#	pandoc --no-tex-ligatures metadata.yaml $*.md -o $@
#
## For standalone images (Not used)
#graphs/%.pdf: graphs/%.tex
#	xelatex $<
#

clean:
	rm -f *.pdf chapter?.tex *.log *.aux *.png

