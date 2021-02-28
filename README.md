### To deploy test framework:
1. Python at least 3.9 version
2. Install pipenv: `pip install pipenv`
3. Install required dependencies: `pipenv install`
4. Make sure all dependencies have been successfully installed writing: `pipenv graph`
5. Run tests and generate allure report: `pipenv run python -m pytest --alluredir=allure_reports`. Make sure that allure has locally installed, otherwise a report will not be generated
6. Look at allure report: `allure serve /allure_reports`  