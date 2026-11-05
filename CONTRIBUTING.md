# Contributing

Thanks for wanting to contribute! You don't need to be an expert. If you can write a small Python function, you can add a plugin. 🎉

## What's a plugin?

A single `.py` file in the `plugins/` folder with a function called `fetch_data()` that returns a dictionary.

## Step-by-step

### 1. Fork the repo
Click the **Fork** button at the top right of the repository page on GitHub. This makes your own copy.

### 2. Clone your fork
```bash
git clone https://github.com/YOUR-USERNAME/REPO-NAME.git
cd REPO-NAME
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a branch
```bash
git checkout -b add-my-plugin
```

### 5. Duplicate the example plugin
```bash
cp plugins/example_coingecko.py plugins/my_plugin.py
```
(On Windows: `copy plugins\example_coingecko.py plugins\my_plugin.py`)

Name your file after what it does, in lowercase with underscores, e.g. `weather_istanbul.py`.

### 6. Edit the API target
Open your new file and change:
- the `URL` and its parameters to your API,
- the line that picks values out of the JSON response,
- the dictionary you return.

Rules for plugins:
- The file must define `fetch_data()` and return a **dict**.
- Keep it to **one file**, ideally short and readable.
- Use only `requests` (or the standard library). Don't add new dependencies.
- Always pass a `timeout` to `requests.get`.
- No API keys or secrets in the code. Prefer free, keyless APIs.
- It's fine to let errors raise: the CLI catches them and keeps going.

### 7. Test it locally
```bash
python main.py
```
You should see your plugin's table. If it breaks, the CLI shows a red error message with the reason, and other plugins still run.

### 8. Commit and push
```bash
git add plugins/my_plugin.py
git commit -m "Add my_plugin"
git push origin add-my-plugin
```

### 9. Open a Pull Request
Go to your fork on GitHub. Click **Compare & pull request**, describe what your plugin does and which API it uses, then submit.

## Need help?

Open an issue and ask. Beginners are very welcome, and no question is too small.
