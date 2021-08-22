import random
import string
id=''
otp_list=list(string.ascii_letters + string.digits)
for i in range(6):
   id+=random.choice(otp_list)
print(id)
