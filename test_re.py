import re

txt = "\n\n\n سلام سلام سلام\n\n\n\n"

matches = re.findall(r'[\n]*سلام[\n]*', txt)
print("ok")
