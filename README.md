# Ninjag
A python package for generating `Ninja` build configuration files based on user input YAML files

## Install
This is a python command line app.  
After the input you will have `ninja` command
on your path.
```
pip install ninjag
```

## Dependency
* [PyYAML](https://github.com/yaml/pyyaml)

## Usage
The first argument is the output file name,  
The rest of the arguments are input files.
```
ninjag build.ninja input1.yaml input2.yaml ...
```

## Examples
input1.yaml
```
const:
  cflags: -Wall -Wconversion -Wextra

rule:
  cc: gcc $cflags $in -o $out

tasks:
- rule: cc
  in: [hello.c]
  out: [hello.exe]
  const:
    cflags: -Wall

```

Then type command:
```
ninjag build.ninja input1.yaml
```
The output is (`build.ninja`):
```
cflags = -Wall -Wconversion -Wextra
rule cc
  command = gcc $cflags $in -o $out
build hello.exe: cc hello.c
  cflags = -Wall

```

## License
MIT/X11 Steven(Yuhang) Wang (c) 2016
