# This is CST-3112 course of [UCSM](https://ucsm.edu.mm).
- [Installing pyton](#installing-python)
- [Installing IDE](#installing-ide)
- [Hello World](#hello-world)

## Installing python
- Download python package [link](https://www.python.org/ftp/python/3.13.5/python-3.13.5-amd64.exe). Then install at your machine.
- When installing process check the box ``Use admin privileges when installing py.exe`` and ``Add python.exe to PATH``
- Check the package is installed. Go command prompt and type
    ```
    python --version
    ```
- Alternately you can check where the python install by type at your command prompt
    ```
    where python
    ```

## Installing IDE
The most use IDE is [PyCharm community edition](https://www.jetbrains.com/pycharm/download/other.html) and [Visual Studio Code](https://code.visualstudio.com/download)


## Hello world
- Run in cmd
    - First open notepad and write
        ```
        print("Hello World!")
        ```
        and then save as ``hello.py``
    - Open cmd and path to directory you have save the file.
    - Then you can run the program by
        ```
        python hello.py
        ```
    - The fromat is ``python <file_name.py>``
    - Alternately you can run the program as
        ```
        python -m hello
        ```
    - The format is ``python -m <file_name>``, no need ``.py``
- Run with IDE(Visual Studio Code)
    - Open Visual Studio Code
    - Click ``Ctrl+Alt+X`` and download some extensions for helping your coding vibe
        - For example ``Python``, ``Pyhton Debugger``, etc. 
    - Then open the project directory
    - Click new file and name as ``hello.py``
    - Write 
        ```
        print("Hello World!")
        ```
    - Then save and click the ``Run Pyhton File``
    - Now you are on road of Pyhton