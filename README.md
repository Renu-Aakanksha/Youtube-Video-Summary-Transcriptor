<h1>YouTube Transcript Summarizer</h1>

<p>YouTube Transcript Summarizer is a Chrome Extension that simplifies the process of summarizing transcripts from YouTube videos using advanced Natural Language Processing (NLP) techniques. It offers both extractive and abstractive summarization methods to provide concise summaries tailored to your needs.</p>

<h2>Features</h2>

<ul>
  <li><strong>Summarization Techniques:</strong> Utilizes Latent Semantic Analysis (LSA) for longer transcripts and Transformer models for shorter ones.</li>
  <li><strong>Adjustable Summary Length:</strong> Allows dynamic adjustment of summary length for flexibility.</li>
  <li><strong>Language-Agnostic:</strong> Supports videos without subtitles by employing a language-agnostic approach.</li>
  <li><strong>Asynchronous Communication:</strong> Uses XMLHttpRequest for non-blocking communication with the Flask Backend.</li>
</ul>

<img src="/extention/images/output.png?raw=true" alt="Output Example">

<h2>Installation</h2>

<h3>Prerequisites</h3>

<ul>
  <li>Python 3.6 or higher</li>
  <li>Google Chrome</li>
</ul>

<h3>Steps</h3>

<ol>
 
    
  <li><strong>Install Dependencies:</strong><br>
    <code>pip install -r Requirements.txt</code></li>
    
  <li><strong>Start Flask Backend:</strong><br>
    <code>python TranscriptApp.py</code><br>
    This will start a local server at <code>http://127.0.0.1:portno.</code>.</li>
    
  <li><strong>Load the Extension into Google Chrome:</strong>
    <ul>
      <li>Open Google Chrome and go to <code>chrome://extensions/</code>.</li>
      <li>Enable the <strong>Developer mode</strong> toggle in the top right corner.</li>
      <li>Click on <strong>Load unpacked</strong> and select the directory where you cloned this repository.</li>
    </ul></li>
    
  <li><strong>Usage:</strong>
    <ul>
      <li>Navigate to any YouTube video in Chrome.</li>
      <li>Click on the extension icon in the toolbar.</li>
      <li>Click "Summarize" to see the summarized transcript of the video.</li>
    </ul></li>
</ol>
