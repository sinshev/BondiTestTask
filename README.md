**DESCRIPTION**

This set of modules is a Python 3.x based framework for Web testing.

**INSTALLATION**

To be able to run tests you have to install Python 3.x and the following external 
libraries:

1. Python 3.x 
2. Execute the following command to install all requirements from the framework root directory:

    >> pip3 install -U -r python_requirements.txt


**RUNNING**

To run all tests execute the command:
	
	>> python3 -m pytest -s --junitxml=./reports/report.xml ./tests/
	
To run the particular test execute the command:

	>> python3 -m pytest -s --junitxml=./reports/report.xml ./tests/<test_name>
