"""
Assignment 1: Python Class
"""

#task 1
def hello():
    return "Hello!"

#task 2
def greet(name):
    return f"Hello, {name}!"

#task 3
def calc(a,b, operation="multiply"):

    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b
            case "modulo":
                return a % b
            case "int_divide":
                return a // b
            case "power":
                return a ** b
            case _:
                return "Invalid operation"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"
    
  #task 4
def data_type_conversion(value,cast_type):
    cast_type = cast_type.lower()
    try:
        match cast_type:
         case "float":
                return float(value)
         case "int":
                return int(value)        
         case "str":
            return str(value)
         case _:
            return "Unknown Type"
    except ValueError:
        return f"You can't convert {value} into a {cast_type}."

#task 5
def grade(*args):
    try:
        avg = sum(args) / len(args)
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."

    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"
# task 6
def repeat(a_string, count):
    new_string = ""
    for i in range(count):
        new_string += a_string
    return new_string

# Task 7
def student_scores(result, **kwargs):
    if not kwargs:
        return "No student scores provided."
        
    low_result = result.lower()
    
    match low_result:
        case "mean":
            total = 0
            count = 0
            for key, value in kwargs.items():
                total += value
                count += 1
            return total / count       
        case "best":
            return max(kwargs, key=kwargs.get)
        case _:
            return "Not a valid entry."

# Task 8
def titleize(a_string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = a_string.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1:
            words[i] = word.capitalize()
        elif word in little_words:
            words[i] = word
        else:
            words[i] = word.capitalize()

    return " ".join(words)

# Task 9
def hangman(secret, guess):
    result = ""
    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"
    return result

# Task 10
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    result_words = []

    for word in words:
        if word[0] in vowels:
            result_words.append(word + "ay")
        else:
            consonants = ""
            i = 0
            while i < len(word) and word[i] not in vowels:
                if word[i:i+2] == "qu":
                    consonants += "qu"
                    i += 2
                    break
                else:
                    consonants += word[i]
                    i += 1
            pig_word = word[i:] + consonants + "ay"
            result_words.append(pig_word)

    return " ".join(result_words)