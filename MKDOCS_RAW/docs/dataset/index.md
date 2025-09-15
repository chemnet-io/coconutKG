# Graph Statistics

To evaluate the quality and completeness of the Knowledge Graph, both core and linking 
statistics were collected. Core statistics measure the scale and density of information, 
while linking statistics highlight the degree of integration with external sources.

## Core Statistics

- Total triples: ~92.5 million  
- Classes: 16  
- Predicates: 98  
- Average relations per molecule: 9.2  

## Linking Statistics

The following table shows the share of instances connected via `owl:sameAs`:

| Class       | Total Instances | With sameAs | Without sameAs | Share with Links |
|-------------|-----------------|--------------|----------------|------------------|
| Molecule    | ~1,000,000        | ~260,000         | ~740,000          | ~26%              |
| Organism    | ~53,000         | ~28,000        | ~25,000           | ~54%              |
| GeoLocation | ~2,640          | ~240          | ~2,400         | ~9%               |

These numbers provide insights into both the richness of the dataset and the degree of 
its interlinking with external Knowledge Graphs.
