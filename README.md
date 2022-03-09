# workaround

**- [Python과 Selemium을 이용한 화면 Capture](#Python과-Selemium을-이용한-화면-Capture)**

<hr>

## Python과 Selemium을 이용한 화면 Capture

### Python 과 Selenium설치
- Python : Microsft Store에서 설치
- Python 가상환경 VENV에 Selenuim 설치
  - DOS CMD
    ```code
    cd C:\seleniumTest
    C:\seleniumTest> python venv -m seleniumTest
    (seleniumTest) C:\seleniumTest> pip install selenium
    ```

### Windows 10에서 Web Browser Driver 설치
- 검색해서 다운로드 


### Python 가상환경에서 실행
- venv 환경 활성화
  - DOS 창에서는 prompt에 venv명이 표시된다
  - PowerShell에서는 별도의 구분이 안되는데 다른 설정이 필요한지 검색 안해봤음
```code
C:\seleniumTest>.\Scripts\activate.bat
```
- 테스트 코드 수행
```code
(seleniumTest) C:\seleniumTest>python main.py
```

- venv 환경에서 빠져 나오기
```code
(seleniumTest) C:\\seleniumTest> deactivate
C:\\seleniumTest>
```
- venv 환경을 없애는 것은 해당 폴더를 삭제하면 된다
