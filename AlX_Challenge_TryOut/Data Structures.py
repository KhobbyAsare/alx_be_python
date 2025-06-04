
"""
Tuple
"""
my_tuple_data = ("monday","tuesday","wednesday","thursday","friday")

print(type(my_tuple_data))

print(my_tuple_data[:3])

for data in my_tuple_data:
    print(f"Day - {data}")

"""
List
"""
# convert tuple to list
new_list = list(my_tuple_data)
print(new_list)

"""
Sets

- Unordered, Mutable, Remove all duplicates
"""
unique_data = [2,4,5,656,2,1,34,767,534]
# convert to Sets
new_set = set(new_list)
print(new_set)

print(unique_data)

empty_set = set()
empty_set.add("car")
print(empty_set)

"""
Set

Union = OR
Intersection = AND
Differences = 
"""

a = {4,5,6}
b = {2,4,6,7,1,8,9,23,2}

print(b)
c = a.intersection(b)
print(c)
d = a.union(b)
print(d)
e = 8
print(e in a)
print(e in b)


f = a.difference(b)
print(f)



"""
Dictionary

key value pair

"""

xdict = dict([('k1','v2'),('k2','v2'),('k3','v3')])
print(xdict)


ydict = {'g1':'H1', 'g2':'H2', 'g3':'H3'}
print(ydict)

print(ydict['g1'])

ydict['g2'] = 450
print(ydict)

# merge dictionaries

xdict.update(ydict)

print(xdict)

z = dict()
z['a'] = "alpha"
z['b'] ='beta'
z['g'] = 'gamma'
z['o'] = 'omega'

print(z)

z['dit'] = 6

if 'z' in z:
    print(z['z'])
elif 'a' in z:
    print(z['a'])


def funcd(d,v):
    for key in d:
        if d[key] == v:
            return key
    return dict()

vdict = dict([('v',2),('v2',3),('v3',4)])

print(funcd(vdict, 3))
