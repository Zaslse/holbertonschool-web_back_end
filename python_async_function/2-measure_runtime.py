#!/usr/bin/env python3
"""Measure average runtime for concurrent random waits."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return elapsed seconds per coroutine for a concurrent run."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
