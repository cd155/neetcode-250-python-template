"""
LeetCode 355: Design Twitter

Design a simplified version of Twitter where users can post tweets, follow/unfollow
another user, and is able to see the 10 most recent tweets in the user's news feed.

Implement the Twitter class:

- Twitter() Initializes your twitter object.
- void postTweet(int userId, int tweetId) Composes a new tweet with ID tweetId by the
  user userId. Each call to this function will be made with a unique tweetId.
- List<Integer> getNewsFeed(int userId) Retrieves the 10 most recent tweet IDs in the
  user's news feed. Each item in the news feed must be posted by users who the user
  followed or by the user themself. Tweets must be ordered from most recent to least
  recent.
- void follow(int followerId, int followeeId) The user with ID followerId started
  following the user with ID followeeId.
- void unfollow(int followerId, int followeeId) The user with ID followerId started
  unfollowing the user with ID followeeId.

Example:
Input: ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
       [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
Output: [null, null, [5], null, null, [6, 5], null, [5]]
Explanation:
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id ->
[5]. return [5]
twitter.follow(1, 2);    // User 1 follows user 2.
twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids ->
[6, 5]. Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
twitter.unfollow(1, 2);  // User 1 unfollows user 2.
twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id ->
[5], since user 1 is no longer following user 2.

Constraints:
- 1 <= userId, followerId, followeeId <= 500
- 0 <= tweetId <= 10^4
- All the tweets have unique IDs.
- At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
- A user cannot follow himself.
"""


class Twitter:
    def __init__(self):
        """
        Initialize the Twitter object.

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement initialization
        pass

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet with id tweetId by user userId.

        Args:
            userId: int - user id
            tweetId: int - tweet id

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement postTweet
        pass

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed.

        Args:
            userId: int - user id

        Returns:
            List[int] - tweet ids ordered from most recent to least recent

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement getNewsFeed
        pass

    def follow(self, followerId, followeeId):
        """
        The user followerId starts following the user followeeId.

        Args:
            followerId: int - follower id
            followeeId: int - followee id

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement follow
        pass

    def unfollow(self, followerId, followeeId):
        """
        The user followerId stops following the user followeeId.

        Args:
            followerId: int - follower id
            followeeId: int - followee id

        Time Complexity: O(?)
        Space Complexity: O(?)
        """
        # TODO: Implement unfollow
        pass


# Example usage (for testing locally)
if __name__ == "__main__":
    twitter = Twitter()
    twitter.postTweet(1, 5)
    print("getNewsFeed(1):", twitter.getNewsFeed(1))  # [5]
    twitter.follow(1, 2)
    twitter.postTweet(2, 6)
    print("getNewsFeed(1):", twitter.getNewsFeed(1))  # [6, 5]
    twitter.unfollow(1, 2)
    print("getNewsFeed(1):", twitter.getNewsFeed(1))  # [5]
