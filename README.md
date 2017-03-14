# synthetic-data
Synthetic Data repository and compiler

This repository holds artificial conversations stored on text files on a special format.
The conversations can then be compiled using `data_compiler.py` to text files to train seq2seq models.

For example the following code:

```
# Example
H:[¿]qué cosa no [sabes|sabés]?
R:¡hay tantas cosas que no se!
R:no se muchas cosas.
```

generates the following outputs:

Human:

```
qué cosa no sabes?
qué cosa no sabes?
qué cosa no sabés?
qué cosa no sabés?
¿qué cosa no sabes?
¿qué cosa no sabes?
¿qué cosa no sabés?
¿qué cosa no sabés?
```

Robot:

```
¡hay tantas cosas que no se!
no se muchas cosas.
¡hay tantas cosas que no se!
no se muchas cosas.
¡hay tantas cosas que no se!
no se muchas cosas.
¡hay tantas cosas que no se!
no se muchas cosas.
```

## Scripting
First draft for two steps seq2seq 

```
H:_GREETING Hello
R:_SAD Hi. BECOUSE:_GREETING
R:_NORMAL Hi, how are you? BECOUSE:_GREETING
R:_HAPPY Hi there! :D BECOUSE:_GREETING

H:_BORED I'm bored
R:What do you like to do in your free time? BECOUSE:_BORED

H:_PROGRAM_TIME What time is it?
R:Is one o'clock BECOUSE:_PROGRAM_TIME 01:00
```

- Get input question.
- Ask the model what data is necesary to answer the question properly.
- Append the data to the question and feed the model with it.
- Return the answer.
