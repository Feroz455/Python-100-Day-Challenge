# count = 0
# amount = 4
# for a in range(amount):
#     for i in range(amount):
#         for j in range(amount):
#             for k in range(amount):
#                 # if not(i == j or j == k or i == k):
#                 print(f"{a}{i}{j}{k}")
#                 count +=1 
# print(count)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def nPr(n, r):
    if r > n:
        return 0
    return factorial(n) // factorial(n - r)

# Example usage
sum = 0
for i in range(1,27):
    print(i)
    print(f"{nPr(26, i)}")
    sum += nPr(26, i)

print(sum)

print(pow(26, 26))
# 1
# 26
# 650
# 15600
# 358800
# 7893600
# 165765600
# 3315312000
# 62990928000
# 1133836704000
# 19275223968000
# 308403583488000
# 4626053752320000
# 64764752532480000
# 841941782922240000
# 10103301395066880000
# 111136315345735680000
# 1111363153457356800000
# 10002268381116211200000
# 80018147048929689600000
# 560127029342507827200000
# 3360762176055046963200000
# 16803810880275234816000000
# 67215243521100939264000000
# 201645730563302817792000000
# 403291461126605635584000000