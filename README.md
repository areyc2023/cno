# cnosolar

<img src='./Protocolos/Uniandes-CNO2.png' width='500' />
 
## Introducción

#### Acuerdo Específico 5: Convenio Marco CNO-Uniandes

Protocolos para el cálculo de la CEN (Capacidad Efectiva Neta) y el modelo que relaciona el recurso y la potencia para plantas solares fotovoltaicas a partir de modelamiento computacional.

#### Objetivos

1. Desarrollar la metodología para la estimación y modelamiento de la Irradiancia Normal Directa (*Direct Normal Irradiance* – DNI), la Irradiancia Horizontal Difusa (*Diffuse Horizontal Irradiance* – DHI) y la irradiancia sobre el plano del arreglo (*Plane-of-Array* – POA) a partir de la Irradiancia Horizontal Global (*Global Horizontal Irradiance* – GHI).
2. Desarrollar protocolo para el cálculo de la CEN de plantas solares fotovoltaicas antes de su entrada en operación.
3. Desarrollar el modelo que relaciona el recurso y la potencia en plantas solares fotovoltaicas. El modelo permitirá obtener la producción de la planta a partir de los parámetros técnicos de la planta (configuración, tecnologías, tipo de seguimiento, entre otros aspectos), la irradiancia y otras variables meteorológicas.

## Documentación

#### Protocolos
Los protocolos se encuentran en la carpeta [`Protocolos`](https://git.cno.org.co/cno/cno_solar/-/tree/main/Protocolos). 

#### Memoria de Cálculos
En la carpeta [`Memoria_de_Calculos`](https://git.cno.org.co/cno/cno_solar/-/tree/main/Memoria_de_Calculos) se encuentra la documentación correspondiente a las pruebas de concepto de las metodologías recomendadas, validación con datos disponibles de la planta fotovoltaica del Edificio Santo Domingo de la Universidad de los Andes y estimación de los errores e incertidumbres.

#### Ejemplos
En la carpeta [`examples`](https://git.cno.org.co/cno/cno_solar/-/tree/main/examples) se encuentra el documento `CNO_Doc_Ejemplos.pdf`. Allí se presentan tres ejemplos de arquitecturas de plantas fotovoltaicas para la ejecución completa del repositorio `cnosolar`. Cada ejemplo dispone de una carpeta en la cual se alojan los archivos necesarios para la ejecución, así como los resultados de la misma.

#### Descargas
La descarga de los archivos de configuración de la planta fotovoltaica (cuaderno `CNO_Configuracion_Sistema.ipynb`) se alojan en la carpeta `configurations`. 

La descarga de los archivos de producción y de las gráficas (cuaderno `CNO_Protocolos.ipynb`) se alojan en la carpeta `downloads`.

## Instalación

#### Distribución y Ambiente

Se recomienda instalar [Miniforge](https://github.com/conda-forge/miniforge) como ambiente para instalar Python y las librerías necesarias para la ejecución de los protocolos. Miniforge es una distribución de Python y el administrador de paquetes `conda`, permite fácilmente la configuración de ambientes y la instalación de paquetes desde el repositorio `conda-forge`.

![conda-forge/miniforge](images/conda-forge.png)

Luego de descargar e instalar `Miniforge`, inicie el terminal mediante la aplicación `Miniforge Prompt`. Si la instalación se realizó de manera correcta, debe estar en el ambiente `(base)`. 



Ahora se puede crear un ambiente específico para PVlib y los demás requerimientos de este sofware, dispuestos en el archivo `requirements.txt`. Por ejemplo, si queremos que el ambiente se llame `pvlib`:

```python
$ conda create --name pvlib
```

Ahora se activa dicho ambiente:

```python
$ conda activate pvlib
```

Después de ejecutar el comando anterior, se debe estar en el ambiente correspondiente, en este caso denotado por `(pvlib)`. Ahora se pueden instalar las librerías requeridas para correr los cuadernos así:

```python
$ conda install package-name
```

Si se desea instalar una versión específica, por ejemplo `pvlib=0.9.0`, el comando es:

```python
$ conda install pvlib==0.9.0
```

Para instalar las librerías especificadas en el archivo `requirements.txt`, por favor use una de las siguientes opciones:

```python
$ conda install -c conda-forge --file requirements.txt
$ pip install -r requirements.txt
```

#### Widgets

La interfaz gráfica de usuario es realizada con [`ipywidgets`](https://ipywidgets.readthedocs.io/en/latest/). Esta es una librería con *widgets* HTML interactivos para Jupyter Notebook y el kernel de IPython.

En el ambiente activado, ejecute:

```python
$ conda install -c conda-forge ipywidgets
```

La mayoría de las veces, la instalación de `ipywidgets` configura automáticamente Jupyter Notebook para utilizar los *widgets*. No obstante, es posible que deba habilitar manualmente la extensión de notebook `ipywidgets` con:

```python
$ jupyter nbextension enable --py widgetsnbextension
```

#### Repositorio

Para [clonar](https://docs.github.com/es/repositories/creating-and-managing-repositories/cloning-a-repository) el repositorio `cnosolar` se recomienda usar el software [GitHub Desktop](https://desktop.github.com/). La url del repositorio es: [andresgm/cno_solar](https://git.cno.org.co/cno/cno_solar).

Otra opción es desde el terminal con en el ambiente activado; para esto ejecute:

```bash
$ git clone https://git.cno.org.co/cno/cno_solar
```

## Licencia

GNU AFFERO GENERAL PUBLIC LICENSE v3.0, dispuesta en el archivo `LICENSE`.
