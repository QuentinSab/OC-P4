# OC-P4

This program is a chess tournament manager that allows you to record and view tournament information and progress.

## Requirements

- Python 3.x
- pip

## Setup

### 1. Clone the repository

Open your terminal and clone the project repository using the following command:

    git clone https://github.com/QuentinSab/OC-P4.git

Change into the project directory:

    cd OC-P4

### 2. Create a virtual environment

To create a virtual environment with venv:

    python -m venv env

### 3. Activate the virtual environment

To activate the virtual environment, use:

On Windows:

    env\Scripts\activate

On macOS/Linux:

    source env/bin/activate

### 4. Install dependencies

With the virtual environment activated, install the required packages listed in requirements.txt using the following command:

    pip install -r requirements.txt

## Usage

### 1. Running the program

Run main.py to start the program:

    python main.py

### 2. Generating a flake8 html report

To generate a new html flake8 report, use:

    flake8 --format=html --htmldir=flake8_rapport