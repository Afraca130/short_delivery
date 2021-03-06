# short_delivery

## 프로젝트 개발 이유

> 배송 관련 일을 하면서 초보자들이나 길이 익숙하지 않는 사람들에게 많은 수의 목적지의 스케쥴을 만드는것 또한 업무다.
>
> 특히 요즘 베민 커넥터, 쿠팡 커넥터 등이 생겼고 그러한 활동을 조금 더 효율적으로 만들고 누구나 시도해볼 수 있도록 접근성을 낮출 수 있다.

---

### 개발 알고리즘

1. 스케쥴을 만들기 위해서 가장 중요한 요소는 거리다. 또한 오토바이는 교통 상황보다 거리에 비중이 많기때문에 최단거리 알고리즘을 이용하였다.
2. 네이버 지도를 통해서 목적지까지의 거리를 가중치로 두고 그 가중치를 최단 거리 경로 탐색 알고리즘을 이용해서 구하고 맵에 표시를 해준다.

### 발전 방향

1. Deep learning기술을 이용해서 더 최적화된 루트를 만들고 싶습니다.
2. Web으로 관련 기술을 만들었지만 이용하는 대다수의 사람들은 app을 이용한다. 그렇기 때문에 안드로이드와 앱을 만들것입니다.
3. 배송기사들이 사용하는 어플(ex. 배민, 쿠팡 등)의 어플에서 바로 구현이 가능하도록 만들고싶습니다.
