# Load text file
from utils.list import Dim
from python import PythonObject

fn main():

    # List of sentences
    var sentences : PythonObject
    try:
        with open("input.txt", "r") as f:
            let text : String = f.read()
            while text.find(".") != -1:
                let index = text.find(".")
                var sentence = text[:index]
                sentences += [sentence]
                text = text[index+1:]
            print(sentences)
    except:
        pass
