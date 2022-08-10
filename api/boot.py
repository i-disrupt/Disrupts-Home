import os

print("[API] Booting...")
os.system('uvicorn main:app --reload')