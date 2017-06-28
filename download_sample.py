path = 'https://www.ets.org/toefl/ibt/prepare/quick_prep/'
lines = []
with urllib.request.urlopen(path) as response:
    raw_lines = response.readlines()
    for line in raw_lines:
        line = line.decode('utf-8')
        lines.append(line)

# 특정 URL(www.ets.org) 페이지에 있는 파일 링크를 통해 해당 파일(mp3)들을 모두 다운로드하는 샘플.
        
file_list = []
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == 'a' and attrs[0][0] == 'href' and attrs[0][1].endswith('mp3') is True:
            if attrs[0][1].startswith('http') is True:
                src_file = attrs[0][1]
                file_list.append(src_file)
            else:
                prefix = 'http://www.ets.org'
                src_file = prefix + attrs[0][1]
                file_list.append(src_file)
        else:
            pass
        self.file_list = file_list
        return self.file_list

parser = MyHTMLParser()
parser.feed(str(lines))
parser.close()

for file_url in parser.file_list:
    src_filename = file_url[33:].replace('/','_')
    local_filename, headers = urllib.request.urlretrieve(file_url, filename = src_filename)
    print('Download completed: %s' % local_filename)
