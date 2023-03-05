#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 20:58:50 2023
@author: Ajit Johnson Nirmal
Converts a BibTeX file to YAML format.
"""

# Libs
import bibtexparser
from pylatexenc.latex2text import LatexNodes2Text
import yaml
import argparse


# function
def bib2yaml (bib, outputDir, fileName='ref'):
    
    """
    Parameters
    ----------
    bib (str): The path to the BibTeX file to be converted.
    outputDir (str): The path where the YAML file will be saved.
    fileName (str): The name of the output file, without extension. Default is 'ref'.

    Returns
    -------
    None.
    
    Example
    -------
    ```python
    # interactive
    bib = '/Users/aj/Downloads/ref.bib'
    outputDir = '/Users/aj/Downloads/'
    bib2yaml (bib, outputDir, fileName='ref')
    
    # commandline
    python bib2yaml.py --bib /Users/aj/Downloads/ref.bib --outputDir /Users/aj/Downloads/
    
    ```

    """
    
    # resolve output path
    outputFile = outputDir + '/' + fileName + '.yml'
    lt = LatexNodes2Text()
    
    with open(bib) as f:
        db = bibtexparser.load(f)
    for e in db.entries:
        for k, v in e.items():
            e[k] = lt.latex_to_text(v)
            
    with open(outputFile, 'w') as f:
        yaml.dump(db.entries, f, allow_unicode=True)

    
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a BibTeX file to YAML format.')
    parser.add_argument('--bib', type=str, help='path to the BibTeX file to be converted')
    parser.add_argument('--outputDir', type=str, help='path where the YAML file will be saved')
    parser.add_argument('--fileName', type=str, default='ref', help='name of the output file, without extension (default: ref)')
    
    args = parser.parse_args()
    bib2yaml(bib=args.bib, 
             outputDir=args.outputDir, 
             fileName=args.fileName)


