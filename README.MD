# Proyecto de Cómputo en la nube | ITS

![alt text](https://raw.githubusercontent.com/seulsale/proyecto-cloud/master/static/images/cloud.png?token=AE5JUXTH2JEKQIYUQSCUCWS6QJUNE "Cloud Icon")

#### Demostración de implicaciones/consideraciones.

1. Trabajo entre NUBE1 - NUBE2.
2. Trabajo entre NUBE y desarrollo local.
3. Subir un desarrollo local a la nube.

**Dependencias del proyecto:**
- python3.6
- pip
- virtualenv
- Microsoft ODBC Driver (opcional)

**Pasos para ejecutarlo:**
```
git clone https://github.com/seulsale/proyecto-cloud.git
cd proyecto-cloud
```
```
virtualenv venv
.\venv.\Scripts\activate (Windows)
pip install -r requirements.txt
```
```
python manage.py migrate
python manage.py runserver
```
