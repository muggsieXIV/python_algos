# /* 
#     Given a search criteria object whose values will only be primitives (ints, strings, bools)
#     and a list of objects,
#     return any object that matches all the key value pairs in the search criteria object
#     Bonus: write a 2nd solution using build in methods to practice functional programming
#     EXAMPLE INPUTS/OUTPUT
#     const collection = [
#         { firstName: "Bob", lastName: "Bobbert", age: 31 },
#         { firstName: "John", lastName: "Smith", age: 25 },
#         { firstName: "Bob", lastName: "Smith", age: 27 },
#         { firstName: "Bob", lastName: "White", age: 31 },
#     ];
#     const criteria = {
#         firstName: "Bob",
#         age: 31,
#     };
#     const expected = [
#         { firstName: "Bob", lastName: "Bobbert", age: 31 },
#         { firstName: "Bob", lastName: "White", age: 31 },
#     ];
# */

def obj_search(criteria, collection):
    matches = []
    for i in range(0, len(collection)):
        match = True
        for key in criteria.keys():
            # print('===key===')
            # print(key)
            # print('=== collection eval ===')
            # print(collection[i].get(key))
            # print('=== criteria eval ===')
            # print(criteria.get(key))
            
            if collection[i].get(key) == None or collection[i].get(key) != criteria.get(key):
                match = False
            if collection[i].get(key) == criteria.get(key):
                match = True

        if match:
            matches.append(collection[i])
    
    return matches


dict = [
    {'first_name': "Bob", 'last_name': "Bobbert", 'age': 31},
    {'first_name': "John", 'last_name': "Smith", 'age': 25},
    {'first_name': "Bob", 'last_name': "Smith", 'age': 27},
    {'first_name': "Bob", 'last_name': "White", 'age': 31},
]

search_que = {
    'first_name': "Bob",
    'age': 31,
}

print(obj_search(search_que, dict))

