# GBIF-gridded-data
### Identifying datasets that have gridded record coordinates or contain a portion of records that are gridded

This tool shall be able to identify gridded data from a "bag-of-records". This presupposes that the records have a dataset identifier and decimal coordinates. 

The records are sorted by coordinate for each dataset key and sent to a grid_distance function. For the moment, the decimal coordinate distance is calculated between pairs of _latitude coordinates_ (until a distance limit is reached). The distance is emitted to a dictionary as the key and the number of times that distance appears under that datasetkey becomes the value.  

Here is an example of a grid_distance() nested dictionary that will be analyzed :
> {'e6fab7b3-c733-40b9-8df3-2a03e49532c1': {Decimal('0.049990'): 1024, Decimal('0.000003'): 1450, Decimal('0.050003'): 1161, Decimal('0.050000'): 1161, Decimal('0.049997'): 1161, Decimal('0.000007'): 1161, Decimal('0.000006'): 505, Decimal('0.049993'): 1024, Decimal('0.049996'): 1024}}, 4236), ({'292a71df-588b-48fa-9ab5-29ae868ba88c': {Decimal('0.033333'): 7, Decimal('0.066666'): 1, Decimal('0.033334'): 1, Decimal('0.016667'): 7, Decimal('0.050000'): 2, Decimal('0.083333'): 7, Decimal('0.066667'): 7, Decimal('0.016666'): 2, Decimal('0.10'): 6}}

#### Analysis
The max value pair of {distance:number_of_appearances} per datasetkey is selected and a percentage is calculated to see how big a share this distance has of the dataset.  

