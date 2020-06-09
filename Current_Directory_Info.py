""" 
Use Regular Expressions to extract operating system 
command line interface data for total file size, 
earliest and last modified files with names. 
by Rick Gosalvez 041020 
"""

import os
import subprocess
import re

def directory_info():
	"""
	list directory contents sorted by date. 
	subprocess recommended over os.system() per python os library
	print number of files, total size of contents, earliest and latest modified filesnames.
	"""

	# list contents
	ls_output_utf_sort = subprocess.check_output(['ls', '-lt']).decode("utf-8")     # Convert bytes to string
	print()
	print(f">>> Running 'ls -lt' command for current directory <<< \n\n {ls_output_utf_sort}")

	# list number of files
	contents = os.listdir()         # includes hidden file(s) in directory
	print(f'Number of files in directory:     {len(os.listdir("."))}')

	# extract user group name
	usergroup = re.search("\s\s([a-zA-Z]+?)\s\s+", ls_output_utf_sort).group().strip()   # identify group name for text extraction

	# use user group name as pattern to match
	new_pattern_two = "\s{2}"+usergroup+"\s*(.*)\s[a-zA-Z]{3}\s{1,2}\d"
	file_size = re.findall(new_pattern_two, ls_output_utf_sort)

	# sum file sizes
	countn = 0
	for i in file_size: countn += int(i)
	print(f'Total File Size for Directory:    {countn}')

	# extract date, time, file
	date_time_file = re.findall(" [a-zA-Z]{3} .*?\w.*", ls_output_utf_sort)

	# clean to create new list
	new_list = []

	for i in date_time_file:
		ii = i.strip()
		new_list.append(ii)
	print(f'Earliest Modified File:           {new_list[-1]}')
	print(f'Lastest Modified File:            {new_list[0]}')
	print()
	# print()
	# print(f'All files including hidden files in directory:\n{contents}')

# call directory info function
directory_info()


