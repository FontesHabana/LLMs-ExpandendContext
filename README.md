
# 🕵️‍♀️ Cuando el Modelo se lo Imagina Todo: Resolución de Crímenes con LLMs  📚
---
Este repositorio contiene el código y los recursos que respaldan la investigación presentada en "Cuando el Modelo se lo Imagina Todo: Resolución de Crímenes con LLMs" 🔍. Este estudio investiga el impacto del enriquecimiento automático del contexto en el rendimiento de los Grandes Modelos de Lenguaje (LLM) en tareas de respuesta a preguntas que involucran narrativas de crímenes.
[Inglés](./README_en.md)
## Resumen del Proyecto 📝

Esta investigación aborda las limitaciones de los LLM para responder con precisión preguntas sobre narrativas con contexto insuficiente. Proponemos un sistema automatizado para enriquecer los textos narrativos y aportamos evidencia de que el enriquecimiento mejora el rendimiento de los LLM en las tareas de respuesta a preguntas.

## Metodología ⚙️

Para evaluar el impacto del enriquecimiento del contexto:

1.  Utilizamos el **dataset Murder Mysteries** 📖, una colección estructurada de narrativas de crímenes diseñadas para la respuesta a preguntas.
   
2.  Desarrollamos un sistema automatizado para generar versiones enriquecidas de estas narrativas. Este sistema emplea un proceso de tres etapas:
    * **Generación de Preguntas** ❓: Generación de preguntas inferenciales relevantes para la narrativa.
    * **Generación de Respuestas** ✍️: Producción de respuestas narrativas a las preguntas generadas.
    * **Fusión de Contenido** 🧩: Integración de las respuestas generadas en las narrativas originales.
       
3.  Evaluamos el rendimiento del modelo LLAMA 3.3 70B 🧠 tanto en las narrativas originales como en las enriquecidas.

## Contenido del Repositorio 📁

Este repositorio proporciona lo siguiente:

* Implementación del código del sistema automatizado de enriquecimiento del contexto 💻.
   
* Scripts para el procesamiento y evaluación del dataset 📊.
   
* Documentación que detalla la configuración experimental 🔬.

## Resultados 📈

Los hallazgos del estudio indican que el proceso de enriquecimiento automático del contexto mejora la precisión de los LLM en las tareas de respuesta a preguntas. El modelo LLAMA 3.3 70B demostró un notable aumento en la precisión cuando se evaluó con las narrativas enriquecidas en comparación con las narrativas originales.

## Implicaciones 💡

Esta investigación destaca el potencial del enriquecimiento automático del contexto para mejorar el rendimiento de los LLM en la comprensión narrativa. La metodología propuesta ofrece un enfoque valioso para mejorar las capacidades de los LLM sin requerir entrenamiento adicional ni intervención humana.



## Contacto 📧

Para consultas, por favor contacte a:

Javier Fontes Basabe

JAVIERFONTBAS@GMAIL.COM