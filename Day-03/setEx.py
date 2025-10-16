# *** SET ***
# * used to process unique entry *

# print("Sets in Python")

# set_one={'laptop','airpod','ipad','mobile','earphone','laptop','ipad'}
# print('\n\nNumber of items in the set are : ',len(set_one))
# print('\n')
# print("The items are :-\t")
# for item in set_one:
#     print(item,end=", ")
# print('\n\n')


# * clear() : to remove all the items from set *

# set_one={'laptop','airpod','ipad','mobile','earphone','laptop','ipad'}
# print('\n\nNumber of items in the set are : \t\t\t',len(set_one))
# set_one.clear()
# print('\nAfter clearing, the number of items in set_one are :\t',len(set_one))
# for item in set_one:
#     print(item,end=", ")
# print('\n')


# * remove() : to remove item from set *

# set_one={'laptop','airpod','ipad','mobile','earphone','laptop','ipad'}
# print('\n\nNumber of items in the set are : \t',len(set_one))
# for item in set_one:
#     print(item,end=", ")
# print('\n')
# item='ipad'
# set_one.remove(item)
# print(f'\nAfter removing {item} from set :\t',len(set_one))
# print('\n\n')


# * union, intersection, difference *

# * a)union *
# * s1.union(s2) : returns a new set with all items from both original sets *

# set_one={100,200,300,500,700,900,150}
# set_two={100,400,700,1000,1300}
# set_three={5000,11000,900,600}
# print('\n')
# print(f'set_one contains : {len(set_one)} items')
# print(set_one)
# print('\n')
# print(f'set_two contains : {len(set_two)} items')
# print(set_two)
# print('\n')
# print(f'set_three contains : {len(set_three)} items')
# print(set_three)
# unionset=set_one.union(set_two,set_three)
# print('\n')
# print(f'Union of set_one and set_two contains : {len(unionset)} following items')
# print(unionset)
# print('\n')


# * b)intersection *
# * s1.intersection(s2) : returns a set of common elements in original sets *

# set_one={100,200,300,500,400,700,900,150}
# set_two={100,400,700,1000,1300}
# set_three={5000,400,11000,900,600,700}
# print('\n')
# print(f'set_one contains : {len(set_one)} items')
# print(set_one)
# print('\n')
# print(f'set_two contains : {len(set_two)} items')
# print(set_two)
# print('\n')
# print(f'set_three contains : {len(set_three)} items')
# print(set_three)
# print('\n')
# interset=set_one.intersection(set_two)
# print(f'Intersection of set_one and set_two contains : {len(interset)} following items')
# print(interset)
# print('\n')
# interset=set_one.intersection(set_two,set_three)
# print(f'Intersection of set_one, set_two and set_three contains : {len(interset)} following items')
# print(interset)
# print('\n')


# * c)difference *
# * s1.difference(s2) : returns items only in first set which are not in other set  *

set_one={100,200,300,500,400,700,900,150}
set_two={100,400,700,1000,1300}
set_three={5000,400,11000,900,600,700}
print('\n')
print(f'set_one contains : {len(set_one)} items')
print(set_one)
print('\n')
print(f'set_two contains : {len(set_two)} items')
print(set_two)
print('\n')
print(f'set_three contains : {len(set_three)} items')
print(set_three)
print('\n')
interset=set_one.difference(set_two)
print(f'Difference of set_one and set_two contains : {len(interset)} following items')
print(interset)
print('\n')
interset=set_one.difference(set_two,set_three)
print(f'Difference of set_one, set_two and set_three contains : {len(interset)} following items')
print(interset)
print('\n')