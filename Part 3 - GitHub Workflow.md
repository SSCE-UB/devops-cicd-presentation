# CI/CD Setup from Scratch: A Keynote Presentation

---

## Slide 1: Let’s Build a CI/CD Pipeline!

**Title:** Setting Up a GitHub CI/CD Project from Scratch  
**Subtitle:** A Hands-On Guide for Beginners  
**Visual:** A GitHub logo with a pipeline graphic  

**Text:**  
Today, we’ll create a project that manages names, tests them, and deploys a webpage!  

**Tools:** GitHub, GitHub Actions, Python  

**Call to Action:** Ready to automate your workflow? Let’s go!

---

## Slide 2: Step 1 - Create Your GitHub Repository

**Title:** Start Fresh with a Repo  
**Visual:** Screenshot of GitHub’s "New Repository" page  

**Text:**  
1. Go to GitHub and click **"New repository"**.  
2. Name: `my-cicd-project`.  
3. Check **"Add a README file"**.  
4. Click **"Create repository"**.  

**Tip:** Make it public for GitHub Pages to work!

---

## Slide 3: Step 2 - Set Up the Project Structure

**Title:** Organize Your Files  
**Visual:** A directory tree graphic  

**Text:**  
Create this structure in your repo:  
```
my-cicd-project/
├── src/
│   ├── names.txt
│   ├── test_names.py
│   └── generate_html.py
├── .github/
│   └── workflows/
│       ├── test.yml
│       └── deploy.yml
└── README.md
```

**Command:**  
Clone the repo locally:  
```bash
git clone https://github.com/your-username/my-cicd-project.git
```

**Next:** Let’s add the files!

---

## Slide 4: Step 3 - Add the Names File

**Title:** Create `names.txt`  
**Visual:** A text editor showing names  

**Text:**  
In `src/`, create `names.txt`:  
```
Alice  
Bob  
Charlie  
```

This file holds names we’ll display on a webpage.  

**Commands:**  
```bash
git add src/names.txt
git commit -m "Add names.txt"
git push origin main
```

---

## Slide 5: Step 4 - Add the Test Script

**Title:** Write `test_names.py`  
**Visual:** Code snippet  

**Text:**  
In `src/`, create `test_names.py`:  
```python
def test_names_uppercase():
    with open('names.txt', 'r') as file:
        names = file.readlines()
    for name in names:
        assert name[0].isupper(), f"Name '{name.strip()}' does not start with an uppercase letter"

if __name__ == '__main__':
    test_names_uppercase()
    print("All names start with an uppercase letter.")
```

Tests ensure all names start with uppercase.  

**Commands:**  
```bash
git add src/test_names.py
git commit -m "Add test script"
git push origin main
```

---

## Slide 6: Step 5 - Add the HTML Generator

**Title:** Create `generate_html.py`  
**Visual:** Python code snippet  

**Text:**  
In `src/`, create `generate_html.py`:  
```python
import os

os.makedirs('../docs', exist_ok=True)

with open('names.txt', 'r') as f:
    names = f.readlines()

with open('../docs/index.html', 'w') as f:
    f.write('<html><body><h1>Names List</h1><ul>\n')
    for name in names:
        f.write(f'<li>{name.strip()}</li>\n')
    f.write('</ul></body></html>\n')
```

Generates `index.html` in `docs/`.  

**Commands:**  
```bash
git add src/generate_html.py
git commit -m "Add HTML generator"
git push origin main
```

---

## Slide 7: Step 6 - Set Up Testing Workflow

**Title:** Automate Tests with GitHub Actions  
**Visual:** GitHub Actions workflow run  

**Text:**  
In `.github/workflows/`, create `test.yml`:  
```yaml
name: Test
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
```

Runs tests on pull requests.  

**Commands:**  
```bash
git add .github/workflows/test.yml
git commit -m "Add test workflow"
git push origin main
```

---

## Slide 8: Step 7 - Set Up Deployment Workflow

**Title:** Deploy to GitHub Pages  
**Visual:** GitHub Pages settings page  

**Text:**  
In `.github/workflows/`, create `deploy.yml`:  
```yaml
name: Deploy
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
```

Deploys `docs/index.html` to `gh-pages` branch.  

**Commands:**  
```bash
git add .github/workflows/deploy.yml
git commit -m "Add deploy workflow"
git push origin main
```

---

## Slide 9: Step 8 - Enable GitHub Pages

**Title:** Make Your Site Live  
**Visual:** GitHub Pages settings screenshot  

**Text:**  
1. Go to your repo’s **"Settings"** > **"Pages"**.  
2. Source: **"GitHub Actions"**.  
3. After first deployment, site will be live at:  
   `https://your-username.github.io/my-cicd-project/docs/`.  

**Note:** First deployment may take a few minutes.

---

## Slide 10: Step 9 - Create a Project Board

**Title:** Track Your Tasks  
**Visual:** GitHub project board  

**Text:**  
1. Go to **"Projects"** tab, create a new project.  
2. Add columns: **"To Do"**, **"In Progress"**, **"Done"**.  
3. Create an issue: **"Add new name to list"** (e.g., Issue #1).  
4. Add issue to **"To Do"** column.  

**Why:** Visual task management!

---

## Slide 11: Step 10 - Add a Name and Test

**Title:** Make Changes and Test  
**Visual:** Pull request creation  

**Text:**  
1. Create a branch:  
   ```bash
   git checkout -b add-name
   ```
2. Add a name to `src/names.txt` (e.g., "David").  
3. Commit and push:  
   ```bash
   git add src/names.txt
   git commit -m "Add David to names"
   git push origin add-name
   ```
4. Open a PR with **"Closes #1"**.  
5. Watch tests run in **"Actions"** tab!

---

## Slide 12: Step 11 - Merge and Deploy

**Title:** Deploy Your Changes  
**Visual:** Deployed webpage screenshot  

**Text:**  
1. Merge the PR if tests pass.  
2. `deploy.yml` runs automatically:  
   - Generates `docs/index.html`.  
   - Deploys to GitHub Pages.  
3. Issue #1 moves to **"Done"** automatically.  
4. Visit your site to see the updated list!

---

## Slide 13: Wrap-Up

**Title:** You Did It!  
**Visual:** Celebration graphic  

**Text:**  
You’ve built a CI/CD pipeline from scratch!  

**What You Learned:**  
- Automating tests and deployment  
- Managing tasks with GitHub  
- Deploying to GitHub Pages  

**Next Steps:** Try adding more names or features!  

**Questions?** Let’s chat!
