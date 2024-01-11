# PyRPG
A simple and complex game on Python that i and my friend made on school(basicly i did but he helped hehe). Open to anyone who wanna help improve the code. Please coment any suggestions and bugs so i can learn and improve the game.

## Learning 
This game is an upgrade of the game that i made (https://github.com/SoyNashi/kill-the-boss).
I improved some graphic and design of the game: Colours, textart, unicode charecters (It doesnt work well on linux because the uniode charecters work diferent or idk but it doesnt show the charecters. Some of them). 
Also i simplified the game by making all in one page. By the moment idk how to combine two diferent codes to work thogether but i think that if that is possible it woud work better if i had to improve the game.
I used python because its more simple and i can use libraries.
The structure of the code is a bit messy but i made all by functions so i can go back and foward in the game more easy. Some variables are copies of other because it didnt work fine or idk but in that way it worked so i won't touch it.
U can make branches but i would prefer that u just comment wat i can improve so i learn.

## Traduction
In the next version the game will be in a variety of languages. Main language is spanish. If you use any other language it can slow down the game because I used a library thet traduces the text by online conection to google translator.
It may be veeeery slow, but i didnt find anithing better. I tryed a library called goselate but it gave me an error because i was trying to traduce so many lines, but i have to so it didnt work for me.
If you know any other library that can do the job better without having to do a variable of the text. let me explain.

Now the traduction is made like this
```
lang = "en" # the language

def anithing():
  global lang # imports the variable
  traductor = GoogleTranslator(source='es', target=lang) # shortcut for the next code

  print(traductor.translate("Hola")) # the code on the print
```
And the result is "hello".
If anyone know a library more fast but that work like this im interested

## Instalation
Install the requiered libraries. (i think that requieriments are well made but if it doesn't install then u will have to install all the libraries by hand, theres only 5)
``` pip install requieriments.txt ``` 

