from http import cookies
from http.cookies import SimpleCookie

# BaseCookie.load(rawdata)
# If rawdata is a string, parse it as an HTTP_COOKIE and add the values found there as Morsels.
# If it is a dictionary, it is equivalent to:
# for k, v in rawdata.items():
#    cookie[k] = v


# method 1
def parse_cookie_1(query: str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)
    cookies_dict = {}
    for key, morsel in cookie.items():
        cookies_dict[key] = morsel.value  # Morsel.value -> The value of the cookie
    return cookies_dict


# method 2
def parse_cookie_2(query: str) -> dict:
    cookie_dict = dict(SimpleCookie(query))
    for key, value in cookie_dict.items():
        cookie_dict[key] = value.value  # Morsel.value -> The value of the cookie
    return cookie_dict


if __name__ == "__main__":
    assert parse_cookie_1("name=John;") == {"name": "John"}
    assert parse_cookie_1("") == {}
    assert parse_cookie_1("name=John;age=28;") == {"name": "John", "age": "28"}
    assert parse_cookie_1("name=John=User;age=28;") == {
        "name": "John=User",
        "age": "28",
    }
    # own assert tests + from python doc
    assert parse_cookie_1('keebler="E=everybody; L=\\"Loves\\"; fudge=\\012;";') == {
        "keebler": 'E=everybody; L="Loves"; fudge=\n;'
    }
    assert parse_cookie_2("name=Vic; surname=Nesterenko") == {
        "name": "Vic",
        "surname": "Nesterenko",
    }
    assert parse_cookie_2("") == {}
    assert parse_cookie_2("name=Vic;age=22;;;;#") == {"name": "Vic", "age": "22"}
    assert parse_cookie_2("name=Vic=User;age=22;") == {
        "name": "Vic=User",
        "age": "22",
    }
