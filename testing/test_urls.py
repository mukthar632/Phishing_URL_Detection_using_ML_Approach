import pytest
import requests

# API URL
API_URL = "http://127.0.0.1:5001/predict"

# Lists of URLs
legitimate_urls = [
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.facebook.com",
    "https://www.baidu.com",
    "https://www.wikipedia.org",
    "https://www.reddit.com",
    "https://www.yahoo.com",
    "https://www.thenextweb.com",
    "https://www.qq.com",
    "https://www.amazon.com",
    "https://www.taobao.com",
    "https://www.twitter.com",
    "https://www.tmall.com",
    "https://www.indianexpress.com",
    "https://www.bestblackhatforum.com",
    "https://www.live.com",
    "https://www.instagram.com",
    "https://www.sohu.com",
    "https://www.sina.com.cn",
    "https://www.jd.com",
    "https://www.weibo.com",
    "https://www.thenextweb.com",
    "https://www.//searchengineland.com"

]


phishing_urls = [
    "http://senarai-bantuan-tunai.1p-ly.com/gov/",
    "https://bingkas-programbantuan-ewallet2024.shoudrh...",
    "https://att-109843-102557.weeblysite.com/",
    "https://binance.support0062.com/",
    "https://swiss-pass-sbb-konto.com/",
    "https://345689090rt67ue4t3454svdf04b8fd5ab427b1be5e7b51d9d812.weeblysi...",
    "https://att-maildttfl-home.weeblysite.com/",
    "https://www.zimbra-updts.x24hr.com/",
    "http://zimbra3.findoutwheretogo.com/0010/zm/z/imbra/fr",
    "https://iwuqoqpa.weeblysite.com/",
    "https://pub-2de5d85f3f6c4bf2898608cbde033af3.r2.dev/AT%26TYA.html...",
    "https://fsyuwsuy.temporary-demo.site/",
    "https://bingkasprogrambantuan2024.shoudrhman.bar/log-masuk.php...",
    "https://currently-att-12-02-2024.weeblysite.com/...",
    "https://mqdattnetttt.mystrikingly.com/",
    "http://senarai-bantuan-tunai.1p-ly.com/gov/",
    "https://attcom-108448.weeblysite.com/",
    "https://purduee-cu.org/log/s/a/session_index",
    "https://fsyuwsuy.temporary-demo.site/",
    "https://currently-att-12-02-2024.weeblysite.com/...",
    "https://ln.run/ahMZ1",
    "https://cgd-secpt.com/login.php",
    "https://cgd-secpt.com",

]


# Test function for legitimate URLs
@pytest.mark.parametrize("url", legitimate_urls)
def test_legitimate_urls(url):
    response = requests.post(API_URL, json={"url": url})
    assert response.status_code == 200
    data = response.json()
    assert not data["phishing"], f"URL {url} incorrectly flagged as phishing!"

# Test function for phishing URLs
@pytest.mark.parametrize("url", phishing_urls)
def test_phishing_urls(url):
    response = requests.post(API_URL, json={"url": url})
    assert response.status_code == 200
    data = response.json()
    assert data["phishing"], f"URL {url} not detected as phishing!"
