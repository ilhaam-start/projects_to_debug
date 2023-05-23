import re

class PostcodeChecker():
    def check(self, postcode):
        if postcode is None:
            return False
        return re.match(
            r"^[A-Za-z]{1,2}[0-9]{1,2}[A-Za-z]? [0-9][A-Za-z]{2}$", #This pattern ensures that the postcode starts with 1 or 2 letters, then 1 or 2 numbers, an optional letter, a space and then two letters.
            postcode,
            re.IGNORECASE) is not None
