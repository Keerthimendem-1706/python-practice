print("==== Mad Libs Generator ====")
name = input("Enter a name: ")
animal = input("Enter an animal: ")
place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")

story=f"""One day,{name} went to {place}. There, {name} saw a {adjective} {animal}. The {animal} suddenly started to {verb}! {name} laughed and ran home."""

print("\n=== Your Funny Story ===")
print(story)