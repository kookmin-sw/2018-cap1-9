

# VISION THROUGH
Team :  9조 VT
## ABSTRACT

### 1. Introduction to the Project
**_'VISION THROUGH' _**  is the IoT project using the smart mirror that coordinating clothes handling virtual clothe images. It is cumbersome to find clothes I want in the closet and wear them in front of the mirror and take them off. Also, it is more so if the distance between the closet and the mirror is long.
  
If you have a lot of clothes, it's hard to find where you want to wear them, and it takes a long time to get some clothes and try to match them. We planned this project because we wanted to have a product that could solve this hassle.
  
There are three major functions as follows.
  
First, you can do the coordination without having to wear clothes in the closet.
Second, you can add clothes in real time to your list of clothes by taking a picture.
Third, when you choose one outfit, it recommends another outfit to match.
  
These advantages will greatly shorten preparation time and reduce concerns about choosing clothes.

### 1. 프로젝트 소개 
**_'VISION THROUGH'_** 는 스마트 미러를 이용한 가상 옷 코디 IoT 프로젝트이다. 옷장에서 내가 원하는 옷을 찾아서 거울 앞에서 입어보고 벗어보는 것은 번거롭다. 또한, 옷장과 거울의 거리가 멀다면 더욱 그렇다.  
  
가지고 있는 옷이 많으면 입고 싶은옷이 어디 있는지 찾는 것이 힘들고, 여러 옷을 가져와서 매치해보는데 시간이 오래 걸린다. 우리는 이러한 번거로움을 해소해 줄 수 있는 제품이 있었으면 좋겠다고 생각하여 이 프로젝트를 기획하였다.  
  
기능은 다음과 같이 크게 세 가지이다.  
  
첫 번째, 옷장에서 옷을 꺼내서 입어보지 않아도 코디를 할 수 있다.  
두 번째, 사진을 찍어 내 옷 리스트에 실시간으로 옷을 추가할 수 있다. 
세 번째, 하나의 옷을 선택했을 때 그와 어울리는 다른 옷을 추천해준다.
  
위와 같은 장점으로  준비 시간을  크게 단축하고, 옷을  고르는데에  대한 고민이 줄어들 것이다.

### 2. 소개 영상
<a href="https://youtu.be/rQBzq_fyQV4"><img src="https://raw.githubusercontent.com/kookmin-sw/2018-cap1-9/master/doc/images/video.png" width = "500"/></a>

### 3. 팀 소개
팀 명 VT는 _Vision Through_ 의 약자로 프로젝트 명의 약어를 사용하였다. 
 _Vision Through_ 란, 사용자가 직접 일일이 옷을 꺼내지 않고도 스마트 미러를 통해 옷을 확인하고 상하의를 매치하여 선택할 수 있다는 것을 의미한다.

<img src = "https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/team_9_picture.jpg?raw=true" width = "500">

(좌측부터) 왕서, 최진영, 이소영, 김도은, 진예진(팀장) 

#### 지도교수  이상환 교수님 (Lee Sang-hwan)
 <img src = "https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/sanghwan.jpg?raw=true" width = "200">

```markdown
역할: 지도교수
E-mail: sanghwan@kookmin.ac.kr 
```

####  팀장  진예진 (Jin Ye-jin)

<img src = "https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/yejin.jpg?raw=true" width ="200">

```markdown
학번: 20153236
역할: 스마트 미러 영상처리, 스마트 미러 하드웨어 제작
E-mail: yeen666@kookmin.ac.kr
```

####  팀원 이소영(Lee So-yeong)

<img src = "https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/soyeong.png?raw=true" width ="200">

```markdown
학번: 20153208
역할: 스마트 미러 및 터치스크린 웹앱 제작, 서버 및 DB 구축, 스마트 미러 하드웨어 제작
E-mail: daiana@kookmin.ac.kr
```
####  팀원   최진영(Choi Jin-yeong)

<img src = "https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/jinyeong.jpg?raw=true" width ="200">

```markdown
학번: 20133272
역할: 행거 하드웨어 제작 및 모터제어, 옷 추천 알고리즘 제작, 스마트 미러 하드웨어 제작
E-mail: wlsduddud23@gmail.com
```

####  팀원  김도은(Kim Do-eun)

<img src = "https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/doeun.jpg?raw=true" width ="200">

```markdown
학번: 20163087
역할: 옷 이미지 영상처리, 스마트 미러 하드웨어 제작
E-mail: doeuncow@gmail.com
```

####  팀원  왕서(Wang-seo)

<img src = "https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/seo.jpg?raw=true" width ="200">

```markdown
학번: 
역할: 문서 작성
E-mail: 
```

### 4. 사용법
 _Vision Through_ 의 경우, 스마트 미러와 스마트 행거의 라즈베리파이에 이미 배포되어있는 상태이기때문에 소스코드 제출시 설치법은 필요하지 않다. 사용법은 내가 가진 옷들을 행거에 걸어놓고 외출을 하기위해 코디를 하고자 할때 스마트 미러와 연결된 터치스크린을 이용한다. 
