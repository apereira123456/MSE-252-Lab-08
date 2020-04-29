import matplotlib.pyplot as plt
import numpy as np

Conversion = 1 / 453.59237
Span = 3

# PORTLAND CEMENT
# Dry
Force_01 = np.array([24.02, 23.96, 16.53])
Length_01 = np.array([5.28, 5.21, 5.24])
Width_01 = np.array([0.96, 1.04, 1.09])
Height_01 = np.array([0.73, 0.76, 0.63])
Mass_01 = np.array([118.50, 126.74, 113.90])

Density_01 = Mass_01 * Conversion / (Length_01 * Width_01 * Height_01)
MOR_01 = 3 * Force_01 * Span / (2 * Width_01 * Height_01 ** 2)

print(Density_01, " lb/in^3")
print(MOR_01, " lb/in^2")

# Wet - 7 Days
Force_02 = np.array([92.35, 51.73, 98.29, 84.71, 113.56, 54.25])
Length_02 = np.array([5.12, 5.25, 5.23, 5.21, 5.14, 5.28])
Width_02 = np.array([1.10, 1.09, 1.14, 0.99, 1.01, 0.96])
Height_02 = np.array([0.73, 0.70, 0.80, 0.73, 0.88, 0.69])
Mass_02 = np.array([141.80, 115.13, 154.28, 143.95, 151.55, 107.15])

Density_02 = Mass_02 * Conversion / (Length_02 * Width_02 * Height_02)
MOR_02 = 3 * Force_02 * Span / (2 * Width_02 * Height_02 ** 2)

print(Density_02, " lb/in^3")
print(MOR_02, " lb/in^2")

# Wet - 14 Days
Force_03 = np.array([55.54, 66.34, 45.52])
Length_03 = np.array([5.38, 4.92, 5.16])
Width_03 = np.array([1.09, 1.11, 1.00])
Height_03 = np.array([0.73, 0.65, 0.61])
Mass_03 = np.array([127.41, 114.78, 96.91])

Density_03 = Mass_03 * Conversion / (Length_03 * Width_03 * Height_03)
MOR_03 = 3 * Force_03 * Span / (2 * Width_03 * Height_03 ** 2)

print(Density_03, " lb/in^3")
print(MOR_03, " lb/in^2")

# Wet - 21 Days
Force_04 = np.array([83.00, 65.11, 66.09])
Length_04 = np.array([5.15, 5.25, 4.98])
Width_04 = np.array([1.00, 1.04, 1.07])
Height_04 = np.array([0.79, 0.58, 0.76])
Mass_04 = np.array([120.91, 104.70, 122.88])

Density_04 = Mass_04 * Conversion / (Length_04 * Width_04 * Height_04)
MOR_04 = 3 * Force_04 * Span / (2 * Width_04 * Height_04 ** 2)

print(Density_04, " lb/in^3")
print(MOR_04, " lb/in^2")

# Wet - 28 Days
Force_05 = np.array([85.29, 89.23, 65.02, 65.04])
Length_05 = np.array([5.34, 4.94, 5.07, 5.46])
Width_05 = np.array([1.04, 0.93, 1.05, 1.11])
Height_05 = np.array([0.67, 0.66, 0.61, 0.63])
Mass_05 = np.array([130.17, 98.95, 98.22, 122.46])

Density_05 = Mass_05 * Conversion / (Length_05 * Width_05 * Height_05)
MOR_05 = 3 * Force_05 * Span / (2 * Width_05 * Height_05 ** 2)

print(Density_05, " lb/in^3")
print(MOR_05, " lb/in^2")
    

# PLASTER OF PARIS
# 50% Water
Force_06 = np.array([105.29, 95.08, 96.65, 109.74])
Length_06 = np.array([5.41, 4.98, 5.35, 5.03])
Width_06 = np.array([0.91, 0.96, 1.13, 1.15])
Height_06 = np.array([0.77, 0.76, 0.70, 0.70])
Mass_06 = np.array([81.75, 75.01, 88.77, 85.37])

Density_06 = Mass_06 * Conversion / (Length_06 * Width_06 * Height_06)
MOR_06 = 3 * Force_06 * Span / (2 * Width_06 * Height_06 ** 2)

print(Density_06, " lb/in^3")
print(MOR_06, " lb/in^2")

# 56% Water
Force_07 = np.array([90.48, 81.89, 71.8, 96.49])
Length_07 = np.array([5.32, 5.14, 4.98, 5.64])
Width_07 = np.array([1.12, 1.00, 1.03, 1.07])
Height_07 = np.array([0.75, 0.73, 0.65, 0.77])
Mass_07 = np.array([85.05, 71.82, 65.27, 92.03])

Density_07 = Mass_07 * Conversion / (Length_07 * Width_07 * Height_07)
MOR_07 = 3 * Force_07 * Span / (2 * Width_07 * Height_07 ** 2)

print(Density_07, " lb/in^3")
print(MOR_07, " lb/in^2")

# 60% Water
Force_08 = np.array([58.62, 58.97, 65.99, 65.45])
Length_08 = np.array([4.95, 5.42, 5.08, 5.22])
Width_08 = np.array([0.92, 0.95, 1.12, 0.99])
Height_08 = np.array([0.82, 0.81, 0.71, 0.71])
Mass_08 = np.array([68.28, 76.17, 75.58, 67.25])

Density_08 = Mass_08 * Conversion / (Length_08 * Width_08 * Height_08)
MOR_08 = 3 * Force_08 * Span / (2 * Width_08 * Height_08 ** 2)

print(Density_08, " lb/in^3")
print(MOR_08, " lb/in^2")
    

# SLIP
# Green
Force_09 = np.array([7.77, 6.24, 4.49])
Length_09 = np.array([7.97, 7.86, 7.76])
Width_09 = np.array([0.79, 0.73, 0.72])
Height_09 = np.array([0.40, 0.37, 0.35])
Mass_09 = np.array([71.08, 61.11, 58.12])

Density_09 = Mass_09 * Conversion / (Length_09 * Width_09 * Height_09)
MOR_09 = 3 * Force_09 * Span / (2 * Width_09 * Height_09 ** 2)

print(Density_09, " lb/in^3")
print(MOR_09, " lb/in^2")

# Sintered
Force_10 = np.array([139.34, 93.54, 122.17, 119.26, 146.98, 149.65])
Length_10 = np.array([7.35, 7.26, 7.16, 7.13, 7.13, 6.85])
Width_10 = np.array([0.66, 0.68, 0.65, 0.68, 0.64, 0.68])
Height_10 = np.array([0.32, 0.34, 0.31, 0.33, 0.31, 0.33])
Mass_10 = np.array([64.02, 64.82, 56.15, 64.60, 55.30, 62.61])

Density_10 = Mass_10 * Conversion / (Length_10 * Width_10 * Height_10)
MOR_10 = 3 * Force_10 * Span / (2 * Width_10 * Height_10 ** 2)

print(Density_10, " lb/in^3")
print(MOR_10, " lb/in^2")