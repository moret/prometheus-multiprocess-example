import os
import random

from prometheus_client import (
    CollectorRegistry,
    Counter,
    generate_latest,
    multiprocess,
)

counter = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    [],
)


async def app(scope, receive, send):
    registry = CollectorRegistry()
    assert scope["type"] == "http"

    if scope["path"] == "/metrics-doc":
        multiprocess.MultiProcessCollector(registry)
        data = generate_latest(registry)
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    [b"content-type", b"text/plain"],
                    [b"x-pid", f"{os.getpid()}".encode("utf-8")],
                ],
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": data,
            }
        )
        return

    if scope["path"] == "/metrics-pr":
        data = generate_latest(multiprocess.MultiProcessCollector(registry))
        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    [b"content-type", b"text/plain"],
                    [b"x-pid", f"{os.getpid()}".encode("utf-8")],
                ],
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": data,
            }
        )
        return

    if scope["path"] == "/inc":
        inc = random.randint(1, 100)
        counter.inc(inc)

        await send(
            {
                "type": "http.response.start",
                "status": 200,
                "headers": [
                    [b"content-type", b"text/plain"],
                ],
            }
        )
        await send(
            {
                "type": "http.response.body",
                "body": f"pid: {os.getpid()} incremented request counter by {inc}".encode(
                    "utf-8"
                ),
            }
        )
        return

    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text/plain"],
            ],
        }
    )
    await send(
        {
            "type": "http.response.body",
            "body": b"Available paths: /metrics-doc, /metrics-pr, /inc",
        }
    )
