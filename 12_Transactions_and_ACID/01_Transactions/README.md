# Transactions

## Definición formal

> Una **transacción** es una **unidad lógica de procesamiento** en una **base de datos**, conformada por una **secuencia de operaciones de acceso a los datos** (lectura, inserción, eliminación, modificación y recuperación).

---

## Descomponiendo la definición

### Unidad lógica

No significa que sea una sola instrucción.

Significa que varias operaciones relacionadas representan **una única tarea con sentido desde el punto de vista del negocio o del usuario**.

Por ejemplo:

```text
"Transferir S/100"
```

Para el usuario es una sola acción.

Pero para la base de datos implica varias operaciones.

---

### Secuencia de operaciones

Una transacción está formada por varias instrucciones ejecutadas en un orden determinado.

Por ejemplo:

```text
Leer saldo de la cuenta A
Restar S/100
Guardar cuenta A

Leer saldo de la cuenta B
Sumar S/100
Guardar cuenta B

Registrar la transferencia
COMMIT
```

No es una operación aislada, sino una secuencia.

---

### Operaciones de acceso a datos

Son las acciones que la base de datos realiza sobre la información almacenada.

Ejemplos:

- Lectura (`READ`)
- Inserción (`INSERT`)
- Modificación (`UPDATE`)
- Eliminación (`DELETE`)
- Recuperación o consulta (`SELECT`)

---

## ¿Por qué la definición usa "unidad lógica" y no simplemente "acción"?

Porque una transacción normalmente **no es una sola acción física**.

Si dijéramos:

> "Una transacción es una acción."

podría interpretarse que corresponde a una única instrucción SQL, lo cual es incorrecto.

Por ejemplo:

```sql
UPDATE Cuenta
SET saldo = saldo - 100;
```

es una acción.

Sin embargo,

```text
Retirar S/100 de un cajero
```

requiere:

```text
Leer saldo
Verificar fondos
Restar dinero
Actualizar la cuenta
Registrar el movimiento
Confirmar la operación
```

Todas esas operaciones deben tratarse como una sola unidad.

---

## Interpretación intuitiva

Una transacción puede entenderse como:

> Un conjunto de operaciones sobre la base de datos que, aunque internamente sean varias instrucciones, representan una única tarea que debe completarse completamente o no ejecutarse en absoluto.

---

## Ejemplo

### Desde el punto de vista del usuario

```text
Transferir S/100 de Ana a Luis.
```

### Desde el punto de vista de la base de datos

```text
Leer cuenta de Ana
Restar S/100
Guardar cuenta de Ana

Leer cuenta de Luis
Sumar S/100
Guardar cuenta de Luis

Registrar transferencia

COMMIT
```

Para el usuario es una sola operación.

Para la base de datos es una secuencia de operaciones agrupadas en una única transacción.