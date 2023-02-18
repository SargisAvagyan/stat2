
templates = [
    "Once upon a time, there was a {adj} {noun} named {name}. {name} loved to {verb} all day long.",
    "In a {adj} land far, far away, a {noun} named {name} set out on a quest to find the {adj} {noun}.",
    "There was a {adj} {noun} who lived in a {adj} {place}. One day, {name} decided to {verb} and discovered a secret {noun}."
]


print("Please choose a story template:")
for i, template in enumerate(templates):
    print(f"{i + 1}. {template}")
template_number = int(input("Enter the template number: ")) - 1
template = templates[template_number]


words = {}
for word_type in ["adj", "noun", "name","Name" ,"verb", "place"]:
    words[word_type] = input(f"Enter a {word_type}: ")


story = template.format(**words)


print(story)

















