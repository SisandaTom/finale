import spacy

nlp = spacy.load("en_core_web_md")

# Define three objects: cat, monkey, and banana
cat = nlp("cat")
monkey = nlp("monkey")
banana = nlp("banana")

# Calculate the similarity between cat and monkey, and cat and banana
cat_monkey_similarity = cat.similarity(monkey)
cat_banana_similarity = cat.similarity(banana)

# Print the results
print("Similarity between cat and monkey:", cat_monkey_similarity)
print("Similarity between cat and banana:", cat_banana_similarity)

# What I find interesting about the similarities between cat, monkey, and banana is that they can be related through their properties and
# attributes, such as being living organisms and having specific physical features. However, they also differ in various ways, such as their
# type of food consumption, behavior, and natural habitats.

# Differences between the models
# 'en_core_web_md' is like a bigger and smarter dictionary, while 'en_core_web_sm' is a smaller and simpler one.
# The bigger dictionary can understand words better but needs more space and might work a bit slower. The smaller one is quicker and
# smaller but not as smart.
