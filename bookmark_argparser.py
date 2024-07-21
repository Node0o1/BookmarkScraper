import argparse

'''
NOTE: This file is the cmdline argument parser for bookmark_scrape.py
'''

def load_parser() -> object:
    parser = argparse.ArgumentParser(
    prog= "python boomark_scraper.py ",
    description= 'Collect local browser bookmarks and export them to a .bin file for easy mobility of bookmarked sites without the hassle of signing into or syncing your browsers. Automatically handles duplicates so each url entry stays unique. Currently supports EDGE, FIREFOX, CHROME browsers.',
    epilog= "Visit github at https://github.com/Node0o1/BookmarkScraper/ for more information"
    )

    ###Browser Parser
    parser.add_argument(
        "--browsername", 
        '-B',  
        type= str, 
        dest= "browsername",
        default= "edge",
        help= "Name of the browser you wish to collect the bookmarks from i.e. edge, firefox, chrome. If omitted, default value is Edge as it is windows native browser. - (currently supports edge, firefox, chrome, brave)"
    )

    parser.add_argument(
        "--exportfile", 
        '-E', 
        dest= "exportfile",
        type= str, 
        default= "./bookmark_exports.bin", 
        help= "Filepath to the export file which to save the bookmarks saves as .bin file. Creates file or appends to an existing file. If omitted, default value is bookmark_exports.bin which will be created within the same directory as this tool."
    )

    args= parser.parse_args()
    return args
    
