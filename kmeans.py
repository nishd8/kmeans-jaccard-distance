import random
from logger import Logger

class K_Means:
    def __init__(self, dataset, K, centeroids=None):
        random.shuffle(dataset)
        self.dataset = dataset
        self.K = K
        self.centeroids = centeroids
        self.cluster = {i: [] for i in range(self.K)}
        self.sse_value = None
        self.sizes = {}

    def train(self):
        if self.centeroids == None:
            self.centeroids = {}
            for i in range(self.K):
                if self.dataset[i] not in self.centeroids:
                    self.centeroids[i] = self.dataset[i]

        for tweet in self.dataset:
            tweet_distances = [self.jaccard_distance(
                tweet.split(), self.centeroids[c].split()) for c in self.centeroids]
            min_distance = tweet_distances.index(min(tweet_distances))
            self.cluster[min_distance].append(tweet)

        updated_centeroid = self.update_centeroid()
        converge = False
        centroids_tweet = list(self.centeroids.values())
        updated_centeroids_tweet = list(updated_centeroid.values())

        for i in range(self.K):
            if(centroids_tweet[i] != updated_centeroids_tweet[i]):
                converge = False
                break
            else:
                converge = True
        if converge == False:
            print("Not Converged...Updating Centeroid")
            self.centeroids = updated_centeroid.copy()
            self.train()
        else:
            print("Converged...logging result")
            self.sse_value = self.sse()
            for i in range(self.K):
                self.sizes[i+1]= len(self.cluster[i])

    def update_centeroid(self):
        updated_centeroid = {i: [] for i in range(self.K)}
        for i in self.cluster:
            cluster = self.cluster[i]
            inter_cluster_dist = []
            inter_total_dist = 0
            for tweet in cluster:
                if tweet is not None:
                    tweet_distance = [self.jaccard_distance(
                        tweet.split(), c.split()) for c in cluster]
                    inter_total_dist = sum(tweet_distance)
                    inter_cluster_dist.append(inter_total_dist)
            cluster_tweet_index = inter_cluster_dist.index(
                min(inter_cluster_dist))
            updated_centeroid[i] = cluster[cluster_tweet_index]
        return updated_centeroid

    def jaccard_distance(self, tweets_1, tweets_2):
        tweets_1 = set(tweets_1)
        tweets_2 = set(tweets_2)
        union = len(list((tweets_1 | tweets_2)))
        intersection = len(list((tweets_1 & tweets_2)))
        return 1-(intersection/union)

    def sse(self):
        sse_sum = 0
        for k_value in self.centeroids.keys():
            for tweet in list(self.cluster[k_value]):
                sse_sum += self.jaccard_distance(
                    self.centeroids[k_value].split(), tweet.split())**2
        return sse_sum