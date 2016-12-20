Appendix X: How was this document made?
=======================================

This document was written on Markdown, and converted to PDF
using Pandoc.

Process
-------
Document is written on Pandoc's extended Markdown, and can be broken amongst
different files. Images are inserted with regular Markdown syntax for images.
A YAML file with metadata information is passed to pandoc, containing things 
such as Author, Title, font, etc... The use of this information depends on
what output we are creating and the template/reference we are using.


Diagrams
--------
Diagrams are were created with LaTeX packages such as tikz or pgfgantt, they 
can be inserted directly as PDF, but if we desire to output to formats other
than LaTeX is more convenient to convert them to .png filesi with tools such
as `pdftoppm`.


References
------------
References are handled by pandoc-citeproc, we can write our bibliography in
a myriad of different formats: bibTeX, bibLaTeX, JSON, YAML, etc..., then
we reference in our markdown, and that reference works for multiple formats


