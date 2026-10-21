# import mymodule

# print(mymodule.greet("jack"))
# print(mymodule.greet1("john"))

# from mymodule import greet,greet1,greet2
# print(greet("james"))

# import mymodule as m
# print(m.greet2("pedri"))

# # built-in modules

# #operating system 
# import os
# print(os.name)

# # maths
# import math
# print(math.sqrt(16))
# print(math.factorial(5))

# # ṣystem
# import sys
# print(sys.version)

# # datetime
# from datetime import datetime
# now = datetime.now()
# print(now) 

# Matplotlib 

# import matplotlib.pyplot as plt

# x=[1,2,3,4,5]
# y=[12,25,33,42,57]
# plt.plot(x,y)
# plt.show() 

# # BeautifulSoup:Web scraping

from bs4 import BeautifulSoup
import requests

page = requests.get("https://facebook.com")
soup= BeautifulSoup(page.content,'html.parser')
print(soup.title.text)

# HTTP Requests
# import requests
# response=requests.get('https://api.github.com')
# print(response.status_code)