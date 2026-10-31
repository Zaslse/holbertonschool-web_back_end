#!/usr/bin/env python3
"""Generate ten random floating-point values asynchronously."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield ten random floats from zero to ten, one per second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
