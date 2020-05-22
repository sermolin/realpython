#!/usr/bin/env python
# coding: utf-8

# In[1]:


# example of argument parsing


# In[6]:


# myls.py
# Import the argparse library
import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='List the content of a folder')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

print(input_path)

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))


# In[ ]:





# In[ ]:




