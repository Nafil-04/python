# import re

# text = "Hello World"
# print(re.search(r"World",text))

# # match
# text= "hello world"
# print(re.match(r"hello",text))
# print(re.match(r"world",text))

# # findall
# text= "i have 2 apples and 5 oranges."
# print(re.findall(r"\d",text))

# text= "the price is 45 dollars, 30 cents and 50 rupees"
# print(re.findall(r"\d+",text))

# # finditer
# text= "i have 2 apples and 5 oranges"
# for match in re.finditer(r"\d+",text):
#     print(match.group() ,"at", match.start())

# # resub
# text="hello 123,welcome 456!"
# print(re.sub(r"\d+","number",text))

# # resplit
# text="apple, orange; banana, grape"
# print(re.split(r"[;,]",text))

# # grouping and caputuring
# text="john:34, alice:45, bob:22"
# print(re.findall(r"(\w+):(\d+)",text))

# # compiling regex
# pattern= re.compile(r"\d+")
# text="123 apples and 456 oranges"
# print(pattern.findall(text))

# # Regex Flags
# text="HELLO world"
# print(re.search(r"hello",text,re.IGNORECASE))

# # MULTILINE
# text="""first line
# second line
# third line """

# print(re.findall(r"^s\w+",text,re.MULTILINE))
# print(re.findall(r"\w+e$",text,re.MULTILINE))

# # re.dotall

# text="hello\nworld"
# print(re.search(r"hello.*world",text,re.DOTALL))

# # validation 
# email="user@example.com"
# if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$",email):
#     print("valid email")
# else:
#     print("invalid email")

# # data cleaning
# text="price: $123.45"
# print(re.sub(r"[^0-9.]","",text))

# # text extraction
# tweet="exicted for #python and following #openai!"
# print(re.findall(r"#\w+",tweet))
# print(re.findall(r"@\w+",tweet))

# # search and replace
# text="card: 1234-5678-9012-3456"
# print(re.sub(r"\d{4}-\d{4}-\d{4}-\d{4}","****-****-****-****",text))

# text="card: 1234-5678-9012-3456"
# print(re.sub(r"\d{4}-\d{4}-\d{4}","****-****-****",text))