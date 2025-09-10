# Problem Statement
# Create a unified timeline that aggregates communications from multiple sources (email, Slack, meetings, calls, SMS). Requirements:
#
# Merge events from different sources into a chronological timeline
# Handle different data formats and schemas
# Support filtering by communication type, date range, participants
# Provide pagination for large timelines
# Calculate communication frequency and patterns
# Handle out-of-order event arrival
#
# DSA Solution Approach
# Data Structures:
#
# Merge Sort/Multi-way Merge: Combine sorted streams from different sources
# Balanced BST (TreeMap): Maintain timeline sorted by timestamp
# Bloom Filter: Quick checks for duplicate events across sources
# Skip List: Efficient range queries and pagination
# Circular Buffer: Store recent events for frequency calculations
#
# Algorithm Strategy:
#
# Stream Merging: K-way merge algorithm for combining multiple sorted sources
# Deduplication: Content hashing + temporal proximity checks
# Pagination: Cursor-based pagination using timestamp + unique ID
# Frequency Analysis: Sliding window algorithms for pattern detection
# Late Event Handling: Insert into sorted structure + recompute affected metrics

















