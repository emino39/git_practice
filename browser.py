import webbrowser

#webbrowser.open("https://www.daum.net")

# 모모랜드 모든 멤버들의 검색 페이지를 한 번에 여는 코드

#webbrowser.open("https://search.daum.net/search?w=tot&q=%EB%82%B8%EC%8B%9C&ppkey=1232419&rtmaxcoll=PRF")
#webbrowser.open("https://search.daum.net/search?w=tot&q=%EC%A3%BC%EC%9D%B4&ppkey=2081903&rtmaxcoll=PRF")

# 멤버별로 페이지를 다 쓰는 것은 비효율적
# 패턴이 같으니까 주소를 분리하자

# url = "https://search.daum.net/search?w=tot&q=검색어"

# 검색어를 입력받아 keyword에 넣으면
#input("검색어를 입력해주세요: ")

#keyword = "모모랜드"

#keyword = input("검색어를 입력해주세요: ")

url = "https://search.daum.net/search?w=tot&q="

#webbrowser.open(url + keyword)

momo = ["나윤", "혜빈(리더)", "아인", "낸시", "주이", "연우", "제인", "데이지", "태하"]

# momo라고 하는 리스트를 한 번씩 돌면서 웹페이지를 열어줘
for member in momo:
    webbrowser.open(url + member)