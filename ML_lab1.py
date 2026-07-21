# Q1
def count_letters(t):
    vow=0
    cons=0
    t=t.lower()
    for char in t:
        if char.isalpha():
            if char in "aeiou":
                vow+=1
            else:
                cons+=1
    print("Vowels:", vow, "Consonants:", cons)


# Q2
def matrix_multiply(A, B):
    if len(A[0])!=len(B):
        print("Error: matrices are not multiplicable")
        return
    
    result=[]
    for i in range(len(A)):
        row=[]
        for j in range(len(B[0])):
            sum_val=0
            for k in range(len(B)):
                sum_val+=A[i][k]*B[k][j]
            row.append(sum_val)
        result.append(row)
    print("matrix product:", result)


# Q3
def common_elements(list1,list2):
    common=[]
    for x in list1:
        if x in list2 and x not in common:
            common.append(x)
    print("common elements:",common)


# Q4
def matrix_transpose(matrix):
    transpose=[]
    for i in range(len(matrix[0])):
        row=[]
        for j in range(len(matrix)):
            row.append(matrix[j][i])
        transpose.append(row)
    print("Transpose:", transpose)


# Q5
def random_statistics():
    numbers=[]
    for i in range(100):
        numbers.append(100 + (i % 51))
    
    total=0
    for num in numbers:
        total+=num
    mean=total/100
    
    sorted_nums = sorted(numbers)
    median = sorted_nums[50]
    
    mode = numbers[0]
    max_count = 1
    for num in numbers:
        count = 0
        for x in numbers:
            if x == num:
                count += 1
        if count > max_count:
            max_count = count
            mode = num
    
    print("Mean:", round(mean, 2))
    print("Median:", median)
    print("Mode:", mode)


def main():
    # Q1
    count_letters("Hello World Python")
    
    # Q2
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    matrix_multiply(A, B)
    
    # Q3
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    common_elements(list1, list2)
    
    # Q4
    matrix = [[1, 2, 3], [4, 5, 6]]
    matrix_transpose(matrix)
    
    # Q5
    random_statistics()


if __name__ == "__main__":
    main()