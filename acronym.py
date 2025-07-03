import re

def abbreviate(words):
    return "".join([w.upper()[0] for w in re.sub("[-_]"," ",words).split()])
    

