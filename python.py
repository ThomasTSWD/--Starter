# Génère la suite de Fibonacci jusqu'au 10e nombre
def suite_fibonacci(n):
    suite = [0, 1]  # Les deux premiers termes de la suite
    for i in range(2, n):
        suite.append(suite[i - 1] + suite[i - 2])
    return suite

# Affiche la suite de Fibonacci jusqu'au 10e terme
fibonacci_10 = suite_fibonacci(100)
print("Suite de Fibonacci (10 termes) :", fibonacci_10)
