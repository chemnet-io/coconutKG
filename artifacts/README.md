# Knowledge Graph files

## Query.csv

A csv file with all properties and number of entities.

## plot_properties.py

Script plots graph of properties and number of entities. 
Usage:

```python plot_properties.py -i <your_file.csv> -o <filename.pdf> -x <column_name> -y <column_name>```

```<your_file.csv>``` path to your csv file

```<filename.pdf>``` path and name of your output file. You can also export as png, ...

```<column_name>``` name of the column you want to use for the x- or y-axis

## extract_fragments.py

This script saves all fragments into a new json file. The original structure of the fragments caused us problems with mapping the data to RDF. For this reason we decided to use this workaround.

## License

The code and experiments are available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

The dataset used for training and benchmark are available under the license [Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).
*Which allows the use of the data only on its current form.*
