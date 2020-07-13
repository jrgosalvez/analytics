"""
HTML Tag Checker
by Rick Gosalvez 050820 
"""

from collections import Counter, deque
import re

class HtmlChecker:
    """program to check html tags"""

    def __init__(self, filename='index.html'):      
        self.filename = filename

    def open_file(self):
        """initialize file and read contents"""
        file = self.filename
        with open(file,'r') as f:
            string = f.read()
            print(f'{string}\n')
            return string

    def verify_tags(self, string):
        """verify HTML tag characters are properly balanced"""
        n = len(string)
        s = deque([])
        count = 0

        # verify '<' and '>' are in balance with stacks
        for i in string:
            if i == '<':             # if character is a opening symbol, push to stack
                s.append(i)
            elif i == '>':
                if len(s) == 0:
                    count += 1       # count number of opening tags missing
                else:
                    s.pop()          # if character is a closing symbol, pop last open character from stack
        
        # verify html tag names are in balance with dictionaries, sets, lists
        open_tags = re.findall('<([^/].+?)>', string)
        closed_tags = re.findall('</(.[^</]+?)>', string) 
        count_open_tags   = Counter(open_tags)
        count_closed_tags = Counter(closed_tags)

        # remove exact matches
        open_tags = count_open_tags.items() - count_closed_tags.items()
        closed_tags = count_closed_tags.items() - count_open_tags.items()

        open_tags_dict = open_tags
        new_open = dict((x, y) for x, y in open_tags_dict)

        closed_tags_dict = closed_tags
        new_closed = dict((x, y) for x, y in closed_tags_dict)

        return count, s, open_tags, closed_tags, new_open, new_closed

    def print_check(self, count, s, open_tags, closed_tags, new_open, new_closed): 
        """
        print HTML Tag check report.
        display unbalanced open and closed tags.
        """

        print('\nHTML NAME Tag Check Report:')
        if not open_tags and not closed_tags:
            print('Balanced.')
        elif not open_tags:
            for k,v in closed_tags:
                print(f'{v} {k} Open tag(s) missing.')
        elif not closed_tags:
            for k,v in open_tags:
                print(f'{v} {k} Close tag(s) missing.')   
        else:
            for k,v in list(new_open.items()):
                if k in list(new_closed.keys()):
                    pass
                else:
                    print(f'{v} {k} Close tag(s) missing.')
            for k,v in list(new_closed.items()):
                if k in list(new_open.keys()):
                    pass
                else:
                    print(f'{v} {k} Open tag(s) missing.')
            for k1,v1 in open_tags:
                for k2,v2 in closed_tags:
                    if k1 == k2:                
                        k = k1
                        v = v1 - v2
                        if v < 0:
                            print(f'{abs(v)} {k} Open tag(s) missing.')
                        else:
                            print(f'{v} {k} Close tag(s) missing.')
        
        print('\nHTML Tag CHARACTER Check Report:')
        if len(s) == 0 and count == 0:
            print('Balanced')
        else:
            if len(s) > 0:
              print(f"Missing {len(s)} '>' closing charcter tag(s).")
            if count > 0:
              print(f"Missing {count} '<' opening character tag(s).")
                            
#########################################################
## Sample html files and what program should catch:
## test.html  - Balanced HTML Tags
## test1.html - entire close tag missing for <div>
## test2.html - '<' missing for title, '>' missing for h1, entire <div> close tag missing
## test3.html - '<' & '>' balanced, but closing tags missing: 1 <head>, 2 <title>, 4 <div> | Opening tags missing: 1 <h1>, 2 <body>
## test4.html - 1 <head>, 2 <title>, 1 body b/c '>'
#########################################################

test_file = 'test3.html'

check = HtmlChecker(test_file)
step1 = check.open_file()
count, s, open_tags, closed_tags, new_open, new_closed = check.verify_tags(step1)
check.print_check(count, s, open_tags, closed_tags, new_open, new_closed)
