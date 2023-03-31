# ==========================
#     written by: raunak
# ==========================

# cleanup tool

# func 1 - descend() - v1 - recursive cleanup based on string matching
#   find quicker hack solution using regex and rm -r
#   replace hack matcher here


## under construction do not fire !!

import os

cwd = os.getcwd()


# deps
def start_with_cwd(pre_whitelist):
    exclude_list = []
    for item in pre_whitelist:
        exclude_list.append(item)
    return exclude_list


placements = {1: "e", 2: "s", 3: "m"}


# prompt
matcher = input("match what? string: ")
is_regex = input("is regex? (y/n)") == "y"

placement = 0
if(not is_regex):
    placement = input("1: ends with, 2: starts with, 3: substring")
    
start = input("start path: (. - cwd)")
whitelist_path = input("exclude file absolute path (- none):")


# recursively descend and wipe all matches excluding the whitelist


if whitelist_path == "-":
    whitelist = []

whitelist = [
    cwd + "\\tailwind.config.js",
    cwd + "\\postcss.config.js",
    cwd + "\\__tests__",
    cwd + "\\build",
    cwd + "\\meta",
    cwd + "\\node_modules",
    cwd + "\\public",
    cwd + "\\views",
    cwd + "\\src\\user-images",
    cwd + "\\.vscode",
    cwd + "\\.git",
]
whitelist = start_with_cwd(whitelist)


def descend(root, descended):
    if root == ".":
        root = cwd
    # windows version
    needed_root = root in whitelist
    # get items in root
    dir = os.listdir(root)
    is_empty = len(dir) == 0  # ?

    if is_empty or needed_root:
        return

    for item in dir:
        tnt = root + item
        if os.path.isdir(tnt) and tnt not in descended:
            descend(tnt)
            descended.append(tnt)
        if os.path.isfile(tnt) and tnt.endswith(".js"):
            # dev
            print("gonna pop " + tnt)

            # deploy
            # os.remove(tnt)
            # print("popped", tnt)
    return


descend(start, [])
