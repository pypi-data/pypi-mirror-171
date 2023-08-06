# complice-api
Python wrapper for the [Complice](https://complice.co) API.

> :construction: The Complice API is in early alpha mode.  Use at your own risk.

## Installation
```bash
pip install complice-api
```

## Usage
```python
from complice import CompliceAPI

# replace with your auth token, found at https://complice.co/apiclient/docs
complice = CompliceAPI('<AUTH_TOKEN>') 

complice.get_goals()
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


## License
[MIT](https://choosealicense.com/licenses/mit/)
