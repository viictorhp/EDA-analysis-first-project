# Primer proyecto Máster Data Science & IA - Evolve Academy
### Este primer proyecto consiste en un análisis exploratorio de datos (EDA) sobre un dataset. 

Antes de empezar con el análisis y ya que es la primera tarea, me gustaría hacer una breve presentación.
Mi nombre es **Víctor Horcas**, tengo 22 años y soy de Granada. Este año finalicé mis estudios universitarios en el grado de Economía y con la intención de seguir avanzando y progresando tanto en el ámbito tanto académico como profesional estoy realizando este Máster, el cuál estoy seguro de que me va a aportar las herramientas necesarias para seguir avanzando en este mundo de la tecnología y los datos.

## Contexto y explicación del dataset escogido (Crossfit Athletes)
El **CrossFit** es un programa de entrenamiento físico que combina ejercicios de alta intensidad de levantamiento de pesas, halterofilia y cardio. Es un deporte que se ha hecho muy popular en los últimos años por su enfoque en mejorar la forma física general y la competitividad.
He elegido este database, ya que, hace poco más de un año que practico este deporte y estoy muy contento. Valoro mucho la comunidad que se crea, como nos apoyamos entre compañeros y me fascina como cada entrenamiento me obliga a sacar lo mejor de mí mismo.
Hace un tiempo empecé a ver varias competiciones que se desarrollan en todo el mundo alrededor de este deporte y este dataset engloba a los mejores atletas a nivel mundial.
La información de este dataset está recogida entre los años 2021 - 2023 y contiene datos numéricos que permiten hacer un análisis estadístico directo y de texto, útiles para segmentar y agrupar datos.

Esta base da datos ha sido extraída de la plataforma **Kaggle**. 
Kaggle es una plataforma online de ciencia de datos y machine learning donde la gente puede descargar datasets, subir los suyos, programar en notebooks en la nube y participar en competiciones de modelado predictivo.
Considero que esta fuente es fiable para fines educativos y de análisis de datos, ya que, la propia comunidad ayuda a detectar errores y mejorar la calidad mediante votos, comentarios y notebooks asociados.
Dominio a mi base de Datos: [consolidated_athletes_information.csv](https://www.kaggle.com/datasets/tgomesjuliana/crossfit-competitions?select=consolidated_athletes_information.csv)

## 1. Exploración de los datos
Este proyecto se realizará haciendo uso de las librerías mencionadas en el archivo de requirements, las cuáles he cargado al principio de este proyecto para después poder realizar todo el análisis sin problema.
Las principales librerías que usaré son Pandas, Seaborn y Matplotlib.

#### Carga del dataset
Cargamos el dataset en nuestro VS Code y lo transformamos en un DataFrame de Pandas para poder trabajar con él. Extraemos información básica, como primeras filas, nombres de las columnas, vemos los valores nulos... para tener una idea general de en qué consiste nuestro dataset.

#### Estructura del dataset
Este dataset contiene 399342 registros (filas) y 18 columnas. Esto indica que cada fila corresponde a un atleta, que se puede identificar por su id o también por su nombre y apellidos y cada columna a una variable o característica registrada sobre ese atleta.
Las variables (columnas) contienen datos de todo tipo sobre los atletas
    - Datos de identificación: id, nombre, apellido...
    - Datos demográficos: región, edad, altura, peso...
    - Datos de rendimiento: puntuaciones y puestos en el rango.
Podemos decir que este dataset cuenta con un nivel de granularidad alto, ya que, contiene información bastante específica y detallada sobre los atletas, lo cuál es muy adecuado para que podamos realizar nuestro análisis de segmentación y las diferentes comparaciones.

#### Tipos de datos
Tenemos datos individuales(con elevada granularidad) de tipo **float** e **integer** (métricas numéricas), como pueden ser la edad, el peso, la altura... y algunos otros datos de tipo **object** (variables de texto), como la región, el nombre...

