import requests
import time
def send_request():

    cookies = {
        'ZSMART_LOCALE': 'en',
        'JSESSIONID': '40A1723F1F55117191832E4B038368A3',
        'TS015192a1': '015ae594218af34aad70c859dfb87cc05cfdd5088cb6befb60ccc3d9de450fa7474a70a0b21b37f25addd6ffbe94345e4a5923d1714a999b62b081759502484256c436eb0e',
        'BIGipServerSelfcare_Portal_Pool_new': '46311616.39455.0000',
        'TS0173adb0': '015ae59421051767271ce2b4c618940d1678fa7f7edfe9fc1d1ae4d535730cea3184b9c1fc22f1a37b75d2c17ae88796349d559aaa0af169142203c87d2ff00cc36f6137b4',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Cache-Control': 'no-cache',  # Prevent caching
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Brave";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    response = requests.get('https://selfcare.hutch.lk/selfcare/login.html', cookies=cookies, headers=headers)
    print(response.status_code)


if __name__ == "__main__":
    while True:
        send_request()
        time.sleep(60)  # Wait for 2 minutes    
