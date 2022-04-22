# Begin

## Init project environment

- git init
- git config
- pipenv install
- git commit

## Develop

- code
- git commit
- tox

## Delivery

### Run tox

Run tox to format code style and check test.

```shell script
tox
```

### Git tag

Modify package version value, then commit.

Add tag

```shell script
git tag -a v0.1.0
```

### Build

Build this tag distribution package.

```shell script
python setup.py bdist_wheel
```

### Upload index server

Upload to pypi server, or pass `--repository-url https://pypi.org/simple` to specify index server.

```shell script
twine upload ./dist/*.whl
```

## Develop guide

### Pycharm Configuration

Open project use Pycharm.

**Module can not import in src**

Check menu bar, click `File` --> `Settings` --> `Project Settings` --> `Project Structure` .
Mark `src` and `tests` directory as sources.

**Enable pytest**

Click `File` --> `Settings` --> `Tools` --> `Python Integrated Tools` --> `Testing` --> `Default runner`, then select
`pytest`.

If you run test by `Unittests` before, you should delete configuration. Open `Edit Run/Debug configurations dialog` in
In the upper right corner of Pycharm window, then delete configuration.

### Others

You should confirm `src` directory in `sys.path`. You can add it by `sys.path.extend(['/tmp/demo/src'])` if it not exist.
