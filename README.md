read me first
==== 
draft schedule of easy python exercises for internal use for the data science team.

# introduction
the data science team generally relies on python for programming. the team members have very varied experience with programming and with python, and also have varied needs to working in python. nevertheless, we should all be able "speak python" to a certain minimal level. these exercises are meant to present some useful features of python to inepxerienced users. it is not aimed at absolute beginners. 

## prerequisites
we assume participants have python 3.7+ installed and ready to use, as well as their favourite text editor and browser. the code examples will not be backwards compatible with python 2.x.

this course assumes the participants can use git, but does not cover how to. matthew franglen (@matthew on slack) wrote a nice short [workshop on git](https://gitlab.com/matthewfranglen/version-control-presentation/tree/master) that might be helpful. 

```
git init
git add * 
git commit 
git remote add origin https://github.com/oh-data-sci/python_exercises.git
git push -u origin master
```

## warning
no sage on stage. at best guide to the side. 

# exercises
the design goal of each exercise is that they are short enough to be discussed with participants in a 30 minute session, and yet complete enough that the participants can then complete a simple 30 minute task to test their understanding of the feature.

## jupyter notebooks
- installation
- launching
- using (modes, keyboard shortcuts, starting and stopping executions, error handling)
- comparison with using the command line interface
- viewing/saving/updating notebook documents
- exercise: set up your environment

## the iterators
- lambda functions
- `map()`, `filter`
- `[]` list iterator
- `()` itereator
- `next()`

## numerical computation
- numpy
- numerical precision
- format numbers for presentation/ rounding. 
- matrices, linear algebra, 

## dates and times
- date time objects
- convert date formats
- extract century, year, quarter, month, weekday, day, hour
- datetime arihmetic
- time zones? (gah!)

## read and write csv
- `os.path.exists`
- `os.path.isfile`
- `os.path.isdir`
- `with open`
- `pandas.read_csv`

## working with JSON
- read
- explore
- write

## read write pickle files 
- import pickle
- pickle.dump() (repeatedly)
- pickle 'pointer chains'
- pickle.load() (repeatedly)

## data manipulation (pipelines)
- pandas data frames
- filter
- select
- mutate

## data manipulation (pipelines) 2
- group by
- summarise
- exercise

## text cleaning exercise
- change case
- split text
- tokenise
- find elements

## simple plots
- ? (do not know much about plotting with python)
- i need to look into matplotlib
- i need to look into plotly
- i need to look into dash
- exercise : reproduce a plot with shared data and output to pdf

## spacy/nltk
- ??

## python style?
- do we need to discuss this?
- details, details
- bw may not have style guide?
- 

## regular expressions
- a bit out of scope but also important
- lots of useful exercises available
- huge topic, really.


# solutions
participants in the tutorial can add their solutions/musings/code into a self-named sub-folder in the `solutions` folder.

# notes
a list of documentation and links to helpful sources explaining features discussed in greater detail.