# resmon-autoclient
Repository for a autoclient component, which is part of ResMon software.

**Info!** All path existing in this file are considered
as being used in project/install root directory.

# Usage

```bash
./resmon-client [-h|--help] [-c|--config CONFIG] [-l|--limit LIMIT] [--register] [-v|--version]
```

### Options
| Option                                 | Default value        | Description                                       |
| -------------------------------------- |:--------------------:| -------------------------------------------------:|
| **-h**, **--help**                     | ---                  | show help message and exit the application        |
| **-c _CONFIG_**, **--config _CONFIG_** | ./data/config.json   | Location where is stored JSON configuration file  |
| **-l _LIMIT_**, **--limit _LIMIT_**    | 10                   | Maximal limit of displayed hosts for every metric |
| **--register**                         | false                | If it's set, then user can be registered at start of the application. In other case user has to be logged before using this. |
| **-v**, **--version**                  | ---                  | show program's version number and exit            |

# Instalation
We provide single file `install-autoclient.sh` which is used to install this application. It's enough that you just run it as following:
```bash
./install-autoclient.sh [--quiet]
```
Later you have to accept unpacking files. It's automatically accepted if you choose option _--quiet_.
Application will be installed in the same place where script `./install-autoclient.sh`

# For developers

**Info!** This instruction is written for developers who use Linux operating system.

You have to clone this repository. Then you can work with it and develop the application.
If you want to run it locally for testing, it doesn't need to create installer `install-autoclient.sh`

## Requirements

## Scripts

You can run some scripts to make your developing process faster and more comfortable.
All scripts can be executed in this way:
```bash
./scripts.sh SCRIPT_NAME
```
where `SCRIPT_NAME` can be as following:
* `build` - it prepares file _install.sh_ to use it later for installing this application
* `docgen` - it generates documentation and puts it into _./docs/_ directory
* `runtest` - it runs all tests available for this project

**Info!** If you need to use environment file manually, it is located in `./data` directory.

## Deployment on Docker
You can develop this application on [Docker](https://docs.docker.com).
It can be used to testing it in a clear environment.
At start you can make yourself sure that the file `install-autoclient.sh`
is created by _build_ script and that it has been executed
after last changes in your code.

Then you can execute these two following commands:
```bash
docker build -t resmon-autoclient .
```
and:
```bash
docker run -it resmon-autoclient
```
Then you can run there this application.