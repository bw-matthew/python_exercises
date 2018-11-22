read me first
==== 
draft schedule of easy python workshops for the data science team.

# introduction
the data science team generally relies on python for programming. the team members need python to varying degree and some have minimal experience with python and possibly programming in general. we should all be able "speak python" to a certain (not currently defined) level.

these exercises are meant to present some useful features of python to inepxerienced users. it is not aimed at absolute beginners.

each week, participants can collectively decide what topic would be of use and will be covered the following week.

## prerequisites
we will be working in the unix command line, acessed e.g. via terminal.app or iterm2.app, so there are some basics that will be helpful for the participants to know: (`ls`,`cd`, `mkdir`, `touch`, `echo`, `wc`, `grep`, `sed`, `awk`, `less`, `cat`, `head`, `tail`)

we assume participants have python 3.x installed and ready to use (code examples will often not be backwards-compatible with python 2.x.), as well as their favourite text editor and browser. you can check your current version by opening up a shell (e.g. terminal.app/iterm.app on macos) and entering `python --version`)

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
the design goal of each workshop is that they 1) tackle some useful aspect of programming with python. 2) are short enough to be discussed with participants in a 1 hour session, and yet complete enough that the participants can then complete a simple exercise to test their understanding of the feature. this may be optimistic.

# solutions
participants in the tutorial can add their solutions/musings/code into a self-named sub-folder of the `solutions` folder.

# notes
a list of documentation and links to helpful sources explaining features discussed in greater detail.
