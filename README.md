<div align="center">
<p align="center">
<img src="https://raw.githubusercontent.com/pystorage/pydownloads/master/docs/source/images/logo.png" alt="PyDownloads">
</p>

![PyPI](https://img.shields.io/pypi/v/pydownloads)
[![Downloads](https://pepy.tech/badge/pydownloads)](https://pepy.tech/project/pydownloads)
![GitHub](https://img.shields.io/github/license/pystorage/pydownloads)

</div>

## Installation

```shell
pip install pydownloads
```

## Documentation

### Total downloads

```python
from pydownloads import Stats
```

#### Parameters:

- package_name (string) - Python package name

##### Code

```python
from pydownloads import Stats


stats = Stats('pykeyboard')
print(stats.total)
```

##### Result

1292
