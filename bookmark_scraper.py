#!/usr/bin/env python
# -*- coding: utf-8 -*-

from enum import Enum
import bookmark_argparser
import file_utils
import msedge_utils
import mozffox_utils
import gchrome_utils
import brave_utils
import opera_utils

'''
NOTE: This file handles the execution of the bookmark_scraper python tool.

'''


#######################################################################################
#       GLOBALS
#######################################################################################
class BrowserTypes(Enum):
    Microsoft_Edge = 0
    Mozilla_Firefox = 1
    Google_Chrome = 2
    Brave_Browser = 3
    Opera_Browser = 4
    Exception_ = -1
    
BROWSERTYPE_FUNCTIONS:tuple = (msedge_utils.bookmark_scrape, mozffox_utils.bookmark_scrape, gchrome_utils.bookmark_scrape, brave_utils.bookmark_scrape, opera_utils.bookmark_scrape, )
#######################################################################################



#######################################################################################
#       MAIN
#######################################################################################
def main() -> None:
    args:object = bookmark_argparser.load_parser()

    try:
        #browser
        browser_strings:dict = file_utils.read_json("./json/browser_strings.json")
        browser_arg:str = args.browsername.lower()
        browser:str = browser_strings["supported_browsers"][browser_arg]
        
        #export filepath
        export_file:str = args.exportfile.lower()
        if(not(export_file.endswith(r'.bin'))):
            export_file += '.bin'

    except Exception as e: 
        msg:str = f"Bad arguments...{chr(0x0a)}{chr(0x09)}--browsername: {args.browsername}{ chr(0x0a)}{chr(0x09)}--exportfile: {args.exportfile}"
        browser:str = "Exception_"
    
    else: msg:str = f"Collecting bookmarks from {browser}..."

    finally:
        print(f'{chr(0x0a)}MSG: {msg}')
        match(browser):

            case BrowserTypes.Microsoft_Edge.name:
                result:str = BROWSERTYPE_FUNCTIONS[BrowserTypes.Microsoft_Edge.value](export_file= export_file)

            case BrowserTypes.Mozilla_Firefox.name:
                result:str = BROWSERTYPE_FUNCTIONS[BrowserTypes.Mozilla_Firefox.value](export_file= export_file)

            case BrowserTypes.Google_Chrome.name:
                result:str = BROWSERTYPE_FUNCTIONS[BrowserTypes.Google_Chrome.value](export_file= export_file)

            case BrowserTypes.Brave_Browser.name:
                result:str = BROWSERTYPE_FUNCTIONS[BrowserTypes.Brave_Browser.value](export_file= export_file)

            case BrowserTypes.Opera_Browser.name:
                result:str = BROWSERTYPE_FUNCTIONS[BrowserTypes.Opera_Browser.value](export_file= export_file)

            case BrowserTypes.Exception_.name:
                result:str = "Unsupported Browser. Please check your parameters."

            case default:
                result:str = "An UNDEFINED ERROR has occured. Unsuccessful export"

    print(f'{chr(0x0a)}RESULT: {result}{chr(0x0a)}')
#######################################################################################



if __name__ == "__main__":
    main()
