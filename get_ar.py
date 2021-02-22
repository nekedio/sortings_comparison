import random as r
ar = r.sample(range(-5, 5), 10)
#print(ar)
my_file = open("random_array.txt", "w")
my_file.write("ar = " + str(ar))
my_file.close()
