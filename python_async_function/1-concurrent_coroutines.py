#!/usr/bin/env python3
"""Run several random-delay coroutines concurrently."""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return random delays in completion order without sorting."""
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = []
    for completed in asyncio.as_completed(tasks):
        results.append(await completed)
    return results
