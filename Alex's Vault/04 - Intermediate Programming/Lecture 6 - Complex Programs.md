Complex programs are made up of numerous modules.

- Consider the frameworks we import - think back to Flask

When we break our code into smaller functional groups we:

- Improve maintainability
- Allow developers to work in parallel
- Add organization to our code
- Allow code to be reused.

## How Imports Work

Import allows us to use code in other modules

- While often presented as “adding the code in a module to our program” - this is an oversimplification of the functionality.
- In reality import:
    - Finds the module file - checks a number of locations for the module. If not found - exception!
    - Compiles it to byte code - in fact, this may not happen. If the latest compiled file (.pyc) is newer than the corresponding source then the file is not recompiled for efficiency.
    - Runs the module’s code as required - this is why we have a name check.
        - When we run a file, things that are defined are in fact run and created in memory - they are used until they are called; this is why we need a name check in modules we import.

## The Search Path

The following locations are searched for a module:

1. The home directory of a program
2. PYTHONPATH directories
3. Standard Library directories
4. Contents of .pth files
5. The site-packages home of third party extensions.

## Virtual Environments

A virtual environment is an isolated Python environment where a project’s dependencies are installed in a different directory from those installed in the system’s default Python path and other virtual environments.

Dependency managers are tools that enable easy management of a project’s dependencies.

  

Creating a virtual environment:

```PowerShell
python -m venv myenv
```

To activate the environment - make sure you are in the directory

```PowerShell
source ./myenv/bin/activate
```

We use pip to install packages and frameworks

```PowerShell
pip install Django
```

We might want to install numerous packages. We can get a list of installed packages using

```PowerShell
python -m pip freeze > requirements.txt
```

We can deactivate a vent using:

```PowerShell
deactivate
```