## Task-Dot

##### A basic task management script

##### // modules/libraries:
- pickle, datetime, os

##### >> Known Issues

##### // revision history

 - 0.9 - re-instated file io 

 - 0.8 - began switch to object orientation, file input/ouput temporarily disabled

 - 0.7 - added test for file existence before importing using os library

 - 0.6 - adjusted printing of task list to loop through all entries, indented machine responses to improve readability, fixed file handling bug

 - 0.5 - pickle module added, added file handling for saving data between sessions

 - 0.4 - main control flow changed to a function call, changed ifs to use boolean value of a list

 - 0.3 - datetime module useage added, tasks changed from a list to a dict; task name: todays date

 - 0.2 - added option to remove tasks

 - 0.1 - formatting and consistency updates

 - 0.0 - very basic list input


##### // upcoming additions
 - switch to cPickle as pickle


#####// future development
 - track task completion status
 - useful task date comparisons
 - add a gui instead of command line
 - multiple task list support
 - task list summary
 - look into if defaultdict offers any advantages
 - adjust code in line with PEP8 standards
 - port to python 3
 
