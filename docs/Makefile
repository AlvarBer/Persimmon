PDF := persimmon.pdf  # PDF Main Target
MARKDOWN := introduction.md state_of_the_art.md workflow.md objectives.md \
	risk_analysis.md implementation.md postmortem.md  # Markdown files
MARKDOWN_COMPLUTENSE := introduction.md focus.md state_of_the_art.md \
	workflow.md objectives.md risk_analysis.md implementation.md postmortem.md
METADATA := metadata.yaml  # Metadata files (Author, Date, Title, etc..)
BIBLIOGRAPHY := persimmon.bib  # BibLaTeX bibliography
CSL := emerald-harvard.csl  # CSL file used for citations
TEMPLATE := template.tex  # LaTeX template for producing PDF

GRAPHS := $(wildcard graphs/*.tex)  # Latex diagrams
IMAGES := $(wildcard images/*.png)  # .png images
IMAGES += $(addprefix images/, $(notdir $(GRAPHS:.tex=.pdf)))  # Generated PDF Images

all: $(PDF)


$(PDF): $(MARKDOWN) $(METADATA) $(TEMPLATE) $(IMAGES) $(BIBLIOGRAPHY) $(CSL)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) --table-of-contents \
		--top-level-division chapter --metadata sansfont:"Helvetica Neue LT Com" \
		$(METADATA) $(MARKDOWN) -o $@

travis: $(MARKDOWN) $(METADATA) $(TEMPLATE) $(IMAGES) $(BIBLIOGRAPHY) $(CSL)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) --table-of-contents \
		--chapters $(METADATA) $(MARKDOWN) -o $(PDF)

complutense: $(MARKDOWN) $(METADATA) $(TEMPLATE) $(IMAGES) $(BIBLIOGRAPHY) $(CSL)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) --table-of-contents \
		--top-level-division chapter --metadata titlepic:images/fdi.png \
		--metadata sansfont:"Helvetica Neue LT Com" \
		--metadata title:"A visual interface for scikit-learn" \
		--metadata date:"Director: Pablo Moreno Ger" \
		$(METADATA) $(MARKDOWN) -o $(PDF)

twocol: $(MARKDOWN) $(METADATA) $(TEMPLATE) $(IMAGES) $(BIBLIOGRAPHY) $(CSL)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) --table-of-contents \
		--top-level-division chapter --metadata classoption:twocolumn \
		--metadata sansfont:"Helvetica Neue LT Com" \
		$(METADATA) $(MARKDOWN) -o $(PDF)

# For standalone images
images/%.pdf: graphs/%.tex
	xelatex $< > /dev/null
	mv $*.pdf images/


clean:
	rm -f images/*.pdf $(PDF) *.log *.aux

