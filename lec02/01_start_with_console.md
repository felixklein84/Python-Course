# Start with Python Console

Use the integrated terminal in VS Code. If it's not visible, [open it](https://code.visualstudio.com/docs/editor/integrated-terminal) (`Terminal > New Terminal`). On Windows, make sure to use `cmd` and not `powershell`.

Depending on your operating system (try both), enter in the terminal:

```shell
> where python
```

or

```shell
> which python
```

You should now see a list of locations where your OS finds a Python installation. If the list is empty, something went wrong during the installation.

Next, we'll check that we have the correct Python version 3.8.5 installed by entering into the terminal:

```shell
bash> python --version
Python 3.8.5
```

Now start Python by typing `python` into the terminal. Python should now run and you should see the following (or a similar) console output:

```shell
bash> python
Python 3.8.5 (default, Aug 22 2020, 10:36:09) 
[Clang 11.0.0 (clang-1100.0.33.8)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

Error handling: If the correct Python version is not found, you need to add the following to the PATH variable in the environment variables on Windows: `C:\Users\%username%\AppData\Local\Programs\Python-38-32\python.exe`. Then log out and log back in again.

# Python as a Calculator

Now enter a simple calculation in Python and you should get the following output.

```python
>>> 1+2
3
```

Now execute the following calculation in the Python console:

$\left(\frac{1}{3} * 5 + 7.3 \right)^2$

```python
>>> (1/3 * 5 + 7.3)**2
80.4011111111111
```

# Variables in Python

Variables can be assigned using the equals sign and used in calculations.

```python
>>> x = 1
>>> print(x)
1
>>> y = 3
>>> x + y
4
```

This also works for text.

```python
>>> abc = "Dies ist ein Text"
>>> print(abc)
Dies ist ein Text
```

And for boolean values:

```python
>>> is_weekday = True
>>> print(is_weekday)
True
```

Some **background knowledge** about variables in Python:

* Unlike other programming languages, Python does not have a command to declare variables. A variable is created at the moment a value is assigned to it.

* Variables do not need to be declared with a specific type; the type is inferred from the assigned value. The type of a variable is not fixed and can be changed.

How can we name variables?

* A variable must start with a letter or underscore.
* A variable cannot start with a number.
* Variables can only contain alphanumeric characters and underscores.
* Variables are case-sensitive.

# Closing Python

Finally, we close the interactive Python instance.

```bash
>>>exit()
bash>
```
