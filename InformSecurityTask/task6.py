from requests import Session
from bs4 import BeautifulSoup as bs
import names

with Session() as s:
	name = names.get_first_name()+names.get_first_name()
	print(name)
	regist = {"txtUsername": name,"txtPassword":"name"}
	s.post("http://3.122.236.22/register",regist)
	site = s.get("http://3.122.236.22/register")
	print(site.content)
	login = {"txtUsername": name,"txtPassword":"name"}
	s.post("http://3.122.236.22/login",login)
	site = s.get("http://3.122.236.22/level1")
	print(site.content)
	site = s.post("http://3.122.236.22/03260ba26962d30022575756459ce5fe")
	print(site.content)
	bs_content = bs(site.content, "html.parser")
	token = bs_content.find("input", {"name":"csrf_token"})["value"]
	csrf_tok = {"txtUsername": name,"txtPassword":"name","csrf_token":token}
	site = s.post("http://3.122.236.22/level3", csrf_tok)
	print(site.content)
	bs_content = bs(site.content, "html.parser")
	number = bs_content.find("label").text
	print(number)
	numbers = number[:-1].split('+')
	sum = int(numbers[0]) + int(numbers[1])
	summa = str(sum)
	print(summa)
	num = {"captcha": summa}
	site = s.post("http://3.122.236.22/level4", num)
	print(site.content)


    




