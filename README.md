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

### Download statistics

#### Parameters:

- package_name (string) - python package name

##### Code

```python
from pydownloads import Stats


stats = Stats('pykeyboard')
```

### Total downloads

##### Code

```python
from pydownloads import Stats


stats = Stats('pykeyboard')
print(stats.total)
```

##### Result

1419

### Total 7 days

##### Code

```python
from pydownloads import Stats


stats = Stats('pykeyboard')
print(stats.week)
```

##### Result

240

### Total 30 days

##### Code

```python
from pydownloads import Stats


stats = Stats('pykeyboard')
print(stats.month)
```

##### Result

1068

### Custom count

#### Parameters:

- days (integer) - amount of days. `No more than 30 days`
- version (string, default None) - package version

##### Code

```python
from pydownloads import Stats


stats = Stats('pykeyboard')
print(stats.custom_count(3, '0.1.0'))
```

##### Result

127
