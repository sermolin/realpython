#!/usr/bin/env python
# coding: utf-8

# In[1]:


# example of argument parsing

# myls.py
# Import the argparse library
import argparse

import os
import sys

# Create the parser
my_parser = argparse.ArgumentParser(description='endpoint name')

# Add the arguments
my_parser.add_argument('ep_name',
                       metavar='ep_name',
                       type=str,
                       help='Enter endpoint name')

my_parser.add_argument('N_itr',
                       help='Number of iterations')


# Execute the parse_args() method
args = my_parser.parse_args()

input_endpoint = args.ep_name
N = args.N_itr

print(input_endpoint)
print(N)