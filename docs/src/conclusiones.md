Conclusiones
============

Tras la evaluación es una oportunidad para observar lo que el sistema ha conseguido.


Revisión de Objetivos
---------------------
Estudio de Viabilidad:
:   La evaluación parece demostrar que es posible crear una interfaz de
    aprendizaje automático visual que es flexible a la vez que relativamente
    fácil de usar, incluso para estudiantes, incluyendo un sistema de tipos y
    notificación de errores en tiempo de escritura.

Diseño y Usabilidad:
:   La implementación final sigue los bosquejos iniciales, demostrando que el
    diseño inicial tenía fundamentos sólidos.
    Los buenos resultados de la evaluación, incluyendo los comentarios finales
    de los participantes, parecen indicar que la interfaz satisface los
    objetivos manteniendo una interfaz simple.

Evaluación:
:   A pesar del bajo número de participantes la evaluación resultó en
    resultados mayormente positivos, incluyendo feedback que influyó la fase
    final de desarrollo.

Herramienta de Aprendizaje:
:   Con la mayor parte de los objetivos cumplidos el sistema ha alcanzado un
    estado en el cual tiene suficiente funcionalidad como para ser usado
    como herramienta de aprendizaje, especialmente gracias al soporte de los
    workflows más simples y usados. Incluso dos participantes reseñaron la
    facilidad de uso y la capacidad de realizar acciones complejas (como
    ajuste de hyper-parametros) de manera sencilla comparado con otros
    frameworks y librerías.

Acelerar análisis exploratorio:
:   Al igual que en el último objetivo, el sistema ha alcanzado un nivel de
    funcionalidad suficiente en el que realizar análisis de datos e iterar
    sobre distintos métodos es relativamente rápido (simplemente desenganchar
    y enganchar las conexiones a otro bloque).
    Cuando un bloque necesario no estaba implementando la implementación
    era relativamente sencilla (la mayoría de bloques son menos de 20 lineas
    de código).

Implementación:
:   Al final del proyecto los requerimientos no-funcionales han sido cumplidos,
    culminando en un ejecutable sin dependencias que los participantes han
    usado para la evaluación.
    Este proceso de fácil instalación ha sido comentado por varios
    participantes, así como el rendimiento del sistema, manteniendo la
    interfaz sensible al input mientras se renderizan múltiples bloques y
    el proceso se ejecuta simultáneamente (multihilo).

Retrospectiva
-------------
Con más de 7000 líneas de código, 10 [releases], y más de 200 commits,
Persimmon se ha convertido en un proyecto de tamaño medio, desde su concepción
ha llamado la atención, con más de 3000 visitas y 100 estrellas en [Github].

Ha aparecido en [múltiples], [páginas] web, e incluso ha ganado el premio al
[mejor proyecto] en el compshow 2017 en la universidad de Hertfordshire.

![Persimmon en el extranjero](images/china.png)


Conclusión
----------
En conclusión el sistema ha conseguido alcanzar un estado testeable en el
cual los participantes han evaluado la usabilidad, flexibilidad y potencial,
valorándolo positivamente.
Esto parece indicar que es posible mejorar la situación de herramientas
visuales de aprendizaje automático con pequeñas mejoras que impactan la
experiencia de usuario.
Características como el menú de búsqueda inteligente usa la introspección
para sugerir bloques adecuados, usando el sistema de tipos para ayudar al
usuario a crear procesos más rápida y fácilmente.

Esto se corresponde con la hipótesis del proyecto, así como con el objetivo
de que el sistema no debería solo hacer difícil o imposible crear procesos
incorrectos, sino hacer más fácil y rápido crear grafos correctos.

Dar más poder al usuario no significar complicar la interfaz, de hecho puede
ser lo contrario.

Trabajo Futuro
--------------
* Exponer parámetros opcionales.
* Pulir aspectos visuales.
    - Categorías en el menú de búsqueda.
    - Más indicadores durante acciones de arrastre.
* Serialización de los grafos.
* Soporte de movimiento y zoom sobre el grafo.
* Generación automática de bloques desde funciones en Python.
* Capacidad de deshacer (Command pattern).
* Selección en área.
* Creación de worflows comunes mediante plantillas.
* Unit/Integración/End to end testing.
* Deployment automático en Windows
* Integración contigua.
* Cacheado de resultados similares a un REPL[^REPLE].

[múltiples]: http://mailchi.mp/pythonweekly/python-weekly-issue-295
[páginas]: http://forum.ai100.com.cn/blog/thread/ml-2017-05-10/
[mejor proyecto]: https://twitter.com/HertfordshireCS/status/857266574356598785

[^REPLE]: Un Read Eval Print Loop es una consola interactiva proveniente de
    LISP que permite la ejecución interactiva de expresiones, guardando los
    resultados intermedios para el uso exploratorio.
