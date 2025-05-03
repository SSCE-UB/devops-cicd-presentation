# Read names from src/names.txt
with open('src/names.txt', 'r') as f:
    names = f.readlines()

# Generate index.html in docs
with open('src//index.html', 'w') as f:
    f.write('<html><body><h1>Names List</h1><ul>\n')
    for name in names:
        f.write(f'<li>{name.strip()}</li>\n')
    f.write('</ul></body></html>\n')
