# from urllib.request import urlopen
# import time
#
#
# class WebPage:
#     def __init__(self, url):
#         self.url = url
#         self._content = None
#
#     @property
#     def content(self):
#         if not self._content:
#             print("获取新页面...")
#             self._content = urlopen(self.url).read()
#         return self._content

class AverageList(list):
    @property
    def average(self):
        return sum(self) / len(self)


if __name__ == '__main__':
    # webpage = WebPage("https://ccphillips.net/")
    # now = time.time()
    # content1 = webpage.content
    # print(time.time() - now)
    #
    # now = time.time()
    # content2 = webpage.content
    # print(time.time() - now)
    #
    # print(content2 == content1)

    a = AverageList([1, 2, 3])
    print(a.average)
