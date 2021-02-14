import sys
import os
import re

PATH_START_STR = "c:/"

DEFAULT_FILE_PATH = os.path.join( PATH_START_STR, "Users", "Hayden Woods", "Desktop", "time.txt")




def addHours(data):
    """
      Add array of numbers up, convert minutes into hours.
      If number of remaining minutes is over 30 add extra hour.
    """
    total_minutes = 0
    for section in data:
        total_minutes = total_minutes+  int(section)
    hour_tuple = divmod(total_minutes, 60)
    hours = hour_tuple[0]
    if hour_tuple[1] > 30:
        hours = hours + 1
    return hours

def readParseFile(file):
    """
      Read file and then santitize off any characters that are not digits or commas
      Split into list and return.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        data = f.read()
    
    sanatized = re.sub("[^0-9,]", "", data )
    split_data = sanatized.split(',')
    return split_data



if __name__ == "__main__":
    file_path = DEFAULT_FILE_PATH
    if len(sys.argv) > 1:
        path_arr = []
        for path in sys.argv[1:]:
            path_arr.append(path)
        file_path = os.path.join(PATH_START_STR, *path_arr)
    
    data = readParseFile(file_path)
    hours = addHours(data)
    print(hours)

    


