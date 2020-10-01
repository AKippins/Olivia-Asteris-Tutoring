#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    scores = list(scores)
    high_score = None
    worst_score = None
    change_counter_high = 0
    change_counter_low = 0
    
    for score in scores:
        if not high_score:
            high_score = score
        elif score > high_score:
            change_counter_high += 1
            high_score = score
        
        if not worst_score:
            worst_score = score
        elif score < worst_score:
            change_counter_low += 1
            worst_score = score

    return(change_counter_high, change_counter_high)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
