


# todo:

- test cases:
    - [] - test to make sure that installation goes through if python version is not installed and that python version is installed
    - [] - test to make sure that pyenv is installed correctly
    - [] -  test to ensure that if not forced and an environment exists, that nothing happens and an error message indicating that it may be useful to use that flag appears
    - [] - test to make sure that if forced, a new environment is created
    - [] - test to ensure that the rc init file operation is idempotent and we don't end up with a bunch of spam/repeats inside the rc files


- starting case: base python image, no pyenv etc
    - test case 1: create virtual environment
        - poetry-new-project test1 --version 3.9.5
    - test case 2: create same virtual environment and expect failure because it is not forced
        - poetry-new-project test1 --version 3.9.5
        - assert fail
    - test case 3: create same virtual environment with force flag and ensure that environment is re-created
        - poetry-new-project test1 --version 3.9.5 --force
    

docker build -t poetry-new-project-test:latest -f test/Dockerfile .
docker run -it --rm -v $(pwd):/code -w /code poetry-new-project-test:latest bash

docker run -it --rm -v $(pwd):/app -w /app python:3.9.5-slim-buster bash