## Task-Dot

##### A basic task management script

##### // modules/libraries:
- pickle, datetime, os

##### >> Known Issues

##### // revision history

 - a1.0 - prefaced revision numbers to represent alpha status, renamed file, changed to cPickle for speed, adjusted print formatting and file io names

 - a0.9 - re-instated file io 

 - a0.8 - began switch to object orientation, file input/ouput temporarily disabled

 - a0.7 - added test for file existence before importing using os library

 - a0.6 - adjusted printing of task list to loop through all entries, indented machine responses to improve readability, fixed file handling bug

 - a0.5 - pickle module added, added file handling for saving data between sessions

 - a0.4 - main control flow changed to a function call, changed ifs to use boolean value of a list

 - a0.3 - datetime module useage added, tasks changed from a list to a dict; task name: todays date

 - a0.2 - added option to remove tasks

 - a0.1 - formatting and consistency updates

 - a0.0 - very basic list input


##### // upcoming additions



#####// future development
 - track task completion status
 - useful task date comparisons
 - add a gui instead of command line
 - multiple task list support
 - task list summary
 - look into if defaultdict offers any advantages
 - adjust code in line with PEP8 standards
 - adjust print statements to work in python 3
 - port to python 3
 - create a proper testing suite
 
