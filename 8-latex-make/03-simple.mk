buildsystem.pdf : buildsystem.tex \
					date_downloaded.tex \
					playcount.pdf top_artists.csv
	latexmk -gg -pdf buildsystem.tex

top_artists.csv : top_artists.json
	./parse_charts.py top_artists.csv

playcount.pdf : top_artists.json
	./parse_charts.py playcount.pdf

top_artists.json date_downloaded.tex : download_charts.sh
	./download_charts.sh

clean : 
	rm -f *.log *.aux *.pdf *.blg *.bbl

extraclean : clean
	rm -f buildsystem.pdf top_artists.jsonrm date_downloaded playcount.pdf top_artists.csv