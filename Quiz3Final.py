#dot takes two vectors and outputs and outputs the dot product
def dot(vec01,vec02):
    '''
    This function dot takes two vectors as its arguments then checks to see if they are of compatible dimensions.
    Then if they are of compatible dimensions it will out the dot product.
    '''

    n = len(vec01)
    m = len(vec02)
    #I take the length of both vectors because I need to know if the lengths are equal
    if n == m:
        total = 0
        for i in range(n):
            total += vec01[i]*vec02[i] #you take the += because it outputs the sum of the multiplication for all elements i
        return total
    else:
        return('Invalid Input')
# The test vectors for the function dot, including one that does not have the same compatible dimensions
testVec01 = [1,2,4]
testVec02 = [2,2,1]
testVec03 = [0,2]
print (dot(testVec01,testVec02)) #outputs 10 which is correct
#print (dot(testVec01,testVec03)) #outputs Invalid Input


#vecSubtract takes two vectors and subtracts them from eachother
def vecSubtract(vec03,vec04):
    '''
    This function, vecSubtract, takes two vectors, checks if they are of compatible dimensions then if they are of compatible dimensions, subtract them
    '''

    n = len(vec03) #the two variables to check if the length is the same
    m = len(vec04)

    if n == m:

        for i in range(n):

            vec03[i] = vec03[i] - vec04[i] #subtracting vec04 from vec03, you use i to go through all of the elements in both vectors
        return vec03
    else:
        return ('invalid input')
testVec04 = [1,2,5]
testVec05 = [2,3,5]
testVec06 = [2,1]
print (vecSubtract(testVec04,testVec05)) #outputs [-1,-1,0] which is correct if you take testVec04 - testVec05
#print (vecSubtract(testVec04,testVec06)) #outputs invalid input

#Scalar times Vector Multiplication
def scalarVecMulti(scalar,vec05):
    '''
    This function takes a scalara and a vector as its arguments, then multiples the scalar to a vector, outputing the scalar*vector.
    It does this by multiplying the scalar to the vector.
    '''
    n = len(vec05)
    for i in range(n):
        vec05[i] = scalar * vec05[i]  # here the scalar is multiplied to the vector through each element i in the vectors range.
    return vec05

testScalar01 = 4
testScalar02 = 'scalar'
testScalar03 = [1,1,1]

testVec07 = [1,1,1]
testVec08 = 4
testVec09 = 'vector'

print (scalarVecMulti(testScalar01,testVec07))
#print (scalarVecMulti(testScalar02,testVec07)) #This prints out ['scalar', 'scalar', 'scalar']
#print (scalarVecMulti(testScalar01,testVec08)) #This prints out a typeerror of object of type 'int' has no len()

#Infinity norm of a vector function
def infNorm(vec06):
    '''
    This function takes a vector and searches through the absolute values for the max
    value of all of its absolute value elements then it outputs that number in absolute
    value form. It does this by making a sort of dummy variable so that it looks for the
    largest value aka it looks until abs(large) is the largest number in the vector.
    :param vec06: vector
    :return: integer
    '''

    large = 0  # The dummy variable, has to be here so that it has a base value for the if statement
    for i in range(len(vec06)):

        while abs(vec06[i]) > abs(large): # Where it searches through the vector till large is the largest
                                          # I use a while loop here because I want it to continue until the statement is false, which is what a while loop does.
            large = vec06[i]
    return abs(large)

testVec10 = [5,-7,2,6,3,2,1]
testVec11 = 'trees'
testVec12 = 4
print (infNorm(testVec10)) # Outputs 7 as it should
#print (infNorm(testVec11)) #Outputs Bad operand type for abs(): 'str'
#print (infNorm(testVec12)) #Outputs object of type 'int' has no len()

#Normalizing the vector with respect to the infinity norm

def normalize(vec07):
    '''
    This function will do what I did above to find the infinity norm, then it will divide the vector by infNorm(vec06)).
    This will give us the normalized vector.
    :param vec07: vector
    :return: vector
    '''
    #I copied and pasted the above code
    large = 0 # The dummy variable
    for i in range(len(vec07)):
        while abs(vec07[i]) > abs(large): # Where it searches through the vector till large is the largest
            large = vec07[i]

    return [n/abs(large) for n in vec07] # Here is where you take the elements in vec07, n here, and divide it indivually by abs(large) that we got above.


testVec13 = [1,-5,2]
testVec14 = 4
testVec15 = 'birds'
print (normalize(testVec13))  #outputs the answer: [0.2, -1.0, 0.4] which is correct for all of the elements in the vector divided by 5.
#print (normalize(testVec14)) #outputs an error that says: object of type 'int' has no len()
#print (normalize(testVec15)) #outputs an error that says: bad operand type for abs(): 'str'

