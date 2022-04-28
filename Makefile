NAME = sparqlfun
SRC = sparqlfun/schema/$(NAME).yaml
CFG = sparqlfun/schema/config_schema.yaml
RUN = poetry run

all: project md
project:
	$(RUN) gen-project -d sparqlfun/data $(SRC)

md:
	$(RUN) gen-markdown -d docs $(SRC) -I docs/index.md && cp README.md docs/home.md

docs/endpoints.md:
	$(RUN) sparqlfun endpoints -D > $@.tmp && mv $@.tmp $@

py:
	$(RUN) gen-python $(SRC) > sparqlfun/model.py.tmp && mv sparqlfun/model.py.tmp sparqlfun/model.py

sparqlfun/config_schema.py: sparqlfun/schema/config_schema.yaml
	$(RUN) gen-python $< > $@

sparqlfun/resultset.py: sparqlfun/schema/resultset.yaml
	$(RUN) gen-python $< > $@
sparqlfun/%.py: sparqlfun/schema/%.yaml
	$(RUN) gen-python $< > $@
sparqlfun/model.py: sparqlfun/schema/sparqlfun.yaml
	$(RUN) gen-python $< > $@

# TODO: https://github.com/linkml/linkml/issues/576
sparqlfun/config/endpoints.ttl: sparqlfun/config/endpoints.yaml
	$(RUN) linkml-convert -s $(CFG) -t ttl  $< > $@.tmp && mv $@.tmp $@

examples/%.ttl: examples/%.tsv $(SRC)
	$(RUN) linkml-convert -s $(SRC) -C Container $< -o $@
examples/%.json: examples/%.tsv $(SRC)
	$(RUN) linkml-convert -s $(SRC) -C Container $< -o $@

all-examples: examples/metadata-example.ttl examples/metadata-example.json

#test: all-examples
test:
	$(RUN) pytest

docserve:
	$(RUN) mkdocs serve

gh-deploy:
	$(RUN) mkdocs gh-deploy
