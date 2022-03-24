LOCAL_VARIABLES := RUN_ENV=DEV \
	LOGGING_LEVEL=DEBUG \
	MYSQL_CONNECTION_STRING="mysql+pymysql://root:krishna13@localhost/secure_communication" \

create_env:
	virtualenv venv
	echo "now call: source ./venv/bin/activate"

activate_env:
	source ./venv/bin/activate

format_code:
	black .

install:
	pip3 install -r ./requirements.txt

test:
	echo "testing"
	pytest --spec --junitxml=junit/test-results.xml --cov=jhh_partner_service/. --cov=tests/. --cov-report=xml --cov-report=html --cov-report=term --no-coverage-upload

unit-test:
	echo "testing"
	pytest tests/unit/. --spec --junitxml=junit/test-unit-results.xml --cov=jhh_partner_service/. --cov=tests/. --cov-report=xml --cov-report=html --cov-report=term --no-coverage-upload

e2e-test:
	echo "testing"
	pytest tests/e2e/. --spec --junitxml=junit/test-e2e-results.xml --cov=jhh_partner_service/. --cov=tests/. --cov-report=xml --cov-report=html --cov-report=term --no-coverage-upload

run:
	$(LOCAL_VARIABLES) python app.py

package:
	echo "to create a docker build/ python package/code artefacts"
	docker-compose -f ./docker-compose.yml build

publish:
	echo "to publish a created docker image / code artefacts to a cental repository"
	docker-compose -f ./docker-compose.yml push

run_package:
	docker-compose -f docker-compose.yml up --remove-orphans

deploy:
	echo "deploying"

lint:
	black --check .

test-ci:
	echo "testing"
	$(LOCAL_VARIABLES) pytest --spec --junitxml=junit/test-results.xml --cov=jhh_partner_service/. --cov=tests/. --cov-report=xml --cov-report=html --cov-report=term --no-coverage-upload
	echo "Running CSS JS Hack utility since Microsoft did an awesome job on CSP security settings." 
	css_js_inliner
	