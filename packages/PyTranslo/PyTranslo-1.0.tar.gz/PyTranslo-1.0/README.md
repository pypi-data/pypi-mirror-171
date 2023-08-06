# PyTranslo
Python Client Library for Translo API. https://rapidapi.com/armangokka/api/translo

# Installing

```sh
pip install -U PyTranslo
```

# Usage

```python
from PyTranslo import PyTranslo

api = PyTranslo("<TOKEN>")

api.translate("Отличная библиотека", "en")  # "Excellent library"

api.translate("Knows many languages", "ru")  # "Знает много языков"

api.translate("没有必要指出翻译来自哪种语言。", "en")  # "There is no need to indicate which language the translation comes from."
api.translate("Но можно если нужно", "en", from_lang="ru")  # "But you can if you need"

api.detect("Что это за язык?") # "ru"
```
