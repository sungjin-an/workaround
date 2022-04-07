# workaround

- [Python과 Selemium을 이용한 화면 Capture](#Python과-Selemium을-이용한-화면-Capture)   
- [Pandas를 이용한 엑셀 파일 읽기 및 저장](#Pandas를-이용한-엑셀-파일-읽기-및-저장)   
- [Terraform](#terraform)
--- 

# Python과 Selemium을 이용한 화면 Capture

## Python 과 Selenium설치
- Python : Microsft Store에서 설치
- Python venv 가상환경 생성 ( 필요 없어지면 디렉터리만 지우면 된다 ) 
  - DOS CMD
    ```
    python -m venv seleniumTest   
    ```

- venv 가상환경 사용  
  - DOS 창에서는 prompt에 venv명이 표시된다
  - PowerShell에서는 별도의 구분이 안되는데 다른 설정이 필요한지 검색 안해봤음    
  - DOS CMD
    ```
    cd seleniumTest 
    .\Scripts\activate.bat
    (seleniumTest) C:\seleniumTest> 
    ```

- venv 가상환경에서 pip로 selenium 설치
  - https://pypi.org/project/selenium/
  - DOS CMD
    ```
    (seleniumTest) C:\seleniumTest> pip install -U selenium
    ```


## Windows 10에서 Web Browser Driver 설치
- 인터넷에서 검색하거나 아래 페이지내에 있는 Link로 다운로드 
- https://pypi.org/project/selenium/
- https://www.selenium.dev/downloads/


## Python 가상환경에서 실행
- venv 환경 활성화
  ```code
  C:\seleniumTest>.\Scripts\activate.bat
  ```

- 테스트 코드 수행
  ```code
  (seleniumTest) C:\seleniumTest>python make_sample_data.py
  (seleniumTest) C:\seleniumTest>python main.py
  ```

## Python 가상환경 종료
- venv 환경에서 빠져 나오기
  ```code
  (seleniumTest) C:\\seleniumTest> deactivate
  C:\\seleniumTest>
  ```

- venv 환경을 없애는 것은 해당 폴더를 삭제하면 된다

---

# Pandas를 이용한 엑셀 파일 읽기 및 저장

## 관련 사이트 
- https://pandas.pydata.org/
- pip모듈 설치  
  ```code
  (seleniumTest) C:\\seleniumTest> pip install pandas
  (seleniumTest) C:\\seleniumTest> pip install xlrd        # Excel 읽을때 필요
  (seleniumTest) C:\\seleniumTest> pip install openpyxl    # Excel 저장시 필요
  ```

---
# Terraform 
## 관련 사이트
- [Terraform AWS modules - Github](https://github.com/terraform-aws-modules)
- [Kurly Tech Blog - DevOps팀의 Terraform 모험 (2021.08)](https://helloworld.kurly.com/blog/terraform-adventure/)   
- [Terraform best practices](https://www.terraform-best-practices.com/)   


