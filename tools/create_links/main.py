import pyperclip


def main():
    name = input("Github org/repo (without https://github.com/): ")
    branch = input("Branch: ")
    d = {
        "stars": f"https://img.shields.io/github/stars/{name}?label=%20",
        "contributors": f"https://img.shields.io/github/contributors/{name}?label=%20",
        "last commit": f"https://img.shields.io/github/last-commit/{name}/{branch}?label=%20",
        "source language": f"https://img.shields.io/github/languages/top/{name}",
        "license": f"https://img.shields.io/github/license/{name}?label=%20"
    }
    for k in d:
        url = d[k]
        pyperclip.copy(url)
        print(f"{k}: {url}")


if __name__ == '__main__':
    main()
