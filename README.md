# learn-python
Different types of exercises to improve your skills on python

## Global note

* You may need additional module, install them with `pip`
* Pour lancer un test sur un exercice : `python -m unittest tests/exercise{number}.py` where {number} corresponds to the exercise number 

## exercise 1 

Use the github API: 
https://api.github.com/users/{username}

1. Create a function `parse_github (username)` in [exercise/exercise1.py](exercise/exercice1.py) which takes as a parameter a `username` to provide to the Github API
2. This function must call the Github API and retrieve the JSON content
3. The function returns two elements in a list: 
    * As a first index (`[0]`) the "node_id" 
    * Second index (`[1]`) the "id"
    * In third index (`[2]`) the "name"
4. The function must take 2 lines (4 maximum)

> Example
> GET https://api.github.com/users/av1m
> ["MDQ6VXNlcjM2NDU2NzA5", 36456709, "Avi Mimoun"]

To test your code:

```bash
python -m unittest tests/exercise1.py
```