import numpy as np

# Exploring basic NumPy methods (without array methods)

# Mathematical Constants
print("Pi:", np.pi)
print("Euler's Number:", np.e)

# Trigonometric Functions
angle_rad = np.deg2rad(45)  # Convert 45 degrees to radians
print("Sin(45 degrees):", np.sin(angle_rad))
print("Cos(45 degrees):", np.cos(angle_rad))
print("Tan(45 degrees):", np.tan(angle_rad))

# Exponential and Logarithmic Functions
print("Exponential of 2:", np.exp(2))
print("Natural Log of 10:", np.log(10))
print("Log base 10 of 100:", np.log10(100))
print("Log base 2 of 8:", np.log2(8))

# Rounding Functions
print("Ceil of 4.3:", np.ceil(4.3))
print("Floor of 4.7:", np.floor(4.7))
print("Round 4.5:", np.round(4.5))

# Random Number Generation
print("Random Number [0,1]:", np.random.rand())
print("Random Integer [1,10]:", np.random.randint(1, 10))

# Statistical Functions
data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))
print("Variance:", np.var(data))

# Greatest Common Divisor (GCD) and Least Common Multiple (LCM)
print("GCD of 24 and 36:", np.gcd(24, 36))
print("LCM of 6 and 8:", np.lcm(6, 8))

# Factorial and Power
print("Factorial of 5:", np.math.factorial(5))
print("2 to the power of 3:", np.power(2, 3))
