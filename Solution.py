
"""
Author: Raguram R D
Python 3.7 - Spyder
"""

from itertools import permutations as perm #to create the permutations
import operator as op #to work with operators
 

line = '40 1 4 3 51'  #Sample input
number_check = 42 #The number that need to evaluated

ip_split = line.split(' ')

list_op = [op.add, op.sub, op.mul] #list of operators to be used
list_operators = [] #storing result for eval for total possibilities


for ip in perm(ip_split):
	
    perm_list = list(ip)
	
    i=0
	
	#since there are 5 numbers and 4 operators, 4 loops are used
    for j in list_op:
        for k in list_op:
            for l in list_op:
                for m in list_op:
					
					#Output of one operation given as input to another operation
                    op1 = j(int(perm_list[i]),int(perm_list[i+1]))
                    op2 = k(op1, int(perm_list[i+2]))
                    op3 = l(op2, int(perm_list[i+3]))
                    op4 = m(op3, int(perm_list[i+4]))
					
                    if op4==number_check:
                        op_set = [j,k,l,m]
                        list_operators.append([perm_list, op_set])
	   


if len(list_operators)>0:
    print('YES')
else:
    print('NO')
	
print('Total number of possibilities to get the desired number ' + str(number_check) + " is " + str(len(list_operators)))
#print(list_operators)




   
