search_term = input("Enter a word to search for: ").lower()

words = ["Apple", "Banana", "Cherry", "Kiwi", "Mango", "Papaya", "Apricot"]

matched = []
for word in words:
    if search_term in word.lower():
        matched.append(word)

if matched:
    print(f"Found {len(matched)} match(es): {matched}")
else:
    print("No matches found.")
