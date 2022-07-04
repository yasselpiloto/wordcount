# Wordcount

## What is it

This is a simple program that queries a stream of news and parses the articles of the first N pages counting the words and calculating the average reading time of it.

## Specs

Program is implemented in Python.

## How to run it

### From github
```bash
git clone git@github.com:yasselpiloto/wordcount.git
cd wordcount 
```

### From tar.gz

```bash
tar -xzvf wordcount.tar.gz
cd wordcount
```

### With Docker

```bash
docker build . -t axios && docker run -it --rm axios <number of pages>
```

Examples
```bash
docker build . -t axios && docker run -it --rm axios # defaults to 1
```
```bash
docker build . -t axios && docker run -it --rm axios 5 
```

### With venv

#### Install Pip

<https://pip.pypa.io/en/stable/installation/>

#### Install virtualenv

```bash
pip3 install virtualenv 
```

#### Create virtual environment

```bash
virtualenv -p python3 venv
```

#### Activate virtual environment

```bash
source venv/bin/activate
```

#### Install dependencies

```bash
pip install -r requirements.txt
```

#### Run

```bash
python -m main <number of pages>
```

Examples
```bash
python -m main # defaults to 1
```
```bash
python -m main 5
```

#### Clean up 

```bash
deactivate
```