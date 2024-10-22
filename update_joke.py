import pyjokes
from datetime import datetime

# Get the current date
current_date = datetime.now()

# Format the date as 'yyyy-mm-dd'
formatted_date = current_date.strftime("%Y-%m-%d")

# Load the README file
with open('README.md', 'r') as file:
    content = file.readlines()

# Get a new joke
joke = pyjokes.get_joke()

# Replace the joke line
for i, line in enumerate(content):
    if '**Enjoy a daily auto-generated joke**:' in line:
        print(f"Found like at {i}, updating with the joke {joke}")
        content[i] = f'**Enjoy a daily auto-generated joke**: (last updated at: {formatted_date}) <p> {joke} </p>'

# Write back to the README file
with open('README.md', 'w') as file:
    file.writelines(content)
