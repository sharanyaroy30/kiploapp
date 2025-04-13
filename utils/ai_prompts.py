import random

# Get a random story prompt
def get_story_prompt():
    prompts = [
        "A dragon in the forest finds a lost treasure.",
        "A brave astronaut lands on a new planet and discovers alien life.",
        "A talking cat helps a young hero save a village.",
        "A young inventor builds a flying machine to explore the clouds.",
        "A time traveler visits ancient Egypt and accidentally changes history.",
        "A mermaid discovers a hidden underwater city.",
        "A child and their pet robot go on an adventure through a futuristic city.",
        "An ancient artifact unlocks a mysterious power in a small town.",
        "A group of friends accidentally stumble upon a portal to another world.",
        "A magical book transports a child into their favorite fairytale."
    ]
    return random.choice(prompts)

# Get a random puzzle hint
def get_puzzle_hint():
    hints = [
        "Try matching the colors first!",
        "Look for similar shapes!",
        "Remember the sequence!",
        "Think about how the objects are related!",
        "Start by solving the easiest part!",
        "Focus on one puzzle at a time.",
        "Look for patterns in the shapes and colors.",
        "Use process of elimination for each choice.",
        "Check if any shapes fit perfectly together.",
        "Sometimes the answer is simpler than you think!"
    ]
    return random.choice(hints)

# Get a random character description for story-building
def get_character_description():
    characters = [
        "A shy and curious young girl with an adventurous spirit.",
        "A brave knight with a heart of gold.",
        "A mischievous raccoon with a knack for solving puzzles.",
        "A wise old owl who knows the secrets of the forest.",
        "A young inventor who can build anything from scratch.",
        "A talking tree with deep knowledge of the world.",
        "A robotic dog programmed to protect its owner.",
        "A fearless pirate who sails the seven seas.",
        "A magical fox with the ability to shape-shift.",
        "A fearless child who never backs down from a challenge."
    ]
    return random.choice(characters)

# Get a random setting for the story
def get_setting():
    settings = [
        "In a bustling city full of bright lights and tall buildings.",
        "Deep inside a mystical forest with hidden secrets.",
        "On a futuristic space station orbiting a distant planet.",
        "In a small village surrounded by mountains and lakes.",
        "On a pirate ship sailing across the open ocean.",
        "In a magical kingdom where everything is possible.",
        "In a secret laboratory hidden beneath a mountain.",
        "In a magical library that holds the secrets of the universe.",
        "In an enchanted cave filled with glowing crystals.",
        "On a flying island floating high in the clouds."
    ]
    return random.choice(settings)

# Get a random object for the story
def get_object():
    objects = [
        "a glowing crystal that holds ancient powers.",
        "a mysterious map that leads to a hidden treasure.",
        "a magical key that opens any door.",
        "a strange compass that always points toward adventure.",
        "an enchanted sword that can defeat any monster.",
        "a powerful gemstone that can control time.",
        "a mystical book that contains the world's secrets.",
        "a flying carpet that can take you anywhere.",
        "a golden amulet that protects against danger.",
        "a silver locket that holds a deep family secret."
    ]
    return random.choice(objects)

# Combine all the prompts to create a full story idea
def get_full_story_prompt():
    character = get_character_description()
    setting = get_setting()
    object = get_object()

    story_prompt = f"Character: {character}\nSetting: {setting}\nObject: {object}\n"
    return story_prompt

