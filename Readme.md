# Coding Challenge Task
## Installation and Usage
Note: Python 3.9 is used during the development and testing of this package
1. Download or unzip the package (https://github.com/maffan-96/coding-challenge-python.git) OR The package can also be downloaded from command-line terminal using git. For using git (assuimg git is already installed).
```git clone https://github.com/maffan-96/coding-challenge-python``` 
2. Now Locate the downloaded folder and navigate inside the downloaded folder by entering ```cd coding-challenge-python-main/``` in command line terminal
3. Upgrade pip package using ```python -m pip install --upgrade pip``` (install if not installed otherwise)
4. Install the necessary python libraries to install or build (if required) custom python package. For this purpose run ```python -m pip install -r requirements.txt```. It is highly recommended to use **conda** or **venv** virtual environment to avoid dependency conflicts with other programs and packages. For creating conda virtual environment following command is used ```conda create -n py39 python=3.9``` (where py39 is the name of virtual environment)
5. Install the **challenge** custom python package by running ```python -m pip install .``` in commandline terminal. The repository is provided with build archives that can be used to install not only custom package, but can also be used to upload it to the PyPI server.
6. Now run the unittest module to check if all the libararies and the python program are setup correctly. For this purpose type, ```python tests/property_manager_unittest.py```. If it run sucessfully and no error are displayed, please proceed to the final step, i.e., running the actual program
7. Now, simply enter ```python -m challenge``` or ```python challenge``` in the command line terminal. If it runs, it will initiate an interactive program of of property manager creation. It will ask the input in following sequence. 
    1. Please enter your name (e.g., ```Affan```) i.e., name of the property manager
    2. Please enter your ID (e.g, ```123```)  i.e., ID of the property manager
    3. Please enter 1 or 2 to create property (Input other than 1 or 2 won't be accepted)
    4. Please enter address and rent of the property per month (e.g., ```Valencia``` and ```450``). Any blank string and invalid number won't be accepted here in respective responses. We are asuming there is only one property needs to be created at the moment.
    5. Please enter 1 or 2 to create applicant (Input other than 1 or 2 won't be accepted)
    6. Please enter name and income of the applicant per month (e.g., ```Khan``` and ```1000`` ). Any blank string and invalid number won't be accepted here in respective responses. We are asuming there is only two applicant needs to be created at the moment.
    7. Now the program will compute the best applicant by computing rent-to-income (R2I) ratio. The applicant with least r2i is returned as a best applicant. If two applicant has the same r2i, the 1st applicant would be nominated as a best applicant
