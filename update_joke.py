import pyjokes

# Load the README file
with open('README.md', 'r') as file:
    content = file.readlines()

# Get a new joke
joke = pyjokes.get_joke()

# Replace the joke line
for i, line in enumerate(content):
    if '**Enjoy a daily auto-generated joke**:' in line:
        content[i] = f'**Enjoy a daily auto-generated joke**: {joke}\\n'

# Write back to the README file
with open('README.md', 'w') as file:
    file.writelines(content)
