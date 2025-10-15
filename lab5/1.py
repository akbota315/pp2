#1
import re

txt = "a ab abb abbb ac b aaab" 
x = re.findall(r"ab*", txt)

print( x)


#2
import re

txt = "ab abb abbb abbbb a abbbbbb ac"
x= re.findall(r"ab{2,3}", txt)

print(x)


#3
import re

txt = "hello_world  my_name is_not_nurr"
x = re.findall(r"[a-z]+_[a-z]+", txt)

print(x)

#4
import re

txt = "Hello World Test string Bota Nurrr PYTHON Code"
x = re.findall(r"[A-Z][a-z]+", txt)

print(x)

#5
import re

txt = "acb a123b azz b ab a-b axyb a_b aaab a-bb"
x = re.findall(r"a.*b", txt)

print(x)

#6
import re

txt = "Hello, world. My name is Akbota Nurshat."
x = re.sub(r"[ ,.]", ":", txt)

print(x)

#7
import re

txt = "my_name_is_aqbota"
def gg(s):
    return re.sub(r"_([a-z])", lambda x: x.group(1).upper(), s)

result = gg(txt)
print(result)


#8
import re

txt = "SplitAtUpperCaseLetters"
x = re.findall('[A-Z][^A-Z]*', txt)
print(x)

#9
import re

txt = "WritePythonProgramToInsertSpaces"
x = re.sub(r'([a-z])([A-Z])', r'\1 \2', txt)
print(x)

#10
import re

txt = "MyNameIsAqbota"
result = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', txt).lower()
print(result)
