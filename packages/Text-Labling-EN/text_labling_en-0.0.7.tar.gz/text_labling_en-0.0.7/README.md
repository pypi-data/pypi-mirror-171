# Text_Labling_EN

Text_Labling_EN is a Python package for Auto labeling English text using the Bart model and then exporting visuals to a pptx file

## Installation
```bash

pip install Text_Labling_EN
```

## Usage

```python
from Text_Labling_EN import *


Text_Labling=Text_Labling(r'path','col_name','NewCol','Lem' or 'stem' or 'None')
Text_Labling.cleanData()

Text_Labling.DoLabels([labels])

Text_Labling.doVis(number of top N want to visualize)

```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)


