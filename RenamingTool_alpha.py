'''
A module that automatically change file names of leetcode problems only.
Copy this file to LeetCode local repository to use.
'''
import re, os, shutil

# set working directory here:
current_dir = os.path.abspath('.')
print(current_dir)

def addprefix(filename):
    form = re.compile('(\d+)(#\S*._\d*\.\w+)')
    m = form.search(filename)
    num = m.group(1)
    last = m.group(2)

    if int(num) < 100 and int(num) > 9 and len(num) < 3:
        num = '0' + num
    elif int(num) < 10 and len(num) < 3:
        num = '00' + num
    else:
        raise AttributeError

    return num+last


def getNameList(directory):
    for i in os.walk(directory):
        namelist = i[2]
        break # the first generated is which directory we need
    return namelist

def changeName(directory):
    absWorkingDir = directory
    names = getNameList(directory)
    for name in names:
        old_name = os.path.join(absWorkingDir, name)
        try:
            prefixed = addprefix(name)
        except AttributeError:
            print('File:', old_name, 'has no need to be changed.\n')
            shutil.move(old_name, old_name)
        else:
            new_name = os.path.join(absWorkingDir, prefixed)
            print('Renaming "%s" to "%s"...\n' % (old_name, new_name))
            shutil.move(old_name, new_name)

if __name__ == '__main__':
    changeName(current_dir)


        





