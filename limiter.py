from time import time
from starlette.exceptions import HTTPException

from config import AMOUNT_LIMITS_CONFIG
from redis import Redis


class Limiter:
    def __init__(self, func):
        self.func = func
        self.redis = Redis(host='redis', decode_responses=True)

    def __call__(self, *args, **kwargs):
        now: int = int(time())  # get the current time
        limit: str or None = self.is_limited(now)  # get error message if the limit is exceeded else None
        if limit is None:  # if the limit is not exceeded
            self.write_request(now)
            return self.func(*args, **kwargs)
        raise HTTPException(status_code=400, detail=limit)

    def is_limited(self, time_now: int) -> str or None:
        for seconds, limit in AMOUNT_LIMITS_CONFIG.items():  # get conditions from AMOUNT_LIMITS_CONFIG and check the limit
            if limit <= self.get_requests_count(time_now, seconds):  # if limit == requests per x seconds
                return f'amount limit exceeded ({limit}/{seconds}sec)'
        return None

    def write_request(self, time_now: int):
        requests_per_second: int or None = self.redis.get(
            time_now)  # get the number of requests for the current second. "None" if the first request in this second
        if requests_per_second is None:
            self.redis.set(time_now, 1)  # create value
        else:
            self.redis.set(time_now, int(requests_per_second) + 1)  # rewrite value

    def get_requests_count(self, time_now: int, seconds: int) -> int:
        keys = [time_now - x for x in range(seconds)]
        values = [0 if x is None else int(x) for x in self.redis.mget(keys)]
        return sum(values)  # return the sum of all requests for a certain period of time
