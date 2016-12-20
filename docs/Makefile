PDF := persimmon.pdf  # PDF Main Target
MARKDOWN := chapter0.md chapter1.md chapter2.md chapter3.md  # Markdown files
APPENDICES := apendixX.md  # APPENDICES
METADATA := metadata.yaml  # Metadata files (Author, Date, Title, etc..)
BIBLIOGRAPHY := persimmon.bib  # BibLaTeX bibliography
CSL := emerald-harvard.csl  # CSL file used for citations
TEMPLATE := template.tex  # LaTeX template for producing PDF

GRAPHS := $(wildcard graphs/*.tex)  # Latex diagrams
IMAGES := $(GRAPHS:.tex=.pdf) 
IMAGES += $(wildcard graphs/*.png)  # Standalone pictures to be inserted

all: pdf

pdf: $(MARKDOWN) $(APPENDICES) $(BIBLIOGRAPHY) $(CSL) $(TEMPLATE) $(IMAGES) $(METADATA)
	pandoc --standalone --smart --latex-engine xelatex --template $(TEMPLATE) \
		--top-level-division chapter --bibliography $(BIBLIOGRAPHY) --csl $(CSL) \
		$(METADATA) $(MARKDOWN) $(APPENDICES) -o $(PDF)

travis: $(MARKDOWN) $(APENDICES) $(BIBLIOGRAPHY) $(CSL) $(TEMPLATE) $(IMAGES) $(METADATA)
	pandoc --standalone --smart --latex-engine xelatex --template $(TEMPLATE) \
		--chapters --bibliography $(BIBLIOGRAPHY) --csl $(CSL) \
		--include-in-header $(LATEXHEADERS) $(METADATA) $(MARKDOWN) $(APPENDICES) -o $(PDF)

# For standalone images 
graphs/%.pdf: graphs/%.tex
	xelatex $< > /dev/null # TODO: actually output in graphs directory
	@rm $*.aux $*.log


# Splitted creation (Bibliography not at the end)
# Breaks tables
CHAPTERS := $(MARKDOWN:.md=.tex)  # LaTeX Chapters

complex: body.tex appendices.tex
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--top-level-division chapter body.tex appendix.tex -o test.pdf

body.tex: $(MARKDOWN) $(IMAGES)
	pandoc --no-tex-ligatures --top-level-division chapter \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) $(METADATA) $(MARKDOWN) \
		-o $@

appendices.tex: $(APPENDICES)
	pandoc --no-tex-ligatures $(APPENDICES) -o $@

clean:
	rm -f *.pdf chapter?.tex body.tex appendix.tex *.log *.aux *.png

