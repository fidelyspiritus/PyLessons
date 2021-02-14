cubes = []
cube_sum = 0

for i in range(1, 1000, 2):
    cubes.append(i ** 3)

# в идеале это стоило убрать в функцию)
for i, cube in enumerate(cubes):
    temp_sum = 0
    while cube != 0:
        temp_sum += cube % 10
        cube //= 10
    if temp_sum % 7 == 0: cube_sum += cubes[i]

print(cube_sum)

for i in range(len(cubes)):
    cubes[i] += 17

cube_sum = 0

for i, cube in enumerate(cubes):
    temp_sum = 0
    while cube != 0:
        temp_sum += cube % 10
        cube //= 10
    if temp_sum % 7 == 0: cube_sum += cubes[i]

print(cube_sum)
