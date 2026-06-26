from django.shortcuts import redirect, render#permite cambiar la plantilla  html con datos  y devolver respuesta

# Esta es la función que se ejecuta cuando entras a la página
# login para incio de sesion  segun el rol
#logout para cerrar sesion
from django.contrib.auth import authenticate, login, logout# type: ignore # Importamos las funciones de autenticación, inicio de sesión y cierre de sesión de Django.
from django.contrib import messages # type: ignore #
from.forms import UserRegisterForm, RecordForm # type: ignore # Importamos el formulario de registro de usuarios personalizado que hemos creado en forms.py.
from.models import Record

def home(request):# type: ignore
    #si el metodo  de la solicitud  es post, significa que se esta  enviado un formulario
    # post esta enviando informacion

    #-----------------------------------------------


    #-----------------------------------------------
    record = Record.objects.all()
    if request.method =='POST': # pyright: ignore[reportUnknownMemberType]
        # si  el metodo  de la solicitud  post  significa que se esta en viando el formulario
        # aqui podemos manehjar  la logica del formulario  como la autentificacion del usuario
        username = request.POST['username'] # pyright: ignore[reportUnknownVariableType, reportUnusedVariable, reportUnknownMemberType] #  ontiene este valor des de  formulario
        password = request.POST['password'] # type: ignore
        user = authenticate(request, username=username, password= password) # type: ignore
        if user is not None: # valor o nulo
            login(request, user) # pyright: ignore[reportUnknownArgumentType] # indicando la sesion
            #muestra el mensaje de exito
            messages.success(request,"ingresado exitosamente") # pyright: ignore[reportUnknownArgumentType]
            return redirect('home')
        else:
            # si las credenciales no fueron existosas
            messages.error(request," las credenciales son invalidas !!📢") # pyright: ignore[reportUnknownArgumentType]
            return render(request, 'home.html', {})  # type: ignore
    else:
        # si el metodo  de la solicitud no es POST, simplemente renderiza la plantilla 'home.html
         return render(request, 'home.html', {'records':record})# type: ignore # El tercer argumento es un diccionario para pasar datos a la plantilla, pero aquí lo dejamos vacío por ahora.
# funcion para logiar
def login_user(request): # type: ignore
    pass


# funcion para poder salir  cerrar sesion
def logout_user(request): # type: ignore
    logout(request)# cierre de la sesion del usuario
    #muestra un mensaje de exito al usuario
    messages.success(request,"cerraste la session correctamente")
    return redirect('home')# direccionar al usuario a la pafina de inicio


# funcion para registrar un nuevo usuario
def register_user(request):# type: ignore
    # si el metodo de la solicitud es POST, significa que se esta enviando el formulario de registro
    if request.method == 'POST': # pyright: ignore[reportUnknownMemberType]
        form = UserRegisterForm(request.POST) # type: ignore # crea una instancia del formulario de registro de usuarios con los datos enviados en la solicitud POST
        if form.is_valid(): # type: ignore# verifica si el formulario es válido, es decir, si los datos cumplen con las reglas de validación definidas en el formulario
            form.save() # type: ignore# si el formulario es válido, guarda el nuevo usuario en la base de datos
            username = form.cleaned_data['username'] # type: ignore # obtiene el nombre de usuario del formulario limpio, es decir, después de que se han aplicado las validaciones y se han limpiado los datos
            password = form.cleaned_data['password1'] # type: ignore # obtiene la contraseña del formulario limpio, es decir, después de que se han aplicado las validaciones y se han limpiado los datos
            user = authenticate(request, username=username, password=password) # type: ignore # autentica al usuario recién registrado utilizando el nombre de usuario y la contraseña proporcionados
            login(request, user) # type: ignore# inicia sesión para el usuario autenticado, lo que significa que el usuario ahora está conectado a la aplicación
             # muestra un mensaje de éxito al usuario indicando que el registro fue exitoso    
            messages.success(request,"registro exitoso") # type: ignore
            return redirect('home')# redirige al usuario a la página de inicio después de un registro exitoso
    else:
        form = UserRegisterForm() # type: ignore # crea una instancia del formulario de registro de usuarios vacía para mostrar en la plantilla cuando el método de la solicitud no es POST, es decir, cuando el usuario accede a la página de registro por primera vez
    return render(request, 'register.html',{'form': form})# type: ignore

def customer_record(request, pk):# type: ignore
    # obtenemos el registro del cliente utilizando su clave primaria (pk)
    if request.user.is_authenticated: # pyright: ignore[reportUnknownMemberType]
        customer_record = Record.objects.get(id=pk) # type: ignore # obtenemos el registro del cliente utilizando su clave primaria (pk)
        return render(request, 'record.html', {'customer_record': customer_record}) # type: ignore# renderizamos la plantilla 'record.html' y pasamos el registro del cliente como contexto para mostrarlo en la página
    else:
        messages.error(request,"debes iniciar sesion para ver el registro del cliente") # type: ignore# si el usuario no está autenticado, mostramos un mensaje de error indicando que debe iniciar sesión para ver el registro del cliente
        return redirect('home')# redirigimos al usuario a la página de inicio si no está autenticado

def delete_record(request, pk):# type: ignore
    if request.user.is_authenticated: # pyright: ignore[reportUnknownMemberType]
        delete_it = Record.objects.get(id=pk) # type: ignore # obtenemos el registro del cliente utilizando su clave primaria (pk)
        delete_it.delete() # type: ignore# eliminamos el registro del cliente de la base de datos
        messages.success(request,"registro eliminado correctamente") # type: ignore# mostramos un mensaje de éxito indicando que el registro fue eliminado correctamente
        return redirect('home')# redirigimos al usuario a la página de inicio después de eliminar el registro
    else:
        messages.error(request,"debes iniciar sesion para eliminar el registro del cliente") # type: ignore# si el usuario no está autenticado, mostramos un mensaje de error indicando que debe iniciar sesión para eliminar el registro del cliente
        return redirect('home')# redirigimos al usuario a la página de inicio si no está autenticado
def update_record(request, pk):# type: ignore
    if request.user.is_authenticated: # pyright: ignore[reportUnknownMemberType]
        current_record = Record.objects.get(id=pk) # type: ignore # obtenemos el registro del cliente utilizando su clave primaria (pk)
        form = RecordForm(request.POST or None, instance=current_record) # type: ignore # creamos una instancia del formulario de registro de clientes, pasando los datos enviados en la solicitud POST (si los hay) y el registro actual como instancia para que el formulario sepa que estamos actualizando un registro existente
        if form.is_valid(): # type: ignore# verificamos si el formulario es válido, es decir, si los datos cumplen con las reglas de validación definidas en el formulario
            form.save() # type: ignore# si el formulario es válido, guardamos los cambios en la base de datos, lo que actualizará el registro del cliente con los nuevos datos proporcionados en el formulario
            messages.success(request,"registro actualizado correctamente") # type: ignore# mostramos un mensaje de éxito indicando que el registro fue actualizado correctamente
            return redirect('home')# redirigimos al usuario a la página de inicio después de actualizar el registro
        return render(request, 'update_record.html', {'form': form}) # type: ignore# si el formulario no es válido o si la solicitud no es POST, renderizamos la plantilla 'update_record.html' y pasamos el formulario como contexto para mostrarlo en la página
    else:
        messages.error(request,"debes iniciar sesion para actualizar el registro del cliente") # type: ignore# si el usuario no está autenticado, mostramos un mensaje de error indicando que debe iniciar sesión para actualizar el registro del cliente
        return redirect('home')# redirigimos al usuario a la página de inicio si no está autenticado

