import re

class PostcodeChecker():
    def check(self, postcode):
        if postcode is None:
            return False
        return re.match(
            r"^[A-Za-z]{1,2}[0-9][A-Za-z]? [0-9][A-Za-z]{2}$",
            postcode,
            re.IGNORECASE) is not None
