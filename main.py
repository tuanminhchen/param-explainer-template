from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def home():
    return "Param Explainer API is running!"

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q")
    if not query:
        return jsonify({"abstract": "没有提供关键词", "url": ""}), 400

    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        res = requests.get(url, timeout=5)
        data = res.json()

        return jsonify({
            "abstract": data.get("Abstract", "未找到相关解释内容"),
            "url": data.get("AbstractURL", "")
        })
    except Exception as e:
        return jsonify({"abstract": "搜索失败", "url": "", "error": str(e)}), 500

if __name__ == "__main__":
    app.run()
