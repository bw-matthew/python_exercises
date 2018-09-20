# welcome to the first workshop, which trains use of the os module

################################################################################
# imagine you found a nice dataset you need to analyse, but instead of consisting 
# of a single file or a set of conveniently named files sitting together in a 
# directory the files are scattered about in folders, sub folders, and sub-sub folders.
# there are tens, or hundreds of them. also, not all of the files are data files, 
# some of them are documentation files.
# you just want a list of the data files so you can iterate over it and process 
# them all in some way. so you now need to:
# create a function that takes a path to a root directory as its arguement,
# and then will traverse the  folder tree structure and collect all the files 
# therein that have a given filename extension
# and returns a list of the files found (path + filename)
# bonus: filter the data files (assumed to have *.dat filename ending)
# and return the list, ordered by decreasing file size.
################################################################################

# we will start easy. 

# this module allows our python session to interact with the wider world of the
#  operating system outside of it, including the file system.
import os

# let's find out where the root folder of the python session is:
os.getcwd() # get-current-working-directory
start_here = os.getcwd() # save it in a variable.

# this command returns a python list whose elements are the contents of the directory
os.listdir('.')      # current directory
os.listdir('../')    # up one level
os.listdir('../../') # up two levels, etc

items = os.listdir('.') # current directory
# we can create a new folder within the python session
os.mkdir('tempfolder')
os.listdir('.')      # see it?
# and even a subfolder
os.mkdir('tempfolder/sub')

os.listdir('tempfolder') # now you see it?
os.rmdir('tempfolder/sub/')
os.listdir('tempfolder') # now you don't!

# to make a subfolder in one go use (new in python3)
os.makedirs('tempfolder/sub1/sub2')

# we can traverse the folder structure
os.chdir('tempfolder/sub1/sub2')
os.listdir('.') # nothing here yet.
os.chdir(start_here) # going back 'home'

all_items = os.listdir('.') # save the list
for item in all_items:
    if os.path.isfile(item):
        print(item, 'is a file')
    elif os.path.isdir(item):
        print(item, 'is a directory')
    else:
        print('what is', item, '??')

# note the home directory component of the cwd:
os.getcwd()

# incidentally, there is a function for expanding the user home directory
print(os.path.expanduser('~'))
USER_HOME = os.path.expanduser('~') # save that

# we can join folder paths together using
example_dir = os.path.join(USER_HOME, 'Desktop')
print(example_dir)

# we probably all have this file on our systems
example_file = USER_HOME + '.bash_profile'
os.path.exists(example_file) # should be true?
os.path.isfile(example_file) # should be true?
example_dir = USER_HOME + "Desktop"
os.path.isdir(example_dir)

# note that there is a way to use the regular shell commands 
os.system('pwd')
os.system('cd ~/Desktop; ls -l')
# note that these do not affect your python session's cwd
os.getcwd()

# how do we solve the issue mentioned earlier about data files in subdirectories?
# we could use the commands above, a recursive function, that took a directory,
# scanned a directory, collected any files found and entered any directory found
# and scanned that, etc...

# but someone has already done that for us. there is a function for that!
# os.walk(somepath). try it:
os.walk('.')
# returns an iteraterator that recursively yields three-tuples of: 
#  1) the current directory path
#  2) directories in the current path
#  3) files in the current path
# then it traverses into the directories in turn and repeats for that path.
# consider this output:
for current_dir, directories, files in os.walk("exciting_data"):
    print('root:', current_dir)
    print('dirs:', directories)
    print('files', files)
    for filename in files:
        print(filename)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# a possible solution
def scrape_directory_tree(starting_dir, file_ending):
    assert os.path.isdir(starting_dir) # do not pass a filename
    matching_files = []
    for current_dir, directories, files in os.walk(starting_dir, topdown=True):
       for filename in files:
           if filename.endswith(file_ending):
               matching_files.append(os.path.join(current_dir, filename))
    return matching_files

def list_files_by_size(filepathlist, decreasing=True):
    sorted_files = sorted(filepathlist, key=os.path.getsize, reverse=decreasing)
    return sorted_files

# test it
start = 'exciting_data'
name_ending = '.cat'
print(scrape_directory_tree(start, name_ending))
name_ending = '.doc'
print(scrape_directory_tree(start, name_ending))
name_ending = '.dat'
filelist = scrape_directory_tree(start, name_ending)
filelist_by_size = list_files_by_size(filelist)
for filepath in filelist_by_size:
    print(filepath, os.path.getsize(filepath))


# more general patterns
import re
pattern = re.compile(".*\.dat$")
def scrape_directory_tree(starting_dir, file_pattern):
    assert os.path.isdir(starting_dir) # do not pass a filename
    matching_files = []
    for current_dir, directories, files in os.walk(starting_dir, topdown=True):
       for filename in files:
           if file_pattern.match(filename):
               matching_files.append(os.path.join(current_dir, filename))
    return matching_files



# ask the slack channel
# /poll "what do you think of the difficulty level of the first workshop?" "too easy, it is not interesting" "fine, i both learned something and leveraged stuff i already knew" "too hard, too many new things, at least for the time allotted"