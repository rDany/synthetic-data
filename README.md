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
no se muchas cosas.```
