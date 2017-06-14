PDF := persimmon.pdf  # PDF Default Target
MARKDOWN := introduction.md literature.md workflow.md milestones.md \
	risk.md interface.md implementation.md types.md \
	evaluation.md postmortem.md  # Markdown files
MARKDOWN_COMPLU := introduction.md introduccion.md focus.md literature.md \
	workflow.md milestones.md risk.md interface.md implementation.md \
	types.md analysis.md evaluation.md postmortem.md
APPENDICES := packages.md how.md eval_form.md # Appendix after bibliography
METADATA := metadata.yaml  # Metadata files (Author, Date, Title, etc..)
BIBLIOGRAPHY := persimmon.bib  # BibLaTeX bibliography
CSL := emerald-harvard.csl  # CSL file used for citations
TEMPLATE := template.tex  # LaTeX template for producing PDF

# Add src prefix to markdown files
MARKDOWN := $(addprefix src/, $(MARKDOWN))
MARKDOWN_COMPLU := $(addprefix src/, $(MARKDOWN_COMPLU))
APPENDICES := $(addprefix src/, $(APPENDICES))

GRAPHS := $(wildcard graphs/*.tex)  # Latex diagrams
IMAGES := $(wildcard images/*.png)  # .png images
# Generated PDF Images
IMAGES += $(addprefix images/, $(notdir $(GRAPHS:.tex=.pdf)))

# Intermediate tex files required for appending after bibliography
APPENDIX := appendix.tex

all: $(PDF)

# Default pdf, no information about university, no extra complutense chapters,
# no cool font
$(PDF): $(MARKDOWN) $(APPENDIX) $(TEMPLATE) $(IMAGES) $(BIBLIOGRAPHY) $(CSL) $(METADATA)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) --table-of-contents \
		--top-level-division chapter --highlight-style breezedark \
		--include-in-header question.tex \
		$(METADATA) $(MARKDOWN) --include-after-body $(APPENDIX) -o $@

# Hertfordshire digital submission
herts: $(MARKDOWN) $(APPENDIX) $(TEMPLATE) $(IMAGES) $(BIBLIOGRAPHY) $(CSL) $(METADATA)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) --table-of-contents \
		--top-level-division chapter --highlight-style breezedark \
		--include-in-header question.tex \
		--metadata geometry:top=2.5cm,left=4cm,right=2.5cm,bottom=2.5cm \
		--metadata sansfont:"Helvetica Neue LT Com" \
		--metadata institute:"University of Hertfordshire" \
		--metadata school:"School of Computer Science" \
		--metadata degree:"Modular BSc Honours in Computer Science" \
		--metadata degreecode:"6COM1054 - Artificial Intelligence Project" \
		--metadata supervisor:"Dr.Mariana Lilley" \
		$(METADATA) $(MARKDOWN) --include-after-body $(APPENDIX) \
		-o persimmon_herts.pdf

# Hertfordshire print submission
herts_print: $(MARKDOWN) $(TEMPLATE) $(IMAGES) $(BIBLIOGRAPHY) $(CSL) $(METADATA)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) --table-of-contents \
		--top-level-division chapter --highlight-style breezedark \
		--metadata geometry:top=2.5cm,left=4cm,right=2.5cm,bottom=2.5cm \
		--metadata sansfont:"Helvetica Neue LT Com" \
		--metadata institute:"University of Hertfordshire" \
		--metadata school:"School of Computer Science" \
		--metadata degree:"Modular BSc Honours in Computer Science" \
		--metadata degreecode:"6COM1054 - Artificial Intelligence Project" \
		--metadata supervisor:"Dr.Mariana Lilley" \
		$(METADATA) $(MARKDOWN) -o persimmon_herts_print.pdf

# Complutense digital submission
complu: $(MARKDOWN_COMPLU) $(APPENDIX) $(TEMPLATE) $(IMAGES) $(BIBLIOGRAPHY) $(CSL) $(METADATA)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) --table-of-contents \
		--top-level-division chapter --highlight-style breezedark \
		--include-in-header question.tex \
		--metadata sansfont:"Helvetica Neue LT Com" \
		--metadata institute:"Universidad Complutense" \
		--metadata school:"Facultad de Informática" \
		--metadata degree:"Computer Engineering" \
		--metadata degreecode:"Tecnología Específica de Computación" \
		--metadata supervisor:"Manuel Freire Moran" \
		--metadata cosupervisor:"Pablo Moreno Ger" \
		--metadata titlepic:images/fdi.png $(METADATA) $(MARKDOWN_COMPLU) \
		--include-after-body $(APPENDIX) -o persimmon_complu.pdf

# For standalone images
images/%.pdf: graphs/%.tex
	xelatex $< > /dev/null
	@mv $*.pdf images/
	@rm -f $*.log $*.aux

# Appendices
$(APPENDIX): $(APPENDICES)
	pandoc --smart --no-tex-ligatures --top-level-division chapter $(APPENDICES) -o $@

# Travis generation, only necessary because travis version of pandoc is old.
APPENDIX_TRAVIS := appendix_travis.tex

travis: $(MARKDOWN) $(APPENDIX_TRAVIS) $(TEMPLATE) $(IMAGES) $(BIBLIOGRAPHY) $(CSL) $(METADATA)
	pandoc --smart --standalone --latex-engine xelatex --template $(TEMPLATE) \
		--bibliography $(BIBLIOGRAPHY) --csl $(CSL) --table-of-contents \
		--chapters --highlight-style espresso \
		--include-in-header question.tex \
		$(METADATA) $(MARKDOWN) --include-after-body $(APPENDIX_TRAVIS) \
		-o $(PDF)

$(APPENDIX_TRAVIS): $(APPENDICES)
	pandoc --no-tex-ligatures --chapters $(APPENDICES) -o $@


clean:
	rm -f images/*.pdf *.pdf *.log *.aux appendix*

