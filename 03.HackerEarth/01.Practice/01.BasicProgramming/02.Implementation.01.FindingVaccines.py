if __name__ == "__main__":
    n = int(input())
    m = int(input())
    r = input()
    
    gV,cV = [r.count("G"),r.count("C")]
    best = 0
    index = 0
    
    for i in range(n):
    
        l = int(input()) #useless input
        string = (input()) 
        
        G = string.count("G")
        C = string.count("C")
        interaction = G*cV + C*gV
        
        if interaction>best:
            best = interaction
            index = i+1
    
    print(index)




'''
You are creating a vaccine to fight against a worldwide novel pandemic virus. A vaccine contains a weakened virus that is injected inside people to produce antibodies to let it fight against the virus. The study of interaction among RNA of various viruses is quite necessary for this. An RNA consists of four types of molecules Guanine (), Adenine (), Cytosine (), and Uracil ().

You are given the structures of RNA for the pandemic virus and several vaccine viruses in the form of strings containing characters , , , and  representing respective molecules. You know that if there is higher interaction between the pandemic virus and vaccine virus, then better the vaccine will be. You also know that the only interaction between any two RNAs is a result of the interaction between their Guanine () and Cytosine () molecules. Formally, if the strings for RNA structures are  and , then you must consider the following points: 

One molecule of Guanine () of  and one molecule of Cytosine () of  will lead to one unit of interaction.
One molecule of Guanine () of  and one molecule of Cytosine () of  will lead to one unit of interaction.
Any other pair of molecules do not add to any interactions.
In this way, the total interaction between  and  is calculated as the sum of individual molecule pair interactions (as discussed above).

You must find the best available vaccine.

Input format

The first line contains a single integer  denoting the number of vaccines
The second line contains a single integer  denoting the length of the string denoting the RNA structure for the pandemic virus.
The third line contains a string  denoting the RNA structure for the pandemic virus.
Next  lines contains the following lines where:
 line contains a single integer  denoting the length of the string denoting the RNA structure for the  vaccine virus
 line contains a string  denoting the RNA structure for the  vaccine virus
Output format

Print a single integer  if the  vaccine is the best, that is, it has the maximum interaction with pandemic virus RNA, where  obviously holds.

If there are more than one answers possible (in case of two or more have the maximum interaction value), then print the smallest answer possible.

Constraints


SAMPLE INPUT 
2
5
ACGGU
6
AGCAAA
8
UAUAAGAG
SAMPLE OUTPUT 
1
Explanation
RNA of MARS-20 virus contains 2 molecules of G and 1 molecule of C.

Interaction with first vaccine = 3 units

Interaction with second vaccine = 2 units

Hence, first vaccine is better.
'''
