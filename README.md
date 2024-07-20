# **BookmarkScraper**
### *type: console application*

## DESCRIPTION
Collects bookmarks from local browsers for easy transfer with hassle of signing in or syncing. Exports .bin file which can be saved on a USB for portability. This is a commandline tool.

## ABOUT
> usage: python boomark_scraper.py  [-h] [--browsername BROWSERNAME] [--exportfile EXPORTFILE]                                                                               
>
> Collect local browser bookmarks and export them to a .bin file for easy mobility of bookmarked sites without the hassle of signing into or syncing your browsers.
> Automatically handles duplicates so each url entry stays unique. Currently supports EDGE, FIREFOX, CHROME browsers.
>
>  options:
>   -h, --help            show this help message and exit
>   --browsername BROWSERNAME, -B BROWSERNAME
>                         Name of the browser you wish to collect the bookmarks from i.e. edge, firefox, chrome. If omitted, default value is Edge as it is windows native
>                         browser. - (currently supports edge, firefox, chrome,)
>   --exportfile EXPORTFILE, -E EXPORTFILE
>                         Filepath to the export file which to save the bookmarks saves as .bin file. Creates file or appends to an existing file. If omitted, default
>                         value is bookmark_exports.bin which will be created within the same directory as this tool.
>
> Visit [Github](https://github.com/Node0o1/BookmarkScraper/) for more information.

### EXAMPLE
- stdin
```bash
python .\bookmark_scraper.py --browser edge --exportfile ./edgetest.bin                       
```

- output
```
MSG: Collecting bookmarks from Microsoft_Edge...
RESULT: Successful Export to ./edgetest.bin
```


