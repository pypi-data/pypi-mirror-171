# Introduction 
This is a project to expose some of the utility tools used by givvable for easy version and use in projects throughout our code.

To use this repo,

`pip install givvableutils`

## DB & Blob
Helps connect to postgresql DB & Azure datalake

```python3
import db
db.get_conn(username='', password='', database='', host='')
db.close_conn()

import blob
blob.initialize_storage_account(storage_account_name='', storage_account_key='')
blob.list_directory_contents(container="data-synapse", directory="staging")
```

# Developing
To install givvableutils, along with the tools you need to develop and run tests, run the following in your virtualenv:

```bash
pip install -e .[dev]
python3 setup.py bdist_wheel
python3 setup.py sdist
twine upload --skip-existing dist/*
```