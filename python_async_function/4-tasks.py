#!/usr/bin/env python3
"""Collect completion-ordered results from asyncio tasks."""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run n scheduled tasks and return their delays in finish order."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for completed in asyncio.as_completed(tasks):
        results.append(await completed)
    return results
