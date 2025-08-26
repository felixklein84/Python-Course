
# Poetry as a Package and Dependency Manager

* Install [Poetry](https://python-poetry.org/docs/#installation). Be sure to follow the `osx / linux / bashonwindows install instructions` or on Windows the `windows powershell install instructions` from the website.
* Now run the following commands in your project as the working directory (e.g. `C:\...\pythonkurs2020`):

  ```shell
  shell> poetry config virtualenvs.in-project true
  ```
* Now initialize the virtual environment:

  ```shell
  shell> poetry install
  Creating virtualenv pythonkurs2020-part1 in /%path_to_folder%/pythonkurs2020_1_get_started/.venv
  Installing dependencies from lock file

  No dependencies to install or update
  ```

  *(Alternatively) If you're initializing a new package, use the following command:*

  ```shell
  shell> poetry init
  ```
* Now we select the created environment as the Python interpreter for our project in VS Code. To do this, open the [Command Palette](https://code.visualstudio.com/docs/getstarted/tips-and-tricks#_command-palette), search for *"Select Python Interpreter"*, and choose the interpreter located in the `.venv` folder of your project directory.
* Then open a new terminal session by clicking on the *"+"* button. The terminal should now open in the venv:

  ```shell
  (.venv)> waiting
  ```

# Install Dev Dependencies

We now install:

* [pylint](https://www.pylint.org) for static code analysis
* [Jupyter Notebook](https://jupyter.org) as an interactive coding notebook

```bash
bash> poetry add pylint notebook jupyter_contrib_nbextensions --dev

Using version ^2.6.0 for pylint  
Using version ^6.1.4 for notebook  
Using version ^0.5.1 for jupyter_contrib_nbextensions

Updating dependencies  
Resolving dependencies... (3.0s)

Writing lock file

Package operations: 62 installs, 0 updates, 0 removals

  - Installing ipython-genutils (0.2.0)
    ...
  - Installing pylint (2.6.0)
```