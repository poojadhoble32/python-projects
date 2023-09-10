def removefun():
    with open('Demo.txt', 'r') as fd:
        text = ','
        data = fd.read()
        data = data.replace(text, '')

    with open('Demo.txt', 'w') as fd:
        fd.write(data)
        fd.close()

if __name__ == "__main__":
    removefun()
