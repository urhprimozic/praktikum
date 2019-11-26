#!/usr/bin/env sh

fn_download=top_artists.json
fn_date=date_downloaded.tex

api_key='cfac3d1b559cc3fc9bce3c896275c052'
api_root='http://ws.audioscrobbler.com/2.0/'
xml='?method=chart.gettopartists&api_key='"$api_key"
json="${xml}&format=json"

curl -o $fn_download "${api_root}${json}"

date '+\newcommand{\datedownloaded}{\formatdate{%d}{%m}{%Y}}' > $fn_date
