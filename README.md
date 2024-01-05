# 인스턴스 유형, 패밀리 등 성능 차이 테스트
SSH연결프로그램 : putty <br>
서버 : Flask <br>

## T 계열의 small측정 테스트
- t2.small <br>
- t3.small <br>
- t3a.small <br>
- t4g.small <br><br>

## 고려사항 1
### 시간 줄이기(AWS웹 내의 인스턴스 유형 변경) 

but. Anaconda cpu architecture & 인스턴스 cpu !!!

- t2.small x64 intel <1> <br>
- t3.small x64 intel <1> <br>
- t3a.small x64 AMD <1> <br>
- t4g.small ARM ARM <2> <br>


예상) t4g.small < t3.small & t3a.small < t2.small
<br><br>

## 고려사항 2
### 가용영역에 따른 인스턴스 변경 불가

ex) t3.small (가용영역 b) -> t2.small (가용영역 b) 불가 -> t2.small (가용영역 c)
<br><br>

## 최종결과

- t2.small x64 intel <1> 1.83766sec 0.0288USD/h <br>
- t3.small x64 intel <2> 1.035504sec 0.086USD/h <br>
- t3a.small x64 AMD <2> 1.784046sec 0.0418USD/h <br>
- t4g.small ARM ARM <3> 0.885204sec 0.0208USD/h <br>

<strong> 시간) t4g.small < t3.small < t3a.small < t2.small </strong> <br>
<strong> 비용) t4g.small < t2.small < t3a.small < t3.small </strong>
