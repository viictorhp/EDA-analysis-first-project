# Primer proyecto Máster Data Science & IA - Evolve Academy
### Este primer proyecto consiste en un análisis exploratorio de datos (EDA) sobre un dataset. 

Antes de empezar con el análisis y ya que es la primera tarea, me gustaría hacer una breve presentación.

Mi nombre es **Víctor Horcas**, tengo 22 años y soy de Granada. Este año finalicé mis estudios universitarios en el grado de Economía y con la intención de seguir avanzando y progresando tanto en el ámbito tanto académico como profesional estoy realizando este Máster, el cuál estoy seguro de que me va a aportar las herramientas necesarias para seguir avanzando en este mundo de la tecnología y los datos.

## Contexto y explicación del dataset escogido (Crossfit Athletes)
El **CrossFit** es un programa de entrenamiento físico que combina ejercicios de alta intensidad de levantamiento de pesas, halterofilia y cardio. Es un deporte que se ha hecho muy popular en los últimos años por su enfoque en mejorar la forma física general y la competitividad.

He elegido este database, ya que, hace poco más de un año que practico este deporte y estoy muy contento. Valoro mucho la comunidad que se crea, como nos apoyamos entre compañeros y me fascina como cada entrenamiento me obliga a sacar lo mejor de mí mismo.
Hace un tiempo empecé a ver varias competiciones que se desarrollan en todo el mundo alrededor de este deporte y este dataset engloba a los mejores atletas a nivel mundial.
La información de este dataset está recogida entre los años 2021 - 2023.

El análisis exploratorio de datos (EDA) en este proyecto sirve para comprender las principales características y distribuciones de los atletas de CrossFit registrados en el dataset. Busco identificar tendencias dentro de las variables demográficas y de rendimiento, descubrir posibles relaciones entre edad, género, país, puntuación y clasificación, así como detectar valores atípicos y errores de datos.

Esta base da datos ha sido extraída de la plataforma **Kaggle**. 

Kaggle es una plataforma online de ciencia de datos y machine learning donde la gente puede descargar datasets, subir los suyos, programar en notebooks en la nube y participar en competiciones de modelado predictivo.
Considero que esta fuente es fiable para fines educativos y de análisis de datos, ya que, la propia comunidad ayuda a detectar errores y mejorar la calidad mediante votos, comentarios y notebooks asociados.

Dominio a mi base de Datos: [consolidated_athletes_information.csv](https://www.kaggle.com/datasets/tgomesjuliana/crossfit-competitions?select=consolidated_athletes_information.csv)

## 1. Exploración de los datos
Este proyecto se realizará haciendo uso de las librerías mencionadas en el archivo de requirements, las cuáles he cargado al principio de este proyecto para después poder realizar todo el análisis sin problema.
Las principales librerías que usaré son Pandas (ideal para el análisis de los datos), Seaborn y Matplotlib (ideales para la visualización de estos datos y generar gráficos).

#### Carga del dataset
Cargamos el dataset en nuestro editor de código, en mi caso, Visual Studio Code y lo transformamos en un DataFrame de Pandas para poder trabajar con él. Extraemos información básica, como primeras filas, nombres de las columnas, vemos los valores nulos... para tener una idea general de en qué consiste nuestro dataset.

#### Estructura del dataset
Este dataset contiene 399342 registros (filas) y 18 columnas. Esto indica que cada fila corresponde a un atleta, que se puede identificar por su id o también por su nombre y apellidos y cada columna a una variable o característica registrada sobre ese atleta.

Las variables (columnas) contienen datos de todo tipo sobre los atletas:
    
    - Datos de identificación: id, nombre, apellido...
    
    - Datos demográficos: región, edad, altura, peso...
    
    - Datos de rendimiento: puntuaciones y puestos en el rango de clasificación de crossfit.

Podemos decir que este dataset cuenta con un nivel de granularidad alto, ya que, contiene información bastante específica y detallada sobre los atletas, lo cuál es muy adecuado para que podamos realizar nuestro análisis de segmentación y las diferentes comparaciones.

Mediante la función "describe" obtenemos información muy valiosa sobre la distribución de las variables:

- La variable de edad oscila entre los 16 y 54 años, la variable de altura entre 150 cm y 200 cm y la variable del peso entre 50 kg y 110 kg lo cuál no presenta outliers evidentes, ya que todas las variables se encuentran dentro de un rango razonable.

- La variable "overallRank" presenta un valor mínimo de -1, lo cuál, si que nos puede mostrar un valor atípico que pueda llevarnos a algún error.

#### Tipos de datos
Tenemos datos individuales(con elevada granularidad) de tipo **float** e **integer** (métricas numéricas), como pueden ser la edad, el peso, la altura... y algunos otros datos de tipo **object** (variables de texto), como la región, el nombre, etc.

Como vemos en el notebook este dataset no cuenta con una gran cantidad de valores nulos, lo cuál va a facilitar nuestro análisis y va a hacer que los resultados que obtengamos sean consistentes y representen de una buena forma la realidad.
En especial, las variables que yo considero más importantes no cuentan casi con ningún valor nulo y las variables que cuentan con más valores nulos, las cuáles son "affiliateId" y "affiliateName" considero que en un futuro se podrían eliminar, ya que aportan identificadores poco útiles para nuestro proyecto, porque ya contamos con otros como nombre y apellidos y sobretodo con el "competitorId".

No cuenta con valores duplicados lo que garantiza que cada atleta es único y no existen repeticiones que puedan distorsionar el análisis.

En cuanto a los valores únicos, he revisado que este dataset cuente con valores únicos para las variable género y año.
Se comprueba que para la variable género sólo existen "Male" y "Female" y para la variable temporal sólo los años 2021, 2022 y 2023, años en los que está basado este dataset. 

He englobado en una variable los valores atípicos que presenta "overallRank", estos valores indican un puesto en el ranking negativo.
Solo son 5 atletas los que tienen estos valores, asi que, se podría considerar eliminarlos para que no hubiera errores a la hora de hacer estimaciones con esta variable.

En la fase de exploración se ha obtenido una visión general sobre la estructura, el contenido y la calidad de los datos disponibles. Se han revisado las variables presentes, su tipología y distribución. Además, se ha explorado la presencia de valores nulos y posibles outliers, así como la consistencia y coherencia entre columnas.

## 2. Limpieza y transformación de los datos


