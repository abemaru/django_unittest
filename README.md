# django unittest study
Django, DjangoRESTFrameworkでテストを行うためにはどうすればいいのかを残しておくメモ


## djangoテストのファイル構造のサンプル
```
# 構造1
sample/
├─ foo/
│  ├─ tests/
│  │  ├─ foo_tests.py
├─ bar/
│  ├─ tests/
│  │  ├─ bar_tests.py

# 構造2
sample/
├─ foo/
├─ bar/
├─ tests/
│  ├─ foo_tests.py
│  ├─ bar_tests.py
```

## テストフレームワークについて
Djangoが提供するテストもあるみたいだけどpytestの方が使い勝手が良い？

### Django
```python
from django.test import TestCase

class SomeTest(TestCase):
  def test_foo(self):
	  self.assertEqual("hello", "hello")
```

### PyTest☆
```python
import pytest

@pytest.mark.unit
def test_foo():
  assert "hello" == "hello"
```
