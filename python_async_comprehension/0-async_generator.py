#!/usr/bin/env python3
"""Module that generates random numbers asynchronously."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Generate ten random numbers with a one-second delay."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
