import os
import file_utils

'''
NOTE: This file is related to procedures and processes in which bookmarks are collected from Opera Browser.
'''
    
def bookmark_scrape(export_file:str) -> str:
    browser_path:str = f'\x43\x3a\x2f\x55\x73\x65\x72\x73\x2f{os.getlogin()}\x2f\x41\x70\x70\x44\x61\x74\x61\x2f\x52\x6f\x61\x6d\x69\x6e\x67\x2f\x4f\x70\x65\x72\x61\x20\x53\x6f\x66\x74\x77\x61\x72\x65\x2f\x4f\x70\x65\x72\x61\x20\x53\x74\x61\x62\x6c\x65\x2f\x44\x65\x66\x61\x75\x6c\x74\x2f\x42\x6f\x6f\x6b\x6d\x61\x72\x6b\x73'
    try: bookmarks:list = file_utils.json_bookmark_parser(browser_path= browser_path)
    except: return "Opera Browser files not found."
    else: return file_utils.write(export_file= export_file, bookmarks= bookmarks)