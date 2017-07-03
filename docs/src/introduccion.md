Introducción
============

En este capítulo se presenta el proyecto, así como los objetivos y las
motivaciones del mismo.
También se incluye una sección sobre temas relacionados con el proyecto pero
que quedan fuera del ámbito del mismo.
Finalmente se encuentra una breve revisión de la estructura de la memoria.

Descripción
-----------
El campo de Data Science ha visto un incremento exponencial de mercado en los
últimos años, con predicciones vaticinando la necesidad de hasta un millón de
Data Scientists para 2018 [@onemillion].
Los científicos de datos se encuentran en una situación excepcional, para el
Harvard Business Review es *"el trabajo más atractivo del siglo 21"* [@sexy].
Y sin embargo, a pesar de todo esto, faltan profesionales que puedan cubrir
estos puestos, ya que la disciplina es inherentemente multidisciplinaria
[@venn], incluyendo conocimiento de estadística, matemáticas, programación y
del dominio.
Esto hace que el camino para convertirse en un experto sea largo y complejo,
lo cual desemboca en las llamadas *"cazas de unicornios"* [@unicorn] y [@hunt].

Herramientas como scikit-learn[^sci], Weka o Tableau permiten una manipulación
de los datos más sencilla y a mayor alto nivel, facilitando las tareas
habituales de estos profesionales, y con ello suavizando la curva de
aprendizaje y aumentando la oferta de profesionales capaces de desarrollar
análisis de datos.

Estas herramientas por otro lado requieren programación, se centran en tareas
de limpieza y pre-procesamiento de datos, o proveen una interfaz muy limitada.

El sistema pretende proporcionar una interfaz visual para scikit-learn, dando
la habilidad de crear complejos procesos de análisis sin escribir una sola
línea de código, proporcionando al usuario una expresividad comparable a la
programación tradicional a la vez que se le ayuda mediante estímulos visuales.

Para poder conseguir esto el proyecto explora las siguientes disciplinas,

* Dataflow Programming. Este paradigma representa programas como grafos
    acíclicos dirigidos, iniciado en los 60 en el MIT y los laboratios Bell
    [@bell].
    Modela los programas como un flujo de datos que pasa por una serie de
    instrucciones en vez de una serie de instrucciones que operan en unos datos
    externos, i.e. los datos fluyen por las instrucciones, no al revés (de ahí
    el nombre de dataflow).
    Esto produce programas paralelos por naturaleza, más cercanos al
    paradigma funcional que al imperativo y a la arquitectura Von
    Neumann [sección 15, @backus1978can].

* Programación Visual. La elección por naturaleza para representar un lenguaje
    de dataflow es una interfaz visual, pudiendo representar el grafo de forma
    clara y precisa [@shu1988visual].
    Se pueden implementar mejoras más avanzadas gracias a la presentación
    visual, incluyendo comprobación de tipos en tiempo de escritura, indicador
    de ejecución, etc, además de una presentación más clara y precisa.

* Experiencia de Usuario. El proyecto se nutre de la experiencia de los
    participantes en los experimentos con el prototipo.
    La interfaz debe indicar el camino más sencillo para realizar la acción
    deseada por el usuario, dando facilidades para reducir la dificultad de
    uso siempre que sea posible.

* Ingeniería del Software. Comunicación con múltiples librerías y frameworks,
    definición de interfaces y organización del código mediante técnicas de
    programación orientada a objetos y módulos.

* Aprendizaje Automático. Aunque no se implementan los algoritmos en sí, es
    necesario extenso conocimiento de la implementación, ya que hay que
    proporcionar un punto de acceso a los hiperparámetros y otros tipos de
    configuración que permite sklearn [@scikitlearn].

* Transformación de Datos. Algunas precondiciones sobre los datos han de ser
    asumidas o el usuario ha de ser provisto con las herramientas necesarias
    para realizar las transformaciones apropiadas.

* Compiladores. El grafo visual que el usuario dibuja tiene que ser
    interpretado por Python.

La hipótesis del proyecto es que la representación visual del programa y los
conceptos asociados pueden ayudar con el aprendizaje y uso de técnicas de
aprendizaje automático, así como acelerar el trabajo de exploración temprana
típico del análisis de datos.

Esta hipótesis coincide con el espíritu de sklearn [@scikitlearn, pp29], que
es intentar simplificar el uso y acceso a herramientas de aprendizaje
automático.

