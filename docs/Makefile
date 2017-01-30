PDF := persimmon.pdf  # PDF Main Target
MARKDOWN := introduction.md state_of_the_art.md workflow.md objectives.md \
	risk_analysis.md implementation.md postmortem.md  # Markdown files
BODY := body.tex  # Markdown files will be converted to this intermediate step
#APPENDICES := appendixX.md  # Markdown Appendices
#APPENDIX := appendix.tex  # And appendices to this intermediate step
#METADATA := metadata.yaml  # Metadata files (Author, Date, Title, etc..)
BIBLIOGRAPHY := persimmon.bib  # BibLaTeX bibliography
CSL := emerald-harvard.csl  # CSL file used for citations
TEMPLATE := template.tex  # LaTeX template for producing PDF

GRAPHS := $(wildcard graphs/*.tex)  # Latex diagrams
IMAGES := $(wildcard images/*.png)  # .png images
IMAGES += $(addprefix images/, $(notdir $(GRAPHS:.tex=.pdf)))  # Generated PDF Images

all: $(PDF)


$(PDF): $(BODY) $(APPENDIX) $(TEMPLATE) $(IMAGES) # TODO: Add abstract
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--metadata author:"Álvaro Bermejo" \
		--metadata date:"$(shell date +"%d/%m/%Y") ($(shell git describe --abbrev=0 --tags))" \
		--metadata title:Persimmon --metadata fontsize:12pt --toc \
		--metadata subtitle:"A sklearn visual programming interface" \
		--metadata mainlang:English --metada keywords:"Machine Learning","Visual Programming" \
		--metadata papersize:A4 --metadata sansfont:"Helvetica Neue LT Com" \
		--metadata colorlinks --metadata documentclass:scrreprt \
		--top-level-division chapter $(BODY) $(APPENDIX) -o $@

travis: $(BODY) $(APPENDIX) $(TEMPLATE) $(IMAGES)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--metadata author:"Álvaro Bermejo" --metadata papersize:A4 \
		--metadata date:"$(shell date +"%d/%m/%Y") ($(shell git describe --abbrev=0 --tags))" \
		--metadata title:Persimmon --metadata fontsize:12pt --toc \
		--metadata subtitle:"A sklearn visual programming interface" \
		--metadata mainlang:English --metada keywords:"Machine Learning","Visual Programming" \
		--metadata colorlinks --metadata documentclass:scrreprt \
		--chapters $(BODY) $(APPENDIX) -o $(PDF)

complutense: $(BODY) $(APPENDIX) $(TEMPLATE) $(IMAGES)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--metadata author:"Álvaro Bermejo" --metadata date:"Director: Pablo Moreno Ger" \
		--metadata title:Persimmon --metadata fontsize:12pt --toc \
		--metadata subtitle:"A scikitlearn visual programming interface" \
		--metadata mainlang:English --metadata colorlinks --metadata titlepic:graphs/fdi.png \
		--metadata papersize:A4 --metadata sansfont:"Helvetica Neue LT Com" \
		--metadata documentclass:scrreprt --metadata institute:"Universidad Complutense" \
		--top-level-division chapter $(BODY) $(APPENDIX) -o $(PDF)

twocol: $(BODY) $(APPENDIX) $(TEMPLATE) $(IMAGES)  # Adjust Spacing with geometry
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--metadata author:"Álvaro Bermejo" --metadata colorlinks \
		--metadata date:"$(shell date +"%d/%m/%Y") ($(shell git describe --abbrev=0 --tags))" \
		--metadata title:Persimmon --metadata fontsize:12p --toc \
		--metadata subtitle:"A sklearn visual programming interface" \
		--metadata mainlang:English --metada keywords:"Machine Learning","Visual Programming" \
		--metadata papersize:A4 --metadata classoption:twocolumn \
		--metadata sansfont:"Helvetica Neue LT Com" --metadata documentclass:scrreprt \
		--top-level-division chapter $(BODY) $(APPENDIX) -o $(PDF)

# For standalone images
images/%.pdf: graphs/%.tex
	xelatex $< > /dev/null # TODO: actually output in graphs directory
	mv $*.pdf images/

# Body and Appendices Middle Steps creation
$(BODY): $(MARKDOWN)
	pandoc --no-tex-ligatures --bibliography $(BIBLIOGRAPHY) --csl $(CSL) \
		metadata.yaml $(MARKDOWN) -o $@

$(APPENDIX): $(APPENDICES)
	pandoc --no-tex-ligatures $(APPENDICES) -o $@

clean:
	rm -f $(BODY) $(APPENDIX) images/*.pdf *.pdf *.log *.aux

