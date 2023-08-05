## Installation:
```python
pip install dataframetranslationscoring
```
## Usage:
Given two folder paths , the translation_quantitative_scoring() function will return a dictionary with translation quality scores.
Example:
```python
import pandas as pd
import dataframetranslationscoring.scoring import translation_quantitative_scoring
metrics = translation_quantitative_scoring(original_dataframe_path="folder1/*.csv", translated_dataframe_path="folder2/*.csv")
```

This will return a dictionary with the following keys:
```python
{'words_percentage': 'X%',
 'characters_percentage': 'X%',
 'non_null_percentage': 'X%',
 'total_characters': X,
 'total_words_translated': 'X',
 'total_words_available': 'X'}
 ```
