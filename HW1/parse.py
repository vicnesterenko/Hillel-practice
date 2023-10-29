from urllib import parse
from urllib.parse import parse_qs, urlparse


# method 1
def parse_1(query: str) -> dict:
    query_dict = parse.parse_qs(parse.urlsplit(query).query)
    return {
        key: value[0] if len(value) == 1 else value for key, value in query_dict.items()
    }


# method 2
def parse_2(query: str) -> dict:
    res = parse_qs(
        urlparse(query).query
    )  # parse_qr -> return key query set -> {'name': ['ferret'], 'color': ['purple']}
    # print(res)
    for key, value in res.items():
        res[key] = value[0]  # first value
    return res  # or return {key: values[0] for key, values in query_dict.items()}


if __name__ == "__main__":
    assert parse_1("https://example.com/path/to/page?name=ferret&color=purple") == {
        "name": "ferret",
        "color": "purple",
    }

    assert parse_2("https://example.com/path/to/page?name=ferret&color=purple") == {
        "name": "ferret",
        "color": "purple",
    }

    assert parse_1("https://example.com/path/to/page?name=ferret&color=purple&") == {
        "name": "ferret",
        "color": "purple",
    }
    assert parse_2("https://example.com/path/to/page?name=ferret&color=purple&") == {
        "name": "ferret",
        "color": "purple",
    }
    assert parse_1("http://example.com/") == {}
    assert parse_1("http://example.com/?") == {}
    assert parse_1("http://example.com/?name=John") == {"name": "John"}

    # own assert test + doc

    assert parse_2(
        "http://docs.python.org:80/3/library/urllib.parse.html?"
        "highlight=params#url-parsing"
    ) == {
        "highlight": "params",
    }
    assert parse_2("http://example.com/") == {}
    assert parse_2("http://example.com/?") == {}
    assert parse_2("http://example.com/?name=Vic") == {"name": "Vic"}
