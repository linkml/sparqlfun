# sparqlfun

LinkML based SPARQL template library and execution engine

 - modularized core library of [SPARQL templates](https://github.com/linkml/sparqlfun/tree/main/sparqlfun/schema)
    - generic templates using common vocabs (rdf, owl, skos, ...)
    - OBO and biology specific, e.g. Ubergraph
    - coming soon: uniprot, wikidata, etc
 - Fully FAIR description of templates
    - Each template has a URI (e.g.: https://linkml.io/sparqlfun/PairwiseCommonDescendant)
    - Each template parameter has a URI (e.g. https://linkml.io/sparqlfun/subject)
    - Full metadata including descriptions of each
    - Templates described in YAML, RDF, SHACL, ShEx, ...
 - Rich expressive language for moedeling templates
     - uses [LinkML](https://linkml.io/linkml/) as base language
 - optional python bindings / [object model](https://github.com/linkml/sparqlfun/blob/main/sparqlfun/model.py) using LinkML
 - supports both SELECT and CONSTRUCT
 - optional export to TSV, JSON, YAML, RDF
 - extensive [endpoint metadata](https://github.com/linkml/sparqlfun/tree/main/sparqlfun/config)

This is currently alpha software, interfaces and organization may change

## Browse the default templates

* [http://linkml.io/sparqlfun/](http://linkml.io/sparqlfun/)

Note: currently not all metadata from the yaml is shown in the generated docs

## Command Line

Use the [sparqlfun:PairwiseCommonSubClassAncestor](https://linkml.io/sparqlfun/PairwiseCommonSubClassAncestor) template

```bash
sparqlfun query -e ubergraph -T PairwiseCommonSubClassAncestor node1=GO:0046220 node2=GO:0008295
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

## Local RDF files

If you specify the `-f` / `--format` option then `-e` is assumed to be a path to a file on disk:

```bash
sparqlfun query -e go.owl.ttl -f ttl -T PairwiseCommonSubClassAncestor node1=GO:0046220 node2=GO:0008295
```


## List all templates

```bash
sparqlfun endpoints
```

## Python

```python
from sparqlfun import SparqlEngine
from sparqlfun.model import PairwiseCommonSubClassAncestor

se = SparqlEngine(endpoint='ubergraph')
se.bind_prefixes(GO='http://purl.obolibrary.org/obo/GO_')
for apair in se.query(PairwiseCommonSubClassAncestor(node1='GO:0046220', node2='GO:0008295')).results:
        print(f'ROW={apair.node1} <-> {apair.node2} ANCESTOR = {apair.ancestor}')
```

For more examples, see [tests/] in GitHub


## Browsing the templates

 - source is in [sparqlfun/schema](https://github.com/linkml/sparqlfun/tree/main/sparqlfun/schema)
     - add new templates here
 - Browse the generated markdown on the site
     - markdown is auto-created from the yaml schema

You can also list templates here:

```bash
sparqlfun templates
```

or for detailed view:

```bash
sparqlfun templates --detail
```

## How it works


### Basics

Templates are defined as YAML files following the LinkML schema.

A yaml file with a single template might look like this:

```yaml
schema:
   id: http://example.org/my-vocab/templates
prefixes:
   my: http://example.org/my-vocab/
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

The YAML file is broken into blocks that minimally include 3 sections:

- schema metadata, including prefix declarations
- your templates, which are in the `classes` section
- your parameters/variables, which are in the `slots` section

Note that the definitions of the slots go in a different section from
the classes/templates. You are encouraged to "reuse" slots across templates.
However, you can use an
[attribute declaration as a shortcut](https://linkml.io/linkml/faq/modeling.html?highlight=attributes#when-should-i-use-attributes-vs-slots)
if you don't want to reuse.

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

This brings a number of tangible benefits:

 - your templates can be strongly typed
 - templates can be compiled to multiple other forms
 - templates are turned into Python dataclasses, giving an optional ORM-like layer, IDE suppport, etc
 - in future applications will be able to use template metadata
    - documentation on each slot
    - pickers for fields such as dates, enums, etc 
    - e.g. if a template slot has a range of class MyClass, applications could provide autocomplete

### Template Inheritance

Templates can be [inherited](https://linkml.io/linkml/schemas/inheritance), facilitating reuse and composition patterns

To illustrate consider a simple "base" template to query a triple:

```yaml
classes:
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

This is arguable not a particularly useful template in isolation - you may as
well query directly with sparql (nevertheless it can be useful to have
templates for even this simple pattern, to faciliate generation of
APIs etc)

New templates can use this as a base class, and inherit from it, which means that slots will be
inherited, eliminating some boilerplate and the need to redefine them


```yaml
classes:
  quad:
    is_a: triple
  slots:
     - graph  ## s/p/o slots inherited from triple
  annotations:
    sparql.select: SELECT  * WHERE {GRAPH ?graph { ?subject ?predicate ?object}}
````

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

Use of inheritance is a matter of choice. You may find it simpler to have some level of redundancy
and repeat information in similar templates. Note you will still get a decent
amount of reuse via a common vocabulary of slots

### SPARQL CONSTRUCT and nested/inlined objects

Example CONSTRUCT query:

```yaml
obo class:
    is_a: class node
    class_uri: owl:Class
    slots:
      - definition
      - exact_synonyms
    annotations:
      sparql.construct: |-
        CONSTRUCT {
          ?id a owl:Class ;
              IAO:0000115 ?definition ;
              oboInOwl:hasExactSynonym ?exact_snonyms
        }
        WHERE {
          ?id a owl:Class .
          OPTIONAL { ?id IAO:0000115 ?definition } .
          OPTIONAL { ?id oboInOwl:hasExactSynonym ?exact_snonyms } .
        }

...

slots:
  definition:
    slot_uri: IAO:0000115
  exact_synonyms:
    slot_uri: oboInOwl:hasExactSynonym
    multivalued: true
```

We can then query this as follows:

```bash
sparqlfun -e ontobee -T OboClass id=GO:0000023
```

The results will be nested following the LinkML specification for the model

```json
{
  "results": [
    {
      "id": "GO:0000023",
      "definition": "The chemical reactions and pathways involving the disaccharide maltose (4-O-alpha-D-glucopyranosyl-D-glucopyranose), an intermediate in the catabolism of glycogen and starch.",
      "exact_synonyms": [
        "malt sugar metabolic process",
        "malt sugar metabolism",
        "maltose metabolism"
      ]
    }
  ],
  "@type": "ResultSet"
}
```

(note: templates are also compiled to JSON-Schema, which can be used for additional validation)

You can also get the turtle as returned by the triplestore using `-f ttl`:

```turtle
@prefix ns1: <http://www.geneontology.org/formats/oboInOwl#> .
@prefix ns2: <http://purl.obolibrary.org/obo/> .
@prefix ns3: <https://w3id.org/sparqlfun/> .

ns2:GO_0000023 a <http://www.w3.org/2002/07/owl#Class> ;
    ns2:IAO_0000115 "The chemical reactions and pathways involving the disaccharide maltose (4-O-alpha-D-glucopyranosyl-D-glucopyranose), an intermediate in the catabolism of glycogen and starch." ;
    ns1:hasExactSynonym "malt sugar metabolic process",
        "malt sugar metabolism",
        "maltose metabolism" .

[] a ns3:ResultSet ;
    ns3:results ns2:GO_0000023 .
```

With `-t tsv` the linkml csv dumper will attempt to flatten the nested structure to TSV as closely as possible, e.g. using pipe internal seperators for multivalued

### Multiple Values

Parameters can be passed as lists, which will be translated to `VALUES` statements

```bash
sparqlfun -e ontobee -T OboClass id=GO:0000023,GO:0000024
```

### Modularity

LinkML allows importing so templates can be modularized using [imports](https://linkml.io/linkml/schemas/imports)

__NOTE__ In future this repo may be split up, with the bio/obo specific features migrating to a new repo.

### Use of Jinja commands

You can incorporate additional logic via Jinja2 templating instructions:

```yaml
obo class filtered:
    is_a: class node
    class_uri: owl:Class
    slots:
      - definition
      - exact_synonyms
    annotations:
      sparql.construct: |-
        CONSTRUCT {
          ?id a owl:Class ;
              IAO:0000115 ?definition ;
              oboInOwl:hasExactSynonym ?exact_snonyms
        }
        WHERE {
          ?id a owl:Class .
          OPTIONAL { ?id IAO:0000115 ?definition } .
          OPTIONAL { ?id oboInOwl:hasExactSynonym ?exact_snonyms } .
          {% if query_has_subclass_ancestor %}
          ?id rdfs:subClassOf ?query_has_subclass_ancestor
          {% endif %}
        }

slots:
  query_has_subclass_ancestor:
    range: class node
    description: transitive is_a parent
    in_subset:
       - ubergraph  ## requires relation-graph closure
```

## Supported Endpoints

This framework can be used with any SPARQL endpoint. However, the
current pre-defined templates are geared towards the combination of
OBO-style ontologies together with storage patterns employed in
triplestores such as ubergraph and ontobee.

 - [ubergraph](https://github.com/INCATools/ubergraph)

In particular, ubergraph uses the relation-graph inference tool to
pre-compute inferred direct triples from TBox existential axioms,
allowing for simple and powerful queries over inferred ontologies

See the config files in sparqlfun/config for a list of all pre-defined endpoints

Example:

```yaml
endpoints:
   ubergraph:
      url: https://stars-app.renci.org/ubergraph/sparql
      example_queries:
         - query_template: PairwiseCommonSubClassAncestor
           bindings:
              node1: GO:0046220
              node2: GO:0008295
```

See config_schema.yaml for the schema for endpoints

Note there is a rich metadata model that is intended to facilitate
applications and automated testing. It should be possible to automatically determine
which templates are compatible with which endpoints based on provided metadata.

## Adding your own templates

Currently this library is easiest to use if you are working with the existing pre-defined templates (PRs are welcome)

However, you can use the framework with your own templates for your own triple data.
__THIS IS NOT YET WELL-SUPPORTED__
There are a couple of steps involved,
in future this should be easier.

First you need to create your own yaml file. This needs to conform to
the LinkML metamodel - we recommend just copying an existing template
to do this. Some of this may seem like unnecessary boilerplate at this
stage, but it will come in useful later.

Next you need to compile the template:

```bash
gen-python my_template.yaml > my_template.py
```

This requires [linkml](https://linkml.io/linkml/) (this library uses linkml as a developer dependency)

You will need to pass BOTH of these as arguments to sparqlfun (`-m` and `-S`)

TODO:

 - add a dependency to the full linkml framework
 - allow dynamic compilation of templates

## See also

This was inspired by and designed as a replacement for the powerful but arcane [sparqlprog](https://github.com/cmungall/sparqlprog/) system.

TODO: list other SPARQL template frameworks

## TODOs

 - Better Document
     - framework
     - templates
     - How-tos for use with Python, SHACL, ...
     - exemplar notebooks
 - Unify with SQL/rdftab functionality in semantic-sql
 - Cypher bindings
 - Split into bio-specific
 - Expose more ubergraph awesomeness
 - FastAPI/serverless endpoint
 - Expose more validation
 - Integrate visualization / obographviz
 - compilation to other frameworks, e.g. grlc
 - Chaining
    - inject output from one into another and merge results, e.g. to get labels
    - similar to wikidata services
 - UI/yasgui integration
 - generation from dosdp (use dosdp-query algorithm)
 - Templates for
    - uniprot
    - gocams
    - wikidata

