# **BookmarkScraper**
### *type: console application*

## ***Whats New?***
- *Integrated support for Brave Browser*
- *Integrated support for Opera Browser*

## DESCRIPTION
Windows
Collects bookmarks and exports the URL's and title of the url to a .bin file which can be saved on a USB for portability, or to another pc, vm, etc. This is a commandline tool. The purpose of this tool is to give ease to gathering bookmarks to transfer to other machines without signing into browsers and/ or syncing data. This tool accepts arguments from stdin. If cmdline arguments are not passed, the application will provide defaults values which are; the native Windows OS browser which is ***Microsoft Edge*** and ***bookmark_exports.bin*** which will be found in the calling directory. 

## ABOUT
  ### ***Supported Browser***
  - Microsoft Edge
  - Mozilla Firefox
  - Google Chrome
  - Brave Browser
  - Opera_browser

  ### ***Coming soon***
  - Tor Browser
  - Duck Duck Go

  ### ***Usage***
```
usage: python boomark_scraper.py  [-h] [--browsername BROWSERNAME] [--exportfile EXPORTFILE]                                                                               

Collect local browser bookmarks and export them to a .bin file for easy mobility of bookmarked sites without the hassle of signing into or syncing your browsers.
Automatically handles duplicates so each url entry stays unique. Currently supports EDGE, FIREFOX, CHROME browsers.

 options:
  -h, --help            show this help message and exit
  --browsername BROWSERNAME, -B BROWSERNAME
                        Name of the browser you wish to collect the bookmarks from i.e. edge, firefox, etc. If omitted, default value is Edge as it is windows native
                        browser. - (currently supports edge, firefox, chrome, brave, opera, )
  --exportfile EXPORTFILE, -E EXPORTFILE
                        Filepath to the export file which to save the bookmarks saves as .bin file. Creates file or appends to an existing file. If omitted, default
                        value is bookmark_exports.bin which will be created within the same directory as this tool.

Visit https://github.com/Node0o1/BookmarkScraper/ for more information.
```

  ### ***Example***
- stdin
```bash
python .\bookmark_scraper.py --browser edge --exportfile ./edgetest.bin                       
```

- output
```
MSG: Collecting bookmarks from Microsoft_Edge...
RESULT: Successful Export to ./edgetest.bin
```


