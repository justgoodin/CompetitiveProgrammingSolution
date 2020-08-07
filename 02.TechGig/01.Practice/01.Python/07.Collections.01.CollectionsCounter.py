#Link to the question below
#https://www.techgig.com/practice/question/collections-counter/RU5TV2FwNHdMbTBwZXpaVGZsK3JZWXpsU1N0VktnLzZ3bnFhbWEvSnBGQy9hVFo5QjJraGlxbzhpa2txeVI3Rw==/1

#Error on test case 4, it requires you to swap the order of output

from collections import Counter

def main():
    string = input()
    cnt = Counter(string)

    top = cnt.most_common(2)
    print(top[0],top[1],end="")

main()


