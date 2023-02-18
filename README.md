# Usage

## Without docker

- Create environment

```shell
conda create --name stud-api python=3.9
```

- Activate virtual environment
  
```shell
conda activate stud-api
```

- Install poetry

```shell
pip install poetry

# or use:
# > conda install -c conda-forge poetry
```

- Install dependencies

```shell
poetry install
```

- Upload data from server

```shell
python3 -m stud_api --upload
```

- Run server

```shell
python3 -m stud_api --server
```

- Set cron

```shell

```

## With docker
