#Lab #1
#Due Date: 01/11/2019, 11:59PM
########################################
#                                      
# Name: Kathryn Stam
# Collaboration Statement: I only used old programs that I had written
# as references for this Lab
#
########################################


def sumSquares(aList):
    """
        >>> sumSquares(5)
        'error'
        >>> sumSquares('5')
        'error'
        >>> sumSquares(6.15)
        'error'
        >>> sumSquares([1,5,-3,5,9,8,4])
        221.0
        >>> sumSquares(['3',5,-3,5,9,8,4,'Hello'])
        229.0
    """
    # --- YOU CODE STARTS HERE 
    #define Sum variable
    Sum = 0
    #open aList file to read
    try:
        file=open(aList, "r")
    #Catch if the user doesn't input a text file
    except FileNotFoundError:
        Sum = "error"
        return Sum
    
    #define list
    lisT=[]
    
    #read the file into an integer list
    with open(aList,"r") as f:
        for line in file:
            data=f.readline().rstrip('\n')
            lisT.append(data)
            lisT=[int(i) for i in lisT]
            
    #loop to find the square of items in the list and total them
    for i in range(len(lisT)):
        lisT[i]=lisT[i]*lisT[i]
        Sum=Sum+lisT[i]
    Sum=float(Sum)
    return Sum

#Call sumSquares function and output Sum of Squares
Sum = sumSquares(input("Enter the name of a list file: "))
print(Sum)
