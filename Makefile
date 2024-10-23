
#########################################################################################
#  postmodern-python environment tasks


# install python dependencies
rye_setup:
	@( 	rye sync; \
	  	source .venv/bin/activate; \
	)



rye.coverage:
	rye run coverage run -m pytest

rye.coverage.report:
	rye run coverage report

docker.build:
	docker build -t postmodern-image -f docker/Dockerfile .

docker.shell:
	docker run --rm -it --name localpostmodern --entrypoint bash postmodern-image

docker.run:
   docker run --rm  --name localpostmodern  postmodern-image