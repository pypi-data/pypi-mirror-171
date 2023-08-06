# generate mongo models automatically with `mongoengine`

### Installation

```bash
python -m pip install mongo-models
```

### Usage

```python
from mongo_dynamic_models import MongoModels

uri = 'mongodb://USER:PASSWORD@HOST_OR_IR:PORT/DB'

models = MongoModels(uri)

print(models.collection_names)


```