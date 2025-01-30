USER = {"model": "users.user",
        "pk": 100,
        "fields": {"first_name": "Alan",
                   "last_name": "Sapid",
                   "username": "BestAlan",
                   "password": "3Al"}
        }

VALID_CREATE_USER = {"username": "BestAlan",
                     "first_name": "Alan",
                     "last_name": "Sapid",
                     "password1": "3Al",
                     "password2": "3Al"}

MISSING_FIELDS_USER = {"username": "BestAlan",
                       "first_name": "",
                       "last_name": "",
                       "password1": "3Al",
                       "password2": "3Al"}

USER2 = {"model": "users.user",
         "pk": 101,
         "fields": {"username": "123123",
                    "first_name": "Qwerty",
                    "last_name": "Qwer",
                    "password": "12345"}
         }

USER2UPDATE = {"username": "AidD",
               "first_name": "Qwerty",
               "last_name": "Qwer",
               "password": "12345",
               "password2": "12345"}

