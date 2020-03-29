deploy_with_profile:
	sls deploy --verbose --aws-profile ${PROFILE}

pip_install:
	pip install -r requirements.txt

pip_freeze:
	pip freeze > requirements.txt

venv_activate:
	source ./myvenv/bin/activate

