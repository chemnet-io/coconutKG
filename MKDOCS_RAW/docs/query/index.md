# Querying COCONUT[KG]

The COCONUT[KG] Knowledge Graph can be queried through its public SPARQL endpoint.  
Example queries demonstrate how knowledge can be discovered and enriched beyond the 
original dataset.

## SPARQL endpoint

At [https://coconut-kg.aksw.org/sparql](https://coconut-kg.aksw.org/sparql) you'll find a SPARQL endpoint.
Both back-end and front-end are provided by OpenLink Virtuoso.
The back-end serves a SPARQL engine.

*NOTE: Before using the SPARQL endpoint we recommend to read this documentation first*


## SPARQL endpoint details

### Endpoint type

The SPARQL enpoint is provided by the [OpenLink Software Virtuoso](https://virtuoso.openlinksw.com)


### Rates and limitations

You can make a limited number of connections. The settings can be seen below:

            ResultSetMaxRows           = 10000
            MaxQueryExecutionTime      =   600  (seconds)
            MaxQueryCostEstimationTime =   400  (seconds)
            Connection limit           =    10  (parallel connections per IP address

**ATTENTION**: *The result size is currently limited to 10000 rows. This way partial results are displayed as complete ones and there is no HTTP error.*

## SPARQL example queries

## Query 1: Molecules of a given organism

This first query retrieves all molecules associated with *Cocos nucifera* and their labels.

```sparql
PREFIX coco: <http://coconutKG.aksw.org/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?organism ?organismLabel ?molecule ?moleculeLabel
WHERE {
  ?organism a coco:Organism ;
            rdfs:label "Cocos nucifera" ;
            rdfs:label ?organismLabel .

  ?molecule coco:originatesFrom ?organism .
  OPTIONAL { ?molecule rdfs:label ?moleculeLabel }
}
ORDER BY ?moleculeLabel
```

## Query 2: Molecules of a given organism with their InChIKeys

```sparql
PREFIX coco: <http://coconutKG.aksw.org/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?organismLabel ?moleculeLabel ?inchi
WHERE {
  ?organism a coco:Organism ;
            rdfs:label "Cocos nucifera" ;
            rdfs:label ?organismLabel .

  ?molecule coco:originatesFrom ?organism .
  OPTIONAL { ?molecule rdfs:label ?moleculeLabel }

  OPTIONAL {
    ?molecule coco:labeledBy ?identifier .
    ?identifier coco:standardInchiKey ?inchi .
  }
}
ORDER BY ?moleculeLabel
```

## Query 3: Molecules of a given organism with their InChIKeys and their owl:sameAs links

```sparql
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX coco: <http://coconutKG.aksw.org/ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?organismLabel ?moleculeLabel ?inchi
       (GROUP_CONCAT(DISTINCT ?sameAsOrganism; SEPARATOR=", ") AS ?sameAsOrganisms)
       (GROUP_CONCAT(DISTINCT ?sameAsMolecule; SEPARATOR=", ") AS ?sameAsMolecules)
WHERE {
  ?organism a coco:Organism ;
            rdfs:label "Cocos nucifera" ;
            rdfs:label ?organismLabel .
  OPTIONAL { ?organism owl:sameAs ?sameAsOrganism }

  ?molecule coco:originatesFrom ?organism .
  OPTIONAL { ?molecule rdfs:label ?moleculeLabel }
  OPTIONAL { ?molecule owl:sameAs ?sameAsMolecule }

  OPTIONAL {
    ?molecule coco:labeledBy ?identifier .
    ?identifier coco:standardInchiKey ?inchi .
  }
}
GROUP BY ?organismLabel ?moleculeLabel ?inchi
ORDER BY ?moleculeLabel
```

