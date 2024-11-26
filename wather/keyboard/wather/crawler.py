import requests
from bs4 import BeautifulSoup


class GoogleWeather:
    def __init__(self):
        self.keyword = ""
        self.result = ""

    def set_keyword(self, keyword):
        """크롤링할 키워드를 설정합니다. (단일 문자열 지원)"""
        if not isinstance(keyword, str):
            raise ValueError("키워드는 문자열이어야 합니다.")
        self.keyword = keyword.strip()
        if not self.keyword:
            raise ValueError("키워드가 빈 문자열입니다.")

    def run(self):
        """크롤링을 실행합니다."""
        if not self.keyword:
            raise ValueError("키워드가 설정되지 않았습니다.")

        print(f"크롤링 중: {self.keyword}")
        search_url = f"https://www.google.com/search?q={self.keyword} 날씨&hl=ko"

        # 크롤링 요청
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/114.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(search_url, headers=headers)

        if response.status_code != 200:
            raise ConnectionError(f"구글 검색 실패 (HTTP {response.status_code})")

        soup = BeautifulSoup(response.text, "html.parser")

        # 날씨 정보 추출
        try:
            weather_info = soup.find("div", {"id": "wob_wc"})
            if not weather_info:
                raise ValueError("날씨 정보를 찾을 수 없습니다.")

            temperature = weather_info.find("span", {"id": "wob_tm"}).text
            condition = weather_info.find("span", {"id": "wob_dc"}).text
            location = soup.find("div", {"id": "wob_loc"}).text

            self.result = f"{location}의 날씨는 {condition}, 온도는 {temperature}°C입니다."

        except Exception as e:
            self.result = f"날씨 정보를 가져오는 중 오류가 발생했습니다: {e}"

    def get_result(self):
        """크롤링 결과를 반환합니다."""
        return self.result


# 테스트용 코드
if __name__ == "__main__":
    crawler = GoogleWeather()

    # 단일 문자열 키워드 설정
    try:
        keyword = input("날씨를 검색할 지역을 입력하세요: ")
        crawler.set_keyword(keyword)
        crawler.run()
        print(crawler.get_result())
    except Exception as e:
        print(f"오류: {e}")