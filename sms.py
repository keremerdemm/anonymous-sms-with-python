
import requests


resp = requests.post("https://textbelt.com/text" , {
    'phone':'number',    
    'message':'message',      #MESAJ
    'key':'textbelt API key', 

})

print(resp.json())
