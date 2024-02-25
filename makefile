CC=cc
TMP=iso tgz aux log toc fls fdb_latexmk xml out synctex.gz

doc:
	@latexmk -pdf -auxdir=tmp/ -shell-escape -cd Report.tex
	@libreoffice --convert-to pdf front_page.docx
	@gs -dNOPAUSE -sDEVICE=pdfwrite -sOUTPUTFILE=SC-Report.pdf -dBATCH front_page.pdf Report.pdf

clean:
	@echo "Removing misc files ..."
	@for i in $(TMP) ; do find . -name "*.$$i" -delete ; done
	@rm -rf tmp doc/_minted* *.log
	@echo "Removed misc files ..."

.PHONY:	doc
