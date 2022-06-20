import requests


who = input("kime: ")  #number
msg = input("mesaj: ") #Message

resp = requests.post("https://textbelt.com/text" , {
    'phone':'{}'.format(who),
    'message':'{}'.format(msg),
    'key':'textbelt API key',  
})

print(resp.json())
