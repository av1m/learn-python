# learn-python
Different types of exercises to improve your skills on python

## Global note

* You may need additional module, install them with `pip`
* To launch a test on an exercise : `python3 -m unittest tests/exercise{number}.py` where {number} corresponds to the exercise number
* To test all : `bash test.sh` 

## Exercise 1 

Use the github API: 
https://api.github.com/users/{username}

1. Create a function `parse_github (username)` in [exercise/exercise1.py](exercise/exercise1.py) which takes as a parameter a `username` to provide to the Github API
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
python3 -m unittest tests/exercise1.py
```

## Exercise 2 

This exercise looks like exercise 1
Create a function `parse_repos (username)` where `username` corresponds to the github user name
The called API will be https://api.github.com/users/{username}/repos
The goal is to recover all the repositories but only:
* if the id is even
* if it is not a fork
* if license.key = "mit"

The API must return a dict : 
* node_id
* owner.avatar_url
* forks (number of forks)

Use lambda (if you need) and inline loop
You can also use ternary operator!!

> Example
> GET https://api.github.com/users/av1m/repos 
> ```json
> {
>   "data" : [
>      {"node_id": "MDEwOlJlcG9zaXRvcnkxNzc5NTIwODI=", "avatar_url": "https://avatars2.githubusercontent.com/u/36456709?v=4", "forks":  0}, 
>      {"node_id": "MDEwOlJlcG9zaXRvcnkxMzQ3MDcyMzA=", "avatar_url": "https://avatars2.githubusercontent.com/u/36456709?v=4", "forks":  0},
>      {"node_id": "MDEwOlJlcG9zaXRvcnkyMzEwNzc1MDA=", "avatar_url": "https://avatars2.githubusercontent.com/u/36456709?v=4", "forks":  1}
>   ]
> }
> ```

To test your code:

```bash
python3 -m unittest tests/exercise2.py
```

## Exercise 3

This exercise deals with ternary operations

* Write an `is_even(number)` function which returns `True` if the number is even is `False` otherwise
    * The function must raise an error of type `TypeError` if the `number` isn't number type
* Write a function `which_case(param)` which returns:
    * `TypeError` if `param` isn't a string or if param is a string containing only numbers
    * 2 if the first and the last letter are in capital letters
    * 1 if the first letter is in capital letters
    * -1 if the last letter is in capital letters
    * 0 if the first and last letters are in lowercase

> All these functions must be written using ternary operators 
 
To test your code:

```bash
python3 -m unittest tests/exercise3.py
```

## Exercise4 

This exercise deals with inline loop

* Write a function `long_words (number, mylist)` which returns all the elements which have the size `number` (cant be string)

    Exemple 
    ```python
    long_words(3, ['hey', 'how', 'test', 'my best']) # {"3": ["hey", "how", "test"]}
    long_words(4, ['hey', 'how', 'test', 'my best']) # {}
    long_words(4, ['hey', 'how', 'test', 'ok', 'my best']) # {"2": ["ok"]} 
    ``` 
    
    * This function should return a `ValueError` error if `mylist` is not a list
    * This function should return a `TypeError` error if `number` is not a convertible to number (if it's "33", we don't throw an error)

To test your code:

```bash
python3 -m unittest tests/exercise4.py
```

## BONUS

Create a `crawl(url)` function that takes a URL parameter
This function must create an html file with: 
```html
<html lang="en">
<head></head>
<body>
    <!-- ALL IMG -->
    <img src="">
    <img src="">
    <img src="">
</body>
</html>
```

You can use inline function

The goal is to recover all the images from the `url` site, then create an export.html file
No unit test for this exercise :(