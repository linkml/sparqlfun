# sparqlfun

LinkML based SPARQL template library and execution engine

 - modularized core library of SPARQL templates
    - generic templates using common vocabs (rdf, owl, skos, ...)
    - OBO and biology specific, e.g. Ubergraph
    - coming soon: uniprot, wikidata, etc
 - Fully FAIR description of templates
    - Each template has a URI
    - Each template parameters has a URI
    - Full metadata including descriptions of each
    - Templates described in YAML, RDF, SHACL, ShEx, ...
 - optional python bindings using LinkML
 - supports both SELECT and CONSTRUCT
 - optional export to TSV, JSON, YAML

## Browse the default templates

* [http://linkml.io/sparqlfun/](http://linkml.io/sparqlfun/)

Note: currently not all metadata from the yaml is shown in the generated docs

## Command Line

```bash
sparqlfun -e ubergraph -T PairwiseCommonSubClassAncestor node1=GO:0046220 node2=GO:0008295
```

results:

```yaml
results:
- node1: GO:0046220
  node2: GO:0008295
  predicate1: rdfs:subClassOf
  predicate2: rdfs:subClassOf
  ancestor: GO:0009987
- node1: GO:0046220
  node2: GO:0008295
  predicate1: rdfs:subClassOf
  predicate2: rdfs:subClassOf
  ancestor: GO:0044237
- node1: GO:0046220
  node2: GO:0008295
  predicate1: rdfs:subClassOf
  predicate2: rdfs:subClassOf
  ancestor: GO:0044271
...
```

## Python

```python
se = SparqlEngine(endpoint='ubergraph')
se.bind_prefixes(GO='http://purl.obolibrary.org/obo/GO_')
for row in se.query(PairwiseCommonSubClassAncestor, node1='GO:0046220', node2='GO:0008295'):
        print(f'ROW={row}')
```

For more examples, see tests/

## Service (via Fast API)

coming soon!

## Browsing the templates

 - source is in sparqlfun/schema
     - add new templates here
 - Browse the generated markdown on the site


## How it works

### Basics

Templates are defined as YAML files following the LinkML schema.

A yaml file with a single template might look like this:

```yaml
classes:
  my template:
    slots:
      - my_var1
      - my_var2
    annotations:
      sparql.select: |-
        SELECT  * WHERE { ... ?my_var1 ... ?my_var2}
      
slots:
  my_var1:
    description: about my var 1
  my_var2:
    description: about my var 2
```      

This defines a template `MyTemplate` with two slots/parameters, and an
arbitrarily complex SPARQL select query.

Note that the definitions of the slots go in a different section from
the classes/templates. You are encouraged to "reuse" slots across templates.

The above can be used in queries:

```bash
sparqlfun -e ubergraph -T MyTemplate my_var2=MY_VAL
```

You can ground any or all of your vars on the command line (if you ground all then your SELECT is effectively an ASK query).

However, the features go beyond other templating systems, and leverage
the fact that LinkML is a fully-fledged rich modeling language with bindings to JSON-Schema, SHACL, ShEx, etc.

For example, you will get markdown documentation describing your templates. This markdown documentation will be even richer if you annotate your schemas with metadata such as

 - descriptions
 - ranges for slots
 - mappings and URIs for your templates and slots

### Template Inheritance

Templates can be inherited, facilitating reuse and composition patterns

To illustrate consider a simple "base" template to query a triple:

```yaml
triple:
    aliases:
      - statement
    description: >-
      Represents an RDF triple
    slots:
      - subject
      - predicate
      - object
    class_uri: rdf:Statement
    in_subset:
      - base table
    annotations:
      sparql.select: SELECT  * WHERE { ?subject ?predicate ?object}
```

This is not a particularly useful template in isolation - you may as
well query directly with sparql (nevertheless it can be useful to have
templates for even this simple pattern, to faciliate generation of
APIs etc)

This template can be inherited, which means that slots will be
inherited, eliminating some boilerplate and the need to redefine them

Inerhitance allows even more powerful features using the LinkML
`classification_rules` construct. Let's say we want to represent type
triples as children of generic triples:


```yaml
rdf type triple:
    is_a: triple
    description: >-
      A triple that indicates the asserted type of the subject entity
    slot_usage:
      object:
        description: >-
          The entity type
        range: class node
    classification_rules:
      - is_a: triple
        slot_conditions:
          predicate:
            equals_string: rdf:type
```            

**Note we don't need to specify a SPARQL template here** - the
template is autogenerated from the classification rule.

### Modularity

LinkML allows importing so templates can be modularized

In future this repo may be split up, with the bio/obo specific features migrating to a new repo.

### Use of Jinja commands

TODO - document this

## Supported Endpoints

This framework can be used with any SPARQL endpoint. However, the
current pre-defined templates are geared towards the combination of
OBO-style ontologies together with storage patterns employed in
triplestores such as ubergraph and ontobee.

 - [ubergraph](https://github.com/INCATools/ubergraph)

In particular, ubergraph uses the relation-graph inference tool to
pre-compute inferred direct triples from TBox existential axioms,
allowing for simple and powerful queries over inferred ontologies

## See also

This was inspired in part by the powerful but arcane [sparqlprog](https://github.com/cmungall/sparqlprog/) system

## TODOs

 - Better Document
     - framework
     - templates
     - How-tos for use with Python, SHACL, ...
     - exemplar notebooks
 - Unify with SQL/rdftab functionality in semantic-sql
 - Split into bio-specific
 - Expose more ubergraph awesomeness
 - FastAPI/serverless endpoint
 - Templates for
    - uniprot
    - gocams
    - wikidata

