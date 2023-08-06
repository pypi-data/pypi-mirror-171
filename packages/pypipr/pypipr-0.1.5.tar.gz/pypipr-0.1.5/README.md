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


## console
`@Log()` / `Log decorator` akan melakukan print ke console. Mempermudah pembuatan log karena tidak perlu mengubah fungsi yg sudah ada. Berguna untuk memberikan informasi proses program yg sedang berjalan.

```python
from pypipr.console import log

@log("Calling some function")
def some_function():
    ...
    return
```
