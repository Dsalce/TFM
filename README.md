# TFM

Proyecto final de master 

El objetivo de este TFM ha sido desarrollar una aplicación que sea capaz de obtener la información necesaria para discernir 
si una inspección de ITV tiene anomalías en sus resultados o no a partir de una fuente de datos introducida por texto o Excel.

En particular, nos interesa detectar si diferentes inspectores dentro de la misma ITV actúan de forma diferente. 

Para ello partiremos  de un fichero de datos con los datos de las inspecciones durante un periodo relativamente largo 
(por ejemplo, un año). 
Para ello nos hemos servido del cálculo de reglas de asociación mediante el algoritmo Apriori.
Las reglas de asociación nos permiten saber qué deficiencias de los vehículos se encuentran habitualmente 
de forma conjunta durante la inspección de un vehículo.

Usando los resultados de las reglas de asociación junto con los test estadísticos, 
podremos verificar si hay alguna discrepancia entre los resultados obtenidos por cada inspector en las ITV.
El resultado del trabajo es un método que permite detectar estas anomalías, 
mostrar los defectos que atestiguan el comportamiento anómalo y, lo que es más importante, 
asegurar que las anomalías detectadas son estadísticamente significativas.
Este método ha sido implementado en una herramienta disponible que puede ser empleada 
por entidades de inspección de ITVs como ENAC.



link descarga :https://drive.google.com/open?id=1LITAwPfk1SAeI_TDTOe1N5Qiae7siHX3