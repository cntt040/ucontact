import random
import string

from appcore.connection import acc_couchdb


def randomcode(length):
    return ''.join(random.choice(string.uppercase) for i in range(length))


def count_ads(account_id, ads_type=None):
    num_ads = list(acc_couchdb.query("account_ad/get_ads_by_state", reduce="true", descending="true",
                                     key=[int(account_id), "{}".format(ads_type)]))
    if len(num_ads) > 0:
        a = num_ads.pop()
        return a["value"], True
    else:
        return 0, True

