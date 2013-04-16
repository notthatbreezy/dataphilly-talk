import nltk
from readability.readability import Document
import os
import sys

def clean_html_directory(source_directory, target_directory):
    """Retains only relevant article text from articles in
    source directory and saves text only files in targe directory.
    
    Arguments:
    - `source_directory`: directory with .html files
    - `target_directory`: directory to save files in
    """
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    html_files = os.listdir(source_directory)
    html_files.sort()
    print "Processing {0} files".format(len(html_files))
    for f in html_files:
        html = open(source_directory+f)
        html_text = html.read()
        relevant = Document(html_text).summary()
        cleaned = nltk.clean_html(relevant)
        # some reason carriage returns still there
        cleaned = cleaned.replace('&#13;', ' ')
        save_f = f.split('.')[0]
        output = open(target_directory+save_f, 'w')
        output.write(cleaned.encode('utf-8', 'ignore'))
        output.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Error: Expected source and target directory"
    else:
        clean_html_directory(sys.argv[1], sys.argv[2])
