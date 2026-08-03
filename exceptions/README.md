# Manejo de Excepciones - Taller Mecánico

## Descripción
Implementación de excepciones personalizadas y bloques de control `try/except/else/finally` para garantizar la robustez del sistema ante entradas erróneas o fallos en operaciones CRUD.

## Excepciones Personalizadas
`CostoInvalidoError`: Se lanza cuando se intenta registrar o actualizar un servicio con un costo menor o igual a 0.
`ServicioNoEncontradoError`: Se lanza al intentar buscar, actualizar o eliminar un registro que no existe en la base de datos.