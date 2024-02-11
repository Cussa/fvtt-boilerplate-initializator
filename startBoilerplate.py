import os
import re
import sys
import urllib.request
import zipfile
import shutil
from distutils.dir_util import copy_tree

args = sys.argv

dryRun = len(args) > 1 and args[1].lower() == "true"
folder = os.getcwd()
folderPrintIndex = folder.rfind("/")
folderPrint = folder[folderPrintIndex:]

os.system("clear")
print(f"""
  _____                     _              ____        _ _                 _       _         ___       _ _   _       _ _          _             
 |  ___|__  _   _ _ __   __| |_ __ _   _  | __ )  ___ (_) | ___ _ __ _ __ | | __ _| |_ ___  |_ _|_ __ (_) |_(_) __ _| (_)______ _| |_ ___  _ __ 
 | |_ / _ \| | | | '_ \ / _` | '__| | | | |  _ \ / _ \| | |/ _ \ '__| '_ \| |/ _` | __/ _ \  | || '_ \| | __| |/ _` | | |_  / _` | __/ _ \| '__|
 |  _| (_) | |_| | | | | (_| | |  | |_| | | |_) | (_) | | |  __/ |  | |_) | | (_| | ||  __/  | || | | | | |_| | (_| | | |/ / (_| | || (_) | |   
 |_|  \___/ \__,_|_| |_|\__,_|_|   \__, | |____/ \___/|_|_|\___|_|  | .__/|_|\__,_|\__\___| |___|_| |_|_|\__|_|\__,_|_|_/___\__,_|\__\___/|_|   
                                   |___/                            |_|                                                                         

Created by: Cussa Mitre
    Discord: CussaMitre
    Github: https://github.com/Cussa
Dry run activate: {dryRun}
{"Changes will not be saved." if dryRun else "Changes will be saved to the files."}
All changes are case sensitive.
""")

if os.path.exists("system.json"):
    print("- system.json found! Will not download the boilerplate!")
else:
    print("- Downloading boilerplate system")
    urllib.request.urlretrieve("https://gitlab.com/asacolips-projects/foundry-mods/boilerplate/-/archive/master/boilerplate-master.zip", "boilerplate.zip")
    with zipfile.ZipFile("boilerplate.zip", 'r') as zip_ref:
        zip_ref.extractall(folder)
    copy_tree("boilerplate-master", folder)
    shutil.rmtree("boilerplate-master")
    os.remove("boilerplate.zip")

systemName = input("Replace Boilerplate by => ")
boilerplateLowercase = systemName.lower() # input("boilerplate => ")
boilerplateUppercase = systemName.upper() # input("BOILERPLATE => ")
boilerplateCapitalize = systemName.capitalize() # input("Boilerplate => ")

changes = {
    "boilerplate": boilerplateLowercase,
    "BOILERPLATE": boilerplateUppercase,
    "Boilerplate": boilerplateCapitalize,
}

skipList = [
    r".*/\.DS_Store.*",
    r".*\.git.*",
    r".*\.png.*",
    r".*/lib.*",
    r".*startBoilerplate\.py.*",
    r".*package-lock\.json.*"
]

def checkFileProcess(filepath):
    for pattern in skipList:
        if bool(re.match(pattern, filepath)):
            return False
    
    return True

def replaceInFile(filePath):
    # Read in the file
    with open(filePath, 'r') as file:
        filedata = file.read()

    # Replace the target string
    newFileData = filedata
    for source, destiny in changes.items():
        newFileData = newFileData.replace(source, destiny)
    
    # Write the file out again if they are different
    if newFileData != filedata:
        if not dryRun:
            with open(filePath, 'w') as file:
                file.write(newFileData)
        print(f'Changing content for: {filePath[folderPrintIndex:]}')

pathiter = (os.path.join(root, filename)
    for root, _, filenames in os.walk(folder)
    for filename in filenames
)
for path in pathiter:
    if checkFileProcess(path):
        fileName = path[folderPrintIndex+len(folderPrint)+1:]
        replaceInFile(path)

    newname =  path.replace("boilerplate", changes["boilerplate"])
    if newname != path:
        if not dryRun:
            os.rename(path,newname)
        print(f'Renamin file from "{path[folderPrintIndex:]}" to "{newname[folderPrintIndex:]}"')

os.remove(args[0])
