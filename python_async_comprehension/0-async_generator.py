#!/usr/bin/env python3
"""This module implements an asynchronous random number generator."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield ten random floating-point numbers with one-second delays."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
