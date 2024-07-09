from fastapi import FastAPI
from predict import router as predict_router  # وارد کردن router از فایل predict.py و نامگذاری آن به predict_router
from predict2 import router as predict2_router  # وارد کردن router از فایل predict2.py و نامگذاری آن به predict2_router

app = FastAPI()

# اضافه کردن routerها به اپلیکیشن FastAPI
app.include_router(predict_router)
app.include_router(predict2_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)









