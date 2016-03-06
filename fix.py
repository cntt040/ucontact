from alphaid import AlphaID
from model.schemas import *



ALPHABET = 'QAZXSWWEDCVFRTGBNHYUJMKIOL'
LEN = 6
SALT = 165123

sql = "select * from referral where code in (select code from referral group by code having count(code) >1)"
query = Referral.raw(sql)
tmp = []
code = AlphaID(ALPHABET, LEN)
for item in query:
    if item.code in tmp:
        ref_code = code.encode(SALT + item.user_id)
        Referral.update(code=ref_code).where(Referral.id == item.id).execute()
    else:
        tmp.append(item.code)



