import functools


def lru_cache[F](f: F) -> F:
    """A better version of `lru_cache` that retains argument information"""

    return functools.lru_cache(f)  # type: ignore
