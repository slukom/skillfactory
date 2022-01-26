import pytest
from api import PetFriends
from settings import valid_email, valid_password

@pytest.fixture()
def some_data():
    return 42

def test_some_data(some_data):
    assert some_data == 42

@pytest.fixture()
def get_key(self):
   self.pf = PetFriends()
   _, status, self.key = self.pf.get_api_key(valid_email, valid_password)
   assert status == 200
   assert 'key' in self.key
   return self.key

def test_getAllPetsWithValidKey(self, get_key, filter=''):  # filter available values : my_pets
   _, status, result = self.pf.get_list_of_pets(self.key, filter)
   assert status == 200
   assert len(result['pets']) > 0

   