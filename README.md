### Converts a BibTeX file to YAML formatBIB2YAML is a lightweight Python package that provides an easy and efficient way to convert BibTeX (.bib) files to YAML (.yaml) format.### Usage```python    # interactive    # path to the bib file    bib = '/Users/aj/Downloads/ref.bib'    # path to the output directory    outputDir = '/Users/aj/Downloads/'        # Run the function    bib2yaml (bib, outputDir, fileName='ref')        # commandline    python bib2yaml.py --bib /Users/aj/Downloads/ref.bib --outputDir /Users/aj/Downloads/    ```