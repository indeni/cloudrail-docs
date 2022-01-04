.PHONY: install
install:
	@bash install.sh

.PHONY: run
run:
	@. env/bin/activate && make pull && python3 template_generator.py

.PHONY: generate
generate:
	@make run

.PHONY: build
build:
	@make run
	@make copy

.PHONY: copy
copy:
	@cp -R output/* ../../docs/rules

.PHONY: test
test:
	@. env/bin/activate && make pull && pytest test.py

.PHONY: test-rule
test-rule:
	@. env/bin/activate && make pull && python3 test_rule.py

.PHONY: pull
pull:
	@cd knowledge && git pull && cd ../
