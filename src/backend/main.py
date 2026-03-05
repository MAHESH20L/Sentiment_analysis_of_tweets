from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import io, base64

app = FastAPI()

# =============================
# CORS
# =============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =============================
# LOAD MODEL
# =============================
MODEL_NAME = "PattimaniM/updated_sentiment"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)
model.eval()

labels = {
    0: "Negative 😡",
    1: "Neutral 😐",
    2: "Positive 😊"
}

# =============================
# CLEAN TEXT
# =============================
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"#\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text

# =============================
# AUTO TOPIC DETECTION
# (works for any uploaded CSV)
# =============================
def detect_topic(text):
    text = str(text).lower()

    if any(w in text for w in ["price","pricing","cost","expensive","cheap","offer","discount"]):
        return "Pricing"

    elif any(w in text for w in ["delivery","shipping","late","delay","courier","order"]):
        return "Delivery"

    elif any(w in text for w in ["quality","product","broken","damaged","good","bad","design"]):
        return "Product Quality"

    elif any(w in text for w in ["support","service","customer","help","response","refund"]):
        return "Customer Service"

    elif any(w in text for w in ["app","website","login","bug","error","payment"]):
        return "Technical/App Issues"

    else:
        return "General"

# =============================
# API
# =============================
@app.post("/predict-csv")
async def predict_csv(file: UploadFile = File(...)):

    df = pd.read_csv(file.file)

    if "Tweet" not in df.columns:
        return {"error": "CSV must contain 'Tweet' column"}

    df = df.head(200)  # can increase later

    results = []
    sentiments = []
    topic_sentiments = []

    # =============================
    # PREDICTION LOOP
    # =============================
    for text in df["Tweet"]:

        text_clean = clean_text(text)
        topic = detect_topic(text)

        inputs = tokenizer(
            text_clean,
            return_tensors="pt",
            truncation=True,
            padding=True
        )

        with torch.no_grad():
            outputs = model(**inputs)
            probs = torch.softmax(outputs.logits, dim=1).numpy()[0]

        pred_id = int(np.argmax(probs))
        sentiment = labels[pred_id]
        confidence = float(probs[pred_id])

        sentiments.append(sentiment)
        topic_sentiments.append((topic, sentiment))

        results.append({
            "tweet": text,
            "topic": topic,
            "sentiment": sentiment,
            "confidence": round(confidence,3)
        })

    # =============================
    # OVERALL SENTIMENT CHART
    # =============================
    counts = pd.Series(sentiments).value_counts()

    plt.figure(figsize=(6,4))
    counts.plot(kind="bar")
    plt.title("Overall Sentiment Distribution")
    plt.xlabel("Sentiment")
    plt.ylabel("Count")

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight")
    buf.seek(0)
    overall_chart = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()

    # =============================
    # TOPIC-WISE SENTIMENT CHART
    # =============================
    topic_df = pd.DataFrame(topic_sentiments, columns=["topic","sentiment"])
    pivot = pd.crosstab(topic_df["topic"], topic_df["sentiment"])

    plt.figure(figsize=(8,5))
    pivot.plot(kind="bar", stacked=True)
    plt.title("Topic-wise Sentiment Analysis")
    plt.xlabel("Topic")
    plt.ylabel("Count")

    buf2 = io.BytesIO()
    plt.savefig(buf2, format="png", bbox_inches="tight")
    buf2.seek(0)
    topic_chart = base64.b64encode(buf2.read()).decode("utf-8")
    plt.close()

    # =============================
    # SMART RECOMMENDATIONS
    # =============================
    recommendations = []

    neg_topics = topic_df[topic_df["sentiment"]=="Negative 😡"]["topic"].value_counts()

    for topic, count in neg_topics.items():
        if topic == "Pricing":
            recommendations.append("Customers unhappy with pricing → Consider discounts or revise pricing strategy.")
        elif topic == "Delivery":
            recommendations.append("Delivery complaints detected → Improve shipping speed and tracking.")
        elif topic == "Product Quality":
            recommendations.append("Product quality issues found → Improve quality control and packaging.")
        elif topic == "Customer Service":
            recommendations.append("Customer service complaints → Train support team & reduce response time.")
        elif topic == "Technical/App Issues":
            recommendations.append("App/Website issues detected → Fix bugs and improve performance.")
        else:
            recommendations.append(f"Negative feedback in {topic} → Needs attention.")

    if len(recommendations) == 0:
        recommendations.append("Overall sentiment is positive. Maintain current strategy.")

    # =============================
    # RETURN RESPONSE
    # =============================
    return {
        "results": results,
        "overall_sentiment_chart": overall_chart,
        "topic_sentiment_chart": topic_chart,
        "recommendations": recommendations
    }
