dataphilly-talk
===============

Example Code for Data Philly Talk given on 04/16/2013 on Natural Language Toolkit and natural language processing.

Slides can be found at my website - http://cmbrown.org/static/media/dataphilly.html

# Requirements
Originally this was developed using the [Anaconda python distribution](https://store.continuum.io/cshop/anaconda) available for free from Continuum Analytics. This is a python distribution with all the key libraries for scientific computing already included.

There is one requirement to install on Anaconda (the readability package for stripping irrelevant html from webpages):

- `conda pip install readability-lxml`

If working from your own python distribution locally or in a virtual environment you will need to install the dependencies above in addition to nltk, numpy, and scipy.

# Description of Files

- `getting_started.py` - basic examples using some NLTK tools

- `scraping.py` - Pulls down articles on front page of memeorandum -- will replace everything in the `memeorandum_pages` directory

- `process_memeorandum_pages.py` - strips html from webpages, writes to directory. Takes 2 command line arguments, source directory (directory with html files) and target directory (where to save plain text files)

- `pre_process_funcs.py` - helper functions for pre-processing text

- `cluster_memeorandum.py` - does the actual clustering using scikit-learn

- `extract_entities.py` - Example of how you might extract entities from news articles
