#7. Write a python program to copy elements 4 and 5 from the following tuple into a new tuple.tuple1=(1,2,3,4,5,6)
import copy
tuple1=(1,2,3,4,5,6)

li3 = copy.deepcopy(tuple1[3])
li4 = copy.deepcopy(tuple1[4])
tuple2=li3,li4
print(tuple2)


