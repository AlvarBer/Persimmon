PDF := persimmon.pdf  # PDF Main Target
MARKDOWN := introduction.md literature.md workflow.md milestones.md \
	risk.md interface.md implementation.md types.md \
	evaluation.md postmortem.md  # Markdown files
MARKDOWN_COMPLUTENSE := introduction.md focus.md literature.md \
	workflow.md milestones.md risk.md interface.md implementation.md \
	types.md analysis.md postmortem.md
APPENDICES := packages.md how.md eval_form.md # Appendix after bibliography
METADATA := metadata.yaml  # Metadata files (Author, Date, Title, etc..)
BIBLIOGRAPHY := persimmon.bib  # BibLaTeX bibliography
CSL := emerald-harvard.csl  # CSL file used for citations
TEMPLATE := template.tex  # LaTeX template for producing PDF

# Add src prefix to markdown files
MARKDOWN := $(addprefix src/, $(MARKDOWN))
MARKDOWN_COMPLUTENSE := $(addprefix src/, $(MARKDOWN_COMPLUTENSE))
APPENDICES := $(addprefix src/, $(APPENDICES))

GRAPHS := $(wildcard graphs/*.tex)  # Latex diagrams
IMAGES := $(wildcard images/*.png)  # .png images
# Generated PDF Images
IMAGES += $(addprefix images/, $(notdir $(GRAPHS:.tex=.pdf)))

# Intermediate tex files required for appending after bibliography
APPENDIX := appendix.tex

all: $(PDF)

$(PDF): $(MARKDOWN) $(APPENDIX) $(TEMPLATE) $(IMAGES) $(BIBLIOGRAPHY) $(CSL) $(METADATA)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) --table-of-contents \
		--top-level-division chapter --highlight-style breezedark \
		--include-in-header question.tex \
		--metadata geometry:top=2.5cm,left=4cm,right=2.5cm,bottom=2.5cm \
		--metadata date:"$(shell date +%Y/%m/%d)" \
		--metadata sansfont:"Helvetica Neue LT Com" \
		$(METADATA) $(MARKDOWN) --include-after-body $(APPENDIX) -o $@

hertfordshire: $(MARKDOWN) $(TEMPLATE) $(IMAGES) $(BIBLIOGRAPHY) $(CSL) $(METADATA)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) --table-of-contents \
		--top-level-division chapter --highlight-style breezedark \
		--include-in-header question.tex \
		--metadata geometry:top=2.5cm,left=4cm,right=2.5cm,bottom=2.5cm \
		--metadata sansfont:"Helvetica Neue LT Com" \
		$(METADATA) $(MARKDOWN) -o pandoc_herts.pdf


complutense: $(MARKDOWN_COMPLUTENSE) $(APPENDIX) $(TEMPLATE) $(IMAGES) $(BIBLIOGRAPHY) $(CSL) $(METADATA)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) --table-of-contents \
		--top-level-division chapter --highlight-style breezedark \
		--metadata title:"A scikit-learn visual programming interface" \
		--metadata date:"Director:Manuel Freire Moran, Codirector: Pablo Moreno Ger" \
		--metadata sansfont:"Helvetica Neue LT Com" --metadata keywords:"Serious Learning","Visual Programming","Dataflow Programming" \
		--metadata titlepic:images/fdi.png $(METADATA) $(MARKDOWN_COMPLUTENSE) \
		--include-after-body $(APPENDIX) -o $(PDF)

# For standalone images
images/%.pdf: graphs/%.tex
	xelatex $< > /dev/null
	@mv $*.pdf images/
	@rm -f $*.log $*.aux

$(APPENDIX): $(APPENDICES)
	pandoc --smart --no-tex-ligatures --top-level-division chapter $(APPENDICES) -o $@

# Travis generation, only necessary because travis version of pandoc is old.
APPENDIX_TRAVIS := appendix_travis.tex

travis: $(MARKDOWN) $(APPENDIX_TRAVIS) $(TEMPLATE) $(IMAGES) $(BIBLIOGRAPHY) $(CSL) $(METADATA)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) --table-of-contents \
		--chapters --highlight-style breezedark \
		--metadata date:"$(shell date +%Y/%m/%d)" \
		$(METADATA) $(MARKDOWN) --include-after-body $(APPENDIX_TRAVIS) \
		-o $(PDF)

$(APPENDIX_TRAVIS): $(APPENDICES)
	pandoc --no-tex-ligatures --chapters $(APPENDICES) -o $@


clean:
	rm -f images/*.pdf $(PDF) *.log *.aux appendix*

