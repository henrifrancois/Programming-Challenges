import re

any_match = re.compile(r'Henri|Edouard')
look = any_match.search("Do you prefer being called Henri or Edouard? ")
print(look.group())
batRegex = re.compile(r'Bat')
batsearch = batRegex.search("I love my brand new Batarang")
print(batsearch.group())

def search(start, *args):
    """Searches for a matching patter with an unspecified number of arguments.

    The first input will be the beginning of the string.
    """
    pass
