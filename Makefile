NAME = sparqlfun
SRC = sparqlfun/schema/$(NAME).yaml
RUN = poetry run

all: project md
project:
	$(RUN) gen-project -d sparqlfun/data $(SRC)

md:
	$(RUN) gen-markdown -d docs $(SRC) -I docs/index.md && cp README.md docs/home.md

py:
	$(RUN) gen-python $(SRC) > sparqlfun/model.py

sparqlfun/config_schema.py: sparqlfun/schema/config_schema.yaml
	$(RUN) gen-python $< > $@

examples/%.ttl: examples/%.tsv $(SRC)
	$(RUN) linkml-convert -s $(SRC) -C Container $< -o $@
examples/%.json: examples/%.tsv $(SRC)
	$(RUN) linkml-convert -s $(SRC) -C Container $< -o $@

all-examples: examples/metadata-example.ttl examples/metadata-example.json

#test: all-examples
test:
	$(RUN) pytest

testdocs:
	mkdocs serve

gh-deploy:
	mkdocs gh-deploy
