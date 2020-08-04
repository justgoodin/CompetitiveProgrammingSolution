# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m = map(int,input().strip().split(" "))
array = list(map(int,input().strip().split(" ")))
arrA = list(map(int,input().strip().split(" ")))
arrB = list(map(int,input().strip().split(" ")))

A = set(arrA)
B = set(arrB)

hA = [1 for i in array if set([i]).intersection(A)]  #Can be simpler logic, intent was to solve using sets
hB = [-1 for i in array if set([i]).intersection(B)] #Can be simpler logic, intent was to solve using sets


happiness = sum(hA) + sum(hB)

print(happiness)

'''
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.

Constraints



Input Format

The first line contains integers  and  separated by a space.
The second line contains  integers, the elements of the array.
The third and fourth lines contain  integers,  and , respectively.

Output Format

Output a single integer, your total happiness.

Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
Explanation

You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.

Hence, the total happiness is .
'''
