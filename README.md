# GBIF-gridded-data tool
### Identifying datasets that have gridded record coordinates or contain a portion of the records that are gridded

This tool shall be able to identify gridded data from a "bag-of-records". This presupposes that the records have a dataset identifier and decimal coordinates. 

The records are sorted by coordinate for each dataset key and sent to a grid_distance function. For the moment, the decimal coordinate distance is calculated between pairs of _latitude coordinates_ (until a distance limit is reached). The distance is emitted to a dictionary as the key and the number of times that distance appears under that datasetkey becomes the value.  

Here is an example of a grid_distance() nested dictionary that will be analyzed :
> {'e6fab7b3-c733-40b9-8df3-2a03e49532c1': {Decimal('0.049990'): 1024, Decimal('0.000003'): 1450, Decimal('0.050003'): 1161, Decimal('0.050000'): 1161, Decimal('0.049997'): 1161, Decimal('0.000007'): 1161, Decimal('0.000006'): 505, Decimal('0.049993'): 1024, Decimal('0.049996'): 1024}}, 4236), ({'292a71df-588b-48fa-9ab5-29ae868ba88c': {Decimal('0.033333'): 7, Decimal('0.066666'): 1, Decimal('0.033334'): 1, Decimal('0.016667'): 7, Decimal('0.050000'): 2, Decimal('0.083333'): 7, Decimal('0.066667'): 7, Decimal('0.016666'): 2, Decimal('0.10'): 6}}

#### Analysis
The max value pair of {distance:number_of_appearances} per datasetkey is selected and a percentage is calculated to see how big a share this distance has of the dataset.  

Here is an analysis example:
> Total combinations for e6fab7b3-c733-40b9-8df3-2a03e49532c1 within grid-limit is: 9671 and original dataset length is: 4236  
Number of occurrences = 1450 for this distance 0.000003   
pct = 34.23

As you can see the distance is actually tiny and this dataset is probably not a gridded one.

Another example is this:
> Total combinations for dee8edc4-b19a-11e2-886d-00145eb45e9a within grid-limit is: 4484 and original dataset length is: 7176  
Number of occurrences = 4484 for this distance 0.1000  
pct = 62.49

The distance here is significant (0.1) and it occurs in 62% of the entire dataset which makes it a candidate for gridded data!

#### Improvements
* Currently the tool only analyzes latitude values. It should be able to do both.
* The initial sorting into a new dictionary relies on CPU and memory which will become expensive and slow for any dataset of significant size. For tens of millions of records it could well blow through memory. An implementation that serializes this process is needed.
* A version of this for R would be welcomed.
* Instead of populating the nested dictionary using Python, perhaps employing Pandas (or in R, the dplyr count() method) might increase performance. This won't solve the memory issue though. (For R it would interesting to explore hash tables for performance gains: https://www.r-bloggers.com/hash-table-performance-in-r-part-i/ )
