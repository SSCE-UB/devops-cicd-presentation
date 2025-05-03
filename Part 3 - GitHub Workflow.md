CI/CD Setup from Scratch: A Keynote Presentation

Slide 1: Let’s Build a CI/CD Pipeline!
Title: Setting Up a GitHub CI/CD Project from ScratchSubtitle: A Hands-On Guide for BeginnersVisual: A GitHub logo with a pipeline graphicText:  

Today, we’ll create a project that manages names, tests them, and deploys a webpage!  
Tools: GitHub, GitHub Actions, Python  
Ready to automate your workflow? Let’s go!


Slide 2: Step 1 - Create Your GitHub Repository
Title: Start Fresh with a RepoVisual: Screenshot of GitHub’s "New Repository" pageText:  

Go to GitHub and click "New repository".  
Name: my-cicd-project.  
Check "Add a README file".  
Click "Create repository".Tip: Make it public for GitHub Pages to work!


Slide 3: Step 2 - Set Up the Project Structure
Title: Organize Your FilesVisual: A directory tree graphicText:  

Create this structure in your repo:  my-cicd-project/
├── src/
│   ├── names.txt
│   ├── test_names.py
│   └── generate_html.py
├── .github/
│   └── workflows/
│       ├── test.yml
│       └── deploy.yml
└── README.md


Clone the repo locally:  git clone https://github.com/your-username/my-cicd-project.git



Next: Let’s add the files!

Slide 4: Step 3 - Add the Names File
Title: Create names.txtVisual: A text editor showing namesText:  

In src/, create names.txt:  Alice
Bob
Charlie


This file holds names we’ll display on a webpage.  
Commit and push:  git add src/names.txt
git commit -m "Add names.txt"
git push origin main




Slide 5: Step 4 - Add the Test Script
Title: Write test_names.pyVisual: Code snippetText:  

In src/, create test_names.py:  def test_names_uppercase():
    with open('names.txt', 'r') as file:
        names = file.readlines()
    for name in names:
        assert name[0].isupper(), f"Name '{name.strip()}' does not start with an uppercase letter"

if __name__ == '__main__':
    test_names_uppercase()
    print("All names start with an uppercase letter.")


Tests ensure all names start with uppercase.  
Commit and push:  git add src/test_names.py
git commit -m "Add test script"
git push origin main




Slide 6: Step 5 - Add the HTML Generator
Title: Create generate_html.pyVisual: Python code snippetText:  

In src/, create generate_html.py:  import os

os.makedirs('../docs', exist_ok=True)

with open('names.txt', 'r') as f:
    names = f.readlines()

with open('../docs/index.html', 'w') as f:
    f.write('<html><body><h1>Names List</h1><ul>\n')
    for name in names:
        f.write(f'<li>{name.strip()}</li>\n')
    f.write('</ul></body></html>\n')


Generates index.html in docs/.  
Commit and push:  git add src/generate_html.py
git commit -m "Add HTML generator"
git push origin main




Slide 7: Step 6 - Set Up Testing Workflow
Title: Automate Tests with GitHub ActionsVisual: GitHub Actions workflow runText:  

In .github/workflows/, create test.yml:  name: Test
on:
  pull_request:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - run: python src/test_names.py


Runs tests on pull requests.  
Commit and push:  git add .github/workflows/test.yml
git commit -m "Add test workflow"
git push origin main




Slide 8: Step 7 - Set Up Deployment Workflow
Title: Deploy to GitHub PagesVisual: GitHub Pages settings pageText:  

In .github/workflows/, create deploy.yml:  name: Deploy
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.x'
      - run: python src/generate_html.py
      - uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs


Deploys docs/index.html to gh-pages branch.  
Commit and push:  git add .github/workflows/deploy.yml
git commit -m "Add deploy workflow"
git push origin main




Slide 9: Step 8 - Enable GitHub Pages
Title: Make Your Site LiveVisual: GitHub Pages settings screenshotText:  

Go to your repo’s "Settings" > "Pages".  
Source: "GitHub Actions".  
After first deployment, site will be live at:https://your-username.github.io/my-cicd-project/docs/.Wait: First deployment may take a few minutes.


Slide 10: Step 9 - Create a Project Board
Title: Track Your TasksVisual: GitHub project boardText:  

Go to "Projects" tab, create a new project.  
Add columns: "To Do", "In Progress", "Done".  
Create an issue: "Add new name to list" (e.g., Issue #1).  
Add issue to "To Do" column.Why: Visual task management!


Slide 11: Step 10 - Add a Name and Test
Title: Make Changes and TestVisual: Pull request creationText:  

Create a branch: git checkout -b add-name.  
Add a name to src/names.txt (e.g., "David").  
Commit and push:  git add src/names.txt
git commit -m "Add David to names"
git push origin add-name


Open a PR with "Closes #1".  
Watch tests run in "Actions" tab!


Slide 12: Step 11 - Merge and Deploy
Title: Deploy Your ChangesVisual: Deployed webpage screenshotText:  

Merge the PR if tests pass.  
deploy.yml runs automatically:  
Generates docs/index.html.  
Deploys to GitHub Pages.


Issue #1 moves to "Done" automatically.  
Visit your site to see the updated list!


Slide 13: Wrap-Up
Title: You Did It!Visual: Celebration graphicText:  

You’ve built a CI/CD pipeline from scratch!  
What You Learned:  
Automating tests and deployment  
Managing tasks with GitHub  
Deploying to GitHub Pages


Try adding more names or features!  
Questions? Let’s chat!
