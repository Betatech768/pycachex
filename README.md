##  Introduction

**pycachex** is a Redis-inspired in-memory key-value cache server built from scratch in **Python** to explore how real-world cache systems work internally.

Rather than focusing on framework abstractions, this project dives into **low-level backend fundamentals** such as TCP networking, protocol design, concurrency, and data-structure-driven performance. The server communicates over a custom text-based protocol, supports multiple concurrent clients using `asyncio`, and implements essential cache features including key expiration (TTL) and LRU eviction.

This project is intentionally designed as a learning-focused systems exercise, aiming to answer practical questions like:
- How does a cache server handle multiple concurrent connections?
- How do TTL and key expiration actually work under the hood?
- Why do data structure choices matter for performance?
- How can an in-memory system recover after a crash?

While not intended to replace Redis in production, **pycachex** serves as a clear, educational implementation that demonstrates the core ideas behind modern in-memory databases and cache servers.
