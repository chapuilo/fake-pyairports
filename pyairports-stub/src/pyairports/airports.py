import random, string
def _rand(n: int = 12) -> str:
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=n))
AIRPORT_LIST = _rand()
__all__ = ["AIRPORT_LIST"]
