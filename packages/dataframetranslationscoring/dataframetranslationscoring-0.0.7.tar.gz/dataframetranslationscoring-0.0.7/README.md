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

This will print the following:
```python
Percentage of words translated vs available: X %
Percentage of characters translated vs available: X %
Percentage of non-null translations: X %
Total number of characters to be translated: X
Total number of words translated/available: X/X
Total number of characters translated/available: X/X
 ```

and return a dictionary with the following keys:
```python
{'words_percentage': 'X%',
 'characters_percentage': 'X%',
 'non_null_percentage': 'X%',
 'total_characters': X,
 'total_words_translated/available': 'X/X',
 'total_characters_translated/available': 'X/X'}
 ```