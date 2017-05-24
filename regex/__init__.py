import re

iter = re.finditer("(ab)(c(d(e)f))(g)","adadfffee")
for match in iter:
    print(match)