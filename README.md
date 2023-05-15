# website-portfolio-flask
Portfolio website

## Step by Step

### Downloading repository

The first step is download this repository in your local environment: 

```bash
git clone https://github.com/jersonmartinez/website-portfolio-flask.git
```

### Open with VS Code

```bash
cd website-portfolio-flask
code .
```

### Install Flask

```bash
pip install flask
```

### Launching app

Open terminal to execute python: `python app.py`.

```bash
$ python app.py

 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 113-333-638
```

### Path directory

```bash
website-portfolio-flask/
├── static/
│   ├── css/
│   │   └── bootstrap.css
│   └── js/
│       └── bootstrap.js
├── templates/
│   ├── base.html
│   └── index.html
└── app.py
```

### How to create new CSS design and JS functions?

**CSS**
Create `style.css` in this path: `\static\css\`.

**JS**
Create `script.js` in this path: `\static\js\`.

**How to add?**

Add `css` and `js` files in `base.html`.

```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}"> 
```

```html
<script src="{{ url_for('static', filename='js/script.js') }}"></script>
```

---

## Using Git

### Download updates from GitHub

```bash
git pull
```

### Upload updates to GitHub

```bash
# Add new updates
git add .

# Add a description about the updates
git commit -m "This is a description"

# Send the updates
git push
```