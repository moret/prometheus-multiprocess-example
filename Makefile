PROMETHEUS_MULTIPROC_DIR=/tmp/prometheus-multiprocess-example

configure:
	pip install -r requirements.txt

run-api:
	mkdir -p $(PROMETHEUS_MULTIPROC_DIR)
	rm -rf $(PROMETHEUS_MULTIPROC_DIR)/*
	PROMETHEUS_MULTIPROC_DIR=$(PROMETHEUS_MULTIPROC_DIR) uvicorn --workers 2 main:app
