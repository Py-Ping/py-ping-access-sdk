# Python Ping Access SDK

Python based SDK for the Ping Access API.
Contains data modules and API interactions


# Setup

To work with the SDK generator there are two ways you can work with the licensed Ping product:

1. This module is built off of the back of the `ping-devops` tool made available [here](https://pingidentity-devops.gitbook.io/devops/getstarted). To run your own local development version of the Access server follow all the steps from the prior link. On completion you will have the following environment variables which should be present in your local profile:

```
PING_IDENTITY_DEVOPS_USER
PING_IDENTITY_DEVOPS_KEY
```

`PING_IDENTITY_DEVOPS_USER` and `PING_IDENTITY_DEVOPS_KEY` are available upon request [here](https://bit.ly/ping-devops-request).

2. If you have a license for the product put it in the root of the project directory with the name `pingaccess.lic`. This will then be mounted into the container used for SDK generation and will allow the product to be worked with.
3. If you use the PingAccess image docker older than three months, you must provide a valid license file.
4. Specify the docker image tag to VERSION variable in makefile


# Installation
```bash
# git clone this repo - something you've probably already done
pipenv install .
# OR python setup.py install
```

# Regenerate SDK

Set the swagger url for the SDK generator, if not set it will default to `localhost`. 

```bash
export PING_ACCESS_SWAGGER_URL=https://<pa_hostname>:<pa_admin_port>/pa-admin-api/v3/api-docs/pa/api-docs.json
```

The Ping Access instance being targeted by the `swagger_url` is assumed to be a newly deployed 
instance with default credentials. To use alternative credentials set the below environment 
variables.

```bash
export PING_ACCESS_ADMIN_USERNAME=<Administrator>
export PING_ACCESS_ADMIN_PASSWORD=<2Access>
```

To regenerate the APIs and models of the SDK

```bash
make generate
```

To do this against a dockerised version of Ping Access run the following:

1. Specify the docker image tag to VERSION variable in makefile
2. Run the following commands

```bash
export PING_IDENTITY_DEVOPS_USER=<Ping Identity DevOps User>
export PING_IDENTITY_DEVOPS_KEY=<Ping Identity DevOps Key>
make docker-generate
```

# Testing

A set of testing commands are available to assert that the generated SDK hasn't had any obvious issues in the generation process.

To run the unit tests use

```bash
make unittest
```

To check the code coverage for the unit tests

```bash
make coverage
```

To lint the generator code and confirm it still follows PEP8 standards

```bash
make lint
```

To lint the generated code and confirm it still follows PEP8 standards

```bash
make lint-generated
```

To confirm the modules generated can be dynamically loaded into memory without syntax or dependency issues

```bash
make module-load-test
```

To load the Java integration kit and run some sample SDK commands to exercise the generated code

```bash
make example
```

# Regenerate Documents

To regenerate the documents, after the generation of the SDK has been performed do the following.

```bash
cd docs
pipenv run sphinx-apidoc -f --implicit-namespaces -o ./source ./../pingaccesssdk
pipenv run make html
```
**You will not be able to generate the documents until AFTER you have generated the sdk**
