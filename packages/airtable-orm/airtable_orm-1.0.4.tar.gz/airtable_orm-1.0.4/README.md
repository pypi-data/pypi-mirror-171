# Python ORM for Airtable tables

## Installation

```
pip install airtable-orm
```

## Usage
```python
from dataclasses import dataclass
# Importing library
from airtable_orm import AirtableORM

# Initialize the object and get the session
orm = AirtableORM("airtable://:<YOUR API KEY>@<YOUR APP KEY>")
session = orm.get_session()

# Create your data class with properties same as your Airtable tables
# The name of the class muse be matched to the Airtable table name
@dataclass
class MyEntity:
    id: str
    name: str

# Create new object for the dataclass
new_entity = MyEntity("id#1", "My name")

# Run add() to create new entry
session.add(new_entity)

# Run commit() to save the data to Airtable
session.commit()
```

To list all the data as object

```python
data = session.query(MyEntity).all()
for _ in data:
    print(_.name)
```



