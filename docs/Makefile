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

BODY := body.tex
APPENDIX := appendices.tex
APPENDICES := appendixA.md appendixB.md


all: $(PDF)

$(PDF): $(BODY) $(APPENDIX) $(TEMPLATE) $(IMAGES)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--table-of-contents --top-level-division chapter --metadata author:Álvaro \
		--metadata title:Persimmon \
		--metadata subtitle:"A sklearn visual programming interface" \
		--metadata date:2017-02-18 --metadata documentclass:scrreprt \
		--metadata sansfont:"Helvetica Neue LT Com" --metadata colorlinks \
		--metadata lof --metadata papersize:A4 --metadata fontsize:12pt \
		--metadata mainlang:English \
		--metadata keywords:"Machine Learning","Visual Programming" \
		$(BODY) $(APPENDIX) -o $@

travis: $(BODY) $(APPENDIX) $(TEMPLATE) $(IMAGES)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--table-of-contents --chapters --metadata author:Álvaro \
		--metadata title:Persimmon \
		--metadata subtitle:"A sklearn visual programming interface" \
		--metadata date:2017-02-18 --metadata documentclass:scrreprt \
		--metadata colorlinks --metadata lof --metadata papersize:A4 \
		--metadata fontsize:12pt --metadata mainlang:English \
		--metadata keywords:"Machine Learning","Visual Programming" \
		$(BODY) $(APPENDIX) -o $(PDF)

complutense: $(BODY_COMPLUTENSE) $(APPENDIX) $(TEMPLATE) $(IMAGES)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--table-of-contents --top-level-division chapter --metadata author:Álvaro \
		--metadata title:"A sklearn visual programming interface" \
		--metadata date:"Director: Pablo Moreno Ger" \
		--metadata documentclass:scrreprt \
		--metadata sansfont:"Helvetica Neue LT Com" --metadata colorlinks \
		--metadata lof --metadata papersize:A4 --metadata fontsize:12pt \
		--metadata mainlang:English \
		--metadata keywords:"Serious Learning","Machine Learning","Visual Programming" \
		--metadata titlepic:images/fdi.png
		$(BODY_COMPLUTENSE) $(APPENDIX) -o $(PDF)

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

$(BODY): $(MARKDOWN) $(BIBLIOGRAPHY) $(CSL)
	pandoc --no-tex-ligatures --top-level-division chapter --table-of-contents \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) \
		$(MARKDOWN) -o $@

$(BODY_COMPLUTENSE): $(MARKDOWN_COMPLUTENSE)

$(APPENDIX): $(APPENDICES)
	pandoc --no-tex-ligatures --top-level-division chapter $(APPENDICES) -o $@

# Complex creation


clean:
	rm -f images/*.pdf $(PDF) *.log *.aux $(BODY) $(APPENDIX)

