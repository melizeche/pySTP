# pySTP

Implementación del Tablero de Control Presidencial de la STP

## Requirements

* Python 3.6
* Django 1.11

## Installation

Virtualenv is optional but strongly suggested
```
git clone git@github.com:melizeche/pytstp.git
cd pystp
virtualenv env -p python3.6
source env/bin/activate
pip install -r requirements.txt
```

## Usage
```
./manage.py migrate
./manage.py runserver localhost:5000
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## Credits

* Marcelo Elizeche Landó
* Cesar Rodas

## License

This project is licensed under the terms of the GPLv3 license - see the [LICENSE](LICENSE) file for details
