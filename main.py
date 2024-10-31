from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


url = "https://www.youtube.com/@NetworkChuck/videos"

driver = webdriver.Chrome()
driver.get(url)

video_list = []


wait = WebDriverWait(driver, 10)

video_list = []
id = 0
try:
    titles = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="video-title"]')))
    views = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="metadata-line"]/span[1]')))
    dates = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="metadata-line"]/span[2]')))

    if len(titles)!= len(views) or len(titles)!= len(dates):
        print(f"Warning: number of titles ({len(titles)}) does not match number of views ({len(views)}) or dates ({len(dates)})")

    for title, view, date in zip(titles, views, dates):
        title_text = title.text
        view_text = view.text
        date_text = date.text

        vid_item = {
            'id': id,
            'title': title_text,
            'view': view_text,
            'date': date_text
        }

        video_list.append(vid_item)

        print(video_list)

        id += 1

except Exception as e:
    print(f"Error: {e}")

with open('videos.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'title', 'view', 'date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for video in video_list:
        writer.writerow(video)




# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import csv


# url = "https://www.youtube.com/@GeeksforGeeksVideos/videos"

# driver = webdriver.Chrome()
# driver.get(url)

# video_list = []


# wait = WebDriverWait(driver, 15)

# video_list = []
# id = 0
# try:
#     titles = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="video-title"]')))
#     views = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="metadata-line"]/span[1]')))
#     dates = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="metadata-line"]/span[2]')))

#     if len(titles)!= len(views) or len(titles)!= len(dates):
#         print(f"Warning: number of titles ({len(titles)}) does not match number of views ({len(views)}) or dates ({len(dates)})")

#     for title, view, date in zip(titles, views, dates):
#         title_text = title.text
#         view_text = view.text
#         date_text = date.text

#         vid_item = {
#             'id': id,
#             'title': title_text,
#             'view': view_text,
#             'date': date_text
#         }

#         video_list.append(vid_item)

#         print(video_list)

#         id += 1

# except Exception as e:
#     print(f"Error: {e}")

# with open('videos_1.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['id', 'title', 'view', 'date']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     for video in video_list:
#         writer.writerow(video)