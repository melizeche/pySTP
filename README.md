# pySTP

Implementación del Sistema de Planificación por Resultado(SPR) Tablero de Control Presidencial(TCP) de la Secretaría Técnica de Planificación

## Requirements

* Python 3.6
* Django 1.11
* Django REST Framework 3.6

## Installation

You need to install python3 and optionally virtualenv

```bash
sudo apt-get install python3 virtualenv -y
```

Virtualenv is optional but strongly suggested
```
git clone https://github.com/melizeche/pySTP.git
cd pySTP
virtualenv env -p python3
source env/bin/activate
pip install -r requirements.txt
```

## Usage
```
./manage.py migrate
./manage.py createsuperuser
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
