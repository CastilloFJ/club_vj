************************************************************
PROYECTO: CLUB V.J. - CATÁLOGO DIGITAL DINÁMICO
CURSO: FULLSTACK PYTHON (MÓDULO 6)
AUTOR: JOSE CASTILLO FUENMAYOR
************************************************************

1. DESCRIPCIÓN DEL PROYECTO
Este MVP es un catálogo digital para el "Club V.J.", desarrollado con Django. 
Permite la visualización de videojuegos, géneros y plataformas con acceso 
restringido y beneficios exclusivos para usuarios VIP.

2. REQUISITOS PREVIOS
- Python 3.10+
- Framework Django 4.2+
- Navegador Web (Chrome/Edge recomendado)

3. GUÍA DE EJECUCIÓN
Para poner en marcha el servidor local, siga estos pasos:
   a. Abra una terminal en la carpeta raíz del proyecto (donde está manage.py).
   b. Ejecute el comando: python manage.py runserver
   c. Acceda a la URL: http://127.0.0.1:8000/

4. CREDENCIALES DE ACCESO
El sistema cuenta con los siguientes perfiles configurados en db.sqlite3:

   A. ADMINISTRADOR (Superuser)
      - Usuario: admin
      - Contraseña: 1234

   B. USUARIO ESTÁNDAR (No VIP)
      - Correo: alicate@mail.com
      - Contraseña: 12345
      - Nota: No puede ver lanzamientos del año 2026.

   C. USUARIO VIP
      - Correo: alambrito@mail.com
      - Contraseña: 12345
      - Nota: Tiene acceso total al catálogo, incluyendo estrenos 2026.

5. NOTA TÉCNICA
El proyecto implementa filtros personalizados en el panel de administración 
(/admin) y una lógica de protección de datos mediante el decorador @login_required 
y validaciones en el servidor para el contenido VIP.
************************************************************