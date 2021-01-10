# Euclid's algorithm
def Euclid_HCF(num1, num2):
    while num2 != 0:
        temporary_num1_holder = num1
        num1 = num2
        num2 = temporary_num1_holder % num2
    return num1

#print(Euclid_HCF(20, 4))
#print(Euclid_HCF(80, 32))


#Big O notation concept

def Big_O(data, alphabet):
    bigo=len(data)
    total = 0
    for datum in data:
        for alpha in alphabet:

            total += 1
            print(datum, alpha)
    
    bigo2 = (total / bigo)
    return f"Big_O is {bigo * bigo2} which is ({bigo} * {bigo2})"
            

data = [1, 2, 3]
alphabet = ['A', 'B', 'C']
print(Big_O(data, alphabet))


