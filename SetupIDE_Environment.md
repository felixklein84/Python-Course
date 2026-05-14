# Get Started Part 1: Setting up development environment

Steps 1–3 can be completed independently.

We’ve also prepared two videos where the installation process is explained and you can see exactly where to click:
* [Windows](https://youtu.be/qn96nt-9jaU)
* [Mac](https://youtu.be/9h5V4XxNm_4)

## Step 1: Install Git and join Github Classroom

- Install [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) using the default settings as recommended.
- Create a [GitHub account](https://github.com/join).

## Step 2: Install VS Code as your IDE

- Download and install the latest version of [VS Code](https://code.visualstudio.com) (Visual Studio Code). Follow the installation instructions for your operating system. Run the `.exe` file you downloaded and follow the default setup steps.

## Step 3: Install Python and Poetry

- Install [Python version 3.8.5](https://www.python.org/downloads/). Download the version matching your operating system and follow the default settings during the installation (Windows). One important change: make sure to check the option  
  ```Add Python 3.8 to PATH```  
  when the installer opens.  
  Reference image: https://docs.python.org/3/_images/win_installer.png

- Log out and log back into your computer.
- Install [Poetry](https://python-poetry.org/docs/#installation). Be sure to follow the `osx / linux / bashonwindows install instructions` or the appropriate instructions for Windows.

- Log out and log back in again.
- Then run the following command in the terminal:
    ```shell
    > poetry config virtualenvs.in-project true
    ```

# Get Started Part 2: Setting up the Python Course Project

## Step 1: Clone the Repository

- Create your assignment repository using the [Classroom link](https://classroom.github.com/a/eDXSZ89X). You may be asked to authenticate during the process.
- Open Git Bash (or Terminal) and navigate with `cd` to the folder where you'd like to store your Python course repository, for example:
    ```shell
    > cd C:\Users\moritzkern\projects\uni
    ```
- Now clone the repository you just created. Replace `%repositoryname%` with the actual name of your generated repo (you’ll find it by clicking on `Code` in GitHub).
    ```shell
    > git clone https://github.com/STADS-Mannheim/%repositoryname%
    ```
    You’ll be asked for your GitHub username and password — enter both.

## Step 2: Setting up the VS Code Workspace

- Open VS Code.
- In VS Code, open the folder where you cloned the repository via `Open Folder`, e.g.  
  `C:\Users\moritzkern\projects\uni\pythonkurs2020_1_get_started_%username%`
- Save the newly created workspace (`File > Save Workspace As...`). Choose a filename like `pythonkurs.code-workspace`.
- Install the following extensions in VS Code from the Extension Marketplace:  
    - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)  
    - [Live Share Extension Pack](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare-pack)  
    - If you follow the links above, you’ll need to press the green `Install` button in both the browser and VS Code, and allow any requested permissions.

## Step 3: Install the Poetry Project

- Open the terminal in VS Code (`Terminal -> New Terminal`). On Windows, make sure NOT to use PowerShell as it may cause issues.
- Run `poetry install`:
    ```shell
    > poetry install
    Creating virtualenv pythonkurs2020-part1 in C:\Users\moritzkern\projects\uni\pythonkurs2020_1_get_started\.venv
    Installing dependencies from lock file

    Package operations: 62 installs, 0 updates, 0 removals

    - Installing ipython-genutils (0.2.0)
    ...
    ```

Congratulations, you've completed the setup and all technical requirements for the Python course are now in place! :)
