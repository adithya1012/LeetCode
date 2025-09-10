# Advanced Search & Filtering
# Problem Statement
# Implement a sophisticated search system for CRM data that supports:
#
# Full-text search across customer names, companies, notes, email content
# Faceted search with multiple filters (industry, location, deal size, activity level)
# Auto-complete suggestions as users type
# Search result ranking based on relevance and business priority
# Support for complex queries with AND/OR logic
# Real-time search with results updating as new data arrives
#
# DSA Solution Approach
# Data Structures:
#
# Inverted Index: Map terms to document lists with position information
# Trie/Radix Tree: Fast prefix matching for autocomplete
# Multi-dimensional Range Tree: Handle numerical filters (deal size, dates)
# BitSets: Fast intersection/union operations for filter combinations
# Priority Queue: Rank search results by relevance scores
#
# Algorithm Strategy:
#
# Text Processing: Tokenization, stemming, stop word removal
# TF-IDF Scoring: Calculate document relevance for search terms
# Query Optimization: Convert complex queries into efficient execution plans
# Faceted Navigation: Pre-compute filter counts using aggregation
# Incremental Updates: Maintain search indices as data changes without full rebuilds


import re
from collections import defaultdict
from typing import List

# --- Your CRMSearch Class (with necessary imports) ---
class CRMSearch:
    def __init__(self):
        self.documents = {}  # doc_id -> document
        self.inverted_index = defaultdict(set)  # term -> set of doc_ids
        self.filters = defaultdict(lambda: defaultdict(set))  # field -> value -> doc_ids

    def add_document(self, doc_id: str, content: str, metadata: dict):
        """Add document to search index"""
        self.documents[doc_id] = {
            'content': content,
            'metadata': metadata
        }

        # Build inverted index
        terms = self._tokenize(content)
        for term in terms:
            self.inverted_index[term].add(doc_id)

        # Build filter indices
        for field, value in metadata.items():
            if value:
                # Ensure filter values are lowercase strings for consistent matching
                self.filters[field][str(value).lower()].add(doc_id)

    def _tokenize(self, text: str) -> List[str]:
        """Simple tokenization"""
        # Remove punctuation and split
        clean_text = re.sub(r'[^\w\s]', ' ', text.lower())
        return clean_text.split()

    def search(self, query: str, filters: dict = None, limit: int = 10) -> List[str]:
        """Search with optional filters"""
        query_terms = self._tokenize(query)

        if not query_terms:
            # If there's no query, but there are filters, return all docs matching filters
            if filters:
                result_docs = set(self.documents.keys())
            else:
                return []
        else:
            # Get documents containing all query terms (AND search)
            # Start with a copy to avoid modifying the original set
            result_docs = self.inverted_index.get(query_terms[0], set()).copy()
            for term in query_terms[1:]:
                result_docs &= self.inverted_index.get(term, set())

        # Apply filters
        if filters:
            for field, value in filters.items():
                field_lower = field.lower()
                value_lower = str(value).lower()
                if field_lower in self.filters and value_lower in self.filters[field_lower]:
                    result_docs &= self.filters[field_lower][value_lower]

        # Simple ranking by term frequency
        ranked_results = self._rank_results(result_docs, query_terms)

        return ranked_results[:limit]

    def _rank_results(self, doc_ids: set, query_terms: List[str]) -> List[str]:
        """Simple TF-based ranking"""
        if not doc_ids:
            return []

        scores = {}
        for doc_id in doc_ids:
            doc_content = self.documents[doc_id]['content'].lower()
            score = 0
            # Only score if there was a query
            if query_terms:
                for term in query_terms:
                    score += doc_content.count(term)
            scores[doc_id] = score

        # Sort by score descending
        return sorted(list(doc_ids), key=lambda x: scores[x], reverse=True)


    def get_autocomplete(self, prefix: str, limit: int = 5) -> List[str]:
        """Simple autocomplete based on indexed terms"""
        if not prefix:
            return []
        prefix_lower = prefix.lower()
        suggestions = []
        # Iterate through sorted terms for more consistent results
        for term in sorted(self.inverted_index.keys()):
            if term.startswith(prefix_lower):
                suggestions.append(term)
            if len(suggestions) >= limit:
                break
        return suggestions

# --- Code to Run and Test Your Implementation ---

# 1. Instantiate the search system
crm = CRMSearch()

# 2. Add sample CRM data
print("## Adding Documents ##")
crm.add_document(
    doc_id="contact_1",
    content="John Doe is the CEO of Acme Inc. Notes: Discussed new contract renewal. Follow up next week.",
    metadata={"industry": "Technology", "location": "San Francisco", "deal_size": 50000}
)
crm.add_document(
    doc_id="contact_2",
    content="Jane Smith from Innovate LLC. Notes: Great potential for a large software deal. Needs a demo.",
    metadata={"industry": "Software", "location": "New York", "deal_size": 150000}
)
crm.add_document(
    doc_id="contact_3",
    content="Peter Jones, a manager at BuildIt Corp. Interested in our new software solutions. Contract pending.",
    metadata={"industry": "Construction", "location": "Chicago", "deal_size": 75000}
)
crm.add_document(
    doc_id="contact_4",
    content="Susan Lee of Tech Solutions. Discussed software integration project.",
    metadata={"industry": "Technology", "location": "San Francisco", "deal_size": 200000}
)
print(f"Total documents indexed: {len(crm.documents)}\n")


# 3. Perform a full-text search
print("## Full-Text Search for 'software contract' ##")
results = crm.search("software contract")
print(f"Found results: {results}\n")


# 4. Perform a faceted search (with filters)
print("## Faceted Search for 'solutions' in the 'Technology' industry ##")
tech_filter = {"industry": "Technology"}
results = crm.search("solutions", filters=tech_filter)
print(f"Found results: {results}\n")

print("## Faceted Search in 'San Francisco' with a deal size > 100000 ##")
# Note: Your current implementation doesn't support range queries like > or <
# It matches exact filter values. We'll filter for a known deal size.
sf_filter = {"location": "San Francisco", "deal_size": 200000}
results = crm.search("software", filters=sf_filter)
print(f"Found results: {results}\n")


# 5. Get auto-complete suggestions
print("## Autocomplete for prefix 'cont' ##")
suggestions = crm.get_autocomplete("cont")
print(f"Suggestions: {suggestions}\n")

# 6. Search with a more complex query (multiple terms)
print("## Search for 'new software solutions' ##")
results = crm.search("new software solutions")
print(f"Found results: {results}\n")

# 7. Search with only filters and no query text
print("## Search for all contacts in the 'Software' industry ##")
software_only_filter = {"industry": "Software"}
results = crm.search("", filters=software_only_filter)
print(f"Found results: {results}\n")

# 8. Search for a term that doesn't exist
print("## Search for a non-existent term 'blockchain' ##")
results = crm.search("blockchain")
print(f"Found results: {results}\n")