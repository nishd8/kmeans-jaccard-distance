class Preprocessor:
    def __init__(self, path):
        f = open(path, "r")
        self.dataset = []
        exclude = set(",.:;-?!/#()\'\"")
        for tweet in f.read().split("\n"):
            text = "".join([(ch if ch not in exclude else " ")
                            for ch in tweet.split("|")[-1].split("http")[0]]).strip().lower()
            self.dataset.append(self.__remove_at(text))

    def __remove_at(self, tweet):
        tweet_without_at = []
        for word in tweet.split(" "):
            if "@" not in word:
                tweet_without_at.append(word)
        return ' '.join(tweet_without_at)