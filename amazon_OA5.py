
# Imagine you're a seller on Amazon, specializing in eco-friendly home products. Each of your items is rated by customers based on its quality and environmental Impact.
# The overall qualityScore of your products is determined by the maximum possible sum of consecutive ratings.
# To improve the quality score of your products and attract more customers, you are given with an integer ImpactFactor and the following two strategies:
# 1, Amplify Ratings: Select a contiguous segment of ratings and amplify them by multiplying each rating In that range by impactFactor.
# 2. Adjust Ratings: Select a contiguous segment of ratings and adjust them by dividing each rating in that range by impactFactor.
# Your task is to determine the maximum possible qualityScore for your eco-friendly products after applying exactly one of these strategies.


# Note: When applying the second strategy ie., Adjust Ratings: For dividing positive ratings, use the floor value of the division result and for dividing negative ratings, use the ceiling value of the division result.
# Example: Given ratings = (4, -5, 5, -7, 1) and
# impactFactor = 2.
# it we choose to apply the second strategy with segment (2, 5) (Assuming 1-based indexing) then,
# = [4,-2,2,-3,0]
# Note that the ceil(-7/2)=-3 and Floors(5/2)=2

def max_qualityScore(impactFactor, ratings):
    pass
