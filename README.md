# ddb-python-fastapi-demo

This demo is a boilerplate for a python/fastapi/poetry project using ddb.
It uses an alpine python 3.13 docker image as a base.

## Quickstart

### Clone the project

```bash
git clone https://github.com/inetum-orleans/ddb-python-fastapi-demo.git
```

### Configure ddb

```bash
ddb configure
```

### Activate ddb if it is the first time opening the project

```bash
$(ddb activate)
```

### Configure your environnement variables

Copy/Paste the `.env.sample` and rename it `.env`.

Set your _"X-API-KEY_" as you want. You will need to pass this value to every request header in order to be authorized.

### Initialize the project

```bash
make init
```

### Launch the server

```bash
make watch
```

## Warning

This demo is still work in progress and was made with limited understanding of a python environnement.