터치스크린을 이용해 내가 가진 옷의 리스트를 확인하고 입어보고자 하는 옷을 선택한다. 그 후 스마트 미러 앞에 서면 내 모습 위로 마치 옷을 입은 것처럼 보여진다. 또한, 옷 추천 알고리즘을 통해 잘 어울릴 것 같은 상의나 하의를 미리 코디해볼 수 있다.
 
 <img src ="https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/USER%20UI%20%EB%A9%94%EC%9D%B8%20%ED%8E%98%EC%9D%B4%EC%A7%80.JPG?raw=true">
 
> [USER UI 메인 페이지](34.225.233.100/VT_WEB/main.php )
 
### 5. 추가개발 계획
 1) **인공지능**
  스마트 미러를 통해 내가 가진 옷을 띄어 볼 뿐만 아니라, 날씨나 계절에 맞춰  코디를 추천해주는 인공지능 스마트미러를  개발할 수 있다.
 2) **사진 및 동영상 촬영**
  스마트 미러에 카메라를 달아 사람의 모습을 인식하고 이를 사진이나 동영상을 촬영 가능하게 하여 이후 사용자가 보고싶을 때 스마트미러를 통해 볼 수 있다.
  
### 6. 포스터
<img src = "https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/%ED%8C%90%EB%84%AC.png?raw=true" width = "550">

### 7. 최종 작품

<img src = "https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/preview.jpg?raw=true" width = "500">

### 8. 시연동영상
<a href="https://youtu.be/0RkNK8AU25o" target="_blank"><img src="https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/VT_preview_thumnail.png?raw=true" width = "500"/></a>

### 9. 설문조사
가지고 있는 옷이 많으면 입고 싶은 옷이 어디 있는지 찾는 것이 힘들고 여러 옷을 가져와서 매치해보는데 시간이 오래 걸린다. 실제로 많은 사람들이 이와 같은 고민을 겪고 있는지에 대해서 조사해보았다. 평소 옷 입는 습관에 대한 3개의 질문에 답변을 받았다.

<img src = "https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/survey4.png?raw=true" width = "550" > 
<img src = "https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/survey5.png?raw=true" width = "550"> 

>총 182명의 불특정 다수에게서 답변을 받았으며, SNS에서 설문을 실시한 연유로 연령대는 20대가 97.3%로 압도적인 비율을 보였다. 또한 여자가 64.8% 남자가 35.2%로 응답하였다.


<img src = "https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/survey1.png?raw=true" width = "550"> 

> ‘옷을 고르는데 불편함을 느끼는가?’에 대한 답변은 그렇다가 57.7%로 가장 많은 비율을 차지하였고, 그렇지 않다가 20.9%로 그 다음 많은 비율을 보였다. 하지만 긍정적인 답변을 표출한 사람들은 총 73.1%로 부정적인 답변을 표한 사람들인 26.9% 보다 46.2%가 많은 압도적인 결과를 볼 수 있다.

<img src = "https://github.com/kookmin-sw/2018-cap1-9/blob/master/doc/images/survey2.png?raw=true" width = "550"> 

>‘평소 옷을 고를 때 얼마나 시간이 걸리는가?’에 대한 답변은 5~10분 사이가 가장 많았으며, 5분 미만이 27.5%로 그 다음을 잇따랐다. 하지만 옷을 고를 때 10분 보다 더 걸리는 사람이 36.2%로 상당히 많은 사람들이 옷을 매치해 보는 데에 많은 시간을 소모하고 있었다. 이를 명수로 바꾸면 182명 중에 약 66명 정도가 해당된다.
 
> 결론적으로, ‘옷 매칭 시간의 절약’과 ‘옷 매치 시에 불편함을 감소’ 이 두가지의 큰 목표를 가지고 이 프로젝트를 기획하게 되었다.

 
### 10. 참고자료
    1) 스마트 미러 repository : https://github.com/evancohen/smart-mirror
	  
    2) 스마트 행거 구상도에 참고한 행거 제품 : https://goo.gl/nZRV1M
  
    3) 기존에 개발된 스마트 미러와 스마트 행거 : https://goo.gl/wzohuL


# **_INTRODUCE_**

### 1. Team
Team name VT is an abbreviation of _Vision Through_, which is the abbreviation of the project name.
 _Vision Through_ means that the user can select clothes by checking the clothes on the smart mirror without having to take out clothes individually and match the top and bottom.
 
### 2. How to use
_Vision Through_ is already deployed in the Raspberry PI of the smart mirror and smart hanger, so installation method is not necessary when submitting source code.
I use the touchscreen which is connected to the smart mirror whenever I want to coordinate my clothes to hang out on my hanger and go out. Using the touchscreen, Check the list of clothes and select the clothes what I want to wear. After that, if the user is in front of the smart mirror, you look like that you wear the clothes. Also, the user can dress up by using the recommending algorithms.
  
### 3. Additional development plans
 #### 1) **A.I**
  I can develop an artificial intelligence smart mirror that not only displays my clothes in a smart mirror but also recommends coordination according to weather and season.
 #### 2) **Taking pictures and videos**
  The camera can be placed on a smart mirror to recognize the person's appearance and make it possible to shoot a photograph or a movie so that the user can view the image through a smart mirror when he / she wants to see it.
