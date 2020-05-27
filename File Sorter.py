import os
import shutil

src = '/Users/jalonthomas/Desktop/Sorter'

#Dictionary of folders with their corresponding paths and suffixes
dict = {
    'word': {'path': '/Users/jalonthomas/Desktop/Sorted Files/Word', 'suffixes': ('.docx', '.pdf', '.doc')},
    'excel': {'path':'/Users/jalonthomas/Desktop/Sorted Files/Excel', 'suffixes': ('.csv', '.rtf', '.xlsx')},
    'image': {'path': '/Users/jalonthomas/Desktop/Sorted Files/Images', 'suffixes': ('.png', '.PNG', '.jpg', '.JPG', '.jpeg', '.JPEG', '.gif')},
    'video': {'path': '/Users/jalonthomas/Desktop/Sorted Files/Videos', 'suffixes': ('.mp4','.mp3', '.wav', '.mov')},
    'powerpoint': {'path': '/Users/jalonthomas/Desktop/Sorted Files/PPT', 'suffixes': ('.pptx')},
    'game': {'path': '/Users/jalonthomas/Desktop/Sorted Files/Games', 'suffixes': ('.nds')},
    'folder': {'path': '/Users/jalonthomas/Desktop/Sorted Files/Folders', 'suffixes': ()},
    'misc': {'path': '/Users/jalonthomas/Desktop/Sorted Files/Misc', 'suffixes': ()}
} 

files = os.listdir(src)

#Check file suffix and return corresponding path
def getPath(f):
    if os.path.isdir(os.path.join(src, f)):
        return dict['folder']['path']
    else:
       for key in dict:
           if f.endswith(dict[key]['suffixes']):
               return dict[key]['path']

    return dict['misc']['path']

#Iterate through all non-hidden files and place them in correct folder according to type
for f in files:
    if not f.startswith('.'):
        shutil.move(os.path.join(src, f), getPath(f))


