import pandas as pd
print(pd.__version__)

import os
print(os.getcwd())
print(os.listdir())

df = pd.read_csv("crispr_patents.csv", encoding="utf-8")
print(df.head())

print(df.columns)

df["text"] = df["Title"] + " " + df["Abstract"]
print(df["text"].iloc[0])

df["text"] = df["text"].fillna('')
df["text"] = df["text"].astype(str)
all_text = " ".join(df["text"])
print(all_text[:500])

temp_text = ""
for char in all_text.lower():
    if (char >= 'a' and char <= 'z') or char == ' ':
        temp_text += char

all_text = temp_text

words = all_text.split()

from collections import Counter
word_counts = Counter(words)
print(word_counts.most_common(30))

remove_list = ['the', 'and', 'of', 'a', 'for', 'to', 'in', 'or', 'methods', 'systems', 'are', 'delivery', 'system', 'compositions', 'as','invention', 'one', 'provided', 'target', 'crisprcas', 'crispr', 'editing', 'an', 'that', 'such']
words_cleaned = [w for w in words if w not in remove_list]

word_counts_cleaned = Counter(words_cleaned)
print(word_counts_cleaned.most_common(30))

remove_list.extend(['cells', 'is', 'comprising', 'provides', 'also', 'with', 'at', 'present', 'method', 'use', 'more', 'thereof', 'by', 'using', 'disclosure', 'be', 'targeted'])
# Removed "targeting" and "targeted" as they lacked meaningful context when considered in isolation.
words_cleaned = [w for w in words if w not in remove_list]

word_counts_cleaned = Counter(words_cleaned)
print(word_counts_cleaned.most_common(30))

remove_list.extend(['which', 'targeting', 'least', 'acids', 'can', 'novel', 'herein', 'sequences', 'relates', 'uses'])
words_cleaned = [w for w in words if w not in remove_list]

word_counts_cleaned = Counter(words_cleaned)
print(word_counts_cleaned.most_common(30))

""" andor_rows = df[df['text'].str.contains('andor', case=False, na=False)]
# Filtered rows containing the term "andor" to determine whether it refers to "and/or" or the test name "Andor BC43".
print(andor_rows[['Title', 'Abstract']])
# No relevant entries found; likely refers to the abbreviation "and/or" rather than the Andor BC43 test.

# Confirmed usage of "and/or" instead of a test name.
andor_rows = df[df['text'].str.contains('and/or', case=False, na=False)]
print(andor_rows[['Title', 'Abstract']])
print(andor_rows[['Title', 'Abstract']].head(5))

for i in range(5):
    print("Title:", andor_rows.iloc[i]['Title'])
    print("Abstract:", andor_rows.iloc[i]['Abstract'])
    print("--------------------------------------------------") """

# Based on manual review, "andor" is consistently used as "and/or", not as a test name.
# Therefore, removing "andor" from the word list.
remove_list.extend(['andor'])
words_cleaned = [w for w in words if w not in remove_list]

word_counts_cleaned = Counter(words_cleaned)
print(word_counts_cleaned.most_common(30))

# Removing plural forms and common stopwords to reduce noise and allow more meaningful words to stand out.
remove_list.extend(['vector', 'proteins', 'disclosed', 'on', 'well', 'said', 'into'])
words_cleaned = [w for w in words if w not in remove_list]

word_counts_cleaned = Counter(words_cleaned)
print(word_counts_cleaned.most_common(30))

remove_list.extend(['from', 'embodiments', 'application', 'some'])
words_cleaned = [w for w in words if w not in remove_list]

word_counts_cleaned = Counter(words_cleaned)
print(word_counts_cleaned.most_common(30))

remove_list.extend(['used', 'occuring'])
words_cleaned = [w for w in words if w not in remove_list]

word_counts_cleaned = Counter(words_cleaned)
print(word_counts_cleaned.most_common(30))

# Removing 'treating' to keep the noun form 'treatment' which is more frequent.
remove_list.extend(['treating', 'occurring'])
words_cleaned = [w for w in words if w not in remove_list]

word_counts_cleaned = Counter(words_cleaned)
print(word_counts_cleaned.most_common(30))

remove_list.extend(['engineering', 'occurring', 'components', 'particular'])
words_cleaned = [w for w in words if w not in remove_list]

word_counts_cleaned = Counter(words_cleaned)
print(word_counts_cleaned.most_common(30))

