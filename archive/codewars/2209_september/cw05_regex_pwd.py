import re

# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a digit
# only contains alphanumeric characters (note that '_' is not alphanumeric)


# Starts with: abc
# Ends with: xyz
# Contains: 123
# Doesn't contain: 456
# The OR version is fairly simple; as you said, it's mostly a matter of inserting pipes between individual conditions. The regex simply stops looking for a match as soon as one of the alternatives matches.
#
# /^abc|xyz$|123|^(?:(?!456).)*$/
# /^(?=^abc)(?=.*xyz$)(?=.*123)(?=^(?:(?!456).)*$).*$/

regex = "\w+"

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)
print(x.group(0))