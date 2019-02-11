#!/bin/sh

#  Python Script.sh

#  Created by Lamont D on 12/25/18.

#  intput() - accepts user input as a python code
#  raw_input() - accepts user input as a normal string
#  int(raw_input()) - accepts user input as a normal integer

list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 4]
list2 = []
for x in list1:
    if x > 5:
        list1.remove(x)

print(list1)