Esto es lo que ha convertido a sklearn en uno de los proyectos de
aprendizaje automático de código libre más importantes, con
más de 16000 estrellas en
[Github](https://github.com/scikit-learn/scikit-learn), siendo usado por
compañías como Spotify, Facebook o Evernote [@whosklearn].


Motivación
----------
Tras cursar Aprendizaje Automático el año pasado, obtuve una beca en una
empresa de trading algorítmico como parte del equipo de quants[^quant].

Allí mi principal responsabilidad era reescribir parte de las herramientas
de MATLAB a Python.
Durante ese proceso observé como algunos de los integrantes del equipo
experimentaban dificultades con el cambio de lenguaje.

Todos los integrantes venían de disciplinas más "puras" (Física, Matemática,
Estadística, Ingeniería Aeroespacial, etc..).

Los expertos de estos campos están acostumbrados a trabajar con lenguajes
de dominio específico como MATLAB, R, Simulink o Julia, y el cambio a un
lenguaje de uso general trae dificultades como la programación orientada a
objetos, estructuras de datos complejas, optimización o sistemas de tipos
más "fuertes".

La situación es aún mas difícil para aquellos que comienzan el aprendizaje de
Data Science,
ya que no solo tienen que lidiar con la barrera de la programación, sino que
además tienen que superar la dificultad de los algoritmos en sí.


Objetivos
---------
Estudio de Viabilidad:
:   El proyecto tiene que explorar el espacio de posibles soluciones visuales,
    evaluando distintas estrategias en el frontend y backend de la aplicación.

Diseño y Usabilidad:
:   El sistema ha de ser diseñado acorde a los requerimientos, tanto en
    términos de hacer sencillo el progreso a través de hitos, como
    produciendo software utilizable en cada release.
    En todos los casos se debe balancear la complejidad y la expresividad
    del sistema, proveyendo al usuario de una herramienta potente sin resultar
    en una interfaz compleja.

Evaluación:
:   El sistema será evaluado por participantes que pertenecen a la audiencia
    potencial del software.
    Un formulario debe ser preparado detallando las actividades que tendrán
    que realizar, así como los datos de los mismos serán tratados.

Herramienta de Aprendizaje:
:   El software debe ayudar con la barrera de la programación, facilitando el
    aprendizaje de Machine Learning y ayudando al estudiante a centrarse en
    las conexiones, intuiciones y bases matemáticas de los algoritmos, y no en
    los detalles de implementación y peculiaridades del lenguaje.

Acelerar el Análisis Exploratorio:
:   Proveyendo una interfaz visual fácil de usar con la capacidad de arrastrar
    y soltar, el usuario puede probar una multitud de algoritmos, ajustando los
    bloques que se ejecutan sin escribir una sola línea de código.

Implementación:
:   Hay ciertos **requisitos no funcionales** que deben ser cumplidos, como
    crear ejecutables para las principales plataformas de escritorio,
    la capacidad de ser distribuido en un ejecutable fácil de instalar para
    facilitar la evaluación, tener un framerate que permita el uso prolongado,
    y hacer uso de múltiple hilos de ejecución para que la interfaz se mantenga
    utilizable mientras el grafo se ejecuta.


Que no es el proyecto
---------------------
El proyecto no lidia con los siguientes aspectos:

* Procesado de datos genéricos. Aunque hay algunas funciones de manipulación de
    datos que son necesarias y/o están incluidas en sklearn, la manipulación
    de datos está fuera del ámbito del proyecto, el sistema trabaja con datos
    ya limpios.
    Estas funciones son difíciles de presentar de manera visual, requiriendo
    interfaces especiales para ser útiles.
* Visualización de Datos. Ya que la visualización suele requerir código
    específico para cada caso, y depende de las características concretas de
    los datos a visualizar.
* Programación Visual de uso general. Ya que limitando el sistema a el
    aprendizaje automático es posible hacer asunciones sobre los posibles
    programas que se pueden crear, es posible añadir características como
    simplificación de tipos (capítulo type), o eliminar la necesidad de
    especificar el orden de ejecución (capítulo literature review).

Estructura de la memoria
------------------------
La estructura de la memoria es paralela a la cronología del proyecto.
Comienza con la revisión de las fuentes académica y la definición de
workflow (proceso).
En el siguiente capítulo se explican los hitos del proyecto (milestones),
incluyendo un diagrama de Gantt.
A continuación se encuentra el capitulo de análisis de riesgos, una tabla
de riesgos, así como una revisión de la metodología de desarrollo.

Hacia la mitad de la memoria, en el capítulo de interfaz, se exponen las
razones que llevan al actual aspecto de la interfaz.
El capítulo de implementación explica el proceso iterativo del proyecto,
centrándose en problemas complejos e interesantes que el proyecto ha tenido que
superar.
En la sección de type checking se introducen múltiples conceptos teóricos
relativos a la teoría de lenguajes, compiladores, teoría de tipos
y la representación intermedia del lenguaje.

La última sección antes de las conclusiones explica el proceso de evaluación y los
resultados.
En las conclusiones se exponen las conclusiones del proyecto, así como posible
áreas de trabajo futuro.

[^sci]: Scikit-learn es una librería de Python que trae una multitud de
    algoritmos de aprendizaje automático a una API que permite el uso y
    comparación de los mismos en un alto nivel de abstracción.
[^quant]: Analista Cuantitativo, en inglés Quantitative Analyst, abreviado
    Quant.
