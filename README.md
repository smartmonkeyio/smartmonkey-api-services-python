Publish

```bash

python setup.py sdist bdist_wheel
python3 setup.py sdist upload

```

Generate documentation

```bash

sphinx-build -a -E -b html -d docs/_build/doctrees docs docs/_build/html

```


# Develop

```
pip install -r requirements.txt
pip install pre-commit
pre-commit install
```
