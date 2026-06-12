import os
from moviepy.video.io.VideoFileClip import VideoFileClip

print("[0] 繁體中文 (Traditional Chinese)")
print("[1] English")
try:
    lang_choice = int(input("Select Language / 選擇語言: "))
except ValueError:
    lang_choice = 1

is_zh = (lang_choice == 0)

files = [f for f in os.listdir('.') if f.endswith(('.mp4', '.mkv', '.avi', '.mov'))]

if not files:
    if is_zh:
        print("錯誤：資料夾內找不到任何影片檔案。")
    else:
        print("Error: No video files found in the directory.")
    exit()

if is_zh:
    print("\n可用的影片列表：")
else:
    print("\nAvailable videos:")

for i, file_name in enumerate(files):
    print(f"[{i}] {file_name}")

try:
    if is_zh:
        choice = int(input("請選擇影片編號: "))
    else:
        choice = int(input("Select video index: "))
    selected_video = files[choice]
except (ValueError, IndexError):
    if is_zh:
        print("無效的選擇。")
    else:
        print("Invalid selection.")
    exit()

if is_zh:
    print("\n請選擇功能：")
    print("[0] 轉檔為 MP3 音訊 (Extract Audio to MP3)")
    print("[1] 影片裁剪 (Cut Video)")
    try:
        mode = int(input("請輸入功能編號: "))
    except ValueError:
        mode = 0
else:
    print("\nSelect Function:")
    print("[0] Extract Audio to MP3")
    print("[1] Cut Video")
    try:
        mode = int(input("Select function index: "))
    except ValueError:
        mode = 0

clip = VideoFileClip(selected_video)

if mode == 0:
    base_name = os.path.splitext(selected_video)[0]
    out_name = f"{base_name}.mp3"
    if is_zh:
        print(f"正在提取音訊並儲存為 {out_name}...")
    else:
        print(f"Extracting audio to {out_name}...")
    clip.audio.write_audiofile(out_name)
    clip.close()
    if is_zh:
        print("音訊提取完成！")
    else:
        print("Audio extraction completed!")

elif mode == 1:
    try:
        if is_zh:
            start_time = float(input("請輸入開始時間 (秒, 例如 10 或 12.5): "))
            end_time = float(input("請輸入結束時間 (秒): "))
        else:
            start_time = float(input("Enter start time (in seconds, e.g., 10 or 12.5): "))
            end_time = float(input("Enter end time (in seconds): "))
    except ValueError:
        if is_zh:
            print("時間格式輸入錯誤。")
        else:
            print("Invalid time format.")
        clip.close()
        exit()
        
    base_name = os.path.splitext(selected_video)[0]
    out_name = f"{base_name}_cut.mp4"
    
    if is_zh:
        print(f"正在裁剪影片並儲存為 {out_name}...")
    else:
        print(f"Cutting video to {out_name}...")
        
    sub_clip = clip.subclip(start_time, end_time)
    sub_clip.write_videofile(out_name, codec="libx264", audio_codec="aac")
    
    sub_clip.close()
    clip.close()
    if is_zh:
        print("影片裁剪完成！")
    else:
        print("Video cutting completed!")