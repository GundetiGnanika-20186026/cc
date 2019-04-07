#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_user = None
current_count = 0
user = None

for line in sys.stdin:
	line = line.strip()
	user, count = line.split('\t', 1)
	try:
        	count = int(count)
    	except ValueError:

        	continue
	if current_user == user:
        	current_count += count
    	else:
        	if current_user:
            		friend_det = []
	    		friend_det.append(current_user)
	                friend_det.append(current_count)
            		print '%s' % friend_det
        	current_count = count
        	current_user = user

#for last line 
if current_user == user:
	friend_det = []
	friend_det.append(current_user)
	friend_det.append(current_count)
        print '%s' % friend_det