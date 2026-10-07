
# Registros, Paginacion, Organizador de archivos

## Recordemos

La semana pasada aprendimos cómo una consulta SQL viaja por las principales capas del SGBD para obtener los datos y generar el resultado:

SQL
↓
Parser
↓
Optimizador
↓
Buffer Manager
↓
Storage Manager
↓
Disco
↓
Storage Manager
↓
Buffer Manager
↓
Ejecución de la consulta
↓
Resultado → tablas/filas solicitadas

- **Parser:** recibe el SQL, verifica su sintaxis y lo transforma en una estructura interna.
- **Optimizador:** genera el plan más eficiente para ejecutar la consulta.
- **Buffer Manager:** verifica si las páginas están en RAM; si no, solicita traerlas.
- **Storage Manager:** localiza y obtiene las páginas almacenadas en disco.
- **Disco:** almacena físicamente los datos y devuelve las páginas solicitadas.

En resumen, la consulta baja hasta el disco para obtener los datos y estos regresan para ejecutar la consulta y obtener el resultado.

