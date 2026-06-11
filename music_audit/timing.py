from time import perf_counter


class Timer:
    def __init__(self):
        self.start = perf_counter()

    @property
    def elapsed(self) -> float:
        return perf_counter() - self.start
