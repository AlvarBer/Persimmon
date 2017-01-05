PDF := persimmon.pdf  # PDF Main Target
MARKDOWN := introduction.md state_of_the_art.md objectives.md risk_analysis.md \
	# Markdown files
BODY := body.tex  # Markdown files will be converted to this intermediate step
APPENDICES := appendixX.md  # Markdown Appendices
APPENDIX := appendix.tex  # And appendices to this intermediate step
#METADATA := metadata.yaml  # Metadata files (Author, Date, Title, etc..)
BIBLIOGRAPHY := persimmon.bib  # BibLaTeX bibliography
CSL := emerald-harvard.csl  # CSL file used for citations
TEMPLATE := template.tex  # LaTeX template for producing PDF

GRAPHS := $(wildcard graphs/*.tex)  # Latex diagrams
IMAGES := $(wildcard graphs/*.png)  # .png images
IMAGES += $(GRAPHS:.tex=.pdf)  # Generated PDF Images

all: $(PDF)

$(PDF): $(BODY) $(APPENDIX) $(TEMPLATE) $(IMAGES)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--metadata author:"Álvaro Bermejo" --metadata date:"01-01-2017" \
		--metadata title:"Persimmon" --metadata fontsize:"12pt" \
		--metadata subtitle:"A sklearn visual programming interface" --toc \
		--metadata version:"0.2" --metadata mainlang:"English" \
		--metadata papersize:"A4" --metadata sansfont:"Helvetica Neue LT Com" \
		--metadata colorlinks:"yes" --metadata documentclass:"scrreprt" \
		--metadata institure:"University of Hertfordshire/Universidad Complutense" \
		--top-level-division chapter $(BODY) $(APPENDIX) -o $@

travis: $(BODY) $(APPENDIX) $(TEMPLATE) $(IMAGES)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--metadata author:"Álvaro Bermejo" --metadata date:"01-01-2017" \
		--metadata title:"Persimmon" --metadata fontsize:"12pt" \
		--metadata subtitle:"A sklearn visual programming interface" --toc \
		--metadata version:"0.2" --metadata mainlang:"English" \
		--metadata papersize:"A4" --metadata sansfont:"Helvetica Neue LT Com" \
		--metadata colorlinks:"yes" --metadata documentclass:"scrreprt" \
		--metadata institure:"University of Hertfordshire/Universidad Complutense" \
		--chapters $(BODY) $(APPENDIX) -o $(PDF)

# For standalone images 
graphs/%.pdf: graphs/%.tex
	xelatex $< > /dev/null # TODO: actually output in graphs directory
	mv $*.pdf graphs/


$(BODY): $(MARKDOWN) $(IMAGES_PDF)
	pandoc --no-tex-ligatures --bibliography $(BIBLIOGRAPHY) --csl $(CSL) \
		$(MARKDOWN) -o $@

$(APPENDIX): $(APPENDICES)
	pandoc --no-tex-ligatures $(APPENDICES) -o $@

clean:
	rm -f $(BODY) $(APPENDIX) graphs/*.pdf *.pdf *.log *.aux

