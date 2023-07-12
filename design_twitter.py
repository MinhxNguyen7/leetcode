from collections import defaultdict
from typing import NamedTuple

class Tweet(NamedTuple):
    id: int
    time: int
    
    def __lt__(self, other: 'Tweet') -> bool:
        return self.time < other.time
    
    def __gt__(self, other: 'Tweet') -> bool:
        return self.time > other.time

class Twitter:

    def __init__(self):
        self.following: defaultdict[int, set[int]] = defaultdict(set)
        self.tweets: defaultdict[int, list[Tweet]] = defaultdict(list)
        self.tweetCount = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(Tweet(tweetId, self.tweetCount))
        self.tweetCount += 1
        
        self.following[userId].add(userId)

    def getNewsFeed(self, userId: int) -> list[int]:
        feed: list[int] = []
        
        # To preserve order
        folowees = self.following[userId]
        
        tweet_indices: list[int] = [
            len(tweets) - 1 for tweets in (
                self.tweets[folowee] for folowee in folowees
            )
        ]
        
        while len(feed) < 10:
            most_recent_tweet = Tweet(0, -pow(10, 5))
            most_recent_folowee_idx = -1
            
            for idx, folowee in enumerate(folowees):
                if tweet_indices[idx] < 0: continue
                
                last_uncounted_tweet = self.tweets[folowee][tweet_indices[idx]]
                if last_uncounted_tweet > most_recent_tweet:
                    most_recent_tweet = last_uncounted_tweet
                    most_recent_folowee_idx = idx
            
            if most_recent_tweet == Tweet(0, -pow(10, 5)): break
            feed.append(most_recent_tweet.id)
            tweet_indices[most_recent_folowee_idx] -= 1
            
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        following = self.following[followerId]
        if followeeId in following:
            following.remove(followeeId)
        

if __name__ == '__main__':
    twitter = Twitter()
    
    # twitter.postTweet(1, 5)
    # print(twitter.getNewsFeed(1))
    # twitter.follow(1, 2)
    # twitter.postTweet(2, 6)
    # print(twitter.getNewsFeed(1))
    
    tweet_inputs = [[2,5],[1,3],[1,101],[2,13],[2,10],[1,2],[2,94],[2,505],[1,333],[1,22]]
    
    for user, tweet in tweet_inputs:
        twitter.postTweet(user, tweet)
        
    twitter.follow(2, 1)
    
    print(twitter.getNewsFeed(2))