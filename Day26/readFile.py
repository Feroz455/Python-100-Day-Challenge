with open('venv/Include/file/file1.txt', 'r') as file:
    file1_lines = [int(line.rstrip()) for line in file.readlines()]
    file1_lines = list(set(file1_lines))
    file1_lines.sort()

with open('venv/Include/file/file2.txt', 'r') as file:
    file2_lines = [int(line.rstrip()) for line in file.readlines()]
    file2_lines = list(set(file2_lines))
    file2_lines.sort()

print(file1_lines)
print(file2_lines)

result = [number for number in file1_lines if (number in file2_lines)]
# i, j = 0, 0

# while i < len(file1_lines) and j < len(file2_lines):
#     if file1_lines[i] == file2_lines[j]:
#         result.append(file1_lines[i])
#         i += 1
#         j += 1
#     elif file1_lines[i] < file2_lines[j]:
#         i += 1
#     else:
#         j += 1

print(result)
# Specify the file path
file_path = "venv/Include/file/result.txt"  # Replace with the desired file name and path

# Open the file in write mode ('w')
with open(file_path, 'w') as file:
    for item in result:

        file.write(str(item) + "\n")

# The file is automatically closed when the 'with' block exits
print(f"File '{file_path}' has been created.")