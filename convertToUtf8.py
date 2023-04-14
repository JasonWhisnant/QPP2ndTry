BLOCKSIZE = 1048576

def convert(source, target):
    with open(source, 'r', encoding='utf-16') as sourceFile:
        with open(target, 'w', encoding='utf-8') as targetFile:
            while True:
                contents = sourceFile.read(BLOCKSIZE)
                if not contents:
                    break
                targetFile.write(contents)

    return print("Success")