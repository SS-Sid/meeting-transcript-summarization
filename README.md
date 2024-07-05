# meeting-transcript-summarization
A pipeline that takes the path of transcript file and path to save summary. It generates the summary of transcript

### How to use?

1. clone the repository
```
git clone https://github.com/SS-Sid/meeting-transcript-summarization.git
```

2. install the dependencies.
    - NOTE: requirements.txt contains torch import also. Make sure to install torch suitable for your system and device requirements (CPU/GPU). Currently torch with cuda version 11.8 is provided in requirements.txt.
```
pip install -r requirements.txt
```

3. the pipeline supoorts the models saved using huggingface or downloaded from huggingface. Save such model in directory ```"models"``` dir.
    
    For example:
    1. create models dir
    ```
    mkdir models
    ``` 
    2. download the summarization model: 
    
        the model shown below is bart-large-xsum finetuned on samsum dataset which contains conversation style similar to meeting transcripts.
    ```
    from huggingface_hub import snapshot_download
    snapshot_download('knkarthick/meeting-summary-samsum', local_dir='../models/meeting-summary-samsum')
    ```
    Now, you can run the ipynb by providing directory path for meeting-summary-samsum and the notebook would run the locally saved model.
