import time

class Logger:

    def __init__(self):
        self._path = "log.csv"
        f = open(self._path,"w")
        f.write("Value of K,SSE,Size Of each Cluster\n")
        f.close()
        self._data = []

    def log(self, value_of_k, sse, size_of_each_cluster):
        entry = {
            "value_of_k": value_of_k,
            "sse": sse,
            "size": size_of_each_cluster
        }
        self._data.append(entry)

    def save(self):
        f = open(self._path,"a")
        for i in self._data:
            line = str(i['value_of_k'])+","+str(i['sse'])+","
            for cluster_num in i['size']:
                line+= str(cluster_num)+"->"+str(i['size'][cluster_num])+","
            line+="\n"
            f.write(line)
        f.close()
        print("Log File Generated....K-Means for all K-Values Completed")