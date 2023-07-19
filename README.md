# MADify

## 허도영, 이선규

### 기능

#### 0. 유저의 노래 취향 분석 & 추천
- 취향 분석을 위해 유저에게 5~ 15개의 노래 설문.
  - 이 노래가 좋은지/안 좋은지 여부를 응답으로 받아 다음 노래를 선택.
  - 해당 노래는 유튜브에서 지원하는 "가장 많이 다시 본 장면" 기능을 이용하여 노래의 하이라이트 부분에서 실행
  - confidence 그래프를 실시간으로 업데이트하여 유저의 취향 분석 정도(해당 추정이 얼마나 신뢰성 있는지)를 보여줌.
-  설문을 통해 어떤 장르를 얼마나 좋아하는지(음악 MBTI), 추천 노래 12개 띄어줌.

![image](https://github.com/icp1481/madcamp3/assets/82937664/171d5888-b274-404d-bd02-9de488c3e233)
![image](https://github.com/icp1481/madcamp3/assets/82937664/04a3a1aa-0437-4572-a1de-6d32074e9961)
![image](https://github.com/icp1481/madcamp3/assets/82937664/e5383552-693c-46e9-9461-979389bf393d)
![image](https://github.com/icp1481/madcamp3/assets/82937664/d8f98a2f-3731-45e3-98e3-05b858604c75)
![image](https://github.com/icp1481/madcamp3/assets/82937664/b45e618a-b4d1-4a4f-a39a-dfb54dc377b1)
![image](https://github.com/icp1481/madcamp3/assets/82937664/1e55e9cb-a013-4a82-94b8-0b30685e43be)


#### 1. 노래 검색 기능
- 제목을 검색한 후, 해당 노래가 있으면 그 노래를 유튜브로 띄워줌.

#### 2. 플레이리스트 관리
- 음악을 듣고 유저가 '좋아요' 버튼을 누른 경우 따로 플레이리스트에 담아져 들을 수 있음.
- next / prev 버튼을 통해 플레이리스트 플레이

### AI 모델
- 학습 데이터 : WSDM 중 한국 노래 위주, sparsity가 낮은 score matrix 일부 발최
- 학습 모델 : MIRT

