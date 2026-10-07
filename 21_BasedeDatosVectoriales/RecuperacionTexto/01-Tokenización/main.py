
from Tokenizer import Tokenizer

tokenizer = Tokenizer()

texto  = "Python es un lenguaje de programación"

tokens  = tokenizer.tokenize(texto)

print(tokens)