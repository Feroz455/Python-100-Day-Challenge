raw1 = ["🏢", "🏢", "🏢"]
raw2 = ["🏢", "🏢", "🏢"]
raw3 = ["🏢", "🏢", "🏢"]
finalRaw = [raw1, raw2, raw3]

row = int(input("Enter row number: "))  # Convert input to integer
column = int(input("Enter column number: "))  # Convert input to integer

finalRaw[row - 1][column - 1] = "X"

for i in range(3):
    print(finalRaw[i])  # Join emojis in a row with spaces
