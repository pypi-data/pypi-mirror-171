# Python ORM for Airtable tables

## Installation

```
pip install airtable-orm
```

## Usage
```python
from airtable_orm import AirtableORM
from dataclasses import dataclass

orm = AirtableORM("airtable://:<YOUR API KEY>@<YOUR APP KEY>")
session = orm.get_session()

@dataclass
class MyEntity:
    id: str
    name: str

new_entity = MyEntity("id#1", "My name")
session.add(new_entity)
session.commit()
```



