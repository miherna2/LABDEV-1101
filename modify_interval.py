import requests

TOKEN = input("Provide Token: ")
AID = input("Provide aid: ")
HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/hal+json",
    "Authorization": f"Bearer {TOKEN}",
}


def get_test_ids(headers, aid):
    url = f"https://api.thousandeyes.com/v7/tests?aid={aid}"
    response = requests.get(url, headers=headers).json()
    tests = response.get("tests")
    test_ids = [test.get("testId") for test in tests]
    return test_ids


def modify_test(headers, test_ids, aid):
    payload = '{"interval": 900, "description": "API Modification"}'
    for test_id in test_ids:
        url = f"https://api.thousandeyes.com/v7/tests/http-server/{test_id}?aid={aid}"
        response = requests.put(url, headers=headers, data=payload)
        print(response.text)


def main():
    test_ids = get_test_ids(HEADERS, AID)
    change_interval = modify_test(HEADERS, test_ids, AID)


if __name__ == "__main__":
    main()
