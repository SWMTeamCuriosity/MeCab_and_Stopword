import os
import sys
from cgi import print_arguments
from konlpy.tag import Mecab


#불용어 리스트
stop_words = "+ - * / . , ? ! n u o b b\ \ ( ) 은 는 을 를 이 있 하 것 들 그 되 수 이 보 않 없 나 사람 주 아니 등 같 우리 때 년 가 한 지 대하 오 말 일 그렇 위하 때문 그것 두 말하 알 그러나 받 못하 일 그런 또 문제 더 사회 많 그리고 좋 크 따르 중 나오 가지 씨 시키 만들 지금 생각하 그러 속 하나 집 살 모르 적 월 데 자신 안 어떤 내 내 경우 명 생각 시간 그녀 다시 이런 앞 보이 번 나 다른 어떻 여자 개 전 들 사실 이렇 점 싶 말 정도 좀 원 잘 통하 소리 놓"
stop_words = stop_words.split(' ')
tokenizer = Mecab()


print("지정된 경로로부터 불러오는 중...\n")
def get_document(fileDir): # 파일 읽기
    doc = []
    for i in os.listdir(fileDir):
        if i[0]=="K":
            address = fileDir+i
            address2 = os.listdir(address)
            for j in address2:
                size = os.path.getsize(address + "/" + j)

                if (".txt" in j) and (size > 500):
                    with open(address + "/" + j, 'r', encoding='cp949') as file:
                        contents = file.readlines()
                    #contents = " ".join(contents)

                    token = tokenizer.morphs(contents[0]) # 형태소 분석기

                    results = []
                    for w in token:
                        if w not in stop_words: #불용어 제거
                            results.append(w)
                    results = " ".join(results)
                    doc.append(results)
    return doc



data = get_document("your address") # 파일 읽기
print("데이터 전처리 완료")
print("데이터 총 개수는 "+str(len(data))+"개 입니다.")


for i in range(len(data)): #파일 쓰기
    arr = []
    with open("your address/no{}".format(i+8)+".txt",'w',encoding='utf-8') as file:
        file.write(data[i])
