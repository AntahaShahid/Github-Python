# format_Specifier: Formats a vlaue based on what kind of flag is inserted after a colon
#                     {:flags}

# To round a number to desire decimal points:
# number=432.65432
# print(f"Your doollars are: {number:.2f}")

# #To allocate a space:
# number=12345678
# print(f"Allocating Space: {number:20}")

# #To preceed a space with zeros..00
# number=1234567
# print(f"allocating zeros: {number:020}")

#For jutifying left:
# number="1234567"
# print(f"justifying left: {number:<30}")

# #For jutifying right:
# number=1234567
# print(f"justifying right: {number:>30}")

# #For center alignment:
number=1234567
print(f"center alignment: {number:^50}")

#For adding + before postive numbers:
# number=123456
# print(f"+ before POsitive numbers: {number:+}")

#if we have negative value then + will wont come before it:
# number=123456
# print(f"+ before neg numbers would not print: {number:+}")

#For adding 0s at end:
# number=432
# print(f"Your given time number is: {number:.2f}")

# #we can also add space:
# number=432
# print(f"Your given time number is: {number: }") # but not more than single space

# # Thousand comma seperator:
# number=123456789
# print(f"Thousand seperator: {number:,}")

# # We can also use multiple specifiers in single query:
# number=432432.6543
# number="6fdknfkdh4737h"
print(f"Your given time number is: {number:,.2f}")

# ye sab ingtegers k upar hi ho raha agar hum numbers ko string krte hain to error atta..
# We will check k agar string k upar bhi format specifiers apply hota hai k nai..