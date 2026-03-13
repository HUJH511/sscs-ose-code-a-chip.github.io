#   CABAgent: <ins>C</ins>omprehensive Layout-Aware <ins>A</ins>nalog <ins>B</ins>enchmark Generation via Self-Improving LLM <ins>Agent</ins>s for Analog Circuit Design Automation

This repository contains code for CABAgent, an open-source framework for comprehensive layout-aware analog benchmark generation via self-improving LLM agents for analog circuit design automation. It integrates agentic analog circuit netlist generation with automated benchmark creation across parameter settings, producing reproducible benchmark instances with schematic-level simulation, layout generation, physical verification, parasitic extraction, and post-layout evaluation


##  Table of Content
1. [Structure](#structure)
2. [Getting Started](#getting-started)
3. [Customization](#customization)
4. [Architecture](#architecture)
5. [Results](#results)
6. [License](#license)
7. [Acknowledgement](#acknowledgement)


##  Structure
While it is possible to have a stand-alone notebook, we have decided to split up the code into modules to improve readability and documentation. The following outline the directory structure.
```
./CABAgent/
|
├───.conda
├───.vscode
├───designs
│   ├───OTA_5T
│   |   └───SKY130
|   │       ├───inputs
|   │       ├───runs
|   │       └───results
|   └───...
├───Layout-ALIGN (submodule)
├───logs
├───src
│   ├───analogagent
│   |   ├───...
|   |   └───...
│   ├───cabgen
│   |   ├───__init__.py
│   |   ├───bench_gen.py
│   |   ├───dconfig.py
│   |   ├───eda_tools.py
│   |   ├───extract_mag.tcl
│   |   ├───log_manager.py
│   |   ├───netlist.py
│   |   ├───spec_manager.py
│   |   ├───visualizing.py
|   |   └───workspace.py
│   ├───dconfigs
│   |   ├───OTA_5T.yaml
|   |   └───...
│   ├───design_pipeline.py
│   └───...
├───.env
├───.gitignore
├───.gitmodules
├───LICENSE
├───README.md
└───CABAgent.ipynb
```


##  Getting Started

### Environment Setup
```
./home/
|
├───EDA_Tools
│   ├───magic
│   ├───netgen
│   └───open_pdks
└───CABAgent
```

Suggest to setup following environment under `EDA_Tools`
```
%% install dependent packages
$ cd /home/EDA_Tools
$ sudo pip3 install flake8 setuptools-scm
$ sudo apt update
$ sudo apt install build-essential tcl-dev tk-dev libx11-dev libcairo2-dev
$ sudo apt install flex bison 

%% install magic
$ git clone https://github.com/RTimothyEdwards/magic.git
$ cd magic
$ ./configure
$ make
$ sudo make install

%% install netgen
$ cd /home/EDA_Tools
$ git clone git://opencircuitdesign.com/netgen
$ cd netgen
$ ./configure
$ make
$ sudo make install

%% install open pdk
cd /home/EDA_Tools
git clone https://github.com/RTimothyEdwards/open_pdks
cd open_pdks
./configure --enable-sky130-pdk --enable-sram-sky130
make
sudo make install
make veryclean
```

Ngspice and Klayout will be installed under `/usr/bin/` by default
```
sudo apt update
sudo apt install ngspice
sudo apt install klayout
```

##  Customization


##  Architecture


##  Results


##  License
This project is licensed under

##  Acknowledgement