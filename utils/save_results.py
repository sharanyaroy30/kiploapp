import pandas as pd

# Save story results to a CSV file
def save_story(character, setting, plot):
    # Check if the CSV file exists, create if not
    try:
        df = pd.read_csv("stories.csv")
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Character", "Setting", "Plot"])
    
    # Append the new story data
    new_story = pd.DataFrame({"Character": [character], "Setting": [setting], "Plot": [plot]})
    df = pd.concat([df, new_story], ignore_index=True)
    df.to_csv("stories.csv", index=False)
    print(f"Story saved: {character} in {setting}")

