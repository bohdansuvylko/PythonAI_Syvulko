import requests
# response = requests.get("https://uaserials.pro/films/")
# print(response.content)
# print(type(response.content))
# response = requests.post("https://httpbin.org/", data="Test data")
# headers = {'h1':"Test title"}
# print(response.text)

response = requests.get("https://coinmarketcap.com/")
responce_text = response.text
responce_parse = responce_text.split("<span>")
for pars_elem_1 in responce_parse:
    if pars_elem_1.startswith('$'):
        for pars_elem_2 in pars_elem_1.split('</span>'):
            if pars_elem_2.startswith('$') and pars_elem_2[1].isdigit():
                print(pars_elem_2)
