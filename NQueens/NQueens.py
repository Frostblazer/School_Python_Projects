import random
# ask the user for an N value
print('N Queens Solution Generator')
n = int(input('Please enter a value for N (for an N x N board): '))

iterations = 1
# generate a candidate NQ solution [random.randint(0,n-1) for x in range(n)]
NQ = [random.randint(0,n-1) for x in range(n)]

# define a function to count number of conflicts()
def conflicts( list ):
    conflicts = 0
    for x in range(len(list) -1 ):
        for y in range( x + 1, len(list) ):
            #horizontal conflicts
            if list[x] == list[y]:
                conflicts += 1
            #diagonal conflicts
            if abs(list[x] - list[y]) == abs( x - y):
                conflicts += 1
    return conflicts            

# while number of conflicts in NQ > 0
while conflicts(NQ) > 0:
    # randomize (or improve) NQ
    if conflicts(NQ) > 0:
        iterations += 1
        NQ = [random.randint(0,n-1) for x in range(n)]
    elif conflicts == 0:
        break
# print NQ
print(NQ)
# print number of iterations
print('Number of conflicts: ' + str(conflicts(NQ)))
print('Number of iterations: ' + str(iterations))

