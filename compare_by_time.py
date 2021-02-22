import random
import timeit

setup_code = """
import bubble_sort as bubble
import random as r
ar = r.sample(range(-500, 500), 1000)
"""
code_to_test = """
ar1 = ar.copy()
#print(ar1)
bubble.sort_r(ar1)
#print(ar1)
"""
elapsed_time = timeit.timeit(setup=setup_code, stmt=code_to_test, number=10)/10

print(elapsed_time)
