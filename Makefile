.PHONY: run
run:
	@cd docs && docsify serve

.PHONY: install
install:
	@cd docs && npm i docsify
	@cd scripts/rules_builder && make install

.PHONY: build
build:
	@cd scripts/rules_builder && make run && make copy

.PHONY: test
test:
	@cd scripts/rules_builder && make test
