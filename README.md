# PS7: Kronos Log Parsing

## Description
This program analyzes Kronos InTouch log files to identify and report device boot events. outputs the start and end of each boot sequence, calculates the boot duration in , and flags incomplete boots while reporting this to a report .rpt file

### Features
I decided to code it in python, as I felt as though it would be a little easier, and I am also not that well versed in python, and its been a while since I used it, so I wanted to warm up with it a bit and try it out. I also wanted to learn more about it, and this was the perfect opprotunity

### Approach
Find where the system boots, keep track of whether or not a boot has already occured, and when the end of the boot is found, set that flag to false and continue to search for starts. But it ended up being ALOT more complicated than I thought it would be, and python is alot more complex than I thought. I had to watch ALOT of videos, read ALOT on the python documentation website and overall it took me longer than anticipated

### Regex
I used re.compile(), which basically a reagular expression or pattern into a regex object. This is what I later used in my re.search

I also used re.search(), this scans trhough a given string to find the first match of the given regex pattern.
re.fullsearch() would require a COMPLETE match.

### Issues
I had trouble because I underestimated python. It was a way biggers truggle than I thought it was going to be.

## Acknowledgements
docs.python.org (python documentation)
StackOverflow
ALOT of python YT vids (way too many to list here)
w3schools.com (for python regex)
geeksforgeeks


