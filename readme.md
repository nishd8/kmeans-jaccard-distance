## Assignment 3

**Net Id s**: `NXR200053 - Nishad Raisinghani, DRI150030 - Daniel Istre`

**Dataset File Name**: `foxnewshealth.txt` 

**Source** :  `https://archive.ics.uci.edu/ml/datasets/Health+News+in+Twitter`

**Directory Structure**:

    Assignment 3
    |-------------- preprocessor.py  
     - A custom class to read and preprocess the dataset.
    |-------------- logger.py  
     - A custom class to log the results of the K-means implementation in a csv
    |-------------- kmeans.py  
     - A custom class which implements K-means using Jaccard Distance.
    |-------------- run.py
     - A utility file to run and save the results of K-means for different values of K.
    |-------------- log.csv
	 - The log of the results for each K value, the SSE and the cluster sizes.
 
**How to run**:
Open Terminal and run `python3 run.py`