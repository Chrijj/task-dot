## Task-Dot

##### A basic task management script

##### // modules/libraries:
- pickle, datetime, os

##### >> Known Issues
- file i/o temporarily disabled

##### // revision history

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
 - adjust style and flow to be object oriented
 - switch to cPickle as pickle


#####// future development
 - track task completion
 - useful task date comparisons
 - line code with PEP8 standards
 - port to python 3
 
