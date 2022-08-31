# Write a program, which reads weights (lbs.) of N students into a list and convert these weights to
# kilograms in a separate list using Loop. N: No of students (Read input from user)
# Ex: L1: [150, 155, 145, 148]
# Output: [68.03, 70.3, 65.77, 67.13]

# 1 lb = 0.45359237 kg 
L1 = [150, 155, 145, 148]
kilos = []
for element in L1:
    kilos.append(element * 0.45359237)

print(f'Lbs in Kilos: {kilos}')