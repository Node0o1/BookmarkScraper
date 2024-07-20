import json
import sqlite3

'''
NOTE: This file relates to the procedure and process of writing and
reading files related to bookmark_scrape.py
'''

##########################################################################################################################################
#       GLOBALS
##########################################################################################################################################
bookmarks:list = list()

##########################################################################################################################################



##########################################################################################################################################
#       EXPORT FILE WRITE
##########################################################################################################################################
def write(export_file:str, bookmarks:list = None) -> str:
    '''Accepts the export filepath and a list of tuples in (title, url) format to write out'''
    
    try:
        with open(export_file, mode="ab+") as outfile:
            file_contents=outfile.read().split()
    except: raise FileExistsError.add_note("Invalid filepath. Please check the export path and try again.")
    else:        
        [file_contents.append(f'{name} - {bookmark_url}{chr(0x0a)}'.encode('utf-8')) if(not(f'{name} - {bookmark_url}{chr(0x0a)}'.encode('utf-8') in file_contents)) else None for name,bookmark_url in bookmarks]
        list.sort(file_contents)
        with open(export_file, mode='wb') as outfile:
            [outfile.write(line) for line in file_contents]
        outfile.close()
        return f"Successful Export to {export_file}."
    
##########################################################################################################################################
    


##########################################################################################################################################
#       READ JSON FILE
##########################################################################################################################################
def read_json(path:str) -> object:
    try:
        with open(path, "rb") as fhandle:
            return json.load(fhandle)
    except: raise FileExistsError

##########################################################################################################################################



##########################################################################################################################################
#       JSON PARSER (EDGE, CHROME,)
#####################################################################################################################################
def search_bookmarks(root:str) -> None:
    [search_bookmarks(child) if("children" in child) else bookmarks.append((child['name'], child['url'])) for child in root["children"]]
    
def json_bookmark_parser(browser_path:str) -> list:
    try: data:object = read_json(browser_path)
    except Exception as e: print(e.args)
    else: [search_bookmarks(root) for root in data["roots"].values()]
    finally: return bookmarks

##########################################################################################################################################



##########################################################################################################################################
#       SQLITE3 QUERY PARSE HANDLER (FIREFOX,)
##########################################################################################################################################
def sql_bookmark_scrape(browser_path:str, query:str) -> list:
    try:
        conn = sqlite3.connect(browser_path)
        cursor = conn.cursor()
        cursor.execute(query)
        bookmarks = cursor.fetchall()
        conn.close()
    except conn.DatabaseError as e: print(e.args)
    return bookmarks

##########################################################################################################################################
