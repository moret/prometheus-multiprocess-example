Install and run:

```sh
make
make run-api
```

Increment counter a bit:

```sh
curl localhost:8000/inc
curl localhost:8000/inc
curl localhost:8000/inc
curl localhost:8000/inc
curl localhost:8000/inc
```

Check if results are consistent:

```sh
curl -vs localhost:8000/metrics-doc
curl -vs localhost:8000/metrics-doc
curl -vs localhost:8000/metrics-doc
```

vs.

```sh
curl -vs localhost:8000/metrics-pr
curl -vs localhost:8000/metrics-pr
curl -vs localhost:8000/metrics-pr
```
