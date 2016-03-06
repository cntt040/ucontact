import unittest
from preggy import expect
from model import ads


class TestLoadAd(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_load_ads_14_should_be_found(self):
        ad = ads.get_by_id(14)
        expect(ad.get('ad').get('ad_id')).to_equal('5')
