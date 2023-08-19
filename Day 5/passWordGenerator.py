import random
import string

letters = int(input("Number of letters: "))
digits = int(input("Number of digits: "))
punctuation = int(input("Number of punctuation: "))

password = []

password.extend(random.choice(string.ascii_letters) for _ in range(letters))
password.extend(random.choice(string.digits) for _ in range(digits))
password.extend(random.choice(string.punctuation) for _ in range(punctuation))

# random.shuffle(password)  # Shuffle the generated characters
generated_password = ''.join(password)  # Convert list to string

print("Generated password:", generated_password)
