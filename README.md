read me first
==== 
draft schedule of easy python workshops for the data science team.

# introduction
the data science team generally relies on python for programming. the team members need python to varying degree and some have minimal experience with python and possibly programming in general. we should all be able "speak python" to a certain (not currently defined) level.

these exercises are meant to present some useful features of python to inepxerienced users. it is not aimed at absolute beginners.

each week, participants can collectively decide what topic would be of use and will be covered the following week.

## prerequisites
we will be working in the unix command line, acessed e.g. via terminal.app or iterm2.app, so there are some basics that will be helpful for the participants to know: (`ls`,`cd`, `mkdir`, `touch`, `echo`, `wc`, `grep`, `sed`, `awk`, ``)

we assume participants have python 3.x installed and ready to use (our code examples will often not be backwards-compatible with python 2.x.), as well as their favourite text editor and browser. you can check your current version by opening up a shell (e.g. terminal.app/iterm.app on macos) and entering `python --version`)

we assume the participants can use git, but does not cover how to. matthew franglen (@matthew on slack) wrote a nice short [workshop on git](https://gitlab.com/matthewfranglen/version-control-presentation/tree/master) that might be helpful. also look into pages 13 through 18 of [this document](http://columbia-applied-data-science.github.io/appdatasci.pdf).

participants should have familiarity with the [PEP-8](https://www.python.org/dev/peps/pep-0008) style guide, so that we can all (attempt to) follow it together. (caveat that "A Foolish Consistency is the Hobgoblin of Little Minds")

### jupyter notebooks
participants can decide whether they edit their code in a text editor and run from the shell, or whether they prefer to work in a jupyter notebook. 

- installation instructions
- launching
- using (modes, keyboard shortcuts, starting and stopping executions, error handling)

### git

```
git init
git add * 
git commit 
git remote add origin https://github.com/oh-data-sci/python_exercises.git
git push -u origin master
```

## warning
there is no sage on the stage. just a guide to the side. 

# workshops
the design goal of each workshop is that they 1) tackle some useful aspect of programming with python. 2) are short enough to be discussed with participants in a 30 minute session, and yet complete enough that the participants can then complete a simple exercise to test their understanding of the feature. this may be optimistic.

## first things first
- get up and running
  + python 3.x
  + anaconda/jupyter/spyder
  + git
- `dir()`
- lambda functions
- `map()`, `filter`
- `[]` lists, list iterator, appending, copy, counting
- `()` itereator
- `.next()`
- list comprehension
- writing functions
- pyperclip.copy()/pyperclip.paste()?
```
mylist = ['A','B','C','D']
for n,listitem in enumerate(mylist):
    print(n, listitem)

{L: n+1 for n, L in enumerate(chr(65+i) for i in range(5))}
      (output: {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5})
```

## 01 access the file system
- first exercise. useful commands for traversing the file system structure
- `os.path.exists`
- `os.path.isfile`
- `os.path.isdir`
### Exercise
- create a new function
- traverses a directory tree
- collects file of a certain type and orders them by a metric


## 02 read and write data
- useful commands for reading csv, json, pickle, ...
- `with open`
- `pandas.read_csv`
- working with JSON
  + read
  + explore
  + write
- read and write pickle files 
  + import pickle
  + pickle.dump() (repeatedly)
  + pickle 'pointer chains'
  + pickle.load() (repeatedly)

```{python}
    objects = []
    with (open("myfile", "rb")) as openfile:
      while True:
          try:
              objects.append(pickle.load(openfile))
          except EOFError:
              break
```


```{python}

    from collections import defaultdict
    s = 'mississippi'
    d = defaultdict(int)
    for k in s:
         d[k] += 1
    
    d.items() # output: [('i', 4), ('p', 2), ('s', 4), ('m', 1)]
```

### Exercise
- create a new function
- list a directory
- read in all pickled files in it
- get a summary of the contents
- export as csv
- export as JSON

## 02 data manipulation (pipelines)
- pandas data frames
- read in from file (pickle)
- filter out rows
- select some columns
- mutate column
- add column
- group by + summarise
- join two dataframes
- anti join to remove rows

### Exercise
- read two pickled data files
- get a set of repeated row identifiers
- get a set of 

## 04 text cleaning exercise
based on examples from [here](https://docs.python.org/3/library/stdtypes.html?highlight=split#str.split)

- change case
- split text
- tokenise
- find elements
- regular expression (huge topic)
- import re; re.sub(r"[ ]+", ' ', 'this    sentence           has                non-uniform      spaces')
- convert to ubbidubbi
- regular expressions
- The isX String Methods
- `isalpha()`   returns True if the string consists only of letters and is not blank.
- `isalnum()`   returns True if the string consists only of letters and numbers and is not blank.
- `isdecimal()` returns True if the string consists only of numeric characters and is not blank.
- `isspace()`   returns True if the string consists only of spaces, tabs, and new-lines and is not blank.
- `istitle()`   returns True if the string consists only of words that begin with an uppercase letter followed by only lowercase letters.
- `startswith()`
- `endswith()`
- `split()`
- `join()`
- `rjust()`
- `ljust()`
- `center()`
- `'-'.join('There can be only one.'.split())`
```

    import pyperclip
    pyperclip.copy('Hello world!')
    pyperclip.paste()
    'Hello world!'
```

- `copy()` (import pyperclip)
- `paste()`
- 
- 

## using brandwatch's api 
- authentication
- fetch/create projects 
- get overciew of projects
- mentions
- fetch


## using apis
- get/put
- APIs
- read nyt api
- web scraping

## 05 dates and times
- date time objects
- convert date formats
- extract century, year, quarter, month, weekday, day, hour
- datetime arihmetic
- time zones? (gah!)


## 06 numerical computation
- numpy
- numerical precision
- format numbers for presentation/ rounding. 
- matrices
- linear algebra
```

    def distance(p1, p2) :
        (sum((wi - vi)**2 for  in zip(p1, p2)))**.5
    print distance((0,0,0), (5,4,3))
```
## 07 graphing
- ? (do not know much about plotting with python) 
- billijoe? ali?
- i need to look into matplotlib
- i need to look into plotly
- i need to look into dash
- exercise: reproduce a plot with shared data and output to pdf

## 08 spark
- spark session
- spark sql
- spark dataframe
- 

## 08 machine learning
- ml basics
- keras


## python style?
- do we need to discuss this?
- details, details
- bw may not have style guide?


## spacy/nltk
- doing the crazy things
- and more?


## machine learning models
- scikit learn/ keras / tensorflow
- regression
- classify
- 

# solutions
participants in the tutorial can add their solutions/musings/code into a self-named sub-folder in the `solutions` folder.

# notes
a list of documentation and links to helpful sources explaining features discussed in greater detail.