# Despite multiple attempts to remove 'occurring' from remove_list, it persists in results.
# To handle this, words and remove_list are converted to lowercase before filtering.
from collections import Counter

def extract_crispr_terms(words, remove_list):
    words_lower = [w.lower() for w in words]
    remove_list_lower = [w.lower() for w in remove_list]
    words_cleaned = [w for w in words_lower if w not in remove_list_lower]
    word_counts = Counter(words_cleaned)
    return word_counts.most_common(30)

top_30_terms = extract_crispr_terms(words, remove_list)
print(top_30_terms)

remove_list.extend(['interest', 'occurring', 'type'])
words_cleaned = [w for w in words if w not in remove_list]

word_counts_cleaned = Counter(words_cleaned)
print(word_counts_cleaned.most_common(30))


remove_list.extend(['including', 'genes'])
words_cleaned = [w for w in words if w not in remove_list]

word_counts_cleaned = Counter(words_cleaned)
print(word_counts_cleaned.most_common(30))

remove_list.extend(['site', 'eg'])
words_cleaned = [w for w in words if w not in remove_list]

word_counts_cleaned = Counter(words_cleaned)
print(word_counts_cleaned.most_common(30))

remove_list.extend(['comprises'])
words_cleaned = [w for w in words if w not in remove_list]

word_counts_cleaned = Counter(words_cleaned)
print(word_counts_cleaned.most_common(30))

""" # Checking if 'design' is used in a biological context:
# We filter rows containing 'design' in the 'text' column (case-insensitive).
design_rows = df[df['text'].str.contains('design', case=False, na=False)]
print(design_rows[['Title', 'Abstract']])

# Then inspect the first 5 entries' Title and Abstract.
for i in range(5):
    print("Title:", design_rows.iloc[i]['Title'])
    print("Abstract:", design_rows.iloc[i]['Abstract'])
    print("--------------------------------------------------")
# Since 'design' appears in a relevant biological context, it remains in the list.


#In this row, we search for the exact term 'nonnaturally' in the text column, regardless of uppercase or lowercase letters.
#If that word doesn't appear, an empty dataframe is returned.
nonnaturally_rows = df[df['text'].str.contains('nonnaturally', case=False, na=False)]
print(nonnaturally_rows[['Title', 'Abstract']])

# Next, we search for variations of 'nonnaturally', including forms with hyphens or spaces,
# to capture fragmented or differently written occurrences.
# We do this using a regex pattern with str.contains().
results = df[df['text'].str.contains(r'non[-\s]?naturally', case=False, na=False)]

for i in range(min(5, len(results))):
    print("Title:", results.iloc[i]['Title'])
    print("Abstract:", results.iloc[i]['Abstract'])
    print("--------------------------------------------------")

# Since no exact matches were found, try searching for hyphenated or spaced versions
# like 'non-naturally' or 'non naturally':
df[df['text'].str.contains(r'non[-\s]?naturally', case=False, na=False)][['Title', 'Abstract']]

# Searching for hyphenated or spaced versions like 'non-naturally' or 'non naturally'
results = df[df['text'].str.contains(r'non[-\s]?naturally', case=False, na=False)]

# Printing the Titles and Abstracts of all matched rows for manual review
for i in range(len(results)):
    print("Title:", results.iloc[i]['Title'])
    print("Abstract:", results.iloc[i]['Abstract'])
    print("--------------------------------------------------")

# After reviewing the output, it was clear that 'non-naturally' is used in biotechnology and genetics contexts to mean 'designed' or 'engineered'.
# Hence, we keep the term in the top 30 word list. """

#GRAPH:
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


top30 = word_counts_cleaned.most_common(30)
print(top30)

words = [item[0] for item in top30]
counts = [item[1] for item in top30]
print(words)
print(counts)

plt.figure(figsize=(12, 6))
plt.bar(words, counts)
plt.xticks(rotation=45, ha='right')
plt.xlabel('Word')
plt.ylabel('Frequency')
plt.title('Top 30 Most Frequent Words')
plt.tight_layout()
plt.show()

save_results = True
df_top30 = pd.DataFrame(top30, columns=['Word', 'Frequency'])
if save_results:
    df_top30.to_csv('top30_words.csv', index=False)
    plt.savefig('top30_words.png')
    print("Results have been saved as 'top30_words.csv' and 'top30_words.png'.")