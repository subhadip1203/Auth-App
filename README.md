# Auth Microservice

**_A auth Microservice for Web application based on Google Firebase_**

- **Languages & Frameworks** Python - FastAPI , JavaScript - Vue.js , MariaDB
- **Supported Auth** Email-password  , Google , Microsoft
- **Auth Signature** JWT with RS256 signing algorithm


## Getting Started

### Windows Environment ( without  Docker )
Install virtualenv : `pip install virtualenv` <br>
Create virtual env: `virtualenv myenv` <br>
Activate virtual env : `myenv\Scripts\activate` <br>
De-Activate virtual env : `deactive` <br>


### Ubuntu / Mac Environment ( without  Docker )
Create virtual environment  `python3 -m venv virtualEnv`<br>
Activate virtual environment `source virtualEnv/bin/activate`<br>
Deactivate virtual env : `deactivate`<br>


## Run the app
For test environment `uvicorn main:app --reload`




## Packages for teh project

install Packages  `pip install -r requirements.txt`  <br>
Update requirements file , after installing new package `pip freeze > requirements.txt pip install -r requirements.txt` <br>



#