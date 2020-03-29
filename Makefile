deploy_with_profile:
	sls deploy --verbose --aws-profile ${PROFILE}

pip_freeze
	pip freeze > requirements.txt
