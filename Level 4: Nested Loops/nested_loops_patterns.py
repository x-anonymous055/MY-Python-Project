# ==========================================
# Nested Loops Practice (For & While)
# ==========================================

# ------------------------------------------
# 1. Triangle Pattern (For Loop)
# ------------------------------------------

print("Triangle Pattern (For Loop):")

for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print()


# ------------------------------------------
# 2. Triangle Pattern (While Loop)
# ------------------------------------------

print("Triangle Pattern (While Loop):")

i = 1

while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i += 1

print()


# ------------------------------------------
# 3. Inverted Triangle (For Loop)
# ------------------------------------------

print("Inverted Triangle (For Loop):")

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print()


# ------------------------------------------
# 4. Inverted Triangle (While Loop)
# ------------------------------------------

print("Inverted Triangle (While Loop):")

i = 5

while i >= 1:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print()
    i -= 1

print()


# ------------------------------------------
# 5. Square Pattern (For Loop)
# ------------------------------------------

print("Square Pattern (For Loop):")

for i in range(5):
    for j in range(5):
        print("*", end="")
    print()

print()


# ------------------------------------------
# 6. Square Pattern (While Loop)
# ------------------------------------------

print("Square Pattern (While Loop):")

i = 1

while i <= 5:
    j = 1
    while j <= 5:
        print("*", end="")
        j += 1
    print()
    i += 1
