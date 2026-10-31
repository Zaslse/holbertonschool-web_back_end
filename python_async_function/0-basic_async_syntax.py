#!/usr/bin/env python3
"""Provide a coroutine that waits for a random duration."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Sleep for and return a random delay up to max_delay seconds."""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
