# The Prompt: ("Imagine you are processing a stream of API endpoint requests from a log file. "
#              "Write a function that processes this stream and can, at any time, return the first endpoint that has been requested only once. "
#              "This could be used to identify new or potentially erroneous API calls that aren't being used frequently.")

# What it's testing: This is a variation of the "first non-repeating character" problem. It tests your ability to track both the frequency of items and their order of appearance.

# The Practical DSA Solution: A single data structure isn't enough. The efficient solution uses a combination:

# A Hash Map to store the count of each endpoint request.

# A Queue to store the endpoints in the order they appear.
# When a new request comes in, you add it to the hash map and the queue.
# To find the first unique endpoint, you look at the front of the queue. If its count in the hash map is 1, that's your answer.
# If its count is greater than 1, you remove it from the queue and check the next item. This ensures you process the data in a single pass (O(n) time complexity).


import collections


class UniqueEndpointFinder:
    """
    Processes a stream of items and finds the first one that has appeared only once.
    """

    def __init__(self):
        # A queue to maintain the arrival order of endpoints.
        # We only add an endpoint the first time we see it.
        self.queue = collections.deque()

        # A hash map (dictionary) to store the frequency of each endpoint.
        self.counts = {}

    def add_request(self, endpoint: str):
        """
        Processes a new endpoint request from the stream.

        Args:
            endpoint: The API endpoint string.
        """
        # Increment the count for the endpoint.
        self.counts[endpoint] = self.counts.get(endpoint, 0) + 1

        # If this is the first time we've seen this endpoint, add it to our queue.
        if self.counts[endpoint] == 1:
            self.queue.append(endpoint)

    def get_first_unique(self) -> str or None:
        """
        Returns the first endpoint that has been requested only once so far.

        This method cleans the front of the queue by removing any non-unique
        endpoints until it finds a unique one or the queue is empty.

        Returns:
            The first unique endpoint string, or None if no unique endpoints exist.
        """
        # Remove any endpoints from the front of the queue that are no longer unique.
        while self.queue:
            front_endpoint = self.queue[0]
            if self.counts[front_endpoint] == 1:
                # We found it! The first item in the queue is unique.
                return front_endpoint
            else:
                # This endpoint is a duplicate, remove it and check the next one.
                self.queue.popleft()

        # If the queue becomes empty, no unique endpoints are left.
        return None


# --- Example Usage ---
# This demonstrates the step-by-step logic from the explanation.

finder = UniqueEndpointFinder()

# 1. Anna ('/users') enters.
finder.add_request('/users')
print(f"First unique is: {finder.get_first_unique()}")  # Expected: /users

# 2. Ben ('/products') enters.
finder.add_request('/products')
print(f"First unique is: {finder.get_first_unique()}")  # Expected: /users

# 3. Anna's twin ('/users') enters.
finder.add_request('/users')
print(f"First unique is: {finder.get_first_unique()}")  # Expected: /products

# 4. Carla ('/orders') enters.
finder.add_request('/orders')
print(f"First unique is: {finder.get_first_unique()}")  # Expected: /products

# 5. Ben's twin ('/products') enters.
finder.add_request('/products')
print(f"First unique is: {finder.get_first_unique()}")  # Expected: /orders

# 6. Carla's twin ('/orders') enters
finder.add_request('/orders')
print(f"First unique is: {finder.get_first_unique()}")  # Expected: None