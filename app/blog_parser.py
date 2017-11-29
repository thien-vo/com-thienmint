def parse_swe_blog(infos):
    i = 0
    headers = []
    texts = []
    while i < len(infos):
        line = infos[i]
        if line.startswith("--"):
            i += 1
            line = infos[i] # header
            headers.append(line)
            i += 1
            line = infos[i] # empty line
            assert line == "\n"
            text_line = []
            while True:
                i += 1
                line = infos[i] # text line
                if line.startswith("--"):
                    break
                text_line.append(line)
            texts.append('\n'.join(text_line))
        i += 1

    return headers, texts


if __name__ == '__main__':
    f = open('static/swe-entries/w01.txt')
    data = f.readlines()
    headers, texts = parse_swe_blog(data)
    d = {k:v for (k,v) in zip(headers, texts)}
    for header in d.keys():
        print header
        print d[header]
