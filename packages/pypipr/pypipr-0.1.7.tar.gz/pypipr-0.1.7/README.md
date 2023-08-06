# About
The Python Package Index Project (pypipr)


# Setup
Install with pip
```
python -m pip install pypipr
```

Test with
```python
from pypipr.pypipr import Pypipr
Pypipr.test_print()
```


# Feature

## Pypipr Class
`test_print()` memastikan module sudah terinstal dan dapat dijalankan
```python
from pypipr.pypipr import Pypipr
Pypipr.test_print()
```


## iconsole
`@Log()` / `Log decorator` akan melakukan print ke console. Mempermudah pembuatan log karena tidak perlu mengubah fungsi yg sudah ada. Berguna untuk memberikan informasi proses program yg sedang berjalan.

```python
from pypipr.iconsole import log

@log("Calling some function")
def some_function():
    ...
    return
```


## idatetime
`datetime_now()` memudahkan dalam membuat tanggal dan waktu untuk suatu timezone

```python
from pypipr.idatetime import datetime_now
datetime_now("Asia/Jakarta")
```
