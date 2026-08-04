#Lab 3

import string

class FeedbackAnalyzer:
    def __init__(self, reviews_list):
        """Initializes the analyzer with a list of customer reviews (strings)."""
        self.reviews = reviews_list

    def get_clean_text(self):
        """Task 1: Combines all reviews, normalizes them to lowercase,

        and strips out basic punctuation.
        """
        # Combine all reviews into one massive string
        combined_text = " ".join(self.reviews)
        
        # Convert to lowercase
        lowercase_text = combined_text.lower()
        
        # Clean up punctuation so words like "reliable!" or "good," count properly
        clean_text = lowercase_text.translate(str.maketrans("", "", string.punctuation))
        return clean_text

    def get_word_frequencies(self):
        """Task 2: Calculates the frequency of every word across all reviews."""
        clean_text = self.get_clean_text()
        
        # Split the string into a list of individual words
        words_list = clean_text.split()
        
        # Count frequencies using a dictionary
        frequencies = {}
        for word in words_list:
            frequencies[word] = frequencies.get(word, 0) + 1
            
        return frequencies

    def get_specific_word_frequency(self, target_word):
        """Task 3: Finds the frequency of one specific word."""
        # Normalize the target word just in case the user capitalized it
        target = target_word.lower().strip()
        
        frequencies = self.get_word_frequencies()
        
        # Return the count if it exists, otherwise return 0
        return frequencies.get(target, 0)


# --- Real-Life Scenario Execution ---

# Our raw dataset of customer reviews (List of Strings)
raw_reviews = [
    "The product is incredibly Reliable and fast!",
    "Great customer service, but the setup was confusing.",
    "Is it reliable? Yes, absolutely. I love this reliable tool.",
    "Not worth the price. The quality is quite poor.",
    "Fast delivery and very reliable performance overall."
]

# Create an instance of our class (Object)
analyzer = FeedbackAnalyzer(raw_reviews)

# Task 1: Clean and Lowercase the text
print("--- Task 1: Standardized Text Sample ---")
print(analyzer.get_clean_text()[:100] + "...\n")

# Task 2: Get overall word frequencies
print("--- Task 2: Overall Word Frequencies ---")
all_frequencies = analyzer.get_word_frequencies()
# Sorting them to show the most common words first
sorted_frequencies = sorted(all_frequencies.items(), key=lambda x: x[1], reverse=True)
for word, count in sorted_frequencies[:5]:  # Show top 5 most frequent words
    print(f"'{word}': used {count} times")
print()

# Task 3: Check frequency of a specific word (e.g., "reliable")
print("--- Task 3: Specific Word Tracking ---")
search_word = "Reliable"
count = analyzer.get_specific_word_frequency(search_word)
print(f"The keyword '{search_word}' appears {count} times in the customer feedback.")