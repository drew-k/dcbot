def toOrdinalNum(n):
    return str(n) + {1: 'st', 2: 'nd', 3: 'rd'}.get(4 if 10 <= n % 100 < 20 else n % 10, "th")

class Format():
    """ Console output format options """
    red = '\033[91m'
    green = '\033[92m'
    yellow = '\033[93m'
    blue = '\033[94m'
    bold = '\033[1m'
    italics = '\033[3m'
    underline = '\033[4m'
    reset = '\033[0m'
