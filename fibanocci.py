def fibonacci(n):
    x = [0, 1] 

    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return x
    for i in range(2, n):
        next_num = x[-1] + x[-2]
        x.append(next_num)
    return x
    
num_terms = 10  
fibonacci_sequence = fibonacci(num_terms)
print(fibonacci_sequence)

