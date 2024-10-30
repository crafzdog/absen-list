# absen-list

Sebuah project mahakarya gabut buatan anak bangsa yang ditujukan untuk data absensi anak-anak IF.

## Table of Contents

- [Getting Started](#getting-started)
- [How to Build the App](#how-to-build-the-app)
  - [Dependency Tool](#dependency-tool)
  - [Run the App](#run-the-app)

## Getting Started

1. Clone the project repository.

```bash
git clone https://github.com/crafzdog/absen-list.git
```

2. Create a new branch for your workflow.

```bash
git branch <branch_name>
```
*Note: The name of a new branch should follow a convention, e.g dev/Crafzdog, dev/Wan.


## How to Build the App

### Dependency Tool

1. You need Poetry, a dependency manager to be installed.

    * On Windows.
  
      ```bash
      (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
      ```

2. Add Poetry to your PATH.

   The installer creates a poetry wrapper in a well-known, platform-specific directory:

     * On Windows.
  
       ```bash
       %APPDATA%\Python\Scripts
       ```

   If this directory is not present in your $PATH, you can add it in order to invoke Poetry as poetry.

3. Use Poetry.

   Once Poetry is installed and in your $PATH, you can execute the following:

      * On Windows.
    
        ```bash
        poetry --version
        ```

   If you see something like Poetry (version 1.2.0), your install is ready to use!


### Run the App

1. Move to the project directory. For example:

   ```bash
   cd ~/Download/git/absen-list
   ```

2. Install project dependencies.

   ```bash
   poetry install
   ```

3. Running your app.

   ```bash
   poetry run start
   ```
