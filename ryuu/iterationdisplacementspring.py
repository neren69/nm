# Given data
g = 9.81
m1, m2, m3 = 2.0, 3.0, 2.5
k = 10.0

# Define the g(x) relations (fixed-point functions)
def g1(s2):  # s1 depends on s2
    return s2 + (m1 * g / k)

def g2(s3):  # s2 depends on s3
    return s3 + (m2 * g / k)

def g3():    # s3 is constant (bottom spring)
    return (m3 * g / k)

# Your iteration method
def iteration_method(g, x, tol=1e-5, max_iter=100):
    for i in range(max_iter):
        x_new = g(x)
        if abs(x_new - x) < tol:
            print(f"Converged in {i+1} iterations")
            return x_new
        x = x_new
    raise ValueError("Iteration did not converge")

# Iteratively compute from bottom to top
s3 = g3()
s2 = iteration_method(lambda s: g2(s3), 0)  # depends on s3
s1 = iteration_method(lambda s: g1(s2), 0)  # depends on s2

print("\nSpring extensions (in meters):")
print(f"s1 = {s1:.4f}")
print(f"s2 = {s2:.4f}")
print(f"s3 = {s3:.4f}")

# Total displacements of masses from ceiling
x1 = s1
x2 = s1 + s2
x3 = s1 + s2 + s3

print("\nMass positions from ceiling (m):")
print(f"x1 = {x1:.4f}")
print(f"x2 = {x2:.4f}")
print(f"x3 = {x3:.4f}")