top_artists.json date_downloaded.tex : download_charts.sh
	./download_charts.sh

playcount.pdf : top_artists.json
	./parse_charts.py playcount.pdf

top_artists.csv : top_artists.json
	./parse_charts.py top_artists.csv

buildsystem.aux : buildsystem.tex playcount.pdf top_artists.csv
	pdflatex buildsystem.tex

buildsystem.pdf : buildsystem.tex buildsystem.aux buildsystem.bbl \
					date_downloaded.tex \
					playcount.pdf top_artists.csv
	pdflatex buildsystem.tex
	pdflatex buildsystem.tex

buildsystem.bbl : buildsystem.tex literature.bib
	bibtex buildsystem

clean : 
	rm -f *.log *.aux *.pdf *.blg *.bbl

extraclean : clean
	rm -f buildsystem.pdf top_artists.jsonrm date_downloaded playcount.pdf top_artists.csv