.PHONY:  help
.DEFAULT_GOAL := help

install: ## creates dev directories and install dependencies
	pipenv install --dev
	pipenv run pre-commit install
	cp commit-msg .git/hooks/

help: ## Displays a help message
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_\/-]+:.*?## / {printf "\033[34m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST) | \
		sort | \
		grep -v '#'

test: ## Execute the automated scenarios for WEB and API
	behave -f allure_behave.formatter:AllureFormatter -o report/reports/first_exec tests/features/
	ifeq ("$(wildcard ./rerun_failing.features)","")
		echo "Re execute the failed scenarios"
		behave -f allure_behave.formatter:AllureFormatter -o report/reports/re_exec @rerun_failing.features
		python -c "from core.utils.utils import delete_jsons_report; delete_jsons_report('report/reports/re_exec/')"
	endif
	allure generate report/reports/first_exec report/reports/re_exec --clean -o report/allure-report