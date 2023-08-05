
## Pre-steps
1. Get pyenv going and install multiple python versions (.python-version) file


## Steps
1. Install your Poetry environment `poetry install`
2. Add the test repo for Pypi `poetry config repositories.testpypi https://test.pypi.org/legacy/`
3. Add your test key for the Test Pypi repo `poetry config http-basic.testpypi __token__ pypi-your-api-token-here`
4. Add your production ket for Pypi repo `poetry config pypi-token.pypi pypi-your-token-here`



### Dev
1. Open a Poetry shell
    - `poetry shell`

### Builds
4. Test your build `poetry build`
5. Publish the package
    - test -> `poetry publish -r testpypi`
    - prod -> `poetry publish`
