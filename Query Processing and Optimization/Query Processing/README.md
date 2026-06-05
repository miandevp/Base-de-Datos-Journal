# Query Processing

Proceso mediante el cual un sistema gestor de bases de datos interpreta, transforma y ejecuta una consulta SQL para obtener el resultado solicitado.

Flujo general:

SQL Query → Parsing → Optimization → Execution → Results

EJEMPLO:
Tú escribes:

SELECT * FROM alumnos WHERE edad > 18;

PostgreSQL internamente hace algo parecido a:

1. Recibe la consulta SQL
           ↓
2. La analiza (Parsing)
           ↓
3. Verifica tablas y columnas
           ↓
4. La optimiza
           ↓
5. Crea un plan de ejecución
           ↓
6. Ejecuta el plan
           ↓
7. Devuelve los resultados
