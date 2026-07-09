```gherkin
Feature: Login de usuario

  Como usuario
  Quiero iniciar sesión
  Para acceder a mi cuenta

  Background:
    Dado que el usuario "usuarioValido" existe en el sistema
    Y que la contraseña correcta es "Password123"
    Y que el usuario "usuarioBloqueado" está bloqueado

  Scenario: Login exitoso
    Cuando el usuario "usuarioValido" ingresa la contraseña "Password123"
    Y envía la solicitud de inicio de sesión
    Entonces el sistema permite el acceso a la cuenta

  Scenario: Login con contraseña inválida
    Cuando el usuario "usuarioValido" ingresa la contraseña "ContraseñaIncorrecta"
    Y envía la solicitud de inicio de sesión
    Entonces el sistema muestra un mensaje de error "Contraseña incorrecta"

  Scenario: Login con usuario bloqueado
    Cuando el usuario "usuarioBloqueado" ingresa la contraseña "CualquierContraseña"
    Y envía la solicitud de inicio de sesión
    Entonces el sistema muestra un mensaje de error "Usuario bloqueado"

  Scenario: Login con usuario vacío
    Cuando el usuario ingresa un nombre de usuario vacío
    Y ingresa la contraseña "Password123"
    Y envía la solicitud de inicio de sesión
    Entonces el sistema muestra un mensaje de error "Nombre de usuario requerido"

  Scenario: Login con contraseña vacía
    Cuando el usuario "usuarioValido" ingresa una contraseña vacía
    Y envía la solicitud de inicio de sesión
    Entonces el sistema muestra un mensaje de error "Contraseña requerida"

  Scenario: Login con usuario y contraseña vacíos
    Cuando el usuario ingresa un nombre de usuario vacío
    Y ingresa una contraseña vacía
    Y envía la solicitud de inicio de sesión
    Entonces el sistema muestra un mensaje de error "Nombre de usuario y contraseña requeridos"
```