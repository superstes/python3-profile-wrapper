from cProfile import Profile
from io import StringIO
from pstats import Stats
from typing import callable


def main(target: callable, args: list = None, kwargs: dict = None, lines: int = 20, sort: str = 'tottime') -> str:
    if args is None or not isinstance(args, list):
        args = []

    if kwargs is None or not isinstance(kwargs, dict):
        kwargs = {}

    p = Profile()
    p.enable()

    main(*args, **kwargs)

    p.disable()

    s = StringIO()
    ps = Stats(p, stream=s).sort_stats(sort)
    ps.print_stats(lines)
    return s.getvalue()
