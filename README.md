# 💼 job-scraper

StackOverflow와 Indeed에서 구직 정보를 수집해 CSV로 저장하는 Python 기반 웹 애플리케이션입니다.

---

## 📌 설명

이 프로젝트는 실제 구직 데이터를 자동으로 수집하고, 검색어 기반 필터링 기능과 함께 CSV 파일로 내보내는 기능을 제공합니다. Flask를 이용해 간단한 웹 서버를 만들고, AWS EC2에 배포 가능한 구조로 개발했습니다.

---

## ⚙️ 사용 기술

- Python 3
- BeautifulSoup (웹 스크래핑)
- Flask (웹 서버)
- Requests
- Pandas (CSV 저장)
- AWS EC2 (배포 예정)

---

## ✨ 주요 기능

- ✅ StackOverflow Jobs, Indeed에서 실시간 구직 정보 크롤링  
- ✅ 키워드 기반 검색 및 필터링 기능  
- ✅ 검색 결과를 CSV로 저장  
- ✅ Flask 기반 웹 인터페이스 제공  
- ✅ AWS EC2 서버에 배포 가능

---

## ▶️ 실행 방법

```bash
git clone git@github.com:jinsoo-lim/job-scraper.git
cd job-scraper
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
