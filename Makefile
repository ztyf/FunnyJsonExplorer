PYTHON := python3
SRC_DIR := src
TEST_DIR := test
MAIN := $(SRC_DIR)/funny_json_explorer.py
TEST_MAIN := $(TEST_DIR)/test_funny_json_explorer.py

.PHONY: all clean test

all:
	@echo "使用方法:"
	@echo "  make run        : 运行主程序"
	@echo "  make test       : 运行测试"

run:
	PYTHONPATH=$(shell pwd)/$(SRC_DIR) $(PYTHON) $(MAIN)

test:
	PYTHONPATH=$(shell pwd)/$(SRC_DIR) $(PYTHON) $(TEST_MAIN)

