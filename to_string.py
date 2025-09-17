import os

def collect_repo_as_string(root_dir, ignore_dirs=None, ignore_ext=None):
    if ignore_dirs is None:
        ignore_dirs = {'.git', '__pycache__', 'node_modules', '.venv', 'venv'}
    if ignore_ext is None:
        ignore_ext = {'.png', '.jpg', '.jpeg', '.gif', '.ico', '.pdf', '.zip', '.pyc'}

    repo_string = []

    for root, dirs, files in os.walk(root_dir):
        # Skip ignored directories
        dirs[:] = [d for d in dirs if d not in ignore_dirs]

        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            if ext.lower() in ignore_ext:
                continue

            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                repo_string.append(f"\n\n# File: {file_path}\n{content}")
            except Exception as e:
                print(f"Skipping {file_path} due to error: {e}")

    return "".join(repo_string)


if __name__ == "__main__":
    repo_root = "."  # change to path of your repo if needed
    big_string = collect_repo_as_string(repo_root)
    print(big_string[:2000])  # preview first 2000 chars
    # Optionally write to a file:
    with open("repo_dump.txt", "w", encoding="utf-8") as out:
        out.write(big_string)
