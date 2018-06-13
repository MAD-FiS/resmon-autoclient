# resmon-autoclient
Repository for a autoclient component, which is part of resmon product.

# Usage

```
./client client [-h] [-c CONFIG] [-l LIMIT] [--register] [-v]
```

### Options
| Option                                 | Default value | Description                                       |
| -------------------------------------- |:-------------:| -------------------------------------------------:|
| **-h**, **--help**                     | ---           | show help message and exit the application        |
| **-c _CONFIG_**, **--config _CONFIG_** | config.json   | Location where is stored JSON configuration file  |
| **-l _LIMIT_**, **--limit _LIMIT_**    | 10            | Maximal limit of displayed hosts for every metric |
| **--register**                         | false         | If it's set, then user can be registered at start of the application. In other case user has to be logged before using this. |
| **-v**, **--version**                  | ---           | show program's version number and exit            |