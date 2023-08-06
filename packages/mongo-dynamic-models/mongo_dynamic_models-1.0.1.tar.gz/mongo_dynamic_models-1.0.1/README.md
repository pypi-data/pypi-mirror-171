# generate mongo models automatically with `mongoengine`

### Installation

```bash
python -m pip install mongo-dynamic-models
```

### Usage

```python
from mongo_dynamic_models import MongoModels

uri = 'mongodb://USER:PASSWORD@HOST_OR_IR:PORT/DB'

models = MongoModels(uri)

print(models.collection_names)
print(models)
print(models.collection_names)
print(models.users.objects)
print(models['users'].objects)
```