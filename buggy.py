import datetime
import httpx

"""
DO NOT MODIFY THIS FILE

WRITE YOUR TESTS IN test_buggy.py
"""

"""
1. Here is a function with a few edge cases.

See if you can write two distinct failing tests and a passing test.

Tip: To save time, you might want to use `pytest.mark.parametrize`
 since all of the tests will be in the format
"""


def gcd(a: int, b: int) -> int:
    """
    Greatest common divisor between two integers.
    """
    # Euclidean algorithm
    while b:
        a, b = b, a % b

    return a


"""
2. These functions expect a complex data structure, as one might load from a DB.

{"user": {"name": "...", "password": "...", "profile": "..."}}

Write a @pytest.fixture that returns a test user and use that to test the two functions below.

Each test should pass and only test one function.
"""


def format_user_html(user_dict: dict) -> str:
    return f"<b>{user_dict['user']['name']}</b><p>{user_dict['user']['name']}</p><span>{user_dict['user']['profile']}"


def validate_user_password(user_dict: dict, password: str) -> bool:
    return user_dict["user"]["password"] == password


"""
3. Here is a function where the tests would fail intermittently since it depends on the time.

A refactor would make sense usually, but let's say you need to test it as-is.

Write two tests that demonstrate both possible return values and pass consistently.
"""


def close_to_midnight():
    now = datetime.datetime.now()
    return (now.hour == 23 and now.minute >= 55) or (now.hour == 0 and now.minute <= 5)


"""
4. This function would make an http request to an API that returns JSON in the form:

    {"response": "OK", "value": [{"name": "Sherlock"}, {"name": "Watson"}]}

It would return ["Sherlock", "Watson"]

Write a passing test that mocks the `httpx.get` response.
"""


def extract_name(url):
    resp = httpx.get(url)
    data = resp.json()
    if data["response"] == "OK":
        return [v["name"] for v in data["value"]]
    else:
        return []


"""
5. This function has error conditions.

Write three passing tests that check for these conditions & the non-error case.

Tip: use `pytest.raises`
"""


def divide_all_by(nums: list[int], divisor: int) -> list[float]:
    if not nums or not all(isinstance(x, int) for x in nums):
        raise ValueError("nums must be a list of integers")
    if divisor == 0:
        raise ZeroDivisionError()
    return [num / divisor for num in nums]
