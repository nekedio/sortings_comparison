import random as r
import bubble_sort as bubble
import shaker_sort as shaker
import odd_even_sort as odd_even

ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r.shuffle(ar)

print("-------bubble_sort-------")
print(bubble.sort(ar.copy()))

print("-------shaker_sort--------")
print(shaker.show_sorting(ar.copy()))

print("------odd-even_sort-------")
print(odd_even.show_sorting(ar.copy()))
