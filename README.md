# Proyecto Final "Blog" CODERHOUSE

Este proyecto **"Blog"** fue relizado por **Jorge Guzmán** y **Juan Almazán**. El lenguaje de programación es **Python** 3.9 bajo el framework **Django** 4.0.5.

Este Blog cuenta con Publicaciones, Búsqueda de publicaciones, Comentarios a publicaciones, Registro a newsletter, Registro de usuarios, Registro de Perfi de usuarios, Acerca de, Autenticación y la sección admin de Django.


Presentación del Blog:
https://www.youtube.com/watch?v=qR96RRRqe-I

Portal on-line Heroku:
https://blog-python-coderhouse.herokuapp.com/


Bajo la metodología agil del marco de trabajo en Scrum nos organizamos para que cada uno realizara tareas específicas, al localizarnos en latitudes diferentes, utilizamos Trello donde definimos los requirimientos y construimos las tarjetas como tareas a realizar en un tiempo determinado.

- Creación de proyecto base (Jorge)
- Layout y CSS (Jorge)
- Profile (Jorge)
- Post (Juan)
- Comment (Juan)
- Acercade (Juan)
- Home (Jorge)
- Authenticacion (Jorge)
- Buscador (Jorge)



Instrucciones de instalación
===
1.- Clonar proyecto de Github por ssh o https
---
	git clone git@github.com:jorgeald77/coders-django-blog.git


2.- Al clonarlo descargará la siguiente estructura del proyecto
---
	- coders-django-blog
		- .git
		- .gitignore
		- README.md
		- app


2.1- Ingresar a la carpeta coders-django-blog
---
	cd coders-django-blog


3.- Instalar entorno virtual dentro de la carpeta "coders-django-blog"
---
	python3 -m venv env
	
	La estructura de directorio quedara de la siguiente manera:
		- coders-django-blog
			- .git
			- .gitignore
			- README.md
			- app
			- env


3.1- Levantar entorno virtual
---
	source env/bin/activate


3.2- Ingresar a la carpeta app
---
	cd app


4.- Instalar dependencias, cerciorarse que el entorno virtual se este ejecutando, siempre que trabajamos en el proyecto.
---
	requerimiento: tener instaldo postgresql ya que es requerido por unas dependencias.
	
	pip install -r requirements.txt --no-cache
	pip freeze (Para verificar que se instalaron las dependencias)


5.- Crear archivo .env de variables de entorno, ojo es un archivo oculto
---
	cp .env.example .env


6.- Generar llave secreta con la shell 
---
	python manage.py shell

	"En la terminal importar la siguiente librería."

	from django.core.management.utils import get_random_secret_key
	print(get_random_secret_key())
	
	La función en el print nos arrojara una llave aleatoria, hay que copiarla


6.1.- Editar archivo .env y pegar la llave generada en SECRET_KEY, dejar el archivo de la siguiente manera, con tu llave generada.
---
	DEBUG=True
	SECRET_KEY=PEGAR_AQUI_LA_LLAVE_GENERADA_EN_EL_PASO_ANTERIOR
	ALLOWED_HOSTS=*,


7.- Crear y ejecutar migraciones
---
	python manage.py makemigrations
	python manage.py migrate


8.- Crear super usuario de Django
---
	python manage.py createsuperuser


9.- Generar statics
---
	python manage.py collectstatic
	
	
10.- Ejecutar servidor web
---
	python manage.py runserver
