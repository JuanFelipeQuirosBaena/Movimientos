from django.db import models
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)# campo de fecha y hora que se establece automáticamente en el momento de la creación del registro, lo que permite rastrear cuándo se creó cada registro en la base de datos.
    first_name = models.CharField(max_length=50)# campo de texto para almacenar el primer nombre del registro, con una longitud máxima de 50 caracteres.
    last_name = models.CharField(max_length=50)# campo de texto para almacenar el apellido del registro, con una longitud máxima de 50 caracteres.
    email = models.EmailField(max_length=100)# campo de correo electrónico para almacenar la dirección de correo del registro, con una longitud máxima de 100 caracteres.
    phone_number = models.CharField(max_length=15)# campo de texto para almacenar el número de teléfono del registro, con una longitud máxima de 15 caracteres.
    address = models.CharField(max_length=100)# campo de texto para almacenar la dirección del registro, con una longitud máxima de 100 caracteres.
    city = models.CharField(max_length=50)# campo de texto para almacenar la ciudad del registro, con una longitud máxima de 50 caracteres.
    state = models.CharField(max_length=50)# campo de texto para almacenar el estado del registro, con una longitud máxima de 50 caracteres.
    zipcode = models.CharField(max_length=10)# campo de texto para almacenar el código postal del registro, con una longitud máxima de 10 caracteres.
    def __str__(self):# método especial que devuelve una representación legible del objeto Record, en este caso, el nombre completo del registro (primer nombre y apellido).
        return (f"{self.first_name} {self.last_name} - {self.email}")# devuelve una cadena que combina el primer nombre, el apellido y el correo electrónico del registro para facilitar su identificación en la interfaz de administración de Django u otras partes del sistema donde se muestre este modelo.

