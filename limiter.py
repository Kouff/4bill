from time import time
from starlette.exceptions import HTTPException

from config import AMOUNT_LIMITS_CONFIG


class Limiter:
    requests = {}

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        now = int(time())
        limit = self.is_limited(now)
        if limit is None:
            self.write_request(now)
            return self.func(*args, **kwargs)
        raise HTTPException(status_code=400, detail=limit)

    def is_limited(self, time_now):
        for seconds, limit in AMOUNT_LIMITS_CONFIG.items():  # {10: 1000, 60: 3000, 3600: 20000}
            if limit <= self.get_requests_count(time_now, seconds):
                return f'amount limit exeeded ({limit}/{seconds}sec)'
        return None

    def write_request(self, time_now):
        requests_per_second = Limiter.requests.get(time_now)
        if requests_per_second is None:
            Limiter.requests[time_now] = 1
        else:
            Limiter.requests[time_now] = requests_per_second + 1

    def get_requests_count(self, time_now, seconds):
        return sum([Limiter.requests.get(time_now - x, 0) for x in range(seconds)])
