import os


# gathering the list of installed programs
programs = os.popen(
    'wmic product get name,version').read().strip().split('\n')[1:]
for program in programs:
    print(program)


'''
#updating the list of installed programs
os.system('wmic product where "name like \'%Adobe%\'" call uninstall /nointeractive')

#installing the latest version of Adobe Reader
os.system('msiexec /i "C:\\Users\\user\\Downloads\\AcroRdrDC1901020030_en_US.msi" /qn')

#installing the latest version of Adobe Flash Player
os.system('msiexec /i "C:\\Users\\user\\Downloads\\FlashPlayer.exe" /qn')

#installing the latest version of Adobe Shockwave Player
os.system('msiexec /i "C:\\Users\\user\\Downloads\\sw_64.msi" /qn')

#installing the latest version of Adobe Acrobat Reader DC
os.system('msiexec /i "C:\\Users\\user\\Downloads\\AcroRdrDC1901020030_en_US.msi" /qn')

#installing the latest version of Adobe Acrobat Pro DC
os.system('msiexec /i "C:\\Users\\user\\Downloads\\AcroProDC1901020030_en_US.msi" /qn')
'''
