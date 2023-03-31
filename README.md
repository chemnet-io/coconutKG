# Schema

## Coconut

As a data basis we have used [Coconut](https://coconut.naturalproducts.net/documentation). Coconut is an open source project for natural products. It combines content from more than 50 datasets.

## Schema creation process

Some properties occur multiple times in original Coconut record. This is probably due to the fact that Coconut was created from multiple datasets. We decided not to transfer these duplications into our ontology, as far as they are visible to us. We used the command line tool [jq](https://stedolan.github.io/jq/) to verify the duplicates. For example with the following command: ```jq 'select(.simpleInchi != .uniqueNaturalProduct.inchi)' sourceNaturalProduct.jsonl```

List of duplicates:
- ```$oid``` and ```$oid```
- ```totalAtomNumber``` and ```total_atom_number``` 
- ```simpleInchi``` and ```inchi```
- ```simpleInchiKey``` and ```inchikey```

We have decided to merge ```citation``` and ```citationDOI``` to ```citationDOI```.

```synonyms``` and ```uniqueNaturalProduct.synonyms``` will also be merged.

Since in many cases there is no information in the property ```continent``` and in ```geoLocation``` there is information about the origin, we decided to keep only ```geoLocation```.

We also used the command line tool jq to find out which properties do not contain values. For example with the following command: ```jq '.uniqueNaturalProduct.collection | select(length > 0)' sourceNaturalProduct.jsonl```

List of empty properties:
- ```allTaxa```
- ```collection```
- ```allWikidataIds```
- ```taxid```
- ```allChemClassifications```

## License

The code and experiments are available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

The dataset used for training and benchmark are available under the license [Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).
*Which allows the use of the data only on its current form.*
