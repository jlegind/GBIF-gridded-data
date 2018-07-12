# GBIF-gridded-data
### Identifying datasets that have gridded record coordinates or contain a portion of records that are gridded

This tool shall be able to identify gridded data from a "bag-of-records". This presupposes that the records have a dataset identifier and decimal coordinates. 

The records are sorted by coordinate for each dataset key and sent to a grid_distance function. The decimal coordinate distance is calculated between pairs of latitude coordinates (until a distance limit is reached). The distance is emitted to a dictionary as the key and the number of times that distance appears under that datasetkey becomes the value.  
The max value pair of {distance:number_of_appearances} per datasetkey is selected and a percentage is calculated to see how big a share this distance has of the dataset.  
