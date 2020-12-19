import regex

import regex

# example:
example_string = "xababababcdcdcdcdaabby"

# regular expression that consumes the whole string
print(bool(regex.match("^x()y$", example_string)))
