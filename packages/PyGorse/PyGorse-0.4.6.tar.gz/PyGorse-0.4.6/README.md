# PyGorse

[![CI](https://github.com/gorse-io/PyGorse/actions/workflows/ci.yml/badge.svg)](https://github.com/gorse-io/PyGorse/actions/workflows/ci.yml)
[![](https://img.shields.io/pypi/v/pygorse)](https://pypi.org/project/PyGorse/)
![](https://img.shields.io/pypi/dm/pygorse)

Python SDK for gorse recommender system.

## Install

- Install from PyPI:

```bash
pip install PyGorse
```

- Install from source:

```bash
git clone https://github.com/gorse-io/PyGorse.git
cd PyGorse
pip install .
```

## Usage

Create a client by the entrypoint and api key.

```python
from gorse import Gorse

client = Gorse('http://127.0.0.1:8087', 'api_key')
client.get_recommend('zhenghaoz')
```
