#!/usr/bin/env python

import sys,os
import json
import csv
import matplotlib.pyplot as plt
from matplotlib import rc

FN_IN = 'top_artists.json'
FN_PLOT = 'playcount.pdf'
FN_CSV = 'top_artists.csv'
MAX_ARTISTS_PLOT = 10
MAX_ARTISTS_CSV = 25

def write_csv(fieldnames, rows, directory, filename):
    '''Write a CSV file to directory/filename. The fieldnames must be a list of
    strings, the rows a list of dictionaries each mapping a fieldname to a
    cell-value.'''
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, filename)
    with open(path, mode='w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
    return None


def parse_json() :
    with open(FN_IN, mode='r', encoding='utf-8') as f :
        artists_json = json.load(f)

    j_data = artists_json['artists']['artist']
    artists = [ {'name' : x['name'], 'playcount' : int(x['playcount']),
                    'listeners' : int(x['listeners'])} for x in j_data ]
    return artists

def json_to_csv (artists) :
    write_csv(artists[0].keys(),
              artists,
              '.', FN_CSV)

def plot_playcount (artists, fn_out) :
    names = [a['name'] for a in artists]
    values = [a['playcount'] / 1000_000 for a in artists]
    plt.rcParams.update({'figure.autolayout': True})
    plt.figure()                # figsize=(20,3)
    plt.bar(names, values)
    plt.xticks(rotation=45, horizontalalignment='right')
    # plt.show()
    plt.ylabel('Playcount (millions)')
    plt.savefig(fn_out)


if __name__ == '__main__' :
    artists = parse_json()
    artists = sorted(artists, key=lambda x: x['playcount'], reverse=True)
    def failwith(msg):
        print("{}.\nCall as {} ({}|{})".format(msg, sys.argv[0], FN_PLOT, FN_CSV))
        exit(1)
    if len(sys.argv) < 2 :
        failwith('Not enough arguments')
    if sys.argv[1] == FN_PLOT :
        # rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
        ## for Palatino and other serif fonts use:
        rc('font',**{'family':'serif','serif':['Palatino']})
        rc('text', usetex=True)
        plot_playcount(artists[:MAX_ARTISTS_PLOT], FN_PLOT)
    elif sys.argv[1] == FN_CSV :
        json_to_csv(artists[:MAX_ARTISTS_CSV])
    else :
        failwith('Unknown argument: {}'.format(sys.argv[1]))
