import time
import os
fileNum = 0
version = "0.0.2"

os.system(f'title IronBrew Lua VM Obfuscator - Version {version}')

# see if is setup...
if not os.path.exists("in\\") or not os.path.exists("out\\"):
    if not os.path.exists("in\\"):
        os.makedirs("in\\")
    if not os.path.exists("out\\"):
        os.makedirs("out\\")
    print("Directories have been made")
    print('You can now put your (.txt/.lua) files in the folder called "in" and then run this software.')
    print("Thanks for using this software! :)")
    print('Please wait...')
    time.sleep(3)
    try:
        os.system('CLS')
    except:
        os.system('clear')# for linux.
# its setup! now try to import requests
try:
    import requests
except:
    # its not installed tell user to install it...
    print('You dont have a required module to run this program.')
    option = input('Would you like to install the following module "requests"? (y/n) ')
    if option.lower() == "y":
        os.system('pip install requests')
    else:
        if option.lower() == "n":
            print('You have chosen to not install it.')
            print('If you would like you could install it by yourself with the following command executed into command prompt.')
            print('pip install requests')
            time.sleep(60)
            exit()
    print()
    print('Please restart the software...')
    time.sleep(60)
    exit()

pastebin = requests.get('https://pastebin.com/raw/0LyvHJpa')
if pastebin.status_code == 200:
    if pastebin.json()["Version"] != version:
        print('You are running an outdated version of this.')
        print('Please check the GitHub for a new version.')
        print(f'Your Version: {version}')
        print(f'Server Version: {pastebin.json()["Version"]}')
        os.system('start https://github.com/Enomphia/IronBrew')
        time.sleep(15)
        exit()

print('Api By Aztup')
print('IronBrew by Defcon42 and Aztup (re wrote some stuff)')
print('Enomphia for making this epic program!')
print()

input('Press ENTER to start the obfuscation process...')

customVar = input('Do you want a custom variable? (y/n) ')
print()

if customVar.lower() == "y":
    customVarNamee = input('Enter custom variable: ')
    print()

def obfuscate(string):
    if customVar.lower() == "y":
        settings = {
            "EncryptStrings": "on",
            "EncryptImportantStrings": "on",
            "AddMemes": "on",
            "CustomVarName": str(customVarNamee)
        }
    else:
        settings = {
            "EncryptStrings": "on",
            "EncryptImportantStrings": "on",
            "AddMemes": "on"
        }
    post = requests.post("https://obfuscator.aztupscripts.xyz/Obfuscate", files={"Input": string}, data=settings)
    return post.text

startTime = time.time()

# check if there are files in "in"
if len(os.listdir('in')) == 0:
    # there are no files in "in" tell to put them in...
    print('You need to put the files in the folder called "in"')
    time.sleep(15)
    exit()

for filename in os.listdir('in'):
    if filename.endswith('.txt') or filename.endswith('.lua'):
        print('obfuscating... ' + filename)
        startTimee = time.time()
        newFile = open('out//' + filename, 'w')
        oldFile = open('in//' + filename, 'r')
        newFile.write(obfuscate(oldFile.read()))
        newFile.close()
        oldFile.close()
        fileNum = fileNum + 1
        print('obfuscated ' + filename + " took: " + str(time.time()-startTimee) + " seconds")

print()
print('finished obfuscating files. you may now close this window!')
print('obfuscated; ' + str(fileNum) + " files")
print('finished in; ' + str(time.time() - startTime) + " seconds")

time.sleep(60)
exit()
