# Set.difference() Operation

english_count = int(input())
english_subscribers = set(map(int, input().split()))

french_count = int(input())
french_subscribers = set(map(int, input().split()))

print(len(english_subscribers.difference(french_subscribers)))