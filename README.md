# Clincal-Trial-Data

## Data Source:
* Clincal trial data, 2013-2017, 2018(4 quarters)
* NCT number, interventions, ICD categories
* Prefer 'Drug', 'Biological'

## Method:
* Data clearning
* Machine learning for drug classification

## Output:
### Formate: Json file
### example: 
```json
{"NCT000001": 
            {"Drug": [statement1, statement2]}, 
            {"ICD": [2-12}
}
```
### Firebase: 
```html
https://trial-b3a4a.firebaseio.com/
```