from flask import Flask, request
from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from nltk.tokenize import sent_tokenize
from langdetect import detect

app = Flask(__name__)

class YouTubeTranscriptSummarizer:
    def __init__(self):
        self.summarizer = pipeline('summarization')

    def get_transcript(self, video_id):
        try:
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        except Exception as e:
            raise e

        transcript = ' '.join([d['text'] for d in transcript_list])
        return transcript

    def abstractive_summarization(self, transcript, max_length):
        summary = ''
        for i in range(0, (len(transcript) // 1000) + 1):
            summary_text = self.summarizer(transcript[i * 1000:(i + 1) * 1000], max_length=max_length)[0]['summary_text']
            summary += summary_text + ' '
        return summary

    def extractive_summarization(self, transcript):
        sentences = sent_tokenize(transcript)
        vectorizer = CountVectorizer(stop_words='english')
        X = vectorizer.fit_transform(sentences)

        svd = TruncatedSVD(n_components=1, random_state=42)
        svd.fit(X)
        components = svd.transform(X)

        ranked_sentences = [item[0] for item in sorted(enumerate(components), key=lambda item: -item[1])]
        num_sentences = int(0.4 * len(sentences))
        selected_sentences = sorted(ranked_sentences[:num_sentences])

        summary = " ".join([sentences[idx] for idx in selected_sentences])
        return summary

    def is_transcript_english(self, transcript):
        try:
            language = detect(transcript)
            return language == 'en'
        except Exception as e:
            return False

@app.route('/summary', methods=['GET'])
def summary_api():
    url = request.args.get('url', '')
    max_length = int(request.args.get('max_length', 150))
    video_id = url.split('=')[1]

    summarizer = YouTubeTranscriptSummarizer()

    try:
        transcript = summarizer.get_transcript(video_id)
    except:
        return "No subtitles available for this video", 404

    if len(transcript.split()) > 3000:
        summary = summarizer.extractive_summarization(transcript)
    else:
        summary = summarizer.abstractive_summarization(transcript, max_length)

    return summary, 200

if __name__ == '__main__':
    app.run(debug=True, port=5010)
