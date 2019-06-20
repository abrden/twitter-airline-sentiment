### Entrenamiento de clasificador con WEKA

* `python3 to_dirs.py` para generar los contenidos del directorio `train`
* Se corrieron varios modelos con split de 66%, todos estan guardados en `models` con sus outputs
  - El mejor resulto ser **Naive Bayes Multinomial** con:
```
Correctly Classified Instances        2579               79.3538 %
Incorrectly Classified Instances       671               20.6462 %
```
* `python3 to_airline_dirs.py` para generar los contenidos del directorio `airlines`
* Se corrio el modelo **Naive Bayes Multinomial** para cada una de las aerolineas
  - La aerolinea mejor valorada fue: Virgin America
  - La aerolinea menor valorada fue: Us Airways

### Lexicón de sentimientos
* `python lexicon.py` para correr el `fastSentimentClassifier.jar` sobre el test dataset
