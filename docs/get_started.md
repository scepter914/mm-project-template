## Set up development environment

- Install [black](https://github.com/psf/black)

```sh
pip install black
```

- Install [isort](https://github.com/PyCQA/isort)

```sh
pip install isort
```

- Install pre-commit

```sh
pip install pre-commit
```

- Formatting by manual command

```sh
# To use:
pre-commit run -a

# runs every time you commit in git
pre-commit install  # ()
```

- If you use VSCode, you can use [tasks of VSCode](https://github.com/tier4/autoware-ml/blob/main/.vscode/tasks.json).
  - "Ctrl+shift+P" -> Select "Tasks: Run Task" -> Select "Pre-commit: Run"
- In addition to it, I recommend VSCode extension
  - [black-formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)
  - [isort](https://marketplace.visualstudio.com/items?itemName=ms-python.isort)

## Get started
### 1. Set environment

- Clone

```
git clone https://github.com/scepter914/mm-project-template
```

- Build docker

```sh
docker build -t mm_template .
```

### 2. Prepare dataset

Prepare the dataset you use.

#### nuScenes for 3D detection

- Download dataset from official website
- Run docker

```sh
docker run -it --rm --gpus all --shm-size=64g -v $PWD/:/workspace -v $PWD/data:/workspace/data mm_template
```

- Make info files for nuScenes
  - If you want to make own pkl, you should change from "nuscenes" to "custom_name"

```sh
python tools/create_data.py nuscenes --root-path ./data/nuscenes --out-dir ./data/nuscenes --extra-tag nuscenes
```

### 3. Train and evaluation

- Change config
  - If you use custom pkl file, you need to change pkl file from `nuscenes_infos_train.pkl`.
