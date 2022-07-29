from preprocessor import Preprocessor
from kmeans import K_Means
from logger import Logger


def run(path, k_values):
    dataset = Preprocessor(path).dataset
    logger = Logger()
    for k in k_values:
        print("Running K-means for K-Value: "+str(k))
        kmeans = K_Means(dataset, k)
        kmeans.train()
        logger.log(kmeans.K,kmeans.sse_value,kmeans.sizes)
        print("--------------------------------------------------")
    logger.save()

file_path = "foxnewshealth.txt"
k_values = [10,20,30,40] 
run(file_path,k_values)
